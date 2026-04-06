"""Request models for single and bulk IPGeolocation lookups."""

from __future__ import annotations

from collections.abc import Mapping as MappingABC
from collections.abc import Sequence as SequenceABC
from dataclasses import dataclass
from types import MappingProxyType
from typing import Dict, Iterable, Mapping, Optional, Sequence, Tuple, Union

from .enums import Language, ResponseFormat
from .exceptions import ValidationException

HeaderValue = Union[str, Sequence[str]]


def _normalize_tokens(
    values: Optional[Iterable[str]],
    field: str,
) -> Tuple[str, ...]:
    """Normalize token sequences and reject blank entries."""
    if values is None:
        return ()
    if isinstance(values, (str, bytes)):
        raise ValidationException(f"{field} must be a sequence of strings, not a single string")
    normalized = []
    for value in values:
        if not isinstance(value, str):
            raise ValidationException(f"{field} value must be a string")
        normalized_value = value.strip()
        if not normalized_value:
            raise ValidationException(f"{field} value must not be blank")
        normalized.append(normalized_value)
    return tuple(normalized)


def _normalize_language(value: Optional[Union[Language, str]]) -> Optional[Language]:
    """Normalize language values to ``Language`` enums."""
    if value is None or isinstance(value, Language):
        return value
    if not isinstance(value, str):
        raise ValidationException("lang must be a Language or string")
    try:
        return Language.from_code(value.strip())
    except ValueError as exc:
        raise ValidationException(str(exc)) from exc


def _normalize_output(value: Optional[Union[ResponseFormat, str]]) -> ResponseFormat:
    """Normalize output values to ``ResponseFormat`` enums."""
    if value is None:
        return ResponseFormat.JSON
    if isinstance(value, ResponseFormat):
        return value
    if not isinstance(value, str):
        raise ValidationException("output must be a ResponseFormat or string")
    try:
        return ResponseFormat(value.strip().lower())
    except ValueError as exc:
        raise ValidationException("output must be either 'json' or 'xml'") from exc


def _normalize_headers(
    value: Optional[Mapping[str, HeaderValue]],
) -> Mapping[str, Tuple[str, ...]]:
    """Normalize request headers into an immutable mapping."""
    if value is None:
        return MappingProxyType({})
    if not isinstance(value, MappingABC):
        raise ValidationException("headers must be a mapping of header names to strings")

    normalized: Dict[str, Tuple[str, ...]] = {}
    for raw_name, raw_value in value.items():
        if not isinstance(raw_name, str):
            raise ValidationException("headers name must be a string")
        name = raw_name.strip()
        if not name:
            raise ValidationException("headers name must not be blank")
        if any(char in name for char in "\r\n"):
            raise ValidationException("headers name must not contain CR or LF")
        normalized[name] = _normalize_header_values(raw_value)
    return MappingProxyType(normalized)


def _normalize_header_values(value: HeaderValue) -> Tuple[str, ...]:
    raw_values: Tuple[str, ...]
    if isinstance(value, str):
        raw_values = (value,)
    elif isinstance(value, (bytes, bytearray)) or not isinstance(value, SequenceABC):
        raise ValidationException("headers value must be a string or sequence of strings")
    else:
        raw_values = tuple(value)
    if not raw_values:
        raise ValidationException("headers value must not be empty")

    normalized_values = []
    for raw_item in raw_values:
        if not isinstance(raw_item, str):
            raise ValidationException("headers value must contain only strings")
        item = raw_item.strip()
        if not item:
            raise ValidationException("headers value must not contain blank strings")
        if any(char in item for char in "\r\n"):
            raise ValidationException("headers value must not contain CR or LF")
        normalized_values.append(item)
    return tuple(normalized_values)


@dataclass(frozen=True)
class LookupIpGeolocationRequest:
    """Parameters for a typed or raw single lookup request."""

    ip: Optional[str] = None
    lang: Optional[Union[Language, str]] = None
    include: Optional[Sequence[str]] = None
    fields: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None
    user_agent: Optional[str] = None
    headers: Optional[Mapping[str, HeaderValue]] = None
    output: Optional[Union[ResponseFormat, str]] = ResponseFormat.JSON

    def __post_init__(self) -> None:
        if self.ip is not None and not isinstance(self.ip, str):
            raise ValidationException("ip must be a string")
        normalized_ip = None if self.ip is None or not self.ip.strip() else self.ip.strip()
        object.__setattr__(self, "ip", normalized_ip)
        object.__setattr__(self, "lang", _normalize_language(self.lang))
        object.__setattr__(self, "include", _normalize_tokens(self.include, "include"))
        object.__setattr__(self, "fields", _normalize_tokens(self.fields, "fields"))
        object.__setattr__(self, "excludes", _normalize_tokens(self.excludes, "excludes"))
        if self.user_agent is not None and not isinstance(self.user_agent, str):
            raise ValidationException("user_agent must be a string")
        if self.user_agent is not None and not self.user_agent.strip():
            raise ValidationException("user_agent must not be blank")
        normalized_user_agent = None if self.user_agent is None else self.user_agent.strip()
        object.__setattr__(self, "user_agent", normalized_user_agent)
        object.__setattr__(self, "headers", _normalize_headers(self.headers))
        object.__setattr__(self, "output", _normalize_output(self.output))


@dataclass(frozen=True)
class BulkLookupIpGeolocationRequest:
    """Parameters for a typed or raw bulk lookup request."""

    ips: Sequence[str]
    lang: Optional[Union[Language, str]] = None
    include: Optional[Sequence[str]] = None
    fields: Optional[Sequence[str]] = None
    excludes: Optional[Sequence[str]] = None
    user_agent: Optional[str] = None
    headers: Optional[Mapping[str, HeaderValue]] = None
    output: Optional[Union[ResponseFormat, str]] = ResponseFormat.JSON

    def __post_init__(self) -> None:
        object.__setattr__(self, "ips", _normalize_tokens(self.ips, "ips"))
        if not self.ips:
            raise ValidationException("ips must not be empty")
        if len(self.ips) > 50_000:
            raise ValidationException("ips must contain at most 50000 entries")
        object.__setattr__(self, "lang", _normalize_language(self.lang))
        object.__setattr__(self, "include", _normalize_tokens(self.include, "include"))
        object.__setattr__(self, "fields", _normalize_tokens(self.fields, "fields"))
        object.__setattr__(self, "excludes", _normalize_tokens(self.excludes, "excludes"))
        if self.user_agent is not None and not isinstance(self.user_agent, str):
            raise ValidationException("user_agent must be a string")
        if self.user_agent is not None and not self.user_agent.strip():
            raise ValidationException("user_agent must not be blank")
        normalized_user_agent = None if self.user_agent is None else self.user_agent.strip()
        object.__setattr__(self, "user_agent", normalized_user_agent)
        object.__setattr__(self, "headers", _normalize_headers(self.headers))
        object.__setattr__(self, "output", _normalize_output(self.output))
