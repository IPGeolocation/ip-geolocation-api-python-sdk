"""Client configuration for the IPGeolocation API."""

from __future__ import annotations

import math
from dataclasses import dataclass
from datetime import timedelta
from typing import Optional, Union
from urllib.parse import urlparse

TimeoutValue = Union[float, int, timedelta]


def _coerce_timeout_seconds(value: TimeoutValue, field: str) -> float:
    """Normalize timeout values to seconds and validate they are positive."""
    if value is None:
        raise TypeError(f"{field} must not be None")
    if isinstance(value, timedelta):
        seconds = value.total_seconds()
    elif isinstance(value, bool) or not isinstance(value, (int, float)):
        raise TypeError(f"{field} must be a float, int, or timedelta")
    else:
        seconds = float(value)
    if not math.isfinite(seconds):
        raise ValueError(f"{field} must be finite")
    if seconds <= 0:
        raise ValueError(f"{field} must be greater than zero")
    return seconds


def _normalize_request_origin(value: Optional[str]) -> Optional[str]:
    if value is None:
        return None
    if not isinstance(value, str):
        raise TypeError("request_origin must be a string")

    normalized_value = value.strip()
    if not normalized_value:
        raise ValueError("request_origin must not be blank")
    if any(char in normalized_value for char in "\r\n"):
        raise ValueError("request_origin must not contain CR or LF")

    parsed_origin = urlparse(normalized_value)
    if parsed_origin.scheme not in {"http", "https"} or not parsed_origin.netloc:
        raise ValueError("request_origin must be an absolute http or https origin")
    if parsed_origin.path not in {"", "/"}:
        raise ValueError("request_origin must not include a path")
    if parsed_origin.params or parsed_origin.query or parsed_origin.fragment:
        raise ValueError("request_origin must not include params, query, or fragment")
    if parsed_origin.username is not None or parsed_origin.password is not None:
        raise ValueError("request_origin must not include userinfo")

    return f"{parsed_origin.scheme}://{parsed_origin.netloc}"


@dataclass(frozen=True)
class IpGeolocationClientConfig:
    """Immutable configuration for :class:`IpGeolocationClient`."""

    api_key: Optional[str] = None
    request_origin: Optional[str] = None
    base_url: str = "https://api.ipgeolocation.io"
    connect_timeout: TimeoutValue = 10.0
    read_timeout: TimeoutValue = 30.0

    def __post_init__(self) -> None:
        if self.api_key is not None and not isinstance(self.api_key, str):
            raise TypeError("api_key must be a string")
        normalized_api_key = None if self.api_key is None else self.api_key.strip()
        if normalized_api_key is not None and not normalized_api_key:
            raise ValueError("api_key must not be blank")
        normalized_request_origin = _normalize_request_origin(self.request_origin)
        if self.base_url is None:
            raise TypeError("base_url must not be None")
        if not isinstance(self.base_url, str):
            raise TypeError("base_url must be a string")
        normalized_base_url = self.base_url.strip()
        trimmed_base_url = normalized_base_url.rstrip("/")
        if not trimmed_base_url:
            raise ValueError("base_url must not be blank")
        parsed_base_url = urlparse(trimmed_base_url)
        if parsed_base_url.scheme not in {"http", "https"} or not parsed_base_url.netloc:
            raise ValueError("base_url must be an absolute http or https URL")
        if parsed_base_url.params or parsed_base_url.query or parsed_base_url.fragment:
            raise ValueError("base_url must not include params, query, or fragment")

        connect_timeout = _coerce_timeout_seconds(self.connect_timeout, "connect_timeout")
        read_timeout = _coerce_timeout_seconds(self.read_timeout, "read_timeout")
        if connect_timeout > read_timeout:
            raise ValueError("connect_timeout must be <= read_timeout")

        object.__setattr__(self, "api_key", normalized_api_key)
        object.__setattr__(self, "request_origin", normalized_request_origin)
        object.__setattr__(self, "base_url", trimmed_base_url)
        object.__setattr__(self, "connect_timeout", connect_timeout)
        object.__setattr__(self, "read_timeout", read_timeout)
