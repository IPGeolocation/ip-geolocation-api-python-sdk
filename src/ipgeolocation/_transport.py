"""HTTP transport abstractions."""

from __future__ import annotations

import codecs
import importlib
from dataclasses import dataclass
from typing import Any, Dict, List, Optional, Protocol

import requests

from .exceptions import RequestTimeoutException, TransportException


@dataclass(frozen=True)
class HttpRequestData:
    """Normalized HTTP request data used by the transport."""

    url: str
    method: str
    headers: Dict[str, List[str]]
    body: Optional[str]
    connect_timeout: float
    read_timeout: float

    def first_header_value(self, name: str) -> Optional[str]:
        for key, values in self.headers.items():
            if key.lower() == name.lower():
                return values[0] if values else None
        return None


@dataclass(frozen=True)
class HttpResponseData:
    """Normalized HTTP response data used by the client."""

    status_code: int
    body: str
    headers: Dict[str, List[str]]


class HttpTransport(Protocol):
    """Protocol for HTTP transports."""

    def send(self, request: HttpRequestData) -> HttpResponseData:
        """Send a request and return the response."""
        ...

    def close(self) -> None:
        """Release any transport resources."""
        ...


class AsyncHttpTransport(Protocol):
    """Protocol for async HTTP transports."""

    async def send(self, request: HttpRequestData) -> HttpResponseData:
        """Send a request and return the response."""
        ...

    async def close(self) -> None:
        """Release any transport resources."""
        ...


class RequestsHttpTransport:
    """Requests-based HTTP transport with response-size protection."""

    DEFAULT_MAX_RESPONSE_BODY_CHARS = 128 * 1024 * 1024

    def __init__(
        self,
        session: Optional[requests.Session] = None,
        max_response_body_chars: int = DEFAULT_MAX_RESPONSE_BODY_CHARS,
    ) -> None:
        if max_response_body_chars <= 0:
            raise ValueError("max_response_body_chars must be greater than zero")
        self._session = session or requests.Session()
        self._owns_session = session is None
        self._max_response_body_chars = max_response_body_chars

    def send(self, request: HttpRequestData) -> HttpResponseData:
        header_map = {
            key: values[0] if len(values) == 1 else ", ".join(values)
            for key, values in request.headers.items()
            if key is not None and values
        }
        try:
            response = self._session.request(
                method=request.method,
                url=request.url,
                headers=header_map,
                data=request.body,
                timeout=(request.connect_timeout, request.read_timeout),
                stream=True,
            )
        except requests.exceptions.Timeout as exc:
            raise RequestTimeoutException("HTTP request timed out") from exc
        except requests.exceptions.RequestException as exc:
            raise TransportException("HTTP transport error") from exc

        try:
            try:
                body = self._read_body(response)
            except requests.exceptions.Timeout as exc:
                raise RequestTimeoutException("HTTP request timed out") from exc
            except requests.exceptions.RequestException as exc:
                raise TransportException("HTTP transport error") from exc
            return HttpResponseData(
                status_code=response.status_code,
                body=body,
                headers=_extract_headers(response),
            )
        finally:
            response.close()

    def close(self) -> None:
        if self._owns_session:
            self._session.close()

    def _read_body(self, response: requests.Response) -> str:
        encoding = getattr(response, "encoding", None) or "utf-8"
        try:
            decoder = codecs.getincrementaldecoder(encoding)(errors="replace")
        except LookupError:
            decoder = codecs.getincrementaldecoder("utf-8")(errors="replace")
        body_parts: List[str] = []
        total_chars = 0

        for chunk in response.iter_content(chunk_size=8192):
            if not chunk:
                continue
            decoded = decoder.decode(chunk)
            if decoded:
                total_chars += len(decoded)
                if total_chars > self._max_response_body_chars:
                    raise TransportException(
                        "Response body exceeded max size of "
                        f"{self._max_response_body_chars} characters"
                    )
                body_parts.append(decoded)

        final_chunk = decoder.decode(b"", final=True)
        if final_chunk:
            total_chars += len(final_chunk)
            if total_chars > self._max_response_body_chars:
                raise TransportException(
                    f"Response body exceeded max size of {self._max_response_body_chars} characters"
                )
            body_parts.append(final_chunk)

        return "".join(body_parts)


def _extract_headers(response: requests.Response) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = {}
    raw_headers = getattr(getattr(response, "raw", None), "headers", None)
    if raw_headers is not None:
        try:
            for key in raw_headers.keys():
                if hasattr(raw_headers, "getlist"):
                    values = [value for value in raw_headers.getlist(key) if value is not None]
                else:
                    value = raw_headers.get(key)
                    values = [] if value is None else [value]
                result[key] = values
            if result:
                return result
        except Exception:
            result = {}

    for key, value in response.headers.items():
        result[key] = [value]
    return result


class HttpxAsyncTransport:
    """HTTPX-based async transport with response-size protection."""

    DEFAULT_MAX_RESPONSE_BODY_CHARS = 128 * 1024 * 1024

    def __init__(
        self,
        client: Optional[Any] = None,
        max_response_body_chars: int = DEFAULT_MAX_RESPONSE_BODY_CHARS,
    ) -> None:
        if max_response_body_chars <= 0:
            raise ValueError("max_response_body_chars must be greater than zero")
        self._client = client
        self._owns_client = client is None
        self._max_response_body_chars = max_response_body_chars

    async def send(self, request: HttpRequestData) -> HttpResponseData:
        httpx = _load_httpx()
        client = self._client
        if client is None:
            client = httpx.AsyncClient()
            self._client = client

        header_map = {
            key: values[0] if len(values) == 1 else ", ".join(values)
            for key, values in request.headers.items()
            if key is not None and values
        }
        timeout = httpx.Timeout(request.read_timeout, connect=request.connect_timeout)

        try:
            async with client.stream(
                method=request.method,
                url=request.url,
                headers=header_map,
                content=request.body,
                timeout=timeout,
            ) as response:
                body = await self._read_body(response)
                return HttpResponseData(
                    status_code=response.status_code,
                    body=body,
                    headers=_extract_httpx_headers(response.headers),
                )
        except httpx.TimeoutException as exc:
            raise RequestTimeoutException("HTTP request timed out") from exc
        except httpx.HTTPError as exc:
            raise TransportException("HTTP transport error") from exc

    async def close(self) -> None:
        if self._owns_client and self._client is not None:
            await self._client.aclose()

    async def _read_body(self, response: Any) -> str:
        body_parts: List[str] = []
        total_chars = 0

        async for chunk in response.aiter_text():
            if not chunk:
                continue
            total_chars += len(chunk)
            if total_chars > self._max_response_body_chars:
                raise TransportException(
                    f"Response body exceeded max size of {self._max_response_body_chars} characters"
                )
            body_parts.append(chunk)

        return "".join(body_parts)


def _extract_httpx_headers(headers: Any) -> Dict[str, List[str]]:
    result: Dict[str, List[str]] = {}
    if hasattr(headers, "multi_items"):
        for key, value in headers.multi_items():
            result.setdefault(key, []).append(value)
        return result

    for key, value in headers.items():
        result.setdefault(key, []).append(value)
    return result


def _load_httpx() -> Any:
    return importlib.import_module("httpx")
