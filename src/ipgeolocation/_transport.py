"""HTTP transport abstractions."""

from __future__ import annotations

import importlib
from contextlib import AsyncExitStack
from dataclasses import dataclass
from typing import Any, Dict, List, Mapping, Optional, Protocol

import requests
from urllib3.exceptions import HTTPError as Urllib3Error
from urllib3.exceptions import ReadTimeoutError
from urllib3.response import HTTPResponse
from urllib3.util import parse_url

from ._response import ACCEPT_ENCODING, CHUNK_SIZE, ResponseBody
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


def _same_origin(source: str, target: str) -> bool:
    original, destination = parse_url(source), parse_url(target)
    default = {"http": 80, "https": 443}
    return (
        destination.auth is None
        and original.scheme in default
        and original.scheme == destination.scheme
        and original.host == destination.host
        and (original.port if original.port is not None else default[original.scheme])
        == (destination.port if destination.port is not None else default[original.scheme])
    )


def _headers(request: HttpRequestData, defaults: Mapping[str, str]) -> Dict[str, str]:
    headers = {k: ", ".join(v) for k, v in request.headers.items() if k and v}
    if not any(name.lower() == "accept-encoding" for name in headers):
        inherited = defaults.get("Accept-Encoding")
        if inherited:
            offered = [item.strip() for item in inherited.split(",")]
            unsafe = {"br", "zstd"} - set(ACCEPT_ENCODING.split(", "))
            safe = [
                item for item in offered if item.partition(";")[0].strip().lower() not in unsafe
            ]
            if safe != offered:
                headers["Accept-Encoding"] = ", ".join(safe) or "identity"
    return headers


def _close_redirect(response: requests.Response, **kwargs: Any) -> requests.Response:
    if response.is_redirect:
        response.close()
    return response


_BODY_ERRORS: tuple[type[BaseException], ...] = (
    TransportException,
    ValueError,
    LookupError,
    Urllib3Error,
    *HTTPResponse.DECODER_ERROR_CLASSES,
)


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
        if self._owns_session:
            self._session.headers["Accept-Encoding"] = ACCEPT_ENCODING
        self._max_response_body_chars = max_response_body_chars

    def send(self, request: HttpRequestData) -> HttpResponseData:
        timeout = (request.connect_timeout, request.read_timeout)
        hooks = getattr(self._session, "hooks", {}).get("response") or ()
        if callable(hooks):
            hooks = (hooks,)
        try:
            response = self._session.request(
                method=request.method,
                url=request.url,
                headers=_headers(request, getattr(self._session, "headers", {})),
                data=request.body,
                timeout=timeout,
                stream=True,
                allow_redirects=False,
                hooks={"response": [_close_redirect, *hooks]},
            )
            redirects = 0
            while True:
                try:
                    next_request = response.next
                    if next_request is None:
                        return self._read_response(response)
                    target = next_request.url
                    if not target or not _same_origin(request.url, target):
                        return HttpResponseData(
                            response.status_code, "", _extract_headers(response)
                        )
                    if redirects >= self._session.max_redirects:
                        raise TransportException("Too many redirects")
                    redirects += 1
                finally:
                    response.close()
                options = self._session.merge_environment_settings(target, {}, True, None, None)
                response = self._session.send(
                    next_request, timeout=timeout, allow_redirects=False, **options
                )
        except (requests.exceptions.Timeout, ReadTimeoutError) as exc:
            raise RequestTimeoutException("HTTP request timed out") from exc
        except (requests.exceptions.RequestException, Urllib3Error, ValueError) as exc:
            raise TransportException("HTTP transport error") from exc

    def close(self) -> None:
        if self._owns_session:
            self._session.close()

    def _read_response(self, response: requests.Response) -> HttpResponseData:
        if response.status_code in (204, 205):
            return HttpResponseData(response.status_code, "", _extract_headers(response))
        try:
            raw_stream = getattr(response.raw, "stream", None)
            if raw_stream is None or getattr(response, "_content_consumed", False):
                chunks = response.iter_content(CHUNK_SIZE)
                coding = ""
            else:
                chunks = raw_stream(CHUNK_SIZE, False)
                coding = response.headers.get("Content-Encoding", "")
            reader = ResponseBody(self._max_response_body_chars, response.encoding, coding)
            for chunk in chunks:
                reader.feed(chunk)
            body = reader.finish()
        except (requests.exceptions.RequestException,) + _BODY_ERRORS as exc:
            if 200 <= response.status_code < 300:
                if isinstance(
                    exc, (requests.exceptions.RequestException, Urllib3Error, TransportException)
                ):
                    raise
                raise TransportException("Invalid response body") from exc
            body = ""
        return HttpResponseData(response.status_code, body, _extract_headers(response))


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
            client = httpx.AsyncClient(headers={"Accept-Encoding": ACCEPT_ENCODING})
            self._client = client

        timeout = httpx.Timeout(request.read_timeout, connect=request.connect_timeout)
        try:
            async with (
                client.stream(
                    method=request.method,
                    url=request.url,
                    headers=_headers(request, getattr(client, "headers", {})),
                    content=request.body,
                    timeout=timeout,
                    follow_redirects=False,
                ) as response,
                AsyncExitStack() as stack,
            ):
                redirects = 0
                while getattr(client, "follow_redirects", False) and response.next_request:
                    next_request = response.next_request
                    if not _same_origin(request.url, str(next_request.url)):
                        return HttpResponseData(
                            response.status_code, "", _extract_httpx_headers(response.headers)
                        )
                    if redirects >= client.max_redirects:
                        raise TransportException("Too many redirects")
                    redirects += 1
                    await response.aclose()
                    response = await client.send(next_request, stream=True, follow_redirects=False)
                    stack.push_async_callback(response.aclose)

                if response.status_code in (204, 205):
                    return HttpResponseData(
                        response.status_code, "", _extract_httpx_headers(response.headers)
                    )
                try:
                    buffered = response.is_stream_consumed
                    coding = "" if buffered else response.headers.get("Content-Encoding", "")
                    reader = ResponseBody(self._max_response_body_chars, response.encoding, coding)
                    chunks = response.aiter_bytes(CHUNK_SIZE) if buffered else response.aiter_raw()
                    async for chunk in chunks:
                        reader.feed(chunk)
                    body = reader.finish()
                except (httpx.HTTPError,) + _BODY_ERRORS as exc:
                    if 200 <= response.status_code < 300:
                        if isinstance(exc, (httpx.HTTPError, TransportException)):
                            raise
                        raise TransportException("Invalid response body") from exc
                    body = ""
                return HttpResponseData(
                    response.status_code, body, _extract_httpx_headers(response.headers)
                )
        except httpx.TimeoutException as exc:
            raise RequestTimeoutException("HTTP request timed out") from exc
        except (httpx.HTTPError, httpx.InvalidURL, UnicodeError, Urllib3Error) as exc:
            raise TransportException("HTTP transport error") from exc

    async def close(self) -> None:
        if self._owns_client and self._client is not None:
            await self._client.aclose()


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
