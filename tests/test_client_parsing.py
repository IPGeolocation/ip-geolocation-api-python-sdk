"""Response parsing behavior tests."""

from __future__ import annotations

import pytest

from ipgeolocation import (
    BulkLookupError,
    BulkLookupIpGeolocationRequest,
    BulkLookupSuccess,
    IpGeolocationClient,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
    ResponseFormat,
    SerializationException,
)

from .test_support import TestTransport, headers


def test_parses_single_lookup_response_and_metadata() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        (
            '{"ip":"91.128.103.196",'
            '"location":{"country_name":"Sweden","is_eu":true,"confidence":"high"},'
            '"time_zone":{"name":"Europe/Stockholm","is_dst":false,'
            '"current_tz_abbreviation":"CET",'
            '"current_tz_full_name":"Central European Standard Time"}}'
        ),
        headers("X-Credits-Charged", "1", "X-Trace-Id", "trace-1"),
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert response.data.ip == "91.128.103.196"
    assert response.data.location.country_name == "Sweden"
    assert response.data.location.is_eu is True
    assert response.data.location.confidence.value == "high"
    assert response.data.time_zone.current_tz_abbreviation == "CET"
    assert response.data.time_zone.current_tz_full_name == "Central European Standard Time"
    assert response.metadata.credits_charged == 1
    assert response.metadata.status_code == 200
    assert response.metadata.duration_ms >= 0


def test_parses_bulk_one_of_items() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        (
            '['
            '{"ip":"8.8.8.8","location":{"country_name":"United States"}},'
            '{"message":"\'10.0.0.1\' is a bogon IP address."}'
            "]"
        ),
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.bulk_lookup_ip_geolocation(
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8", "10.0.0.1"])
    )

    assert len(response.data) == 2
    assert isinstance(response.data[0], BulkLookupSuccess)
    assert response.data[0].data.ip == "8.8.8.8"
    assert isinstance(response.data[1], BulkLookupError)
    assert response.data[1].error.message is not None
    assert "bogon" in response.data[1].error.message


def test_parses_headers_case_insensitively_and_ignores_malformed_numeric_values() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        '{"ip":"8.8.8.8"}',
        headers("x-credits-charged", "not-a-number", "x-trace-id", "trace-2"),
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert response.metadata.credits_charged is None
    assert response.metadata.status_code == 200


def test_metadata_headers_are_read_only() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}', headers("X-Trace-Id", "trace-2"))

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    with pytest.raises(TypeError):
        response.metadata.raw_headers["X-Other"] = ("value",)


def test_bulk_typed_response_rejects_non_array_payload() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(SerializationException, match="expected an array payload"):
        client.bulk_lookup_ip_geolocation(BulkLookupIpGeolocationRequest(ips=["8.8.8.8"]))


def test_single_typed_response_rejects_malformed_json() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, "{malformed-json")

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(SerializationException, match="Failed to deserialize API response"):
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())


def test_bulk_typed_response_rejects_malformed_json() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, "[{")

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(SerializationException, match="Failed to deserialize bulk lookup response"):
        client.bulk_lookup_ip_geolocation(BulkLookupIpGeolocationRequest(ips=["8.8.8.8"]))


def test_single_typed_response_rejects_invalid_nested_object_shape() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8","location":"bad"}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(SerializationException, match="Failed to deserialize API response"):
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())


def test_bulk_typed_response_rejects_invalid_nested_object_shape() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '[{"ip":"8.8.8.8","location":"bad"}]')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(SerializationException, match="Failed to deserialize API response"):
        client.bulk_lookup_ip_geolocation(BulkLookupIpGeolocationRequest(ips=["8.8.8.8"]))


def test_handles_empty_headers_from_transport() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}', {})

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert response.metadata.credits_charged is None
    assert response.metadata.successful_records is None
    assert response.metadata.raw_headers == {}
    assert response.metadata.status_code == 200


def test_blank_credits_header_value_is_ignored() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":"8.8.8.8"}', headers("X-Credits-Charged", " "))

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert response.metadata.credits_charged is None


def test_bulk_entry_containing_message_and_ip_is_treated_as_success() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        (
            '[{"ip":"8.8.8.8","message":"ignored-message",'
            '"location":{"country_name":"United States"}}]'
        ),
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.bulk_lookup_ip_geolocation(BulkLookupIpGeolocationRequest(ips=["8.8.8.8"]))

    assert len(response.data) == 1
    assert isinstance(response.data[0], BulkLookupSuccess)
    assert response.data[0].data.ip == "8.8.8.8"


def test_null_collection_fields_become_empty_tuples() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        (
            '{"ip":"8.8.8.8",'
            '"security":{"proxy_provider_names":null,"vpn_provider_names":null},'
            '"abuse":{"emails":null,"phone_numbers":null},'
            '"country_metadata":{"languages":null}}'
        ),
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert response.data.security is not None
    assert response.data.security.proxy_provider_names == ()
    assert response.data.security.vpn_provider_names == ()
    assert response.data.abuse is not None
    assert response.data.abuse.emails == ()
    assert response.data.abuse.phone_numbers == ()
    assert response.data.country_metadata is not None
    assert response.data.country_metadata.languages == ()


def test_typed_response_coerces_string_scalars_for_numeric_and_boolean_fields() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        (
            '{"ip":"8.8.8.8",'
            '"security":{"is_vpn":"false","threat_score":"7.2"},'
            '"time_zone":{"offset":"1.5","current_time_unix":"1740000000"}}'
        ),
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert response.data.ip == "8.8.8.8"
    assert response.data.security is not None
    assert response.data.security.is_vpn is False
    assert response.data.security.threat_score == 7.2
    assert response.data.time_zone is not None
    assert response.data.time_zone.offset == 1.5
    assert response.data.time_zone.current_time_unix == 1740000000.0


def test_empty_optional_dst_transition_objects_become_none() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        (
            '{"ip":"1.1.1.1",'
            '"time_zone":{"name":"Australia/Brisbane","dst_exists":false,'
            '"dst_start":{},"dst_end":{}}}'
        ),
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert response.data.time_zone is not None
    assert response.data.time_zone.dst_exists is False
    assert response.data.time_zone.dst_start is None
    assert response.data.time_zone.dst_end is None


def test_single_typed_response_rejects_non_string_ip_value() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"ip":8.8}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(SerializationException, match="Failed to deserialize API response"):
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())


def test_single_typed_response_rejects_invalid_scalar_value() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, '{"security":{"is_vpn":"maybe"}}')

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    with pytest.raises(SerializationException, match="Failed to deserialize API response"):
        client.lookup_ip_geolocation(LookupIpGeolocationRequest())


def test_unknown_location_confidence_falls_back_to_unknown() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        '{"ip":"8.8.8.8","location":{"confidence":"very_high"}}',
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    assert response.data.location is not None
    assert response.data.location.confidence.value == "unknown"


def test_raw_single_returns_xml_body_without_deserialization() -> None:
    transport = TestTransport()
    transport.enqueue_response(
        200,
        (
            "<ipgeo><ip>8.8.8.8</ip><location>"
            "<country_name>United States</country_name></location></ipgeo>"
        ),
        headers("X-Credits-Charged", "1"),
    )

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.lookup_ip_geolocation_raw(
        LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
    )

    assert response.data.startswith("<ipgeo>")
    assert response.metadata.credits_charged == 1


def test_raw_bulk_returns_xml_body_without_deserialization() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, "<items><item><ip>8.8.8.8</ip></item></items>")

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    response = client.bulk_lookup_ip_geolocation_raw(
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], output=ResponseFormat.XML)
    )

    assert response.data.startswith("<items>")
