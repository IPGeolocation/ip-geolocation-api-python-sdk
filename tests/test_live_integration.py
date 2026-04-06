"""Optional live integration tests."""

from __future__ import annotations

import os

import pytest

from ipgeolocation import (
    BulkLookupError,
    BulkLookupIpGeolocationRequest,
    BulkLookupSuccess,
    IpGeolocationClient,
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


def test_free_plan_base_lookup_works() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=FREE_KEY)) as client:
        response = client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))
        assert response.data.ip == "8.8.8.8"
        assert response.metadata.credits_charged >= 1
        assert response.data.network is None
        assert response.data.company is None
        assert response.data.asn is not None
        assert response.data.asn.type is None
        assert response.data.time_zone is not None
        assert response.data.time_zone.current_tz_abbreviation
        assert response.data.time_zone.current_tz_full_name


def test_free_plan_domain_lookup_is_rejected() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=FREE_KEY)) as client:
        with pytest.raises(UnauthorizedException) as exc:
            client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="ipgeolocation.io"))
        assert exc.value.status_code == 401


def test_paid_plan_request_origin_auth_works_without_api_key() -> None:
    if not REQUEST_ORIGIN:
        pytest.skip("Set IPGEO_REQUEST_ORIGIN to an allowlisted origin to enable this test")

    with IpGeolocationClient(
        IpGeolocationClientConfig(request_origin=REQUEST_ORIGIN)
    ) as client:
        response = client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))
        assert response.data.ip == "8.8.8.8"
        assert response.metadata.credits_charged >= 1


@pytest.mark.parametrize(
    "include_value",
    [
        "security",
        "abuse",
        "user_agent",
        "geo_accuracy",
        "dma_code",
        "hostname",
        "liveHostname",
        "hostnameFallbackLive",
    ],
)
def test_free_plan_restricted_modules_are_rejected(include_value: str) -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=FREE_KEY)) as client:
        with pytest.raises(UnauthorizedException) as exc:
            client.lookup_ip_geolocation(
                LookupIpGeolocationRequest(ip="8.8.8.8", include=[include_value])
            )
        assert exc.value.status_code == 401


def test_free_plan_include_star_returns_default_response_without_additional_modules() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=FREE_KEY)) as client:
        response = client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(ip="8.8.8.8", include=["*"])
        )
        assert response.data.ip == "8.8.8.8"
        assert response.data.security is None
        assert response.data.abuse is None
        assert response.data.user_agent is None
        assert response.data.hostname is None


def test_free_plan_bulk_is_rejected() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=FREE_KEY)) as client:
        with pytest.raises(UnauthorizedException):
            client.bulk_lookup_ip_geolocation(BulkLookupIpGeolocationRequest(ips=["8.8.8.8"]))


def test_paid_plan_security_and_abuse_works() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
        response = client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(ip="8.8.8.8", include=["security", "abuse"])
        )
        assert response.data.security is not None
        assert response.data.abuse is not None
        assert response.metadata.credits_charged >= 4


@pytest.mark.parametrize("field_name", ["security", "abuse"])
def test_paid_plan_optional_module_fields_still_require_include(field_name: str) -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
        response = client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(ip="8.8.8.8", fields=[field_name])
        )
        assert getattr(response.data, field_name) is None
        assert response.data.location is not None
        assert response.metadata.credits_charged == 1


def test_paid_plan_bulk_mixed_returns_success_and_error_items() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
        response = client.bulk_lookup_ip_geolocation(
            BulkLookupIpGeolocationRequest(ips=["8.8.8.8", "invalid-ip"])
        )
        assert len(response.data) == 2
        assert isinstance(response.data[0], BulkLookupSuccess)
        assert response.data[0].data.ip == "8.8.8.8"
        assert isinstance(response.data[1], BulkLookupError)
        assert response.data[1].error.message


def test_paid_plan_xml_output_is_rejected_for_typed_method() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
        with pytest.raises(ValidationException, match="XML output is not supported"):
            client.lookup_ip_geolocation(
                LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
            )


def test_paid_plan_include_user_agent_reflects_request_user_agent_override() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
        default_ua_response = client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(ip="8.8.8.8", include=["user_agent"])
        )
        override_user_agent = "python-requests/2.32.5"
        overridden_ua_response = client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(
                ip="8.8.8.8",
                include=["user_agent"],
                user_agent=override_user_agent,
            )
        )
        assert default_ua_response.data.user_agent is not None
        assert default_ua_response.data.user_agent.user_agent_string
        assert overridden_ua_response.data.user_agent is not None
        assert overridden_ua_response.data.user_agent.user_agent_string == override_user_agent
        assert (
            overridden_ua_response.data.user_agent.user_agent_string
            != default_ua_response.data.user_agent.user_agent_string
        )


def test_paid_plan_raw_methods_return_xml_when_requested() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
        single = client.lookup_ip_geolocation_raw(
            LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
        )
        assert "<" in single.data

        bulk = client.bulk_lookup_ip_geolocation_raw(
            BulkLookupIpGeolocationRequest(
                ips=["8.8.8.8", "invalid-ip"],
                output=ResponseFormat.XML,
            )
        )
        assert "<" in bulk.data
