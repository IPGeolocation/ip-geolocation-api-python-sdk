"""Typed response models for the IPGeolocation API."""

from __future__ import annotations

from abc import ABC, abstractmethod
from dataclasses import dataclass, field
from enum import Enum
from types import MappingProxyType
from typing import Generic, Mapping, Optional, Tuple, TypeVar

T = TypeVar("T")


@dataclass(frozen=True)
class ApiResponseMetadata:
    """Response metadata extracted from headers and SDK timing."""

    credits_charged: Optional[int]
    successful_records: Optional[int]
    status_code: int
    duration_ms: int
    raw_headers: Mapping[str, Tuple[str, ...]]

    def __post_init__(self) -> None:
        if self.status_code < 100 or self.status_code > 599:
            raise ValueError("status_code must be between 100 and 599")
        if self.duration_ms < 0:
            raise ValueError("duration_ms must be >= 0")
        normalized = {
            key: tuple(values or ())
            for key, values in (self.raw_headers or {}).items()
            if key is not None
        }
        object.__setattr__(self, "raw_headers", MappingProxyType(normalized))

    def header_values(self, name: str) -> Tuple[str, ...]:
        """Return all values for a response header using case-insensitive lookup."""
        if name is None or not str(name).strip():
            raise ValueError("header name must not be blank")
        for key, values in self.raw_headers.items():
            if key.lower() == name.lower():
                return values
        return ()

    def first_header_value(self, name: str) -> Optional[str]:
        """Return the first value for a response header using case-insensitive lookup."""
        values = self.header_values(name)
        return values[0] if values else None


@dataclass(frozen=True)
class ApiResponse(Generic[T]):
    """Wrap typed or raw response data with response metadata."""

    data: T
    metadata: ApiResponseMetadata


class LocationConfidence(str, Enum):
    """API confidence category for geolocation precision."""

    HIGH = "high"
    MEDIUM = "medium"
    LOW = "low"
    UNKNOWN = "unknown"


@dataclass(frozen=True)
class Abuse:
    """Abuse-contact details returned by ``include=[\"abuse\"]``."""

    route: Optional[str] = None
    country: Optional[str] = None
    name: Optional[str] = None
    organization: Optional[str] = None
    kind: Optional[str] = None
    address: Optional[str] = None
    emails: Tuple[str, ...] = field(default_factory=tuple)
    phone_numbers: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Asn:
    """Autonomous system details for the resolved IP or domain."""

    as_number: Optional[str] = None
    organization: Optional[str] = None
    country: Optional[str] = None
    type: Optional[str] = None
    domain: Optional[str] = None
    date_allocated: Optional[str] = None
    rir: Optional[str] = None


@dataclass(frozen=True)
class Company:
    """Organization details associated with the resolved IP address."""

    name: Optional[str] = None
    type: Optional[str] = None
    domain: Optional[str] = None


@dataclass(frozen=True)
class CountryMetadata:
    """Country-level metadata such as TLD, languages, and calling code."""

    calling_code: Optional[str] = None
    tld: Optional[str] = None
    languages: Tuple[str, ...] = field(default_factory=tuple)


@dataclass(frozen=True)
class Currency:
    """Currency details for the resolved country."""

    code: Optional[str] = None
    name: Optional[str] = None
    symbol: Optional[str] = None


@dataclass(frozen=True)
class DstTransition:
    """Daylight-saving transition details for a time zone."""

    utc_time: Optional[str] = None
    duration: Optional[str] = None
    gap: Optional[bool] = None
    date_time_after: Optional[str] = None
    date_time_before: Optional[str] = None
    overlap: Optional[bool] = None


@dataclass(frozen=True)
class Location:
    """Geolocation details for the resolved IP address or domain."""

    continent_code: Optional[str] = None
    continent_name: Optional[str] = None
    country_code2: Optional[str] = None
    country_code3: Optional[str] = None
    country_name: Optional[str] = None
    country_name_official: Optional[str] = None
    country_capital: Optional[str] = None
    state_prov: Optional[str] = None
    state_code: Optional[str] = None
    district: Optional[str] = None
    city: Optional[str] = None
    locality: Optional[str] = None
    accuracy_radius: Optional[str] = None
    confidence: Optional[LocationConfidence] = None
    dma_code: Optional[str] = None
    zipcode: Optional[str] = None
    latitude: Optional[str] = None
    longitude: Optional[str] = None
    is_eu: Optional[bool] = None
    country_flag: Optional[str] = None
    geoname_id: Optional[str] = None
    country_emoji: Optional[str] = None


@dataclass(frozen=True)
class Network:
    """Network-routing details for the resolved IP address."""

    connection_type: Optional[str] = None
    route: Optional[str] = None
    is_anycast: Optional[bool] = None


@dataclass(frozen=True)
class Security:
    """Security and IP risk signals returned by ``include=[\"security\"]``."""

    threat_score: Optional[float] = None
    is_tor: Optional[bool] = None
    is_proxy: Optional[bool] = None
    proxy_provider_names: Tuple[str, ...] = field(default_factory=tuple)
    proxy_confidence_score: Optional[float] = None
    proxy_last_seen: Optional[str] = None
    is_residential_proxy: Optional[bool] = None
    is_vpn: Optional[bool] = None
    vpn_provider_names: Tuple[str, ...] = field(default_factory=tuple)
    vpn_confidence_score: Optional[float] = None
    vpn_last_seen: Optional[str] = None
    is_relay: Optional[bool] = None
    relay_provider_name: Optional[str] = None
    is_anonymous: Optional[bool] = None
    is_known_attacker: Optional[bool] = None
    is_bot: Optional[bool] = None
    is_spam: Optional[bool] = None
    is_cloud_provider: Optional[bool] = None
    cloud_provider_name: Optional[str] = None


@dataclass(frozen=True)
class TimeZoneInfo:
    """Time zone and daylight-saving details for the resolved location."""

    name: Optional[str] = None
    offset: Optional[float] = None
    offset_with_dst: Optional[float] = None
    current_time: Optional[str] = None
    current_time_unix: Optional[float] = None
    current_tz_abbreviation: Optional[str] = None
    current_tz_full_name: Optional[str] = None
    standard_tz_abbreviation: Optional[str] = None
    standard_tz_full_name: Optional[str] = None
    is_dst: Optional[bool] = None
    dst_savings: Optional[float] = None
    dst_exists: Optional[bool] = None
    dst_tz_abbreviation: Optional[str] = None
    dst_tz_full_name: Optional[str] = None
    dst_start: Optional[DstTransition] = None
    dst_end: Optional[DstTransition] = None


@dataclass(frozen=True)
class UserAgentDevice:
    """Device details extracted from a supplied user-agent string."""

    name: Optional[str] = None
    type: Optional[str] = None
    brand: Optional[str] = None
    cpu: Optional[str] = None


@dataclass(frozen=True)
class UserAgentEngine:
    """Rendering-engine details extracted from a supplied user-agent string."""

    name: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None
    version_major: Optional[str] = None


@dataclass(frozen=True)
class UserAgentOperatingSystem:
    """Operating-system details extracted from a supplied user-agent string."""

    name: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None
    version_major: Optional[str] = None
    build: Optional[str] = None


@dataclass(frozen=True)
class UserAgent:
    """Browser, device, engine, and operating-system details for a user agent."""

    user_agent_string: Optional[str] = None
    name: Optional[str] = None
    type: Optional[str] = None
    version: Optional[str] = None
    version_major: Optional[str] = None
    device: Optional[UserAgentDevice] = None
    engine: Optional[UserAgentEngine] = None
    operating_system: Optional[UserAgentOperatingSystem] = None


@dataclass(frozen=True)
class IpGeolocationResponse:
    """Typed response model for ``/v3/ipgeo`` lookups."""

    ip: Optional[str] = None
    domain: Optional[str] = None
    hostname: Optional[str] = None
    location: Optional[Location] = None
    country_metadata: Optional[CountryMetadata] = None
    network: Optional[Network] = None
    currency: Optional[Currency] = None
    asn: Optional[Asn] = None
    company: Optional[Company] = None
    security: Optional[Security] = None
    abuse: Optional[Abuse] = None
    time_zone: Optional[TimeZoneInfo] = None
    user_agent: Optional[UserAgent] = None


class BulkLookupResult(ABC):
    """Base type for bulk lookup items."""

    @property
    @abstractmethod
    def success(self) -> bool:
        """Whether this item represents a successful lookup."""


@dataclass(frozen=True)
class BulkLookupErrorDetails:
    """Error details returned for an individual bulk lookup entry."""

    message: Optional[str] = None


@dataclass(frozen=True)
class BulkLookupSuccess(BulkLookupResult):
    """Successful item returned by a bulk lookup."""

    data: IpGeolocationResponse

    @property
    def success(self) -> bool:
        return True


@dataclass(frozen=True)
class BulkLookupError(BulkLookupResult):
    """Error item returned for an individual bulk lookup entry."""

    error: BulkLookupErrorDetails = field(default_factory=BulkLookupErrorDetails)

    @property
    def success(self) -> bool:
        return False
