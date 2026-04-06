"""Model API behavior tests."""

from __future__ import annotations

import pytest

from ipgeolocation import BulkLookupResult


def test_bulk_lookup_result_is_abstract() -> None:
    with pytest.raises(TypeError):
        BulkLookupResult()
