from __future__ import annotations

import json
import logging
import re
from contextlib import contextmanager
from contextvars import ContextVar
from typing import Iterator, Optional
from urllib.parse import quote, quote_plus

from .exceptions import ApiException, IpGeolocationException

MASK = "[REDACTED]"
_active_key: ContextVar[Optional[str]] = ContextVar("ipgeolocation_api_key", default=None)
_percent_escape = re.compile(r"%[0-9a-fA-F]{2}")


def redact(text: str, key: Optional[str]) -> str:
    if not key:
        return text
    for encoded in {quote(key, safe=""), quote_plus(key, safe="")} - {key}:
        if "%" in encoded:
            normalized = _percent_escape.sub(lambda m: m[0].upper(), text)
            pieces: list[str] = []
            start = 0
            pos = normalized.find(encoded)
            while pos >= 0:
                pieces.extend((text[start:pos], MASK))
                start = pos + len(encoded)
                pos = normalized.find(encoded, start)
            if pieces:
                text = "".join(pieces) + text[start:]
        else:
            text = text.replace(encoded, MASK)
    for escaped in {json.dumps(key)[1:-1], json.dumps(key, ensure_ascii=False)[1:-1]} - {key}:
        text = text.replace(escaped, MASK)
    return text.replace(key, MASK)


class _RequestLogFilter(logging.Filter):
    def filter(self, record: logging.LogRecord) -> bool:
        key = _active_key.get()
        if record.name.startswith("hpack."):
            if key or (
                record.name == "hpack.hpack"
                and isinstance(record.msg, str)
                and record.msg.startswith(("Decoding %s", "Decoded %s,"))
            ):
                return False
            if (
                record.name == "hpack.table"
                and record.msg == "Evicting %s: %s from the header table"
                and isinstance(record.args, tuple)
                and len(record.args) == 2
            ):
                record.args = (record.args[0], MASK)
        if key:
            message = record.getMessage()
            safe = redact(message, key)
            if safe != message:
                record.msg, record.args = safe, ()
        return True


_log_filter = _RequestLogFilter()
for _name in (
    "hpack.hpack",
    "hpack.table",
    "httpx",
    "httpcore.connection",
    "httpcore.proxy",
    "httpcore.socks",
    "httpcore.http11",
    "httpcore.http2",
    "urllib3.connectionpool",
    "urllib3.util.retry",
    "urllib3.connection",
):
    logging.getLogger(_name).addFilter(_log_filter)


@contextmanager
def protect_api_key(key: Optional[str]) -> Iterator[None]:
    if key is None:
        yield
        return
    token = _active_key.set(key)
    try:
        yield
    except IpGeolocationException as exc:
        if isinstance(exc, ApiException) and exc.api_message is not None:
            exc.api_message = redact(exc.api_message, key)
        exc.args = tuple(redact(arg, key) if isinstance(arg, str) else arg for arg in exc.args)
        exc.__cause__ = None
        exc.__context__ = None
        exc.__suppress_context__ = True
        raise
    finally:
        _active_key.reset(token)
