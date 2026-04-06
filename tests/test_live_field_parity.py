"""Optional live hardening tests that compare raw JSON to typed models."""

from __future__ import annotations

import json
import os
from decimal import Decimal
from typing import Any

import pytest

from ipgeolocation import (
    BulkLookupError,
    BulkLookupIpGeolocationRequest,
    BulkLookupSuccess,
    IpGeolocationClient,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
    to_json,
)

RUN_LIVE_HARDENING = os.getenv("IPGEO_RUN_LIVE_HARDENING", "").lower() == "true"
PAID_KEY = os.getenv("IPGEO_PAID_KEY")

pytestmark = pytest.mark.skipif(
    not RUN_LIVE_HARDENING or not PAID_KEY,
    reason="Set IPGEO_RUN_LIVE_HARDENING=true and IPGEO_PAID_KEY to enable live field parity tests",
)


def test_include_star_response_matches_typed_model() -> None:
    _assert_single_lookup_parity(LookupIpGeolocationRequest(ip="8.8.8.8", include=["*"]))


def test_geo_accuracy_and_dma_response_matches_typed_model() -> None:
    _assert_single_lookup_parity(
        LookupIpGeolocationRequest(ip="8.8.8.8", include=["geo_accuracy", "dma_code"])
    )


def test_domain_lookup_response_matches_typed_model() -> None:
    _assert_single_lookup_parity(
        LookupIpGeolocationRequest(ip="ipgeolocation.io", include=["hostnameFallbackLive"])
    )


def test_security_abuse_and_user_agent_response_matches_typed_model() -> None:
    _assert_single_lookup_parity(
        LookupIpGeolocationRequest(
            ip="8.8.8.8",
            include=["security", "abuse", "user_agent"],
            user_agent=(
                "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) "
                "AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
            ),
        )
    )


def test_bulk_mixed_response_matches_typed_model() -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
        request = BulkLookupIpGeolocationRequest(ips=["8.8.8.8", "invalid-ip", "1.1.1.1"])
        raw = client.bulk_lookup_ip_geolocation_raw(request)
        typed = client.bulk_lookup_ip_geolocation(request)

        raw_array = json.loads(raw.data)
        assert isinstance(raw_array, list)
        assert len(typed.data) == len(raw_array)

        for index, raw_item in enumerate(raw_array):
            typed_item = typed.data[index]
            if isinstance(typed_item, BulkLookupSuccess):
                assert_json_subset(raw_item, json.loads(to_json(typed_item.data)), "$[%d]" % index)
            else:
                assert isinstance(typed_item, BulkLookupError)
                assert raw_item.get("message") == typed_item.error.message


def _assert_single_lookup_parity(request: LookupIpGeolocationRequest) -> None:
    with IpGeolocationClient(IpGeolocationClientConfig(api_key=PAID_KEY)) as client:
        raw = client.lookup_ip_geolocation_raw(request)
        typed = client.lookup_ip_geolocation(request)

        raw_node = json.loads(raw.data)
        typed_node = json.loads(to_json(typed.data))
        assert_json_subset(raw_node, typed_node, "$")


def assert_json_subset(raw_node: Any, typed_node: Any, path: str) -> None:
    if raw_node is None:
        assert typed_node is None, path
        return

    assert typed_node is not None, path

    if _is_live_clock_field(path):
        assert typed_node is not None, path
        return

    if isinstance(raw_node, dict):
        assert isinstance(typed_node, dict), path
        for key, value in raw_node.items():
            child_path = path + "." + key
            if key not in typed_node and _is_omittable_empty_object(value, child_path):
                continue
            assert key in typed_node, child_path
            assert_json_subset(value, typed_node[key], child_path)
        return

    if isinstance(raw_node, list):
        assert isinstance(typed_node, list), path
        assert len(typed_node) == len(raw_node), path + " size"
        for index, item in enumerate(raw_node):
            assert_json_subset(item, typed_node[index], "%s[%d]" % (path, index))
        return

    if isinstance(raw_node, bool) and isinstance(typed_node, bool):
        assert typed_node == raw_node, path
        return

    if isinstance(raw_node, (int, float)) and isinstance(typed_node, (int, float)):
        assert Decimal(str(typed_node)).normalize() == Decimal(str(raw_node)).normalize(), path
        return

    assert typed_node == raw_node, path


def _is_live_clock_field(path: str) -> bool:
    return path.endswith(".time_zone.current_time") or path.endswith(".time_zone.current_time_unix")


def _is_omittable_empty_object(raw_node: Any, path: str) -> bool:
    return raw_node == {} and path.endswith((".time_zone.dst_start", ".time_zone.dst_end"))
