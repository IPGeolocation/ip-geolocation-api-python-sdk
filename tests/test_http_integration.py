"""Exercise both SDK transports against a local Postman simulation."""

from __future__ import annotations

import asyncio
import json
import os
import shutil
import signal
import subprocess
import time
from pathlib import Path

import pytest

from ipgeolocation import (
    ApiException,
    AsyncIpGeolocationClient,
    BulkLookupError,
    BulkLookupIpGeolocationRequest,
    BulkLookupSuccess,
    IpGeolocationClient,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
    RateLimitException,
    RequestTimeoutException,
    SerializationException,
    ServerErrorException,
    TransportException,
    UnauthorizedException,
)
from ipgeolocation._transport import HttpRequestData, HttpxAsyncTransport, RequestsHttpTransport

TEST_KEY = "TEST_KEY &+?=#%"


@pytest.fixture(scope="module")
def api_url(tmp_path_factory):
    postman = shutil.which("postman")
    if postman is None or os.name != "posix":
        pytest.skip("HTTP integration tests require Postman CLI on Linux or macOS")
    log_path = tmp_path_factory.mktemp("simulation") / "requests.ndjson"
    with log_path.open("w") as output, pytest.MonkeyPatch.context() as env:
        env.setenv("NO_PROXY", "localhost,127.0.0.1")
        process = subprocess.Popen(
            [
                postman,
                "simulation",
                "run",
                "postman/simulations/python-sdk/python-sdk.sim.yaml",
                "--port",
                "auto",
                "--no-history",
                "--output",
                "ndjson",
            ],
            cwd=Path(__file__).resolve().parents[1],
            stdout=output,
            stderr=subprocess.STDOUT,
            start_new_session=True,
        )
        try:
            deadline = time.monotonic() + 20
            while time.monotonic() < deadline:
                for line in log_path.read_text().splitlines():
                    try:
                        event = json.loads(line)
                    except json.JSONDecodeError:
                        continue
                    if event.get("event") == "listening":
                        yield event["mocks"][0]["address"]
                        assert '"event":"request"' in log_path.read_text(errors="replace")
                        return
                assert process.poll() is None, log_path.read_text()
                time.sleep(0.1)
            pytest.fail("Postman simulation did not start: " + log_path.read_text())
        finally:
            try:
                os.killpg(process.pid, signal.SIGINT)
            except ProcessLookupError:
                pass
            try:
                process.wait(timeout=5)
            except subprocess.TimeoutExpired:
                process.kill()
                process.wait(timeout=5)


@pytest.fixture(params=[IpGeolocationClient, AsyncIpGeolocationClient], ids=["requests", "httpx"])
def client_type(request):
    return request.param


def _call(client_type, api_url, method, request, *, api_key=TEST_KEY, origin=None, timeout=1):
    config = IpGeolocationClientConfig(
        api_key=api_key,
        request_origin=origin,
        base_url=api_url,
        connect_timeout=min(0.1, timeout),
        read_timeout=timeout,
    )
    if client_type is AsyncIpGeolocationClient:

        async def run():
            async with client_type(config) as client:
                return await getattr(client, method)(request)

        return asyncio.run(run())
    with client_type(config) as client:
        return getattr(client, method)(request)


def test_http_lookup(client_type, api_url):
    result = _call(
        client_type,
        api_url,
        "lookup_ip_geolocation",
        LookupIpGeolocationRequest(ip="2001:db8::1", include=["security"]),
    )
    assert result.data.ip == "2001:db8::1"
    assert result.data.location.city == "Test City"
    assert result.metadata.status_code == 200
    assert result.metadata.credits_charged == 1
    assert result.metadata.header_values("x-credits-charged") == ("1",)
    assert result.metadata.first_header_value("X-CREDITS-CHARGED") == "1"


def test_http_raw_lookup_preserves_query_and_headers(client_type, api_url):
    result = _call(
        client_type,
        api_url,
        "lookup_ip_geolocation_raw",
        LookupIpGeolocationRequest(
            ip="8.8.8.8", fields=["location.city"], headers={"X-Request-Test": "kept"}
        ),
    )
    request = json.loads(result.data)["_request"]
    assert request["query"]["apiKey"] == TEST_KEY
    assert request["query"]["fields"] == "location.city"
    assert request["headers"]["x-request-test"] == "kept"
    assert request["headers"]["user-agent"] == client_type.default_user_agent()


def test_http_bulk_lookup(client_type, api_url):
    result = _call(
        client_type,
        api_url,
        "bulk_lookup_ip_geolocation",
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8", "invalid-ip"]),
    )
    assert isinstance(result.data[0], BulkLookupSuccess)
    assert result.data[0].data.ip == "8.8.8.8"
    assert isinstance(result.data[1], BulkLookupError)
    assert result.data[1].error.message == "IP address not found"


def test_http_raw_bulk_lookup(client_type, api_url):
    result = _call(
        client_type,
        api_url,
        "bulk_lookup_ip_geolocation_raw",
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8", "invalid-ip"]),
    )
    request = json.loads(result.data)[0]["_request"]
    assert request["method"] == "POST"
    assert request["body"] == {"ips": ["8.8.8.8", "invalid-ip"]}


@pytest.mark.parametrize(
    "key,exception,status",
    [
        ("BAD_KEY", UnauthorizedException, 401),
        ("FORBIDDEN", ApiException, 403),
        ("RATE_LIMIT", RateLimitException, 429),
        ("SERVER_ERROR", ServerErrorException, 503),
    ],
)
def test_http_errors(client_type, api_url, key, exception, status):
    with pytest.raises(exception) as error:
        _call(
            client_type,
            api_url,
            "lookup_ip_geolocation",
            LookupIpGeolocationRequest(ip="8.8.8.8"),
            api_key=key,
        )
    assert error.value.status_code == status
    assert error.value.api_message == f"Test failure for {key}"


def test_http_invalid_json(client_type, api_url):
    with pytest.raises(SerializationException):
        _call(
            client_type,
            api_url,
            "lookup_ip_geolocation",
            LookupIpGeolocationRequest(ip="8.8.8.8"),
            api_key="BAD_JSON",
        )


def test_http_unknown_encoding_falls_back_to_utf8(client_type, api_url):
    result = _call(
        client_type,
        api_url,
        "lookup_ip_geolocation",
        LookupIpGeolocationRequest(ip="8.8.8.8"),
        api_key="BAD_ENCODING",
    )
    assert result.data.location.city == "東京"


def test_http_timeout(client_type, api_url):
    with pytest.raises(RequestTimeoutException):
        _call(
            client_type,
            api_url,
            "lookup_ip_geolocation",
            LookupIpGeolocationRequest(ip="8.8.8.8"),
            api_key="SLOW_REQUEST",
            timeout=0.05,
        )


def test_http_origin_authentication(client_type, api_url):
    result = _call(
        client_type,
        api_url,
        "lookup_ip_geolocation",
        LookupIpGeolocationRequest(ip="8.8.8.8"),
        api_key=None,
        origin="https://app.example.test",
    )
    assert result.data.ip == "8.8.8.8"


def test_http_streaming_size_limit(client_type, api_url):
    request = HttpRequestData(
        url=f"{api_url}/v3/ipgeo?apiKey=LARGE_RESPONSE",
        method="GET",
        headers={},
        body=None,
        connect_timeout=0.1,
        read_timeout=1,
    )
    if client_type is AsyncIpGeolocationClient:

        async def run():
            transport = HttpxAsyncTransport(max_response_body_chars=128)
            try:
                with pytest.raises(TransportException, match="Response body exceeded max size"):
                    await transport.send(request)
            finally:
                await transport.close()

        asyncio.run(run())
    else:
        transport = RequestsHttpTransport(max_response_body_chars=128)
        try:
            with pytest.raises(TransportException, match="Response body exceeded max size"):
                transport.send(request)
        finally:
            transport.close()
