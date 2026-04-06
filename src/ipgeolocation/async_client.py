"""Async IPGeolocation API client."""

from __future__ import annotations

import json
import time
from typing import List, Optional, cast

from ._client_shared import (
    build_query,
    merge_headers,
    parse_bulk_lookup,
    parse_single_lookup,
    resolve_user_agent_header,
    to_api_exception,
    to_metadata,
    validate_json_output,
)
from ._transport import AsyncHttpTransport, HttpRequestData, HttpxAsyncTransport
from ._version import get_version
from .config import IpGeolocationClientConfig
from .enums import Language, ResponseFormat
from .exceptions import SerializationException, ValidationException
from .models import (
    ApiResponse,
    BulkLookupResult,
    IpGeolocationResponse,
)
from .request_models import BulkLookupIpGeolocationRequest, LookupIpGeolocationRequest


class AsyncIpGeolocationClient:
    """Primary async client for the IPGeolocation API."""

    def __init__(
        self,
        config: IpGeolocationClientConfig,
        transport: Optional[AsyncHttpTransport] = None,
    ) -> None:
        if config is None:
            raise TypeError("config must not be None")
        self._config = config
        self._owns_transport = transport is None
        self._transport = transport if transport is not None else HttpxAsyncTransport()
        self._closed = False

    @staticmethod
    def default_user_agent() -> str:
        """Return the SDK user-agent header value."""
        return f"ipgeolocation-python-sdk/{get_version()}"

    async def lookup_ip_geolocation(
        self,
        request: Optional[LookupIpGeolocationRequest],
    ) -> ApiResponse[IpGeolocationResponse]:
        """Run a typed single lookup against ``/v3/ipgeo``."""
        self._ensure_open()
        self._validate_lookup_request_base(request)
        typed_request = cast(LookupIpGeolocationRequest, request)
        validate_json_output(cast(Optional[ResponseFormat], typed_request.output))
        http_request = self._build_lookup_http_request(typed_request)
        response, duration_ms = await self._execute_with_metrics(http_request)
        if response.status_code // 100 != 2:
            raise to_api_exception(response.status_code, response.body)
        return ApiResponse(
            data=parse_single_lookup(response.body),
            metadata=to_metadata(response.status_code, duration_ms, response.headers),
        )

    async def lookup_ip_geolocation_raw(
        self,
        request: Optional[LookupIpGeolocationRequest],
    ) -> ApiResponse[str]:
        """Run a raw single lookup and return the decoded response text without typed parsing."""
        self._ensure_open()
        self._validate_lookup_request_base(request)
        typed_request = cast(LookupIpGeolocationRequest, request)
        http_request = self._build_lookup_http_request(typed_request)
        response, duration_ms = await self._execute_with_metrics(http_request)
        if response.status_code // 100 != 2:
            raise to_api_exception(response.status_code, response.body)
        return ApiResponse(
            data=response.body,
            metadata=to_metadata(response.status_code, duration_ms, response.headers),
        )

    async def bulk_lookup_ip_geolocation(
        self,
        request: Optional[BulkLookupIpGeolocationRequest],
    ) -> ApiResponse[List[BulkLookupResult]]:
        """Run a typed bulk lookup against ``/v3/ipgeo-bulk``."""
        self._ensure_open()
        self._validate_bulk_request_base(request)
        typed_request = cast(BulkLookupIpGeolocationRequest, request)
        validate_json_output(cast(Optional[ResponseFormat], typed_request.output))
        http_request = self._build_bulk_http_request(typed_request)
        response, duration_ms = await self._execute_with_metrics(http_request)
        if response.status_code // 100 != 2:
            raise to_api_exception(response.status_code, response.body)
        return ApiResponse(
            data=parse_bulk_lookup(response.body),
            metadata=to_metadata(response.status_code, duration_ms, response.headers),
        )

    async def bulk_lookup_ip_geolocation_raw(
        self,
        request: Optional[BulkLookupIpGeolocationRequest],
    ) -> ApiResponse[str]:
        """Run a raw bulk lookup and return the decoded response text without typed parsing."""
        self._ensure_open()
        self._validate_bulk_request_base(request)
        typed_request = cast(BulkLookupIpGeolocationRequest, request)
        http_request = self._build_bulk_http_request(typed_request)
        response, duration_ms = await self._execute_with_metrics(http_request)
        if response.status_code // 100 != 2:
            raise to_api_exception(response.status_code, response.body)
        return ApiResponse(
            data=response.body,
            metadata=to_metadata(response.status_code, duration_ms, response.headers),
        )

    async def aclose(self) -> None:
        """Close the underlying HTTP transport when this client created it."""
        if self._closed:
            return
        self._closed = True
        if self._owns_transport:
            await self._transport.close()

    async def __aenter__(self) -> "AsyncIpGeolocationClient":
        self._ensure_open()
        return self

    async def __aexit__(self, exc_type, exc, tb) -> None:
        await self.aclose()

    def _build_lookup_http_request(
        self,
        request: LookupIpGeolocationRequest,
    ) -> HttpRequestData:
        output = cast(ResponseFormat, request.output or ResponseFormat.JSON)
        lang = cast(Optional[Language], request.lang)
        query = build_query(
            {
                "apiKey": self._config.api_key,
                "ip": request.ip,
                "lang": lang.value if lang else None,
                "include": ",".join(request.include) if request.include else None,
                "fields": ",".join(request.fields) if request.fields else None,
                "excludes": ",".join(request.excludes) if request.excludes else None,
                "output": output.value,
            }
        )
        headers = merge_headers(
            {"Origin": [self._config.request_origin]} if self._config.request_origin else {},
            request.headers or {},
            {
                "User-Agent": resolve_user_agent_header(
                    request.user_agent,
                    request.headers or {},
                    self.default_user_agent(),
                ),
                "Accept": [
                    "application/xml" if output == ResponseFormat.XML else "application/json"
                ],
            },
        )
        return HttpRequestData(
            url=f"{self._config.base_url}/v3/ipgeo{query}",
            method="GET",
            headers=headers,
            body=None,
            connect_timeout=cast(float, self._config.connect_timeout),
            read_timeout=cast(float, self._config.read_timeout),
        )

    def _build_bulk_http_request(
        self,
        request: BulkLookupIpGeolocationRequest,
    ) -> HttpRequestData:
        output = cast(ResponseFormat, request.output or ResponseFormat.JSON)
        lang = cast(Optional[Language], request.lang)
        query = build_query(
            {
                "apiKey": self._config.api_key,
                "lang": lang.value if lang else None,
                "include": ",".join(request.include) if request.include else None,
                "fields": ",".join(request.fields) if request.fields else None,
                "excludes": ",".join(request.excludes) if request.excludes else None,
                "output": output.value,
            }
        )
        try:
            payload = json.dumps({"ips": list(request.ips)}, separators=(",", ":"))
        except Exception as exc:  # pragma: no cover - defensive
            raise SerializationException("Failed to serialize bulk lookup request body") from exc
        headers = merge_headers(
            {"Origin": [self._config.request_origin]} if self._config.request_origin else {},
            request.headers or {},
            {
                "User-Agent": resolve_user_agent_header(
                    request.user_agent,
                    request.headers or {},
                    self.default_user_agent(),
                ),
                "Accept": [
                    "application/xml" if output == ResponseFormat.XML else "application/json"
                ],
                "Content-Type": ["application/json"],
            },
        )
        return HttpRequestData(
            url=f"{self._config.base_url}/v3/ipgeo-bulk{query}",
            method="POST",
            headers=headers,
            body=payload,
            connect_timeout=cast(float, self._config.connect_timeout),
            read_timeout=cast(float, self._config.read_timeout),
        )

    async def _execute_with_metrics(self, request: HttpRequestData):
        started = time.perf_counter()
        response = await self._transport.send(request)
        duration_ms = int(max(0.0, (time.perf_counter() - started) * 1000))
        return response, duration_ms

    def _validate_lookup_request_base(
        self,
        request: Optional[LookupIpGeolocationRequest],
    ) -> None:
        if request is None:
            raise ValidationException("request must not be null")
        if self._config.api_key is None and self._config.request_origin is None:
            raise ValidationException(
                "single lookup requires apiKey or request_origin in client config"
            )

    def _validate_bulk_request_base(
        self,
        request: Optional[BulkLookupIpGeolocationRequest],
    ) -> None:
        if request is None:
            raise ValidationException("request must not be null")
        if self._config.api_key is None:
            raise ValidationException("bulk lookup requires apiKey in client config")

    def _ensure_open(self) -> None:
        if self._closed:
            raise ValidationException("client is closed")
