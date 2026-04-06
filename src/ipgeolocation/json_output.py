"""JSON serialization helpers for SDK objects."""

from __future__ import annotations

import json
from typing import Any

from ._serde import to_plain_data
from .enums import JsonOutputMode
from .exceptions import SerializationException


def to_json(value: Any, mode: JsonOutputMode = JsonOutputMode.COMPACT) -> str:
    """Serialize a value as compact JSON."""
    return _write(value, mode, pretty=False)


def to_pretty_json(value: Any, mode: JsonOutputMode = JsonOutputMode.COMPACT) -> str:
    """Serialize a value as pretty JSON."""
    return _write(value, mode, pretty=True)


def _write(value: Any, mode: JsonOutputMode, pretty: bool) -> str:
    normalized_mode = _normalize_mode(mode)
    try:
        payload = to_plain_data(value, normalized_mode)
        if pretty:
            return json.dumps(payload, indent=2, ensure_ascii=False, sort_keys=False)
        return json.dumps(payload, ensure_ascii=False, separators=(",", ":"))
    except Exception as exc:  # pragma: no cover - defensive
        raise SerializationException("Failed to serialize output as JSON") from exc


def _normalize_mode(mode: Any) -> JsonOutputMode:
    if mode is None:
        raise TypeError("mode must not be None")
    if isinstance(mode, JsonOutputMode):
        return mode
    if isinstance(mode, str):
        try:
            return JsonOutputMode(mode.strip().lower())
        except ValueError as exc:
            raise ValueError("mode must be either 'compact' or 'full'") from exc
    raise TypeError("mode must be a JsonOutputMode or string")
