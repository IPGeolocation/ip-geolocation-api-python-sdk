"""Dataclass and JSON serialization helpers."""

from __future__ import annotations

import types
from collections.abc import Iterable as IterableABC
from collections.abc import Mapping as MappingABC
from collections.abc import Sequence as SequenceABC
from dataclasses import fields, is_dataclass
from enum import Enum
from functools import lru_cache
from typing import (
    Any,
    Dict,
    Iterable,
    Mapping,
    Optional,
    Sequence,
    Tuple,
    Type,
    TypeVar,
    Union,
    cast,
    get_args,
    get_origin,
    get_type_hints,
)

from .enums import JsonOutputMode

T = TypeVar("T")
FieldSpec = Tuple[str, str, Any]


def _is_optional(annotation: Any) -> bool:
    union_type = getattr(types, "UnionType", None)
    return get_origin(annotation) in (Union, union_type) and type(None) in get_args(annotation)


def _strip_optional(annotation: Any) -> Any:
    if not _is_optional(annotation):
        return annotation
    return next(arg for arg in get_args(annotation) if arg is not type(None))


@lru_cache(maxsize=None)
def _field_specs(cls: Any) -> Tuple[FieldSpec, ...]:
    type_hints = get_type_hints(cls)
    return tuple(
        (
            field.name,
            field.metadata.get("alias", field.name),
            type_hints.get(field.name, field.type),
        )
        for field in fields(cast(Any, cls))
    )


def from_mapping(cls: Type[T], data: Optional[Mapping[str, Any]]) -> Optional[T]:
    if data is None:
        return None
    if not isinstance(data, MappingABC):
        raise TypeError(f"Expected object for {cls.__name__}, got {type(data).__name__}")
    kwargs: Dict[str, Any] = {}
    for field_name, alias, annotation in _field_specs(cast(Any, cls)):
        raw_value = data.get(alias)
        kwargs[field_name] = _convert_value(annotation, raw_value)
    return cls(**kwargs)


def _convert_value(annotation: Any, value: Any) -> Any:
    is_optional = _is_optional(annotation)
    annotation = _strip_optional(annotation)
    origin = get_origin(annotation)

    if value is None:
        if origin is list:
            return []
        if origin in (tuple, Sequence, Iterable, SequenceABC, IterableABC):
            return ()
        return None

    if origin in (list, tuple, SequenceABC, IterableABC):
        if isinstance(value, (str, bytes, bytearray)) or not isinstance(value, IterableABC):
            raise TypeError(
                f"Expected array for {getattr(annotation, '__name__', annotation)}, "
                f"got {type(value).__name__}"
            )
        item_type = get_args(annotation)[0] if get_args(annotation) else Any
        converted = [_convert_value(item_type, item) for item in value]
        return tuple(converted) if origin is tuple else converted

    if isinstance(annotation, type) and issubclass(annotation, Enum):
        try:
            return annotation(value)
        except ValueError:
            if hasattr(annotation, "UNKNOWN"):
                return cast(Any, annotation).UNKNOWN
            raise

    if isinstance(annotation, type) and is_dataclass(annotation):
        if is_optional and isinstance(value, MappingABC) and not value:
            return None
        return from_mapping(annotation, value)

    if annotation is bool:
        return _coerce_bool(value)

    if annotation is int:
        return _coerce_int(value)

    if annotation is float:
        return _coerce_float(value)

    if annotation is str:
        return _coerce_str(value)

    return value


def _coerce_bool(value: Any) -> bool:
    if isinstance(value, bool):
        return value
    if isinstance(value, str):
        normalized = value.strip().lower()
        if normalized == "true":
            return True
        if normalized == "false":
            return False
    raise TypeError(f"Expected boolean value, got {type(value).__name__}")


def _coerce_int(value: Any) -> int:
    if isinstance(value, bool):
        raise TypeError("Expected integer value, got bool")
    if isinstance(value, int):
        return value
    if isinstance(value, float):
        if value.is_integer():
            return int(value)
        raise TypeError("Expected integer value, got float")
    if isinstance(value, str):
        normalized = value.strip()
        if not normalized:
            raise TypeError("Expected integer value, got blank string")
        try:
            return int(normalized)
        except ValueError as exc:
            raise TypeError("Expected integer value, got string") from exc
    raise TypeError(f"Expected integer value, got {type(value).__name__}")


def _coerce_float(value: Any) -> float:
    if isinstance(value, bool):
        raise TypeError("Expected numeric value, got bool")
    if isinstance(value, (int, float)):
        return float(value)
    if isinstance(value, str):
        normalized = value.strip()
        if not normalized:
            raise TypeError("Expected numeric value, got blank string")
        try:
            return float(normalized)
        except ValueError as exc:
            raise TypeError("Expected numeric value, got string") from exc
    raise TypeError(f"Expected numeric value, got {type(value).__name__}")


def _coerce_str(value: Any) -> str:
    if isinstance(value, str):
        return value
    if isinstance(value, (bytes, bytearray)):
        return value.decode("utf-8")
    raise TypeError(f"Expected string value, got {type(value).__name__}")


def to_plain_data(value: Any, mode: JsonOutputMode = JsonOutputMode.COMPACT) -> Any:
    if value is None:
        return None

    if isinstance(value, Enum):
        return value.value

    if is_dataclass(value):
        result = {}
        for field in fields(value):
            item = getattr(value, field.name)
            if item is None and mode == JsonOutputMode.COMPACT:
                continue
            key = field.metadata.get("alias", field.name)
            result[key] = to_plain_data(item, mode)
        return result

    if isinstance(value, Mapping):
        result = {}
        for key, item in value.items():
            if item is None and mode == JsonOutputMode.COMPACT:
                continue
            result[key] = to_plain_data(item, mode)
        return result

    if isinstance(value, (list, tuple)):
        return [to_plain_data(item, mode) for item in value]

    return value
