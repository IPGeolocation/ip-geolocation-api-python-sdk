"""Error-mapping behavior tests."""

from __future__ import annotations

import pytest

from ipgeolocation import (
    ApiException,
    BadRequestException,
    ClientClosedRequestException,
    IpGeolocationClient,
    IpGeolocationClientConfig,
    LockedException,
    LookupIpGeolocationRequest,
    MethodNotAllowedException,
    NotFoundException,
    PayloadTooLargeException,
    RateLimitException,
    ServerErrorException,
    UnauthorizedException,
    UnsupportedMediaTypeException,
)

from .test_support import TestTransport


@pytest.mark.parametrize(
    ("status_code", "expected_type"),
    [
        (400, BadRequestException),
        (401, UnauthorizedException),
        (403, ApiException),
        (404, NotFoundException),
        (405, MethodNotAllowedException),
        (413, PayloadTooLargeException),
        (415, UnsupportedMediaTypeException),
        (423, LockedException),
        (429, RateLimitException),
        (499, ClientClosedRequestException),
        (503, ServerErrorException),
    ],
)
def test_status_codes_map_to_expected_exceptions(status_code, expected_type) -> None:
    transport = TestTransport()
    transport.enqueue_response(status_code, '{"message":"error detail"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(expected_type, match=f"HTTP status {status_code}"):
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())


def test_preserves_api_error_details() -> None:
    transport = TestTransport()
    transport.enqueue_response(401, '{"message":"invalid key"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(ApiException) as exc:
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert exc.value.status_code == 401
    assert exc.value.api_message == "invalid key"


def test_preserves_nested_api_error_details() -> None:
    transport = TestTransport()
    transport.enqueue_response(401, '{"error":{"message":"invalid key"}}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(ApiException) as exc:
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert exc.value.status_code == 401
    assert exc.value.api_message == "invalid key"


def test_exception_messages_do_not_expose_configured_api_keys() -> None:
    api_key = "secret-api-key"
    transport = TestTransport()
    transport.enqueue_response(401, '{"message":"invalid key"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key=api_key), transport=transport)
    with pytest.raises(ApiException) as exc:
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert api_key not in str(exc.value)
    assert api_key not in (exc.value.api_message or "")


def test_non_json_error_body_is_truncated() -> None:
    transport = TestTransport()
    transport.enqueue_response(400, "x" * 700)

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(BadRequestException) as exc:
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert len(exc.value.api_message) == 512
    assert "HTTP status 400" in str(exc.value)


def test_empty_error_body_uses_generic_status_message() -> None:
    transport = TestTransport()
    transport.enqueue_response(400, "")

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(BadRequestException) as exc:
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert exc.value.api_message is None
    assert str(exc.value) == "API request failed with HTTP status 400"


def test_short_non_json_error_body_is_exposed_without_truncation() -> None:
    transport = TestTransport()
    transport.enqueue_response(400, "plain-error-body")

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(BadRequestException) as exc:
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert exc.value.api_message == "plain-error-body"
    assert "plain-error-body" in str(exc.value)
