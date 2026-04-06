"""Request-building behavior tests."""

from __future__ import annotations

from ipgeolocation import (
    BulkLookupIpGeolocationRequest,
    IpGeolocationClient,
    IpGeolocationClientConfig,
    Language,
    LookupIpGeolocationRequest,
    ResponseFormat,
)

from .test_support import TestTransport


def test_lookup_builds_expected_query_and_headers() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

    client = IpGeolocationClient(
        IpGeolocationClientConfig(
            api_key="test-key",
            base_url="https://api.ipgeolocation.io/",
            connect_timeout=2,
            read_timeout=4,
        ),
        transport=transport,
    )

    client.lookup_ip_geolocation(
        LookupIpGeolocationRequest(
            ip="8.8.8.8",
            lang=Language.EN,
            include=["security"],
            fields=["location.city"],
            excludes=["currency"],
            output=ResponseFormat.JSON,
        )
    )

    sent = transport.captured_requests[0]
    assert sent.url.startswith("https://api.ipgeolocation.io/v3/ipgeo?")
    assert "apiKey=test-key" in sent.url
    assert "ip=8.8.8.8" in sent.url
    assert "lang=en" in sent.url
    assert "include=security" in sent.url
    assert "fields=location.city" in sent.url
    assert "excludes=currency" in sent.url
    assert "output=json" in sent.url
    assert sent.first_header_value("User-Agent") == IpGeolocationClient.default_user_agent()
    assert sent.first_header_value("Accept") == "application/json"
    assert sent.connect_timeout == 2
    assert sent.read_timeout == 4


def test_bulk_lookup_builds_payload_and_path() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '[{"ip":"8.8.8.8"}]')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="bulk-key"), transport=transport)
    client.bulk_lookup_ip_geolocation(BulkLookupIpGeolocationRequest(ips=["8.8.8.8", "1.1.1.1"]))

    sent = transport.captured_requests[0]
    assert sent.url.startswith("https://api.ipgeolocation.io/v3/ipgeo-bulk?")
    assert "apiKey=bulk-key" in sent.url
    assert sent.first_header_value("Content-Type") == "application/json"
    assert sent.first_header_value("Accept") == "application/json"
    assert sent.body == '{"ips":["8.8.8.8","1.1.1.1"]}'


def test_lookup_uses_request_origin_when_config_has_no_api_key() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

    client = IpGeolocationClient(
        IpGeolocationClientConfig(request_origin="https://app.example.com"),
        transport=transport,
    )
    client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))

    assert "apiKey=" not in transport.captured_requests[0].url
    assert (
        transport.captured_requests[0].first_header_value("Origin")
        == "https://app.example.com"
    )


def test_bulk_lookup_includes_optional_query_params_when_configured() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '[{"ip":"8.8.8.8"}]')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="bulk-key"), transport=transport)
    client.bulk_lookup_ip_geolocation(
        BulkLookupIpGeolocationRequest(
            ips=["8.8.8.8"],
            lang=Language.DE,
            include=["hostname"],
            fields=["location.city"],
            excludes=["currency"],
        )
    )

    sent = transport.captured_requests[0]
    assert "apiKey=bulk-key" in sent.url
    assert "lang=de" in sent.url
    assert "include=hostname" in sent.url
    assert "fields=location.city" in sent.url
    assert "excludes=currency" in sent.url


def test_lookup_does_not_infer_include_values_from_fields() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.lookup_ip_geolocation(
        LookupIpGeolocationRequest(ip="8.8.8.8", fields=["security.threat_score"])
    )

    sent = transport.captured_requests[0]
    assert "fields=security.threat_score" in sent.url
    assert "include=" not in sent.url


def test_lookup_treats_blank_ip_as_omitted() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"1.2.3.4"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="   "))

    assert "ip=" not in transport.captured_requests[0].url


def test_sdk_managed_headers_are_set_by_default() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))

    sent = transport.captured_requests[0]
    assert sent.first_header_value("User-Agent") == IpGeolocationClient.default_user_agent()
    assert sent.first_header_value("Accept") == "application/json"


def test_lookup_request_headers_are_merged_case_insensitively() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

    client = IpGeolocationClient(
        IpGeolocationClientConfig(api_key="k", request_origin="https://app.example.com"),
        transport=transport,
    )
    client.lookup_ip_geolocation(
        LookupIpGeolocationRequest(
            ip="8.8.8.8",
            headers={
                "origin": "https://override.example.com",
                "X-Trace-Id": ["trace-1", "trace-2"],
                "accept": "text/plain",
                "user-agent": "custom-ua",
            },
        )
    )

    sent = transport.captured_requests[0]
    assert sent.first_header_value("Origin") == "https://override.example.com"
    assert sent.headers["X-Trace-Id"] == ["trace-1", "trace-2"]
    assert sent.first_header_value("Accept") == "application/json"
    assert sent.first_header_value("User-Agent") == "custom-ua"


def test_bulk_request_headers_include_request_origin_and_custom_headers() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '[{"ip":"8.8.8.8"}]')

    client = IpGeolocationClient(
        IpGeolocationClientConfig(api_key="k", request_origin="https://app.example.com"),
        transport=transport,
    )
    client.bulk_lookup_ip_geolocation(
        BulkLookupIpGeolocationRequest(
            ips=["8.8.8.8"],
            headers={
                "X-Trace-Id": "trace-9",
                "Content-Type": "text/plain",
                "User-Agent": "bulk-custom-ua",
            },
        )
    )

    sent = transport.captured_requests[0]
    assert sent.first_header_value("Origin") == "https://app.example.com"
    assert sent.first_header_value("X-Trace-Id") == "trace-9"
    assert sent.first_header_value("Content-Type") == "application/json"
    assert sent.first_header_value("User-Agent") == "bulk-custom-ua"


def test_default_user_agent_includes_resolved_version() -> None:
    assert IpGeolocationClient.default_user_agent().startswith("ipgeolocation-python-sdk/")
    assert "${" not in IpGeolocationClient.default_user_agent()


def test_lookup_request_user_agent_overrides_sdk_default() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.lookup_ip_geolocation(
        LookupIpGeolocationRequest(ip="8.8.8.8", user_agent="python-requests/2.32.5")
    )

    assert (
        transport.captured_requests[0].first_header_value("User-Agent")
        == "python-requests/2.32.5"
    )


def test_lookup_request_user_agent_field_overrides_custom_header() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.lookup_ip_geolocation(
        LookupIpGeolocationRequest(
            ip="8.8.8.8",
            user_agent="field-user-agent",
            headers={"User-Agent": "header-user-agent"},
        )
    )

    assert transport.captured_requests[0].first_header_value("User-Agent") == "field-user-agent"


def test_bulk_request_user_agent_overrides_sdk_default() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '[{"ip":"8.8.8.8"}]')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.bulk_lookup_ip_geolocation(
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], user_agent="python-requests/2.32.5")
    )

    assert (
        transport.captured_requests[0].first_header_value("User-Agent")
        == "python-requests/2.32.5"
    )


def test_raw_single_lookup_with_xml_sets_output_and_accept_headers() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, "<ipgeo><ip>8.8.8.8</ip></ipgeo>")

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.lookup_ip_geolocation_raw(
        LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
    )

    sent = transport.captured_requests[0]
    assert "output=xml" in sent.url
    assert sent.first_header_value("Accept") == "application/xml"


def test_raw_bulk_lookup_with_xml_sets_output_and_accept_headers() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, "<items><item><ip>8.8.8.8</ip></item></items>")

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.bulk_lookup_ip_geolocation_raw(
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], output=ResponseFormat.XML)
    )

    sent = transport.captured_requests[0]
    assert "output=xml" in sent.url
    assert sent.first_header_value("Accept") == "application/xml"
