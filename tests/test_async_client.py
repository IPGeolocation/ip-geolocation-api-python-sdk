"""Async client behavior tests."""

from __future__ import annotations

import asyncio

import pytest

from ipgeolocation import (
    ApiException,
    AsyncIpGeolocationClient,
    BulkLookupError,
    BulkLookupIpGeolocationRequest,
    BulkLookupSuccess,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
    ResponseFormat,
    UnauthorizedException,
    ValidationException,
)

from .test_support import AsyncTestTransport, headers


def _run(coro):
    return asyncio.run(coro)


def test_async_lookup_builds_expected_query_and_headers() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        )
        await client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(
                ip="8.8.8.8",
                include=["security"],
                fields=["location.city"],
                excludes=["currency"],
            )
        )

        sent = transport.captured_requests[0]
        assert sent.url.startswith("https://api.ipgeolocation.io/v3/ipgeo?")
        assert "apiKey=k" in sent.url
        assert "ip=8.8.8.8" in sent.url
        assert "include=security" in sent.url
        assert "fields=location.city" in sent.url
        assert "excludes=currency" in sent.url
        assert (
            sent.first_header_value("User-Agent")
            == AsyncIpGeolocationClient.default_user_agent()
        )
        assert sent.first_header_value("Accept") == "application/json"

    _run(scenario())


def test_async_lookup_uses_request_origin_and_custom_headers() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(request_origin="https://app.example.com"),
            transport=transport,
        )
        await client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(
                ip="8.8.8.8",
                headers={"origin": "https://override.example.com", "accept": "text/plain"},
            )
        )

        sent = transport.captured_requests[0]
        assert "apiKey=" not in sent.url
        assert sent.first_header_value("Origin") == "https://override.example.com"
        assert sent.first_header_value("Accept") == "application/json"

    _run(scenario())


def test_async_lookup_forwards_custom_user_agent_header() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        )
        await client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(
                ip="8.8.8.8",
                headers={"User-Agent": "header-user-agent"},
            )
        )

        sent = transport.captured_requests[0]
        assert sent.first_header_value("User-Agent") == "header-user-agent"

    _run(scenario())


def test_async_lookup_request_user_agent_field_overrides_custom_header() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(200, '{"ip":"8.8.8.8"}')

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        )
        await client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(
                ip="8.8.8.8",
                user_agent="field-user-agent",
                headers={"User-Agent": "header-user-agent"},
            )
        )

        sent = transport.captured_requests[0]
        assert sent.first_header_value("User-Agent") == "field-user-agent"

    _run(scenario())


def test_async_parses_single_lookup_response_and_metadata() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(
            200,
            '{"ip":"8.8.8.8","location":{"country_name":"United States"}}',
            headers("X-Credits-Charged", "1"),
        )

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        )
        response = await client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))

        assert response.data.ip == "8.8.8.8"
        assert response.data.location is not None
        assert response.data.location.country_name == "United States"
        assert response.metadata.credits_charged == 1

    _run(scenario())


def test_async_bulk_parses_success_and_error_items() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(
            200,
            '[{"ip":"8.8.8.8"},{"message":"bad ip"}]',
        )

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        )
        response = await client.bulk_lookup_ip_geolocation(
            BulkLookupIpGeolocationRequest(ips=["8.8.8.8", "invalid-ip"])
        )

        assert isinstance(response.data[0], BulkLookupSuccess)
        assert response.data[0].data.ip == "8.8.8.8"
        assert isinstance(response.data[1], BulkLookupError)
        assert response.data[1].error.message == "bad ip"

    _run(scenario())


def test_async_typed_methods_reject_xml_output() -> None:
    async def scenario() -> None:
        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=AsyncTestTransport(),
        )
        with pytest.raises(ValidationException, match="XML output is not supported"):
            await client.lookup_ip_geolocation(
                LookupIpGeolocationRequest(output=ResponseFormat.XML)
            )

    _run(scenario())


def test_async_lookup_rejects_missing_api_key_and_request_origin() -> None:
    async def scenario() -> None:
        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(),
            transport=AsyncTestTransport(),
        )
        with pytest.raises(
            ValidationException,
            match="single lookup requires apiKey or request_origin",
        ):
            await client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))

    _run(scenario())


def test_async_raw_methods_allow_xml_output() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(200, "<ipgeo><ip>8.8.8.8</ip></ipgeo>")
        transport.enqueue_response(200, "<items><item><ip>8.8.8.8</ip></item></items>")

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        )
        single = await client.lookup_ip_geolocation_raw(
            LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
        )
        bulk = await client.bulk_lookup_ip_geolocation_raw(
            BulkLookupIpGeolocationRequest(ips=["8.8.8.8"], output=ResponseFormat.XML)
        )

        assert "<" in single.data
        assert "<" in bulk.data

    _run(scenario())


def test_async_closed_client_rejects_future_requests() -> None:
    async def scenario() -> None:
        client = AsyncIpGeolocationClient(IpGeolocationClientConfig(api_key="k"))
        await client.aclose()

        with pytest.raises(ValidationException, match="client is closed"):
            await client.lookup_ip_geolocation(LookupIpGeolocationRequest(ip="8.8.8.8"))

    _run(scenario())


def test_async_client_context_manager_closes_owned_transport() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        async with AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        ) as client:
            assert client is not None

        assert transport.closed is False

    _run(scenario())


def test_async_api_error_mapping_preserves_details() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(401, '{"message":"invalid key"}')

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        )
        with pytest.raises(UnauthorizedException) as exc:
            await client.lookup_ip_geolocation(LookupIpGeolocationRequest())

        assert exc.value.status_code == 401
        assert exc.value.api_message == "invalid key"

    _run(scenario())


def test_async_api_exception_type_for_unmapped_status_codes() -> None:
    async def scenario() -> None:
        transport = AsyncTestTransport()
        transport.enqueue_response(403, '{"message":"forbidden"}')

        client = AsyncIpGeolocationClient(
            IpGeolocationClientConfig(api_key="k"),
            transport=transport,
        )
        with pytest.raises(ApiException, match="HTTP status 403"):
            await client.lookup_ip_geolocation(LookupIpGeolocationRequest())

    _run(scenario())
