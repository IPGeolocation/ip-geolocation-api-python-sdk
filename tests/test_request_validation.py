"""Request validation tests."""

from __future__ import annotations

import pytest

from ipgeolocation import (
    BulkLookupIpGeolocationRequest,
    IpGeolocationClient,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
    ResponseFormat,
    ValidationException,
)

from .test_support import TestTransport


def test_bulk_request_rejects_empty_ip_list() -> None:
    with pytest.raises(ValidationException, match="ips must not be empty"):
        BulkLookupIpGeolocationRequest(ips=[])


def test_typed_lookup_rejects_xml_output() -> None:
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=TestTransport())
    with pytest.raises(ValidationException, match="XML output is not supported"):
        client.lookup_ip_geolocation(LookupIpGeolocationRequest(output=ResponseFormat.XML))


def test_typed_bulk_rejects_xml_output() -> None:
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=TestTransport())
    with pytest.raises(ValidationException, match="XML output is not supported"):
        client.bulk_lookup_ip_geolocation(
            BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], output=ResponseFormat.XML)
        )


def test_raw_methods_allow_xml_output() -> None:
    transport = TestTransport()
    transport.enqueue_response(200, "<ipgeo><ip>8.8.8.8</ip></ipgeo>")
    transport.enqueue_response(200, "<items><item><ip>8.8.8.8</ip></item></items>")

    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=transport)
    client.lookup_ip_geolocation_raw(
        LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
    )
    client.bulk_lookup_ip_geolocation_raw(
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], output=ResponseFormat.XML)
    )


def test_lookup_rejects_null_request() -> None:
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=TestTransport())
    with pytest.raises(ValidationException, match="request must not be null"):
        client.lookup_ip_geolocation(None)


def test_lookup_rejects_missing_api_key_and_request_origin_before_sending() -> None:
    transport = TestTransport()
    client = IpGeolocationClient(IpGeolocationClientConfig(), transport=transport)

    with pytest.raises(
        ValidationException,
        match="single lookup requires apiKey or request_origin",
    ):
        client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))

    assert transport.captured_requests == []


def test_single_lookup_request_rejects_blank_include_value() -> None:
    with pytest.raises(ValidationException, match="include value must not be blank"):
        LookupIpGeolocationRequest(include=[" "])


def test_single_lookup_request_rejects_string_include_value() -> None:
    with pytest.raises(ValidationException, match="include must be a sequence of strings"):
        LookupIpGeolocationRequest(include="security")


def test_single_lookup_request_rejects_non_string_include_value() -> None:
    with pytest.raises(ValidationException, match="include value must be a string"):
        LookupIpGeolocationRequest(include=[1])


def test_single_lookup_request_rejects_string_fields_value() -> None:
    with pytest.raises(ValidationException, match="fields must be a sequence of strings"):
        LookupIpGeolocationRequest(fields="location.city")


def test_single_lookup_request_rejects_non_string_ip_value() -> None:
    with pytest.raises(ValidationException, match="ip must be a string"):
        LookupIpGeolocationRequest(ip=123)


def test_single_lookup_request_rejects_blank_user_agent() -> None:
    with pytest.raises(ValidationException, match="user_agent must not be blank"):
        LookupIpGeolocationRequest(user_agent=" ")


def test_single_lookup_request_rejects_non_string_user_agent() -> None:
    with pytest.raises(ValidationException, match="user_agent must be a string"):
        LookupIpGeolocationRequest(user_agent=123)


def test_single_lookup_request_rejects_non_mapping_headers() -> None:
    with pytest.raises(ValidationException, match="headers must be a mapping"):
        LookupIpGeolocationRequest(headers=["x-test"])


def test_single_lookup_request_rejects_blank_header_name() -> None:
    with pytest.raises(ValidationException, match="headers name must not be blank"):
        LookupIpGeolocationRequest(headers={" ": "v"})


def test_single_lookup_request_rejects_blank_header_value() -> None:
    with pytest.raises(ValidationException, match="headers value must not contain blank strings"):
        LookupIpGeolocationRequest(headers={"X-Test": ["ok", " "]})


def test_single_lookup_request_rejects_header_values_with_newlines() -> None:
    with pytest.raises(ValidationException, match="headers value must not contain CR or LF"):
        LookupIpGeolocationRequest(headers={"X-Test": "bad\r\nvalue"})


def test_bulk_rejects_null_request() -> None:
    client = IpGeolocationClient(IpGeolocationClientConfig(api_key="k"), transport=TestTransport())
    with pytest.raises(ValidationException, match="request must not be null"):
        client.bulk_lookup_ip_geolocation(None)


def test_typed_bulk_rejects_missing_api_key_before_sending() -> None:
    transport = TestTransport()
    client = IpGeolocationClient(IpGeolocationClientConfig(), transport=transport)

    with pytest.raises(ValidationException, match="bulk lookup requires apiKey"):
        client.bulk_lookup_ip_geolocation(BulkLookupIpGeolocationRequest(ips=["8.8.8.8"]))

    assert transport.captured_requests == []


def test_raw_bulk_rejects_missing_api_key_before_sending() -> None:
    transport = TestTransport()
    client = IpGeolocationClient(IpGeolocationClientConfig(), transport=transport)

    with pytest.raises(ValidationException, match="bulk lookup requires apiKey"):
        client.bulk_lookup_ip_geolocation_raw(BulkLookupIpGeolocationRequest(ips=["8.8.8.8"]))

    assert transport.captured_requests == []


def test_lookup_request_normalizes_surrounding_whitespace() -> None:
    request = LookupIpGeolocationRequest(
        ip=" 8.8.8.8 ",
        lang=" en ",
        include=[" security ", " abuse "],
        fields=[" location.city "],
        excludes=[" currency "],
        user_agent=" python-requests/2.32.5 ",
        headers={" X-Test ": [" one ", " two "]},
        output=" json ",
    )

    assert request.ip == "8.8.8.8"
    assert request.lang.value == "en"
    assert request.include == ("security", "abuse")
    assert request.fields == ("location.city",)
    assert request.excludes == ("currency",)
    assert request.user_agent == "python-requests/2.32.5"
    assert dict(request.headers) == {"X-Test": ("one", "two")}
    assert request.output == ResponseFormat.JSON


def test_bulk_request_normalizes_surrounding_whitespace() -> None:
    request = BulkLookupIpGeolocationRequest(
        ips=[" 8.8.8.8 ", " 1.1.1.1 "],
        lang=" de ",
        include=[" hostname "],
        fields=[" location.city "],
        excludes=[" currency "],
        user_agent=" python-requests/2.32.5 ",
        headers={" X-Test ": " value "},
        output=" json ",
    )

    assert request.ips == ("8.8.8.8", "1.1.1.1")
    assert request.lang.value == "de"
    assert request.include == ("hostname",)
    assert request.fields == ("location.city",)
    assert request.excludes == ("currency",)
    assert request.user_agent == "python-requests/2.32.5"
    assert dict(request.headers) == {"X-Test": ("value",)}
    assert request.output == ResponseFormat.JSON


def test_bulk_request_rejects_string_ips_value() -> None:
    with pytest.raises(ValidationException, match="ips must be a sequence of strings"):
        BulkLookupIpGeolocationRequest(ips="8.8.8.8")


def test_bulk_request_rejects_non_string_ip_value() -> None:
    with pytest.raises(ValidationException, match="ips value must be a string"):
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8", 1])


def test_lookup_request_rejects_unsupported_language_string() -> None:
    with pytest.raises(ValidationException, match="Unsupported language code: zz"):
        LookupIpGeolocationRequest(lang="zz")


def test_lookup_request_rejects_non_string_language_value() -> None:
    with pytest.raises(ValidationException, match="lang must be a Language or string"):
        LookupIpGeolocationRequest(lang=123)


def test_lookup_request_rejects_unsupported_output_string() -> None:
    with pytest.raises(ValidationException, match="output must be either 'json' or 'xml'"):
        LookupIpGeolocationRequest(output="yaml")


def test_lookup_request_rejects_non_string_output_value() -> None:
    with pytest.raises(ValidationException, match="output must be a ResponseFormat or string"):
        LookupIpGeolocationRequest(output=123)


def test_bulk_request_rejects_unsupported_language_string() -> None:
    with pytest.raises(ValidationException, match="Unsupported language code: zz"):
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], lang="zz")


def test_bulk_request_rejects_non_string_language_value() -> None:
    with pytest.raises(ValidationException, match="lang must be a Language or string"):
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], lang=123)


def test_bulk_request_rejects_unsupported_output_string() -> None:
    with pytest.raises(ValidationException, match="output must be either 'json' or 'xml'"):
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], output="yaml")


def test_bulk_request_rejects_non_string_output_value() -> None:
    with pytest.raises(ValidationException, match="output must be a ResponseFormat or string"):
        BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], output=123)
