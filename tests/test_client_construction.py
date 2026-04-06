"""Client construction and lifecycle tests."""

from __future__ import annotations

import pytest

from ipgeolocation import (
    IpGeolocationClient,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
    ValidationException,
)


class CloseAwareTransport:
    def __init__(self) -> None:
        self.closed = False

    def send(self, request):  # pragma: no cover - not used in these tests
        raise AssertionError("send should not be called")

    def close(self) -> None:
        self.closed = True


class FalseyTransport(CloseAwareTransport):
    def __bool__(self) -> bool:
        return False


def test_client_constructs_with_default_transport() -> None:
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"))
    client.close()


def test_client_does_not_close_injected_transport() -> None:
    transport = CloseAwareTransport()
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)

    client.close()

    assert transport.closed is False


def test_client_preserves_falsey_injected_transport() -> None:
    transport = FalseyTransport()
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)

    assert client._transport is transport


def test_closed_client_rejects_future_requests() -> None:
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"))
    client.close()

    with pytest.raises(ValidationException, match="client is closed"):
        client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))


def test_closed_client_rejects_reentering_context_manager() -> None:
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"))
    client.close()

    with pytest.raises(ValidationException, match="client is closed"):
        with client:
            raise AssertionError("context body should not run")
