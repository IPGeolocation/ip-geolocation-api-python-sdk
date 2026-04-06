"""Optional live async integration tests."""

from __future__ import annotations

import asyncio
import os

import pytest

from ipgeolocation import (
    AsyncIpGeolocationClient,
    BulkLookupError,
    BulkLookupIpGeolocationRequest,
    BulkLookupSuccess,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
    ResponseFormat,
    UnauthorizedException,
    ValidationException,
)

RUN_LIVE = os.getenv("IPGEO_RUN_LIVE_TESTS", "").lower() == "true"
FREE_KEY = os.getenv("IPGEO_FREE_KEY")
PAID_KEY = os.getenv("IPGEO_PAID_KEY")
REQUEST_ORIGIN = os.getenv("IPGEO_REQUEST_ORIGIN")

pytestmark = pytest.mark.skipif(
    not RUN_LIVE or not FREE_KEY or not PAID_KEY,
    reason="Set IPGEO_RUN_LIVE_TESTS=true, IPGEO_FREE_KEY, and IPGEO_PAID_KEY to enable live tests",
)


def _run(coro):
    return asyncio.run(coro)


def test_async_free_plan_base_lookup_works() -> None:
    async def scenario() -> None:
        async with AsyncIpGeolocationClient(IpGeolocationClientConfig(api_key=FREE_KEY)) as client:
            response = await client.lookup_ip_geolocation(
                LookupIpGeolocationRequest(ip="8.8.8.8")
            )
            assert response.data.ip == "8.8.8.8"
            assert response.metadata.credits_charged is not None
            assert response.metadata.credits_charged >= 1
            assert response.data.network is None
            assert response.data.company is None
            assert response.data.time_zone is not None

    _run(scenario())


def test_async_free_plan_domain_lookup_is_rejected() -> None:
    async def scenario() -> None:
        async with AsyncIpGeolocationClient(IpGeolocationClientConfig(api_key=FREE_KEY)) as client:
            with pytest.raises(UnauthorizedException) as exc:
                await client.lookup_ip_geolocation(
                    LookupIpGeolocationRequest(ip="ipgeolocation.io")
                )
            assert exc.value.status_code == 401

    _run(scenario())


def test_async_paid_plan_request_origin_auth_works_without_api_key() -> None:
    if not REQUEST_ORIGIN:
        pytest.skip("Set IPGEO_REQUEST_ORIGIN to an allowlisted origin to enable this test")

    async def scenario() -> None:
        async with AsyncIpGeolocationClient(
            IpGeolocationClientConfig(request_origin=REQUEST_ORIGIN)
        ) as client:
            response = await client.lookup_ip_geolocation(
                LookupIpGeolocationRequest(ip="8.8.8.8")
            )
            assert response.data.ip == "8.8.8.8"
            assert response.metadata.credits_charged is not None
            assert response.metadata.credits_charged >= 1

    _run(scenario())


def test_async_paid_plan_security_and_abuse_works() -> None:
    async def scenario() -> None:
        async with AsyncIpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
            response = await client.lookup_ip_geolocation(
                LookupIpGeolocationRequest(ip="8.8.8.8", include=["security", "abuse"])
            )
            assert response.data.security is not None
            assert response.data.abuse is not None
            assert response.metadata.credits_charged is not None
            assert response.metadata.credits_charged >= 4

    _run(scenario())


def test_async_paid_plan_bulk_mixed_returns_success_and_error_items() -> None:
    async def scenario() -> None:
        async with AsyncIpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
            response = await client.bulk_lookup_ip_geolocation(
                BulkLookupIpGeolocationRequest(ips=["8.8.8.8", "invalid-ip"])
            )
            assert len(response.data) == 2
            assert isinstance(response.data[0], BulkLookupSuccess)
            assert response.data[0].data.ip == "8.8.8.8"
            assert isinstance(response.data[1], BulkLookupError)
            assert response.data[1].error.message

    _run(scenario())


def test_async_paid_plan_xml_output_is_rejected_for_typed_method() -> None:
    async def scenario() -> None:
        async with AsyncIpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
            with pytest.raises(ValidationException, match="XML output is not supported"):
                await client.lookup_ip_geolocation(
                    LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
                )

    _run(scenario())


def test_async_paid_plan_raw_methods_return_xml_when_requested() -> None:
    async def scenario() -> None:
        async with AsyncIpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
            single = await client.lookup_ip_geolocation_raw(
                LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
            )
            assert "<" in single.data

            bulk = await client.bulk_lookup_ip_geolocation_raw(
                BulkLookupIpGeolocationRequest(
                    ips=["8.8.8.8", "invalid-ip"],
                    output=ResponseFormat.XML,
                )
            )
            assert "<" in bulk.data

    _run(scenario())
