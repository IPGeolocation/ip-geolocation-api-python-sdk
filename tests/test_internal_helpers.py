"""Internal helper coverage tests."""

from __future__ import annotations

from dataclasses import dataclass
from enum import Enum
from importlib import metadata
from pathlib import Path
from typing import List, Mapping, Optional

import pytest

import ipgeolocation._serde as serde_module
from ipgeolocation._serde import from_mapping, to_plain_data
from ipgeolocation._transport import HttpRequestData, RequestsHttpTransport, _extract_headers
from ipgeolocation._version import FALLBACK_VERSION, _load_local_version, get_version
from ipgeolocation.enums import JsonOutputMode

from .test_transport import StubResponse, StubSession


class UnknownCapableEnum(str, Enum):
    """Local enum for testing UNKNOWN fallback behavior."""

    KNOWN = "known"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class EnumContainer:
    """Local dataclass used to test enum conversion."""

    value: Optional[UnknownCapableEnum] = None


@dataclass(frozen=True)
class ListContainer:
    """Local dataclass used to test list normalization."""

    items: Optional[List[str]] = None


@dataclass(frozen=True)
class ScalarContainer:
    """Local dataclass used to test scalar coercion."""

    text: Optional[str] = None
    flag: Optional[bool] = None
    number: Optional[float] = None


@dataclass(frozen=True)
class NestedContainer:
    """Local dataclass used to test optional nested object handling."""

    text: Optional[str] = None


@dataclass(frozen=True)
class OptionalNestedContainer:
    """Local dataclass used to test empty optional nested objects."""

    nested: Optional[NestedContainer] = None


def test_from_mapping_returns_none_for_none_input() -> None:
    assert from_mapping(ListContainer, None) is None


def test_from_mapping_uses_unknown_enum_fallback() -> None:
    parsed = from_mapping(EnumContainer, {"value": "unexpected"})

    assert parsed is not None
    assert parsed.value == UnknownCapableEnum.UNKNOWN


def test_from_mapping_normalizes_null_list_fields_to_empty_list() -> None:
    parsed = from_mapping(ListContainer, {"items": None})

    assert parsed is not None
    assert parsed.items == []


def test_from_mapping_coerces_scalar_values_to_declared_types() -> None:
    parsed = from_mapping(ScalarContainer, {"text": "8.8", "flag": "true", "number": "1.5"})

    assert parsed is not None
    assert parsed.text == "8.8"
    assert parsed.flag is True
    assert parsed.number == 1.5


def test_from_mapping_treats_empty_optional_dataclass_as_none() -> None:
    parsed = from_mapping(OptionalNestedContainer, {"nested": {}})

    assert parsed is not None
    assert parsed.nested is None


def test_from_mapping_rejects_non_string_value_for_string_field() -> None:
    with pytest.raises(TypeError, match="Expected string value, got float"):
        from_mapping(ScalarContainer, {"text": 8.8})


def test_from_mapping_rejects_invalid_boolean_string() -> None:
    with pytest.raises(TypeError, match="Expected boolean value"):
        from_mapping(ScalarContainer, {"flag": "maybe"})


def test_from_mapping_caches_field_specs(monkeypatch: pytest.MonkeyPatch) -> None:
    serde_module._field_specs.cache_clear()
    original_get_type_hints = serde_module.get_type_hints
    calls = 0

    def counting_get_type_hints(cls):
        nonlocal calls
        calls += 1
        return original_get_type_hints(cls)

    monkeypatch.setattr(serde_module, "get_type_hints", counting_get_type_hints)

    from_mapping(ScalarContainer, {"text": "a"})
    from_mapping(ScalarContainer, {"text": "b"})

    assert calls == 1
    serde_module._field_specs.cache_clear()


def test_to_plain_data_handles_mappings_in_compact_and_full_modes() -> None:
    value: Mapping[str, object] = {"a": 1, "b": None}

    assert to_plain_data(value) == {"a": 1}
    assert to_plain_data(value, JsonOutputMode.FULL) == {"a": 1, "b": None}


def test_http_request_data_returns_none_for_missing_header() -> None:
    request = HttpRequestData(
        url="https://api.ipgeolocation.io/v3/ipgeo",
        method="GET",
        headers={"User-Agent": ["ua"]},
        body=None,
        connect_timeout=1.0,
        read_timeout=2.0,
    )

    assert request.first_header_value("Accept") is None


def test_requests_transport_rejects_invalid_response_cap() -> None:
    with pytest.raises(ValueError, match="max_response_body_chars must be greater than zero"):
        RequestsHttpTransport(max_response_body_chars=0)


def test_requests_transport_closes_owned_session(monkeypatch: pytest.MonkeyPatch) -> None:
    owned_session = StubSession(response=StubResponse())

    monkeypatch.setattr("ipgeolocation._transport.requests.Session", lambda: owned_session)
    transport = RequestsHttpTransport()
    transport.close()

    assert owned_session.closed is True


def test_requests_transport_does_not_close_external_session() -> None:
    external_session = StubSession(response=StubResponse())
    transport = RequestsHttpTransport(session=external_session)
    transport.close()

    assert external_session.closed is False


def test_extract_headers_falls_back_to_response_headers_when_raw_headers_are_unavailable() -> None:
    response = StubResponse(headers={"X-Trace-Id": ["trace-1"]})
    response.raw = None

    assert _extract_headers(response) == {"X-Trace-Id": ["trace-1"]}


def test_extract_headers_falls_back_to_response_headers_when_raw_headers_raise() -> None:
    response = StubResponse(headers={"X-Trace-Id": ["trace-2"]})

    class BrokenRawHeaders:
        def keys(self):
            raise RuntimeError("boom")

    response.raw = type("Raw", (), {"headers": BrokenRawHeaders()})()

    assert _extract_headers(response) == {"X-Trace-Id": ["trace-2"]}


def test_get_version_returns_installed_value(monkeypatch: pytest.MonkeyPatch) -> None:
    monkeypatch.setattr("ipgeolocation._version.metadata.version", lambda _: "9.9.9")

    assert get_version() == "9.9.9"


def test_get_version_uses_legacy_distribution_name_when_primary_name_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def fake_version(name: str) -> str:
        if name == "ipgeolocationio":
            raise metadata.PackageNotFoundError
        if name == "ipgeolocation-sdk":
            return "9.9.9"
        raise AssertionError(f"Unexpected package name: {name}")

    monkeypatch.setattr("ipgeolocation._version.metadata.version", fake_version)

    assert get_version() == "9.9.9"


def test_load_local_version_matches_project_metadata() -> None:
    project_version = next(
        line.split('"')[1]
        for line in Path("pyproject.toml").read_text(encoding="utf-8").splitlines()
        if line.startswith("version = ")
    )
    assert _load_local_version() == project_version


def test_get_version_reads_pyproject_when_package_metadata_is_missing(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_package_not_found(_: str) -> str:
        raise metadata.PackageNotFoundError

    monkeypatch.setattr("ipgeolocation._version.metadata.version", raise_package_not_found)

    assert get_version() == _load_local_version()


def test_get_version_uses_fallback_when_local_version_cannot_be_loaded(
    monkeypatch: pytest.MonkeyPatch,
) -> None:
    def raise_package_not_found(_: str) -> str:
        raise metadata.PackageNotFoundError

    monkeypatch.setattr("ipgeolocation._version.metadata.version", raise_package_not_found)
    monkeypatch.setattr("ipgeolocation._version._load_local_version", lambda: FALLBACK_VERSION)

    assert get_version() == FALLBACK_VERSION
