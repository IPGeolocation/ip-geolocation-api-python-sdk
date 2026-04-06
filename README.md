# IPGeolocation Python SDK

Typed Python SDK for the [IPGeolocation.io](https://ipgeolocation.io/) IP Location API.

- Single lookup (`/v3/ipgeo`) and bulk lookup (`/v3/ipgeo-bulk`)
- Sync client built on `requests` and async client built on `httpx`
- Typed response models plus raw JSON/XML methods
- Python 3.8+

## Table of Contents

- [Install](#install)
- [Quick Start](#quick-start)
- [Authentication](#authentication)
- [Notes](#notes)
- [Plan Behavior](#plan-behavior)
- [Examples](#examples)
- [Request Options](#request-options)
- [Response Metadata](#response-metadata)
- [Errors](#errors)
- [Links](#links)
- [Development](#development)

## Install

```bash
pip install ipgeolocationio
```

PyPI package: `ipgeolocationio`
Package page: <https://pypi.org/project/ipgeolocationio/>
Import: `ipgeolocation`

## Quick Start

```python
from ipgeolocation import (
    IpGeolocationClient,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
)

config = IpGeolocationClientConfig(api_key="YOUR_API_KEY")

with IpGeolocationClient(config) as client:
    response = client.lookup_ip_geolocation(
        LookupIpGeolocationRequest(ip="8.8.8.8")
    )

    print(response.data.ip)

    if response.data.location is not None:
        print(response.data.location.country_name)
        print(response.data.location.city)

    if response.data.time_zone is not None:
        print(response.data.time_zone.name)
```

### Async

```python
import asyncio

from ipgeolocation import (
    AsyncIpGeolocationClient,
    IpGeolocationClientConfig,
    LookupIpGeolocationRequest,
)


async def main() -> None:
    config = IpGeolocationClientConfig(api_key="YOUR_API_KEY")

    async with AsyncIpGeolocationClient(config) as client:
        response = await client.lookup_ip_geolocation(
            LookupIpGeolocationRequest(ip="8.8.8.8")
        )
        print(response.data.ip)

        if response.data.location is not None:
            print(response.data.location.country_name)


asyncio.run(main())
```

The async client exposes the same methods as coroutines. Use `async with` for cleanup, or call `await client.aclose()` manually.

## Authentication

**API key**: Works on all plans for single lookup and bulk lookup.

```python
config = IpGeolocationClientConfig(api_key="YOUR_API_KEY")
```

**Request-origin auth**: Paid plans only, and only for single lookup. If your origin is allowlisted in the [IPGeolocation dashboard](https://ipgeolocation.io/), the SDK sends it in the `Origin` header.

```python
config = IpGeolocationClientConfig(request_origin="https://app.example.com")
```

`request_origin` must be an absolute `http` or `https` URL with no path, query string, or fragment. Bulk lookups always require `api_key`, even if `request_origin` is set. You can set both on the same config. Single lookups require at least one of them.

### Client Config

| Field | Use |
|---|---|
| `api_key` | API key auth for single lookup and bulk lookup |
| `request_origin` | Paid request-origin auth for single lookup |
| `base_url` | Override the API base URL |
| `connect_timeout` | Time to wait for the connection in seconds |
| `read_timeout` | Time to wait for the response body in seconds |

## Notes

- **Typed methods require JSON.** For XML output, use the `_raw` methods with `output=ResponseFormat.XML`.
- **Optional modules need `include`.** Fields like `security`, `abuse`, `user_agent`, `hostname`, `geo_accuracy`, and `dma_code` only appear in the response when you pass the matching `include` value. Without it, those fields will be `None`.
- **`fields` and `excludes` only filter the response.** They do not enable optional modules or unlock paid data.
- **Domain lookup is paid only.** Passing a domain as `ip="google.com"` works on paid plans. Free plans get a 401.
- **The SDK does not retry.** Timeouts, server errors, and rate limits raise exceptions directly. Implement your own retry logic if you need it.
- **Do not reuse a closed client.** After `close()`, `aclose()`, or leaving a `with` or `async with` block, further requests raise `ValidationException`.

## Plan Behavior

Responses vary by plan.

### Capabilities

| Capability | Free | Paid |
|---|---|---|
| Single IPv4/IPv6 lookup | Yes | Yes |
| Domain lookup | No | Yes |
| Bulk lookup (`/v3/ipgeo-bulk`) | No | Yes |
| Non-English `lang` | No | Yes |
| Request-origin auth | No | Yes |
| Optional modules via `include` | No | Yes |
| `include=["*"]` | Base response only | All plan-available modules |

### Default Response Sections

Default single-lookup response:

| Section | Free | Paid |
|---|---|---|
| `location` | Yes | Yes |
| `country_metadata` | Yes | Yes |
| `currency` | Yes | Yes |
| `asn` (basic: `as_number`, `organization`, `country`) | Yes | Yes |
| `asn` (full: adds `type`, `domain`, `date_allocated`, `rir`) | No | Yes |
| `time_zone` | Yes | Yes |
| `network` | No | Yes |
| `company` | No | Yes |

## Examples

The examples below assume you already have a configured client in scope. See [Quick Start](#quick-start) for setup.

### Caller IP

Omit the `ip` parameter to look up the IP of the machine making the request:

```python
response = client.lookup_ip_geolocation(LookupIpGeolocationRequest())
print(response.data.ip)  # your public IP
```

### Domain Lookup (Paid)

When you look up a domain, the response includes the resolved IP and the original domain name:

```python
response = client.lookup_ip_geolocation(
    LookupIpGeolocationRequest(ip="google.com")
)
print(response.data.ip)       # resolved IP address
print(response.data.domain)   # "google.com"
```

### Security and Abuse

```python
response = client.lookup_ip_geolocation(
    LookupIpGeolocationRequest(
        ip="9.9.9.9",
        include=["security", "abuse"],
    )
)

if response.data.security is not None:
    print(response.data.security.threat_score)

if response.data.abuse is not None and response.data.abuse.emails:
    print(response.data.abuse.emails[0])
```

### User-Agent Parsing

To parse a visitor's user-agent string, pass `include=["user_agent"]` and send the visitor string in the request `User-Agent` header:

```python
visitor_ua = (
    "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) "
    "AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9"
)

response = client.lookup_ip_geolocation(
    LookupIpGeolocationRequest(
        ip="115.240.90.163",
        include=["user_agent"],
        headers={"User-Agent": visitor_ua},
    )
)

if response.data.user_agent is not None:
    print(response.data.user_agent.name)
    print(response.data.user_agent.operating_system)
```

> **Note:** The `user_agent` field on the request model is different. It overrides the outbound `User-Agent` header for the HTTP request itself and takes precedence over `headers["User-Agent"]`. If you set both, the API parses the `user_agent` value.

### Filtered Response

Use `fields` to keep specific fields, or `excludes` to remove them:

```python
response = client.lookup_ip_geolocation(
    LookupIpGeolocationRequest(
        ip="8.8.8.8",
        include=["security"],
        fields=["location.country_name", "security.threat_score", "security.is_vpn"],
        excludes=["currency"],
    )
)

if response.data.location is not None:
    print(response.data.location.country_name)

if response.data.security is not None:
    print(response.data.security.threat_score)
    print(response.data.security.is_vpn)
```

### Raw XML

Typed methods only support JSON. For XML, use a raw method:

```python
from ipgeolocation import ResponseFormat

response = client.lookup_ip_geolocation_raw(
    LookupIpGeolocationRequest(ip="8.8.8.8", output=ResponseFormat.XML)
)
print(response.data)  # raw XML string
```

### Bulk Lookup (Paid)

Bulk lookup uses POST and accepts up to 50,000 IPs or domains. Each item in the response is either `BulkLookupSuccess` or `BulkLookupError`:

```python
from ipgeolocation import (
    BulkLookupError,
    BulkLookupIpGeolocationRequest,
    BulkLookupSuccess,
)

response = client.bulk_lookup_ip_geolocation(
    BulkLookupIpGeolocationRequest(
        ips=["8.8.8.8", "invalid-ip", "1.1.1.1"],
        include=["security"],
    )
)

for result in response.data:
    if isinstance(result, BulkLookupSuccess):
        print(result.data.ip, result.data.security)  # 8.8.8.8 Security(...)
    elif isinstance(result, BulkLookupError):
        print(result.error.message)  # 'invalid-ip' is not a valid IP address.
```

## Request Options

### Single Lookup

| Field | Type | Notes |
|---|---|---|
| `ip` | `str` or `None` | IPv4, IPv6, or domain (domain is paid only). Omit for caller IP lookup. |
| `lang` | `Language`, `str`, or `None` | Response language. Non-English requires a paid plan. |
| `include` | sequence of strings | Optional modules to enable. See [include values](#include-values). |
| `fields` | sequence of strings | Response field filter. Does not unlock data. |
| `excludes` | sequence of strings | Response field filter. Does not unlock data. |
| `output` | `ResponseFormat` or `str` | `"json"` (default) or `"xml"`. Typed methods require JSON. |
| `user_agent` | `str` or `None` | Overrides the outbound `User-Agent` header. Takes precedence over `headers["User-Agent"]`. |
| `headers` | mapping of strings | Custom request headers. `Accept` is always SDK-managed. Sequence values are sent as one comma-joined header line. |

### Bulk Lookup

Bulk lookup accepts the same fields as single lookup, plus:

| Field | Type | Notes |
|---|---|---|
| `ips` | sequence of strings | Required. Up to 50,000 IPs or domains. |

Differences from single lookup: `Content-Type: application/json` is always set by the SDK. Bulk lookup always requires `api_key` in the config, even if `request_origin` is also set.

### `include` Values

| Value | What it adds |
|---|---|
| `security` | `security` object (threat score, VPN/proxy/Tor detection, bot detection) |
| `abuse` | `abuse` object (abuse contact info, emails, phone numbers) |
| `user_agent` | `user_agent` object (browser, device, OS parsed from the request `User-Agent` header) |
| `hostname` | `hostname` field (reverse DNS lookup) |
| `liveHostname` | `hostname` field (live DNS) |
| `hostnameFallbackLive` | `hostname` field (fallback to live DNS) |
| `geo_accuracy` | `location.locality`, `location.accuracy_radius`, `location.confidence` |
| `dma_code` | `location.dma_code` |
| `*` | All optional modules available on your plan |

Supported `lang` values: `en`, `de`, `ru`, `ja`, `fr`, `cn`, `es`, `cs`, `it`, `ko`, `fa`, `pt`

## Response Metadata

Every SDK method returns `ApiResponse(data=..., metadata=...)`.

- Typed single lookup returns `IpGeolocationResponse`
- Typed bulk lookup returns a list of `BulkLookupResult`
- Raw methods return the response body as a string

| Field | Type | Description |
|---|---|---|
| `status_code` | `int` | HTTP status code |
| `duration_ms` | `int` | Wall-clock request time in milliseconds, measured by the SDK |
| `credits_charged` | `int` or `None` | Parsed from the `X-Credits-Charged` response header |
| `successful_records` | `int` or `None` | Parsed from the `X-Successful-Record` response header |
| `raw_headers` | read-only mapping | All response headers. Values are tuples of strings. |

Header access helpers:

```python
metadata.header_values("Header-Name")        # all values as a tuple
metadata.first_header_value("Header-Name")   # first value or None
```

### JSON Serialization

Use `to_json()` or `to_pretty_json()` to serialize SDK objects:

```python
from ipgeolocation import JsonOutputMode, to_pretty_json

# Compact mode (default): omits None fields
print(to_pretty_json(response.data))

# Full mode: includes None fields as null
print(to_pretty_json(response.data, mode=JsonOutputMode.FULL))
```

## Errors

All exceptions inherit from `IpGeolocationException`. The SDK does not retry failed requests.

**Before the request is sent:**

- `ValidationException` for bad config, invalid request parameters, or calling a closed client

**Transport problems:**

- `RequestTimeoutException` for timeouts
- `TransportException` for connection or other HTTP-level failures

**API errors (non-2xx responses):**

| Exception | HTTP Status |
|---|---|
| `BadRequestException` | 400 |
| `UnauthorizedException` | 401 |
| `NotFoundException` | 404 |
| `MethodNotAllowedException` | 405 |
| `PayloadTooLargeException` | 413 |
| `UnsupportedMediaTypeException` | 415 |
| `LockedException` | 423 |
| `RateLimitException` | 429 |
| `ClientClosedRequestException` | 499 |
| `ServerErrorException` | 5xx |
| `ApiException` | Any other non-2xx |

All API exceptions have `.status_code` and `.api_message` attributes.

## Links

- [PyPI package](https://pypi.org/project/ipgeolocationio/)
- [Python SDK documentation](https://ipgeolocation.io/documentation/ip-geolocation-api-python-sdk.html)
- [API documentation](https://ipgeolocation.io/documentation/ip-location-api.html)
- [Authentication](https://ipgeolocation.io/documentation/api-authentication.html)
- [Response formats](https://ipgeolocation.io/documentation/api-response-formats.html)
- [Credits and usage](https://ipgeolocation.io/documentation/credits-usage.html)
- [GitHub repository](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk)
