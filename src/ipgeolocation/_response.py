from __future__ import annotations

import codecs
import zlib
from io import StringIO
from typing import Any, Iterator, Optional

from urllib3 import response as urllib_response
from urllib3.response import HTTPResponse, MultiDecoder

from .exceptions import TransportException

CHUNK_SIZE = 8192


class _ZlibStream:
    def __init__(self, gzip: bool) -> None:
        self.gzip = gzip
        self.decoder: Any = zlib.decompressobj(31) if gzip else None
        self.prefix = b""
        self.retry_header: bytearray | None = None

    def chunks(self, data: bytes, size: int) -> Iterator[bytes]:
        if self.decoder is None:
            data = self.prefix + data
            if len(data) < 2:
                self.prefix = data
                return
            self.prefix = b""
            header = int.from_bytes(data[:2], "big")
            wrapped = data[0] & 15 == 8 and data[0] >> 4 <= 7 and header % 31 == 0
            self.decoder = zlib.decompressobj(15 if wrapped else -15)
            if wrapped:
                self.retry_header = bytearray()
        if self.retry_header is not None:
            if len(self.retry_header) + len(data) <= 65536:
                self.retry_header.extend(data)
            else:
                self.retry_header = None
        while True:
            if self.decoder.eof:
                if not self.gzip:
                    return
                data = data.lstrip(b"\x00")
                if not data:
                    return
                self.decoder = zlib.decompressobj(31)
            try:
                piece = self.decoder.decompress(data, size)
            except zlib.error:
                if self.retry_header is None:
                    raise
                self.decoder = zlib.decompressobj(-15)
                data = bytes(self.retry_header)
                self.retry_header = None
                continue
            if piece:
                self.retry_header = None
                yield piece
            data = self.decoder.unused_data if self.decoder.eof else self.decoder.unconsumed_tail
            if not data and len(piece) < size:
                return

    def finish(self) -> bytes:
        if self.decoder is None or not self.decoder.eof:
            raise TransportException("Incomplete compressed response")
        return b""


def _bounded_brotli() -> bool:
    module = getattr(urllib_response, "brotli", None)
    if module is None:
        return False
    decoder = module.Decompressor()
    process = getattr(decoder, "decompress", None) or getattr(decoder, "process", None)
    if process is None:
        return False
    try:
        process(b"", output_buffer_limit=1)
    except (TypeError, AttributeError):
        return False
    return hasattr(decoder, "can_accept_more_data") and hasattr(decoder, "is_finished")


_ENCODINGS = ["gzip", "deflate"]
if "br" in HTTPResponse.CONTENT_DECODERS and _bounded_brotli():
    _ENCODINGS.append("br")
if "zstd" in HTTPResponse.CONTENT_DECODERS:
    _ENCODINGS.append("zstd")
ACCEPT_ENCODING = ", ".join(_ENCODINGS)


class _OtherStream:
    def __init__(self, coding: str) -> None:
        self.brotli: Any = None
        if coding == "br":
            self.brotli = getattr(urllib_response, "brotli").Decompressor()
        else:
            self.decoder = MultiDecoder(coding)

    def chunks(self, data: bytes, size: int) -> Iterator[bytes]:
        while True:
            if self.brotli is None:
                part = self.decoder.decompress(data, max_length=size)
                done = not self.decoder.has_unconsumed_tail
            else:
                process = getattr(self.brotli, "decompress", None) or self.brotli.process
                part = process(data, output_buffer_limit=size)
                done = self.brotli.can_accept_more_data()
            if part:
                yield part
            if done:
                return
            data = b""

    def finish(self) -> bytes:
        if self.brotli is not None:
            if not self.brotli.is_finished():
                raise TransportException("Incomplete compressed response")
            return b""
        return self.decoder.flush()


class ResponseBody:
    def __init__(self, limit: int, charset: Optional[str], content_encoding: str) -> None:
        self.limit = limit
        self.size = 0
        self.text_buffer = StringIO()
        self.chunk_size = min(CHUNK_SIZE, limit + 1)
        try:
            b" ".decode(charset or "utf-8", errors="replace")
            self.text = codecs.getincrementaldecoder(charset or "utf-8")(errors="replace")
        except (LookupError, ValueError):
            self.text = codecs.getincrementaldecoder("utf-8")(errors="replace")
        self.stages: list[_ZlibStream | _OtherStream] = []
        codings = [c.strip().lower() for c in content_encoding.split(",")]
        if len(codings) > 5:
            raise TransportException("Too many response encodings")
        for coding in reversed(codings):
            if coding in ("", "identity"):
                continue
            if coding in ("gzip", "x-gzip", "deflate"):
                self.stages.append(_ZlibStream(coding != "deflate"))
            elif coding in _ENCODINGS:
                self.stages.append(_OtherStream(coding))
            else:
                raise TransportException("Unsupported response encoding")
        self.layer_sizes = [0] * (len(self.stages) + 1)

    def _append(self, value: str) -> None:
        if value:
            self.size += len(value)
            if self.size > self.limit:
                raise TransportException(
                    f"Response body exceeded max size of {self.limit} characters"
                )
            self.text_buffer.write(value)

    def feed(self, data: bytes, layer: int = 0) -> None:
        self.layer_sizes[layer] += len(data)
        if self.layer_sizes[layer] > 4 * self.limit + 65536:
            raise TransportException(f"Response body exceeded max size of {self.limit} characters")
        if layer == len(self.stages):
            self._append(self.text.decode(data))
        else:
            for piece in self.stages[layer].chunks(data, self.chunk_size):
                self.feed(piece, layer + 1)

    def finish(self) -> str:
        for i, stage in enumerate(self.stages):
            last = stage.finish()
            if last:
                self.feed(last, i + 1)
        self._append(self.text.decode(b"", final=True))
        return self.text_buffer.getvalue()
