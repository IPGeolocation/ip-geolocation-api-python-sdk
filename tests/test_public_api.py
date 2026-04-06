"""Public API surface tests."""

from __future__ import annotations

from importlib import resources

import pytest

import ipgeolocation


def test_location_confidence_is_exported() -> None:
    assert "LocationConfidence" in ipgeolocation.__all__
    assert ipgeolocation.LocationConfidence.HIGH.value == "high"


def test_async_client_is_exported() -> None:
    assert "AsyncIpGeolocationClient" in ipgeolocation.__all__
    assert ipgeolocation.AsyncIpGeolocationClient.__name__ == "AsyncIpGeolocationClient"


def test_bulk_lookup_error_details_is_exported() -> None:
    assert "BulkLookupErrorDetails" in ipgeolocation.__all__
    assert ipgeolocation.BulkLookupErrorDetails.__name__ == "BulkLookupErrorDetails"


def test_typed_package_marker_exists() -> None:
    marker = resources.files("ipgeolocation").joinpath("py.typed")
    assert marker.is_file()


def test_language_from_code_is_case_insensitive() -> None:
    assert ipgeolocation.Language.from_code("EN") == ipgeolocation.Language.EN
    assert ipgeolocation.Language.from_code("pT") == ipgeolocation.Language.PT


def test_language_from_code_rejects_unsupported_language() -> None:
    with pytest.raises(ValueError, match="Unsupported language code: zz"):
        ipgeolocation.Language.from_code("zz")
