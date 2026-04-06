"""JSON output helper tests."""

from __future__ import annotations

import json

import pytest

from ipgeolocation import (
    IpGeolocationResponse,
    JsonOutputMode,
    LookupIpGeolocationRequest,
    TimeZoneInfo,
    to_json,
    to_pretty_json,
)


def test_to_json_uses_compact_mode_by_default() -> None:
    value = LookupIpGeolocationRequest(ip="8.8.8.8")
    parsed = json.loads(to_json(value))
    assert parsed == {
        "ip": "8.8.8.8",
        "include": [],
        "fields": [],
        "excludes": [],
        "headers": {},
        "output": "json",
    }


def test_full_mode_includes_nulls() -> None:
    value = LookupIpGeolocationRequest()
    parsed = json.loads(to_json(value, JsonOutputMode.FULL))
    assert "ip" in parsed
    assert "lang" in parsed
    assert parsed["output"] == "json"


def test_pretty_json_returns_indented_output() -> None:
    value = LookupIpGeolocationRequest(ip="8.8.8.8")
    output = to_pretty_json(value)
    assert "\n" in output
    assert '  "ip": "8.8.8.8"' in output


def test_full_mode_serializes_missing_dst_transitions_as_null() -> None:
    value = IpGeolocationResponse(
        time_zone=TimeZoneInfo(
            dst_tz_abbreviation="",
            dst_tz_full_name="",
            dst_start=None,
            dst_end=None,
        )
    )

    parsed = json.loads(to_pretty_json(value, JsonOutputMode.FULL))
    assert parsed["time_zone"]["dst_tz_abbreviation"] == ""
    assert parsed["time_zone"]["dst_tz_full_name"] == ""
    assert parsed["time_zone"]["dst_start"] is None
    assert parsed["time_zone"]["dst_end"] is None


def test_json_output_rejects_none_mode() -> None:
    with pytest.raises(TypeError, match="mode must not be None"):
        to_json(LookupIpGeolocationRequest(ip="8.8.8.8"), None)


def test_json_output_accepts_valid_string_mode() -> None:
    parsed = json.loads(to_json(LookupIpGeolocationRequest(), "full"))
    assert "ip" in parsed


def test_json_output_rejects_invalid_string_mode() -> None:
    with pytest.raises(ValueError, match="mode must be either 'compact' or 'full'"):
        to_json(LookupIpGeolocationRequest(ip="8.8.8.8"), "weird")


def test_json_output_rejects_non_string_non_enum_mode() -> None:
    with pytest.raises(TypeError, match="mode must be a JsonOutputMode or string"):
        to_pretty_json(LookupIpGeolocationRequest(ip="8.8.8.8"), 123)
