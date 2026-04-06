"""Requests transport tests."""

from __future__ import annotations

from typing import Dict, List

import pytest
import requests

from ipgeolocation import RequestTimeoutException, TransportException
from ipgeolocation._transport import HttpRequestData, RequestsHttpTransport


class StubRawHeaders:
    def __init__(self, values: Dict[str, List[str]]) -> None:
        self._values = values

    def keys(self):
        return self._values.keys()

    def getlist(self, key):
        return list(self._values.get(key, []))


class StubResponse:
    def __init__(self, status_code=200, body="{}", headers=None, iter_exception=None) -> None:
        self.status_code = status_code
        self._body_bytes = body.encode("utf-8")
        self.content_accessed = False
        self.closed = False
        self.headers = {key: values[0] for key, values in (headers or {}).items() if values}
        self.raw = type("Raw", (), {"headers": StubRawHeaders(headers or {})})()
        self.iter_exception = iter_exception

    @property
    def content(self):
        self.content_accessed = True
        return self._body_bytes

    def iter_content(self, chunk_size=1):
        if self.iter_exception is not None:
            raise self.iter_exception
        for index in range(0, len(self._body_bytes), chunk_size):
            yield self._body_bytes[index : index + chunk_size]

    def close(self) -> None:
        self.closed = True


class StubSession:
    def __init__(self, response=None, exception=None) -> None:
        self.response = response
        self.exception = exception
        self.closed = False
        self.last_request = None

    def request(self, **kwargs):
        self.last_request = kwargs
        if self.exception is not None:
            raise self.exception
        return self.response

    def close(self):
        self.closed = True


def test_requests_transport_sends_request_and_extracts_headers() -> None:
    session = StubSession(
        response=StubResponse(
            status_code=200,
            body='{"ip":"8.8.8.8"}',
            headers={"X-Credits-Charged": ["1"]},
        )
    )
    transport = RequestsHttpTransport(session=session)

    response = transport.send(
        HttpRequestData(
            url="https://api.ipgeolocation.io/v3/ipgeo?apiKey=k",
            method="GET",
            headers={"User-Agent": ["ua"]},
            body=None,
            connect_timeout=1.0,
            read_timeout=2.0,
        )
    )

    assert response.status_code == 200
    assert response.body == '{"ip":"8.8.8.8"}'
    assert response.headers["X-Credits-Charged"] == ["1"]
    assert session.last_request["timeout"] == (1.0, 2.0)
    assert session.last_request["stream"] is True
    assert session.response.content_accessed is False
    assert session.response.closed is True


def test_requests_transport_joins_multi_value_headers_with_commas() -> None:
    session = StubSession(response=StubResponse())
    transport = RequestsHttpTransport(session=session)

    transport.send(
        HttpRequestData(
            url="https://api.ipgeolocation.io/v3/ipgeo?apiKey=k",
            method="GET",
            headers={"X-Test": ["one", "two"]},
            body=None,
            connect_timeout=1.0,
            read_timeout=2.0,
        )
    )

    assert session.last_request is not None
    assert session.last_request["headers"]["X-Test"] == "one, two"


def test_requests_transport_maps_timeout() -> None:
    session = StubSession(exception=requests.exceptions.Timeout())
    transport = RequestsHttpTransport(session=session)

    with pytest.raises(RequestTimeoutException, match="HTTP request timed out"):
        transport.send(
            HttpRequestData(
                url="https://api.ipgeolocation.io/v3/ipgeo",
                method="GET",
                headers={},
                body=None,
                connect_timeout=1.0,
                read_timeout=2.0,
            )
        )


def test_requests_transport_maps_request_exception() -> None:
    session = StubSession(exception=requests.exceptions.RequestException("boom"))
    transport = RequestsHttpTransport(session=session)

    with pytest.raises(TransportException, match="HTTP transport error"):
        transport.send(
            HttpRequestData(
                url="https://api.ipgeolocation.io/v3/ipgeo",
                method="GET",
                headers={},
                body=None,
                connect_timeout=1.0,
                read_timeout=2.0,
            )
        )


def test_requests_transport_maps_timeout_during_response_stream() -> None:
    session = StubSession(response=StubResponse(iter_exception=requests.exceptions.Timeout("boom")))
    transport = RequestsHttpTransport(session=session)

    with pytest.raises(RequestTimeoutException, match="HTTP request timed out"):
        transport.send(
            HttpRequestData(
                url="https://api.ipgeolocation.io/v3/ipgeo",
                method="GET",
                headers={},
                body=None,
                connect_timeout=1.0,
                read_timeout=2.0,
            )
        )


def test_requests_transport_maps_request_exception_during_response_stream() -> None:
    session = StubSession(
        response=StubResponse(iter_exception=requests.exceptions.RequestException("boom"))
    )
    transport = RequestsHttpTransport(session=session)

    with pytest.raises(TransportException, match="HTTP transport error"):
        transport.send(
            HttpRequestData(
                url="https://api.ipgeolocation.io/v3/ipgeo",
                method="GET",
                headers={},
                body=None,
                connect_timeout=1.0,
                read_timeout=2.0,
            )
        )


def test_requests_transport_rejects_oversized_response_body() -> None:
    session = StubSession(response=StubResponse(status_code=200, body="x" * 20))
    transport = RequestsHttpTransport(session=session, max_response_body_chars=10)

    with pytest.raises(TransportException, match="Response body exceeded max size"):
        transport.send(
            HttpRequestData(
                url="https://api.ipgeolocation.io/v3/ipgeo",
                method="GET",
                headers={},
                body=None,
                connect_timeout=1.0,
                read_timeout=2.0,
            )
        )

    assert session.response.content_accessed is False
    assert session.response.closed is True
