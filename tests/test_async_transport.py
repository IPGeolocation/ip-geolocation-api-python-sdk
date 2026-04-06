"""HTTPX async transport tests."""

from __future__ import annotations

import asyncio
from typing import Any, Dict, List, Optional

import pytest

from ipgeolocation import RequestTimeoutException, TransportException
from ipgeolocation._transport import HttpRequestData, HttpxAsyncTransport


def _run(coro):
    return asyncio.run(coro)


class StubAsyncHeaders:
    def __init__(self, values: Dict[str, List[str]]) -> None:
        self._values = values

    def multi_items(self):
        for key, values in self._values.items():
            for value in values:
                yield key, value


class StubAsyncResponse:
    def __init__(
        self,
        status_code: int = 200,
        chunks: Optional[List[str]] = None,
        headers: Optional[Dict[str, List[str]]] = None,
        iter_exception: Optional[Exception] = None,
    ) -> None:
        self.status_code = status_code
        self._chunks = chunks or ["{}"]
        self.headers = StubAsyncHeaders(headers or {})
        self.iter_exception = iter_exception

    async def aiter_text(self):
        if self.iter_exception is not None:
            raise self.iter_exception
        for chunk in self._chunks:
            yield chunk


class StubAsyncStream:
    def __init__(self, response: StubAsyncResponse) -> None:
        self.response = response

    async def __aenter__(self) -> StubAsyncResponse:
        return self.response

    async def __aexit__(self, exc_type, exc, tb) -> None:
        return None


class StubAsyncClient:
    def __init__(self, response=None, exception=None) -> None:
        self.response = response
        self.exception = exception
        self.closed = False
        self.last_request: Optional[Dict[str, Any]] = None

    def stream(self, **kwargs):
        self.last_request = kwargs
        if self.exception is not None:
            raise self.exception
        return StubAsyncStream(self.response)

    async def aclose(self) -> None:
        self.closed = True


class FakeHttpxModule:
    class HTTPError(Exception):
        pass

    class TimeoutException(HTTPError):
        pass

    class Timeout:
        def __init__(self, timeout, connect=None) -> None:
            self.timeout = timeout
            self.connect = connect

    class AsyncClient:
        def __init__(self) -> None:
            self.closed = False

        async def aclose(self) -> None:
            self.closed = True


def test_httpx_async_transport_sends_request_and_extracts_headers(monkeypatch) -> None:
    async def scenario() -> None:
        fake_httpx = FakeHttpxModule()
        response = StubAsyncResponse(
            status_code=200,
            chunks=['{"ip":"8.8.8.8"}'],
            headers={"X-Credits-Charged": ["1"]},
        )
        client = StubAsyncClient(response=response)
        transport = HttpxAsyncTransport(client=client)

        monkeypatch.setattr("ipgeolocation._transport._load_httpx", lambda: fake_httpx)
        result = await transport.send(
            HttpRequestData(
                url="https://api.ipgeolocation.io/v3/ipgeo?apiKey=k",
                method="GET",
                headers={"User-Agent": ["ua"]},
                body=None,
                connect_timeout=1.0,
                read_timeout=2.0,
            )
        )

        assert result.status_code == 200
        assert result.body == '{"ip":"8.8.8.8"}'
        assert result.headers["X-Credits-Charged"] == ["1"]
        assert client.last_request is not None
        assert client.last_request["timeout"].connect == 1.0
        assert client.last_request["timeout"].timeout == 2.0

    _run(scenario())


def test_httpx_async_transport_joins_multi_value_headers_with_commas(monkeypatch) -> None:
    async def scenario() -> None:
        fake_httpx = FakeHttpxModule()
        response = StubAsyncResponse()
        client = StubAsyncClient(response=response)
        transport = HttpxAsyncTransport(client=client)

        monkeypatch.setattr("ipgeolocation._transport._load_httpx", lambda: fake_httpx)
        await transport.send(
            HttpRequestData(
                url="https://api.ipgeolocation.io/v3/ipgeo?apiKey=k",
                method="GET",
                headers={"X-Test": ["one", "two"]},
                body=None,
                connect_timeout=1.0,
                read_timeout=2.0,
            )
        )

        assert client.last_request is not None
        assert client.last_request["headers"]["X-Test"] == "one, two"

    _run(scenario())


def test_httpx_async_transport_maps_timeout(monkeypatch) -> None:
    async def scenario() -> None:
        fake_httpx = FakeHttpxModule()
        client = StubAsyncClient(exception=fake_httpx.TimeoutException("boom"))
        transport = HttpxAsyncTransport(client=client)
        monkeypatch.setattr("ipgeolocation._transport._load_httpx", lambda: fake_httpx)

        with pytest.raises(RequestTimeoutException, match="HTTP request timed out"):
            await transport.send(
                HttpRequestData(
                    url="https://api.ipgeolocation.io/v3/ipgeo",
                    method="GET",
                    headers={},
                    body=None,
                    connect_timeout=1.0,
                    read_timeout=2.0,
                )
            )

    _run(scenario())


def test_httpx_async_transport_maps_http_error_during_stream(monkeypatch) -> None:
    async def scenario() -> None:
        fake_httpx = FakeHttpxModule()
        response = StubAsyncResponse(iter_exception=fake_httpx.HTTPError("boom"))
        client = StubAsyncClient(response=response)
        transport = HttpxAsyncTransport(client=client)
        monkeypatch.setattr("ipgeolocation._transport._load_httpx", lambda: fake_httpx)

        with pytest.raises(TransportException, match="HTTP transport error"):
            await transport.send(
                HttpRequestData(
                    url="https://api.ipgeolocation.io/v3/ipgeo",
                    method="GET",
                    headers={},
                    body=None,
                    connect_timeout=1.0,
                    read_timeout=2.0,
                )
            )

    _run(scenario())


def test_httpx_async_transport_rejects_oversized_response_body(monkeypatch) -> None:
    async def scenario() -> None:
        fake_httpx = FakeHttpxModule()
        response = StubAsyncResponse(chunks=["12345", "67890", "x"])
        client = StubAsyncClient(response=response)
        transport = HttpxAsyncTransport(client=client, max_response_body_chars=10)
        monkeypatch.setattr("ipgeolocation._transport._load_httpx", lambda: fake_httpx)

        with pytest.raises(TransportException, match="Response body exceeded max size"):
            await transport.send(
                HttpRequestData(
                    url="https://api.ipgeolocation.io/v3/ipgeo",
                    method="GET",
                    headers={},
                    body=None,
                    connect_timeout=1.0,
                    read_timeout=2.0,
                )
            )

    _run(scenario())


def test_httpx_async_transport_closes_owned_client(monkeypatch) -> None:
    async def scenario() -> None:
        fake_httpx = FakeHttpxModule()
        monkeypatch.setattr("ipgeolocation._transport._load_httpx", lambda: fake_httpx)

        transport = HttpxAsyncTransport()
        owned_client = fake_httpx.AsyncClient()
        transport._client = owned_client
        await transport.close()

        assert owned_client.closed is True

    _run(scenario())
