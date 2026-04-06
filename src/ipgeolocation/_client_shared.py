"""Shared helpers for sync and async IPGeolocation clients."""

from __future__ import annotations

import json
from typing import Any, Dict, List, Mapping, Optional, Sequence, cast
from urllib.parse import quote

from ._serde import from_mapping
from .enums import ResponseFormat
from .exceptions import (
    ApiException,
    BadRequestException,
    ClientClosedRequestException,
    LockedException,
    MethodNotAllowedException,
    NotFoundException,
    PayloadTooLargeException,
    RateLimitException,
    SerializationException,
    ServerErrorException,
    UnauthorizedException,
    UnsupportedMediaTypeException,
    ValidationException,
)
from .models import (
    ApiResponseMetadata,
    BulkLookupError,
    BulkLookupErrorDetails,
    BulkLookupResult,
    BulkLookupSuccess,
    IpGeolocationResponse,
)


def validate_json_output(output: Optional[ResponseFormat]) -> None:
    if (output or ResponseFormat.JSON) == ResponseFormat.XML:
        raise ValidationException(
            "XML output is not supported by typed methods. Use ResponseFormat.JSON."
        )


def build_query(params: Mapping[str, Optional[str]]) -> str:
    items = []
    for key, value in params.items():
        if key is None or not str(key).strip() or value is None or not str(value).strip():
            continue
        items.append(f"{quote(str(key), safe='')}={quote(str(value), safe='')}")
    return "" if not items else "?" + "&".join(items)


def merge_headers(*header_maps: Mapping[str, Sequence[str]]) -> Dict[str, List[str]]:
    """Merge headers case-insensitively, letting later maps override earlier ones."""
    merged: Dict[str, List[str]] = {}
    names_by_lower: Dict[str, str] = {}
    for header_map in header_maps:
        for raw_name, raw_values in header_map.items():
            if raw_name is None or not str(raw_name).strip():
                continue
            name = str(raw_name).strip()
            existing_name = names_by_lower.get(name.lower())
            if existing_name is not None and existing_name != name:
                del merged[existing_name]
            names_by_lower[name.lower()] = name
            merged[name] = [value for value in raw_values]
    return merged


def resolve_user_agent_header(
    request_user_agent: Optional[str],
    request_headers: Mapping[str, Sequence[str]],
    default_user_agent: str,
) -> List[str]:
    """Pick the outbound User-Agent header value for a request."""
    if request_user_agent is not None:
        return [request_user_agent]
    custom_values = header_values_ignore_case(request_headers, "User-Agent")
    if custom_values:
        return list(custom_values)
    return [default_user_agent]


def parse_single_lookup(body: str) -> IpGeolocationResponse:
    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise SerializationException("Failed to deserialize API response") from exc
    if not isinstance(payload, dict):
        raise SerializationException("Failed to deserialize API response")
    try:
        parsed = from_mapping(IpGeolocationResponse, cast(Mapping[str, Any], payload))
    except (TypeError, ValueError) as exc:
        raise SerializationException("Failed to deserialize API response") from exc
    if parsed is None:  # pragma: no cover - defensive
        raise SerializationException("Failed to deserialize API response")
    return parsed


def parse_bulk_lookup(body: str) -> List[BulkLookupResult]:
    try:
        payload = json.loads(body)
    except json.JSONDecodeError as exc:
        raise SerializationException("Failed to deserialize bulk lookup response") from exc
    if not isinstance(payload, list):
        raise SerializationException(
            "Failed to deserialize bulk response: expected an array payload"
        )
    results: List[BulkLookupResult] = []
    for item in payload:
        if isinstance(item, dict) and "message" in item and "ip" not in item:
            results.append(
                BulkLookupError(
                    error=BulkLookupErrorDetails(message=_string_or_none(item.get("message")))
                )
            )
        else:
            if not isinstance(item, Mapping):
                raise SerializationException("Failed to deserialize API response")
            try:
                parsed_item = from_mapping(IpGeolocationResponse, cast(Mapping[str, Any], item))
            except (TypeError, ValueError) as exc:
                raise SerializationException("Failed to deserialize API response") from exc
            if parsed_item is None:  # pragma: no cover - defensive
                raise SerializationException("Failed to deserialize API response")
            results.append(BulkLookupSuccess(data=parsed_item))
    return results


def to_api_exception(status_code: int, body: str) -> ApiException:
    api_message = extract_api_message(body)
    if api_message:
        message = f"API request failed with HTTP status {status_code}: {api_message}"
    else:
        message = f"API request failed with HTTP status {status_code}"

    mapping = {
        400: BadRequestException,
        401: UnauthorizedException,
        404: NotFoundException,
        405: MethodNotAllowedException,
        413: PayloadTooLargeException,
        415: UnsupportedMediaTypeException,
        423: LockedException,
        429: RateLimitException,
        499: ClientClosedRequestException,
    }
    exception_type = mapping.get(status_code)
    if exception_type is None and 500 <= status_code <= 599:
        exception_type = ServerErrorException
    if exception_type is None:
        exception_type = ApiException
    return exception_type(message, status_code, api_message)


def extract_api_message(body: Optional[str]) -> Optional[str]:
    if body is None or not str(body).strip():
        return None
    try:
        payload = json.loads(body)
    except json.JSONDecodeError:
        return body[:512]
    if isinstance(payload, Mapping):
        message = payload.get("message")
        if message is None:
            error = payload.get("error")
            if isinstance(error, Mapping):
                message = error.get("message")
        return _string_or_none(message)
    return body[:512]


def _string_or_none(value: Any) -> Optional[str]:
    if value is None:
        return None
    return str(value)


def parse_int_header(value: Optional[str]) -> Optional[int]:
    if value is None or not str(value).strip():
        return None
    try:
        return int(str(value).strip())
    except ValueError:
        return None


def to_metadata(
    status_code: int,
    duration_ms: int,
    raw_headers: Optional[Mapping[str, Sequence[str]]],
) -> ApiResponseMetadata:
    headers = {
        key: tuple(values or ())
        for key, values in (raw_headers or {}).items()
        if key is not None
    }
    credits = parse_int_header(first_header_ignore_case(headers, "X-Credits-Charged"))
    success_count = parse_int_header(first_header_ignore_case(headers, "X-Successful-Record"))
    return ApiResponseMetadata(
        credits_charged=credits,
        successful_records=success_count,
        status_code=status_code,
        duration_ms=duration_ms,
        raw_headers=headers,
    )


def header_values_ignore_case(
    headers: Mapping[str, Sequence[str]],
    name: str,
) -> Optional[Sequence[str]]:
    for key, values in headers.items():
        if key.lower() == name.lower():
            return values
    return None


def first_header_ignore_case(
    headers: Mapping[str, Sequence[str]],
    name: str,
) -> Optional[str]:
    values = header_values_ignore_case(headers, name)
    if values:
        return values[0]
    return None
