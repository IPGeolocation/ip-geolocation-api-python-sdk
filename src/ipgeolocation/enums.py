"""Enums used by the SDK."""

from __future__ import annotations

from enum import Enum


class Language(str, Enum):
    """Language codes supported by the IPGeolocation API."""

    EN = "en"
    DE = "de"
    RU = "ru"
    JA = "ja"
    FR = "fr"
    CN = "cn"
    ES = "es"
    CS = "cs"
    IT = "it"
    KO = "ko"
    FA = "fa"
    PT = "pt"

    @classmethod
    def from_code(cls, code: str) -> "Language":
        for item in cls:
            if item.value.lower() == code.lower():
                return item
        raise ValueError(f"Unsupported language code: {code}")


class ResponseFormat(str, Enum):
    """Response formats supported by the API."""

    JSON = "json"
    XML = "xml"


class JsonOutputMode(str, Enum):
    """Controls whether null fields are emitted in JSON output."""

    COMPACT = "compact"
    FULL = "full"

