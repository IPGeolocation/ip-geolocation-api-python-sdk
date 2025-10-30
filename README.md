# IP Geolocation API Client Library/SDK for Python

The official **Python Client Library** for **[IPGeolocation.io](https://ipgeolocation.io)**'s set of APIs, provides a quick, developer friendly, way 
to access IP Location, Security, Timezone, Astronomy, ASN, Abuse Contact, and useragent data. Lookup your own IP or provide any IPv4, 
IPv6 or domain name to get structured results in Python, without the need for manual HTTP handling.

- [IP Location API](https://ipgeolocation.io/ip-location-api.html): Get all-in-one unified solution for **location** (city, locality, state, country, etc.), **currency**, 
  **network** (AS number, ASN name, organization, asn type, date of allocation, company/ISP name, company type, 
  company domain), **timezone** , **useragent** string parsing, **security** (threat score, is_tor, is_bot, 
  proxy_provider, cloud_provider), and **abuse contact** (route/CIDR network, country, address, email, phone numbers) information.
- [IP Security API](https://ipgeolocation.io/ip-security-api.html): Get security, network, location, hostname, timezone and useragent parsing.
- [ASN API](https://ipgeolocation.io/asn-api.html): Get ASN details along with peers, upstreams, downstreams, routes, and raw WHOIS.
- [Abuse Contact API](https://ipgeolocation.io/ip-abuse-contact-api.html): Get abuse emails, phone numbers, kind, organization, route/CIDR network and country.
- [Astronomy API](https://ipgeolocation.io/astronomy-api.html): Get sunrise, sunset, moonrise, moonset, moon phases with precise twilight period times in combination 
  with location information.
- [Timezone API](https://ipgeolocation.io/timezone-api.html): Get timezone name, multiple time formats, daylight saving status and its details along with 
  location information.
- [Timezone Convert API](https://ipgeolocation.io/timezone-api.html): Convert time between timezone names, geo coordinates, location addresses, IATA codes, 
  ICAO codes, or UN/LOCODE.
- [User Agent API](https://ipgeolocation.io/user-agent-api.html): Get browser, Operating System, and device info from single or multiple Useragent string parsing.

This library aims to empower developers to integrate threat intelligence, personalization, fraud prevention, 
compliance, and analytics features directly into Python based applications. Whether you're enriching signup forms 
with ip geolocation data, localizing content, embedding threat intelligence in back-end systems, or converting 
time zones and currencies, the library ensures seamless, scalable integration with IPGeolocation.io’s global API infrastructure.

Based on:
- API version: 2.0.0

**Official Release:**
- Available on [**PyPI**](https://pypi.org/project/ipgeolocationio/)  
- Source Code: [**GitHub Repository**](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk)

## Table of Contents
1. [Requirements](#requirements)
2. [Installation](#installation)
   - [From PyPI](#from-pypi)
   - [From GitHub](#from-github)
3. [API Plan Tiers and Documentation](#api-plan-tiers-and-documentation)
4. [API Endpoints](#api-endpoints)
5. [Fields and Methods Availability](#fields-and-methods-availability)
6. [Authentication Setup](#authentication-setup)
   - [How to Get Your API Key](#how-to-get-your-api-key)
   - [ApiKeyAuth](#apikeyauth)
7. [Tests setup](#tests)
8. [IP Geolocation Examples](#ip-geolocation-examples)
   - [Developer (Free) Plan Examples](#developer-plan-examples) 
   - [Standard Plan Examples](#standard-plan-examples)
   - [Advanced Plan Examples](#advanced-plan-examples)
   - [Bulk IP Geolocation Example](#bulk-ip-geolocation-example)
9. [IP Security Examples](#ip-security-examples)
   - [Get Default Fields](#get-default-fields-2)
   - [Include Multiple Optional Fields](#include-multiple-optional-fields)
   - [Request with Field Filtering](#request-with-field-filtering)
   - [Bulk IP Security Request](#bulk-ip-security-request)
10. [ASN API Examples](#asn-api-examples)
    - [Get ASN Information by IP Address](#get-asn-information-by-ip-address)
    - [Get ASN Information by ASN Number](#get-asn-information-by-asn-number)
    - [Combine All objects using Include](#combine-all-objects-using-include)
11. [Abuse Contact API Examples](#abuse-contact-api-examples)
    - [Lookup Abuse Contact by IP](#lookup-abuse-contact-by-ip)
    - [Lookup Abuse Contact with Specific Fields](#lookup-abuse-contact-with-specific-fields)
    - [Lookup Abuse Contact while Excluding Fields](#lookup-abuse-contact-while-excluding-fields)
12. [Timezone API Examples](#timezone-api-examples)
    - [Get Timezone by IP Address](#get-timezone-by-ip-address)
    - [Get Timezone by Timezone Name](#get-timezone-by-timezone-name)
    - [Get Timezone from Any Address](#get-timezone-from-any-address)
    - [Get Timezone from Location Coordinates](#get-timezone-from-location-coordinates)
    - [Get Timezone and Airport Details from IATA Code](#get-timezone-and-airport-details-from-iata-code)
    - [Get Timezone and City Details from UN/LOCODE](#get-timezone-and-city-details-from-unlocode)
13. [Timezone Converter Examples](#timezone-converter-examples)
    - [Convert Current Time from One Timezone to Another](#convert-current-time-from-one-timezone-to-another)
14. [User Agent API Examples](#user-agent-api-examples)
    - [Parse a Basic User Agent String](#parse-a-basic-user-agent-string)
    - [Bulk User Agent Parsing Example](#bulk-user-agent-parsing-example)
15. [Astronomy API Examples](#astronomy-api-examples)
    - [Lookup Astronomy by Coordinates](#lookup-astronomy-api-by-coordinates)
    - [Lookup Astronomy by IP Address](#lookup-astronomy-api-by-ip-address)
    - [Lookup Astronomy by Location String](#lookup-astronomy-api-by-location-string)
    - [Lookup Astronomy for Specific Date](#lookup-astronomy-api-for-a-specific-date)
    - [Lookup Location Info in Different Language](#lookup-location-info-in-different-language)
16. [Documentation for Models](#documentation-for-models)

## Requirements

- Python 3.9+
- API Key from [IPGeolocation.io](https://ipgeolocation.io)

## Installation
### From PyPI

You can install package directly from [![PyPI](https://badge.fury.io/py/ipgeolocationio.svg)](https://pypi.org/project/ipgeolocationio/) using:

```sh
pip install ipgeolocationio
```
(you may need to run `pip` with root permission: `sudo pip install ipgeolocationio`)

### From GitHub

```sh
python -m pip install git+https://github.com/IPGeolocation/ip-geolocation-api-python-sdk.git
```
(or append `sudo` in the start to install the package for all users)

Then import the package:
```python
import ipgeolocation
```

## API Plan Tiers and Documentation

The documentation below corresponds to the four available API tier plans:

- **Developer Plan** (Free): [Full Documentation](https://ipgeolocation.io/ip-location-api.html#Free)
- **Standard Plan**: [Full Documentation](https://ipgeolocation.io/ip-location-api.html#Standard)
- **Advance Plan**: [Full Documentation](https://ipgeolocation.io/ip-location-api.html#Advance)
- **Security Plan**: [Full Documentation](https://ipgeolocation.io/ip-security-api.html#documentation-overview)

For a detailed comparison of what each plan offers, visit the [Pricing Page](https://ipgeolocation.io/pricing.html).

## API Endpoints

All URIs are relative to *https://api.ipgeolocation.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*IPGeolocationApi* | [**get_ip_geolocation**](docs/IPGeolocationApi.md#get_ip_geolocation) | **GET** /ipgeo | Get geolocation data for a single IP address
*IPGeolocationApi* | [**get_bulk_ip_geolocation**](docs/IPGeolocationApi.md#get_bulk_ip_geolocation) | **POST** /ipgeo-bulk | Get geolocation data for multiple IP addresses in a single API request
*IPSecurityApi* | [**get_ip_security_info**](docs/IPSecurityApi.md#get_ip_security_info) | **GET** /security | Retrieve security information (VPN, TOR, proxy, etc.) for a single IP
*IPSecurityApi* | [**get_bulk_ip_security_info**](docs/IPSecurityApi.md#get_bulk_ip_security_info) | **POST** /security-bulk | Retrieve security threat intelligence for multiple IPs
*ASNLookupApi* | [**get_asn_info**](docs/ASNLookupApi.md#get_asn_info) | **GET** /asn | Get details of any ASN number or associated IP address
*AbuseContactApi* | [**get_abuse_contact_info**](docs/AbuseContactApi.md#get_abuse_contact_info) | **GET** /abuse | Retrieve abuse reporting contact information for a given IP address
*AstronomyApi* | [**get_astronomy_details**](docs/AstronomyApi.md#get_astronomy_details) | **GET** /astronomy | Get sunrise, sunset, moonrise, moonset, and related data for a location
*AstronomyApi* | [**get_time_series_lookup**](docs/AstronomyApi.md#get_time_series_lookup) | **GET** /astronomy/timeSeries | Get astronomy information for given date range at once
*TimezoneApi* | [**get_timezone_info**](docs/TimezoneApi.md#get_timezone_info) | **GET** /timezone | Timezone information details
*TimeConversionApi* | [**convert_time_between_timezones**](docs/TimeConversionApi.md#convert_time_between_timezones) | **GET** /timezone/convert | Convert time between two specified timezones
*UserAgentApi* | [**get_user_agent_details**](docs/UserAgentApi.md#get_user_agent_details) | **GET** /user-agent | Get details of user-agent
*UserAgentApi* | [**parse_user_agent_string**](docs/UserAgentApi.md#parse_user_agent_string) | **POST** /user-agent | Handle single User-Agent string
*UserAgentApi* | [**parse_bulk_user_agent_strings**](docs/UserAgentApi.md#parse_bulk_user_agent_strings) | **POST** /user-agent-bulk | Handle multiple user-agent string lookups

## Fields and Methods Availability
IP Geolocation offers four plans from billing point of view: **Free, Standard, Security, Advance**. The availability of each method calling
from the respective class, over all plans are presented below. 

| Class               | Method                                                                                         | Free | Standard | Security | Advance |
|---------------------|------------------------------------------------------------------------------------------------|:----:|:--------:|:--------:|:-------:|
| *IPGeolocationApi*  | [**get_ip_geolocation**](docs/IPGeolocationApi.md#get_ip_geolocation)                          |  ✔   |    ✔     |    ✖     |    ✔    |
| *IPGeolocationApi*  | [**get_bulk_ip_geolocation**](docs/IPGeolocationApi.md#get_bulk_ip_geolocation)                |  ✖   |    ✔     |    ✖     |    ✔    |
| *IPSecurityApi*     | [**get_ip_security_info**](docs/IPSecurityApi.md#get_ip_security_info)                         |  ✖   |    ✖     |    ✔     |    ✖    |
| *IPSecurityApi*     | [**get_bulk_ip_security_info**](docs/IPSecurityApi.md#get_bulk_ip_security_info)               |  ✖   |    ✖     |    ✔     |    ✖    |
| *ASNLookupApi*      | [**get_asn_info**](docs/ASNLookupApi.md#get_asn_info)                                          |  ✖   |    ✖     |    ✖     |    ✔    |
| *AbuseContactApi*   | [**get_abuse_contact_info**](docs/AbuseContactApi.md#get_abuse_contact_info)                   |  ✖   |    ✖     |    ✖     |    ✔    |
| *AstronomyApi*      | [**get_astronomy_details**](docs/AstronomyApi.md#get_astronomy_details)                        |  ✔   |    ✔     |    ✔     |    ✔    |
| *AstronomyApi*      | [**get_time_series_lookup**](docs/AstronomyApi.md#get_time_series_lookup)                      |  ✔   |    ✔     |    ✔     |    ✔    |
| *TimezoneApi*       | [**get_timezone_info**](docs/TimezoneApi.md#get_timezone_info)                                 |  ✔   |    ✔     |    ✔     |    ✔    |
| *TimeConversionApi* | [**convert_time_between_timezones**](docs/TimeConversionApi.md#convert_time_between_timezones) |  ✔   |    ✔     |    ✔     |    ✔    |
| *UserAgentApi*      | [**get_user_agent_details**](docs/UserAgentApi.md#get_user_agent_details)                      |  ✔   |    ✔     |    ✔     |    ✔    |
| *UserAgentApi*      | [**parse_user_agent_string**](docs/UserAgentApi.md#parse_user_agent_string)                    |  ✔   |    ✔     |    ✔     |    ✔    |
| *UserAgentApi*      | [**parse_bulk_user_agent_strings**](docs/UserAgentApi.md#parse_bulk_user_agent_strings)        |  ✖   |    ✔     |    ✔     |    ✔    |

> **Note:** The availability of fields in every API endpoint across all API plans is provided in the **_Reference Table_** within each respective API Documentation. e.g., for IPGeolocationApi, please visit [https://ipgeolocation.io/ip-location-api.html#fields-reference](https://ipgeolocation.io/ip-location-api.html#fields-reference). 

## Authentication Setup
To authenticate API requests, you need to get an API key from [ipgeolocation.io](https://ipgeolocation.io/).

### How to Get Your API Key

1. **Sign up** here: [https://app.ipgeolocation.io/signup](https://app.ipgeolocation.io/signup)
2. **(optional)** Verify your email, if you signed up using email.
3. **Log in** to your account: [https://app.ipgeolocation.io/login](https://app.ipgeolocation.io/login)  
4. After logging in, navigate to your **Dashboard** to find your API key: [https://app.ipgeolocation.io/dashboard](https://app.ipgeolocation.io/dashboard)

<a id="ApiKeyAuth"></a>
### ApiKeyAuth
Once you've obtained the api key, configure your API client as follows:

The client must configure the authentication and authorization parameters in accordance with the API server security 
policy.
```python
import ipgeolocation
import os
# from dotenv import load_dotenv
# load_dotenv(".env")

# Defining the host is optional and defaults to https://api.ipgeolocation.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ipgeolocation.Configuration(
    host = "https://api.ipgeolocation.io/v2"
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.getenv("API_KEY")
```

> **Note:** Uncomment the `dotenv` part, if you placed the API_KEY in `.env` file. 

## Tests

Set the environment variable for `API_KEY` or specify in `.env` file and execute `pytest` to run the tests.

## IP Geolocation Examples

This section provides usage examples of the `get_ip_geolocation()` method from the package across **Free**, **Standard**, and **Advanced** subscription tiers. Each example highlights different combinations of parameters: `fields`, `include`, and `excludes`.

**Parameters**

- `fields`
Use this parameter to include specific fields in the response.

- `excludes`
Use this parameter to omit specific fields from the response.

- `include`
  Use this parameter to add optional modules to the response, such as:
  - `security`
  - `user_agent`
  - `hostname`
  - `liveHostname`
  - `hostnameFallbackLive`
  - `abuse`
  - `dma`
  - `time_zone`

For complete details, refer to the official documentation: [IP Geolocation API Documentation](https://ipgeolocation.io/ip-location-api.html#documentation-overview)

The `ip` parameter in the package can accept any valid IPv4 address, IPv6 address, or domain name. If `ip=` the parameter is omitted, the API will return information about the public IP address of the device or server where the package is executing.

### Developer Plan Examples

#### Get Default Fields
```python
import ipgeolocation
from pprint import pprint

with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="1.1.1.1")
    pprint(response.to_dict()) 
```
Sample Response:
```json
{
  "ip": "1.1.1.1",
  "location": {
    "continent_code": "OC",
    "continent_name": "Oceania",
    "country_code2": "AU",
    "country_code3": "AUS",
    "country_name": "Australia",
    "country_name_official": "Commonwealth of Australia",
    "country_capital": "Canberra",
    "state_prov": "Queensland",
    "state_code": "AU-QLD",
    "district": "Brisbane",
    "city": "South Brisbane",
    "zipcode": "4101",
    "latitude": "-27.47306",
    "longitude": "153.01421",
    "is_eu": false,
    "country_flag": "https://ipgeolocation.io/static/flags/au_64.png",
    "geoname_id": "10113228",
    "country_emoji": "🇦🇺"
  },
  "country_metadata": {
    "calling_code": "+61",
    "tld": ".au",
    "languages": [
      "en-AU"
    ]
  },
  "currency": {
    "code": "AUD",
    "name": "Australian Dollar",
    "symbol": "A$"
  }
}
```

Filtering Specific Fields from the Response (Use of 'exclude' and 'fields')
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="1.1.1.1", fields="location", excludes="location.continent_code,location.continent_name")
    pprint(response.to_dict())
```

Sample Response:
```json
{
  "ip": "1.1.1.1",
  "location": {
    "country_code2": "AU",
    "country_code3": "AUS",
    "country_name": "Australia",
    "country_name_official": "Commonwealth of Australia",
    "country_capital": "Canberra",
    "state_prov": "Queensland",
    "state_code": "AU-QLD",
    "district": "Brisbane",
    "city": "South Brisbane",
    "zipcode": "4101",
    "latitude": "-27.47306",
    "longitude": "153.01421",
    "is_eu": false,
    "country_flag": "https://ipgeolocation.io/static/flags/au_64.png",
    "geoname_id": "10113228",
    "country_emoji": "🇦🇺"
  }
}
```
### Standard Plan Examples
#### Get Default Fields

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="8.8.8.8")
    pprint(response.to_json())
```
Sample Response:
```json
{
  "ip": "8.8.8.8",
  "location": {
    "continent_code": "NA",
    "continent_name": "North America",
    "country_code2": "US",
    "country_code3": "USA",
    "country_name": "United States",
    "country_name_official": "United States of America",
    "country_capital": "Washington, D.C.",
    "state_prov": "California",
    "state_code": "US-CA",
    "district": "Santa Clara",
    "city": "Mountain View",
    "zipcode": "94043-1351",
    "latitude": "37.42240",
    "longitude": "-122.08421",
    "is_eu": false,
    "country_flag": "https://ipgeolocation.io/static/flags/us_64.png",
    "geoname_id": "6301403",
    "country_emoji": "🇺🇸"
  },
  "country_metadata": {
    "calling_code": "+1",
    "tld": ".us",
    "languages": [
      "en-US",
      "es-US",
      "haw",
      "fr"
    ]
  },
  "network": {
    "asn": {
      "as_number": "AS15169",
      "organization": "Google LLC",
      "country": "US"
    },
    "company": {
      "name": "Google LLC"
    }
  },
  "currency": {
    "code": "USD",
    "name": "US Dollar",
    "symbol": "$"
  }
}
```

#### Retrieving Geolocation Data in Multiple Languages
Here is an example to get the geolocation data for IP address '2001:4230:4890::1' in French language:
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="2001:4230:4890::1", lang="fr")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "2001:4230:4890:0:0:0:0:1",
  "location": {
    "continent_code": "AF",
    "continent_name": "Afrique",
    "country_code2": "MU",
    "country_code3": "MUS",
    "country_name": "Maurice",
    "country_name_official": "",
    "country_capital": "Port Louis",
    "state_prov": "Wilhems des plaines",
    "state_code": "MU-PW",
    "district": "Quatre Bornes",
    "city": "Quatre Bornes",
    "zipcode": "72201",
    "latitude": "-20.24304",
    "longitude": "57.49631",
    "is_eu": false,
    "country_flag": "https://ipgeolocation.io/static/flags/mu_64.png",
    "geoname_id": "1106777",
    "country_emoji": "🇲🇺"
  },
  "country_metadata": {
    "calling_code": "+230",
    "tld": ".mu",
    "languages": [
      "en-MU",
      "bho",
      "fr"
    ]
  },
  "network": {
    "asn": {
      "as_number": "AS52095",
      "organization": "Netassist International s.r.o.",
      "country": "CZ"
    },
    "company": {
      "name": "African Network Information Center AfriNIC Ltd"
    }
  },
  "currency": {
    "code": "MUR",
    "name": "Mauritius Rupee",
    "symbol": "₨"
  }
}
```

#### Include HostName, Timezone and User-Agent
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="219.100.37.207", fields="location.country_name,location.country_capital",
                                               include="user_agent,time_zone,hostnameFallbackLive")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "219.100.37.207",
  "hostname": "public-vpn-13-15.vpngate.v4.open.ad.jp",
  "location": {
    "country_name": "Japan",
    "country_capital": "Tokyo"
  },
  "time_zone": {
    "name": "Asia/Tokyo",
    "offset": 9,
    "offset_with_dst": 9,
    "current_time": "2025-10-29 20:55:57.268+0900",
    "current_time_unix": 1761738957.268,
    "is_dst": false,
    "dst_savings": 0,
    "dst_exists": false,
    "dst_start": {},
    "dst_end": {}
  },
  "user_agent": {
    "user_agent_string": "IPGeolocation-API/1.0.0/python",
    "name": "IPGeolocation-API",
    "type": "Special",
    "version": "1.0.0",
    "version_major": "1",
    "device": {
      "name": "Unknown",
      "type": "Unknown",
      "brand": "Unknown",
      "cpu": "Unknown"
    },
    "engine": {
      "name": "Unknown",
      "type": "Unknown",
      "version": "??",
      "version_major": "??"
    },
    "operating_system": {
      "name": "Unknown",
      "type": "Unknown",
      "version": "??",
      "version_major": "??",
      "build": "??"
    }
  }
}
```
> **Note:** Hostname Parameters possible alternatives
> 
> The IP Geolocation API supports hostname lookup for all paid subscriptions. However, this is not included by default. To enable hostname resolution, use the `include` parameter with one of the following options:
> 
> - `hostname`: Performs a quick lookup using the internal hostname database. If no match is found, the IP is returned as-is. This is fast but may produce incomplete results.
> - `liveHostname`: Queries live sources for accurate hostname resolution. This may increase response time.
> - `hostnameFallbackLive`: Attempts the internal database first, and falls back to live sources if no result is found. This option provides a balance of speed and reliability.

### Advanced Plan Examples
#### Include DMA, Abuse and Security

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="8.8.8.8", excludes="location.country_flag,location.country_emoji",
                                               include="dma,abuse,security")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "8.8.8.8",
  "location": {
    "continent_code": "NA",
    "continent_name": "North America",
    "country_code2": "US",
    "country_code3": "USA",
    "country_name": "United States",
    "country_name_official": "United States of America",
    "country_capital": "Washington, D.C.",
    "state_prov": "California",
    "state_code": "US-CA",
    "district": "Santa Clara",
    "city": "Mountain View",
    "zipcode": "94043-1351",
    "latitude": "37.42240",
    "longitude": "-122.08421",
    "is_eu": false,
    "geoname_id": "6301403",
    "accuracy_radius": "25.388",
    "locality": "Mountain View",
    "dma_code": "807"
  },
  "country_metadata": {
    "calling_code": "+1",
    "tld": ".us",
    "languages": [
      "en-US",
      "es-US",
      "haw",
      "fr"
    ]
  },
  "network": {
    "asn": {
      "as_number": "AS15169",
      "organization": "Google LLC",
      "country": "US",
      "asn_name": "GOOGLE",
      "type": "BUSINESS",
      "domain": "google.com",
      "date_allocated": "",
      "allocation_status": "",
      "num_of_ipv4_routes": "1026",
      "num_of_ipv6_routes": "106",
      "rir": "ARIN"
    },
    "connection_type": "",
    "company": {
      "name": "Google LLC",
      "type": "business",
      "domain": "google.com"
    }
  },
  "currency": {
    "code": "USD",
    "name": "US Dollar",
    "symbol": "$"
  },
  "security": {
    "threat_score": 0,
    "is_tor": false,
    "is_proxy": false,
    "proxy_type": "",
    "proxy_provider": "",
    "is_anonymous": false,
    "is_known_attacker": false,
    "is_spam": false,
    "is_bot": false,
    "is_cloud_provider": false,
    "cloud_provider": ""
  },
  "abuse": {
    "route": "8.8.8.0/24",
    "country": "",
    "handle": "ABUSE5250-ARIN",
    "name": "Abuse",
    "organization": "Abuse",
    "role": "abuse",
    "kind": "group",
    "address": "1600 Amphitheatre Parkway\nMountain View\nCA\n94043\nUnited States",
    "emails": [
      "network-abuse@google.com"
    ],
    "phone_numbers": [
      "+1-650-253-0000"
    ]
  }
}
```

These examples demonstrate typical usage of the IP Geolocation API with different subscription tiers. Use `fields` to specify exactly which data to receive, `include` for optional data like security and user agent, and `excludes` to omit specific keys from the response.

> **Note:** All features available in the Free plan are also included in the Standard and Advanced plans. Similarly, all features of the Standard plan are available in the Advanced plan.

### Bulk IP Geolocation Example
The Package also supports bulk IP geolocation requests using the `get_bulk_ip_geolocation()` method. All parameters like `fields`, `include`, and `excludes` can also be used in bulk requests.
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    bulk_ipgeolocation_request = ipgeolocation.GetBulkIpGeolocationRequest.from_dict({"ips": ["8.8.8.8", "1.1.0.0"]})
    response = api_instance.get_bulk_ip_geolocation(bulk_ipgeolocation_request, fields="location.country_name,location.city",
                                               include="security,timezone", excludes="location.continent_code")
    for item in response:
        pprint(item.to_dict())
```
## IP Security Examples

This section provides usage examples of the `get_ip_security_info()` method from the SDK across various subscription tiers. Each example demonstrates different ways to query threat intelligence and risk metadata using parameters like fields, excludes, and optional modules.

For full API specifications, refer to the [official IP Security API documentation](https://ipgeolocation.io/ip-security-api.html#documentation-overview).

---

### Get Default Fields

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPSecurityApi(client)
    response = api_instance.get_ip_security_info(ip="2.56.188.34")
    pprint(response.to_dict())
```

Sample Response:
```json
{
  "ip": "2.56.188.34",
  "security": {
    "threat_score": 80,
    "is_tor": false,
    "is_proxy": true,
    "proxy_type": "VPN",
    "proxy_provider": "Nord VPN",
    "is_anonymous": true,
    "is_known_attacker": true,
    "is_spam": false,
    "is_bot": false,
    "is_cloud_provider": true,
    "cloud_provider": "Packethub S.A."
  }
}
```

### Include Multiple Optional Fields
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPSecurityApi(client)
    response = api_instance.get_ip_security_info(ip="2.56.188.34", include="location,network,currency,time_zone,user_agent,country_metadata,hostname")
    pprint(response.to_dict())
```
> **Note:** You can get all the available fields in standard plan in combination with security data.

### Request with Field Filtering
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPSecurityApi(client)
    response = api_instance.get_ip_security_info(ip="195.154.221.54", 
                                                 fields="security.is_tor,security.is_proxy,security.is_bot,security.is_spam")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "195.154.221.54",
  "security": {
    "is_tor": false,
    "is_proxy": true,
    "is_spam": false,
    "is_bot": false
  }
}
```
### Bulk IP Security Request
The SDK also supports bulk IP Security requests using the `get_bulk_ip_security_info()` method. All parameters like `fields`, `include`, and `excludes` can also be used in bulk requests.
```python
with ipgeolocation.ApiClient(configuration) as client:
    bulk_security_request = ipgeolocation.GetBulkIpGeolocationRequest(ips=["2.56.188.34", "2.56.188.35"])
    api_instance = ipgeolocation.IPSecurityApi(client)
    response = api_instance.get_bulk_ip_security_info(bulk_security_request, include="location,network", fields="security.threat_score,location.country_name")
    for item in response:
        pprint(item.to_dict())
```
## ASN API Examples

This section provides usage examples of the `get_asn_info()` method from the SDK. These methods allow developers to retrieve detailed ASN-level network data either by ASN number or by IP address.

> **Note:** ASN API is only available in the Advanced Plan

Refer to the [ASN API documentation](https://ipgeolocation.io/asn-api.html#documentation-overview) for a detailed list of supported fields and behaviors.

### Get ASN Information by IP Address
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.ASNLookupApi(client)
    response = api_instance.get_asn_info(ip="8.8.8.8")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "8.8.8.8",
  "asn": {
    "as_number": "AS15169",
    "organization": "Google LLC",
    "country": "US",
    "asn_name": "GOOGLE",
    "type": "BUSINESS",
    "domain": "google.com",
    "date_allocated": "",
    "allocation_status": "",
    "num_of_ipv4_routes": "1026",
    "num_of_ipv6_routes": "106",
    "rir": "ARIN"
  }
}
```

### Get ASN Information by ASN Number
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.ASNLookupApi(client)
    response = api_instance.get_asn_info(asn="AS15169")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "asn": {
    "as_number": "AS15169",
    "organization": "Google LLC",
    "country": "US",
    "asn_name": "GOOGLE",
    "type": "BUSINESS",
    "domain": "google.com",
    "date_allocated": "",
    "allocation_status": "",
    "num_of_ipv4_routes": "1026",
    "num_of_ipv6_routes": "106",
    "rir": "ARIN"
  }
}
```

### Combine All objects using Include

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.ASNLookupApi(client)
    response = api_instance.get_asn_info(asn="12",
                                         include="peers,downstreams,upstreams,routes,whois_response")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "asn": {
    "as_number": "AS12",
    "organization": "New York University",
    "country": "US",
    "asn_name": "NYU-DOMAIN",
    "type": "EDUCATION",
    "domain": "nyu.edu",
    "date_allocated": "",
    "allocation_status": "",
    "num_of_ipv4_routes": "11",
    "num_of_ipv6_routes": "1",
    "rir": "ARIN",
    "routes": [
      "192.76.177.0/24",
      "...",
      "216.165.103.0/24"
    ],
    "upstreams": [
      {
        "as_number": "AS3269",
        "description": "Telecom Italia S.p.A.",
        "country": "IT"
      },
      "...",
      {
        "as_number": "AS137",
        "description": "Consortium GARR",
        "country": "IT"
      }
    ],
    "downstreams": [
      {
        "as_number": "AS394666",
        "description": "NYU Langone Health",
        "country": "US"
      },
      {
        "as_number": "AS54965",
        "description": "Polytechnic Institute of NYU",
        "country": "US"
      }
    ],
    "peers": [
      {
        "as_number": "AS3269",
        "description": "Telecom Italia S.p.A.",
        "country": "IT"
      },
      "...",
      {
        "as_number": "AS54965",
        "description": "Polytechnic Institute of NYU",
        "country": "US"
      }
    ],
    "whois_response": "<raw-whois-response>"
  }
}
```
## Abuse Contact API Examples
This section demonstrates how to use the `get_abuse_contact_info()` method of the AbuseContact API. This API helps security teams, hosting providers, and compliance professionals quickly identify the correct abuse reporting contacts for any IPv4 or IPv6 address. You can retrieve data like the responsible organization, role, contact emails, phone numbers, and address to take appropriate mitigation action against abusive or malicious activity.
> **Note:**: Abuse Contact API is only available in the Advanced Plan

Refer to the official [Abuse Contact API documentation](https://ipgeolocation.io/ip-abuse-contact-api.html#documentation-overview) for details on all available fields.
### Lookup Abuse Contact by IP
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AbuseContactApi(client)
    response = api_instance.get_abuse_contact_info(ip="1.0.1.0")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "1.0.1.0",
  "abuse": {
    "route": "1.0.1.0/24",
    "country": "CN",
    "handle": "IRT-CHINANET-CN",
    "name": "IRT-CHINANET-CN",
    "organization": "",
    "role": "abuse",
    "kind": "group",
    "address": "No.31 ,jingrong street,beijing\n100032",
    "emails": [
      "anti-spam@chinatelecom.cn"
    ],
    "phone_numbers": [
      "+86-591-83371954",
      " +86-591-83309761"
    ]
  }
}
```
### Lookup Abuse Contact with Specific Fields
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AbuseContactApi(client)
    response = api_instance.get_abuse_contact_info(ip="2.76.19.0", fields="abuse.role,abuse.emails")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "2.76.19.0",
  "abuse": {
    "role": "abuse",
    "emails": [
      "abuse@kcell.kz"
    ]
  }
}
```
### Lookup Abuse Contact while Excluding Fields
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AbuseContactApi(client)
    response = api_instance.get_abuse_contact_info(ip="2.76.19.0", excludes="abuse.handle,abuse.emails")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "2.76.19.0",
  "abuse": {
    "route": "2.76.0.0/15",
    "country": "KZ",
    "name": "Abuse-C Role",
    "organization": "",
    "role": "abuse",
    "kind": "group",
    "address": "MEDEU DISTRICT, Alimzhanov street, house 51\n050004\nAlmaty\nKAZAKHSTAN",
    "phone_numbers": [
      "+77272582755 ext. 1889"
    ]
  }
}
```
## Timezone API Examples

This section provides usage examples of the `get_timezone_info()` method from the SDK, showcasing how to fetch timezone and time-related data using different query types — IP address, latitude/longitude, and timezone ID.

For full API specifications, refer to the [Timezone API documentation](https://ipgeolocation.io/timezone-api.html#documentation-overview).

### Get Timezone by IP Address
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(ip="8.8.8.8")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "8.8.8.8",
  "location": {
    "continent_code": "NA",
    "continent_name": "North America",
    "country_code2": "US",
    "country_code3": "USA",
    "country_name": "United States",
    "country_name_official": "United States of America",
    "is_eu": false,
    "state_prov": "California",
    "state_code": "US-CA",
    "district": "Santa Clara",
    "city": "Mountain View",
    "zipcode": "94043-1351",
    "latitude": "37.42240",
    "longitude": "-122.08421"
  },
  "time_zone": {
    "name": "America/Los_Angeles",
    "offset": -8,
    "offset_with_dst": -7,
    "date": "2025-10-29",
    "date_time": "2025-10-29 05:32:11",
    "date_time_txt": "Wednesday, October 29, 2025 05:32:11",
    "date_time_wti": "Wed, 29 Oct 2025 05:32:11 -0700",
    "date_time_ymd": "2025-10-29T05:32:11-0700",
    "date_time_unix": 1761741131.303,
    "time_24": "05:32:11",
    "time_12": "05:32:11 AM",
    "week": 44,
    "month": 10,
    "year": 2025,
    "year_abbr": "25",
    "is_dst": true,
    "dst_savings": 1,
    "dst_exists": true,
    "dst_start": {
      "utc_time": "2025-03-09 TIME 10",
      "duration": "+1H",
      "gap": true,
      "date_time_after": "2025-03-09 TIME 03",
      "date_time_before": "2025-03-09 TIME 02",
      "overlap": false
    },
    "dst_end": {
      "utc_time": "2025-11-02 TIME 09",
      "duration": "-1H",
      "gap": false,
      "date_time_after": "2025-11-02 TIME 01",
      "date_time_before": "2025-11-02 TIME 02",
      "overlap": true
    }
  }
}
```
### Get Timezone by Timezone Name
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(tz="Europe/London")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "time_zone": {
    "name": "Europe/London",
    "offset": 0,
    "offset_with_dst": 0,
    "date": "2025-10-29",
    "date_time": "2025-10-29 12:33:16",
    "date_time_txt": "Wednesday, October 29, 2025 12:33:16",
    "date_time_wti": "Wed, 29 Oct 2025 12:33:16 +0000",
    "date_time_ymd": "2025-10-29T12:33:16+0000",
    "date_time_unix": 1761741196.188,
    "time_24": "12:33:16",
    "time_12": "12:33:16 PM",
    "week": 44,
    "month": 10,
    "year": 2025,
    "year_abbr": "25",
    "is_dst": false,
    "dst_savings": 0,
    "dst_exists": true,
    "dst_start": {
      "utc_time": "2025-03-30 TIME 01",
      "duration": "+1H",
      "gap": true,
      "date_time_after": "2025-03-30 TIME 02",
      "date_time_before": "2025-03-30 TIME 01",
      "overlap": false
    },
    "dst_end": {
      "utc_time": "2025-10-26 TIME 01",
      "duration": "-1H",
      "gap": false,
      "date_time_after": "2025-10-26 TIME 01",
      "date_time_before": "2025-10-26 TIME 02",
      "overlap": true
    }
  }
}
```
### Get Timezone from Any Address
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(location="Munich, Germany")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "location": {
    "location_string": "Munich, Germany",
    "country_name": "Germany",
    "state_prov": "Bavaria",
    "city": "Munich",
    "locality": "",
    "latitude": "48.13711",
    "longitude": "11.57538"
  },
  "time_zone": {
    "name": "Europe/Berlin",
    "offset": 1,
    "offset_with_dst": 1,
    "date": "2025-10-29",
    "date_time": "2025-10-29 13:34:16",
    "date_time_txt": "Wednesday, October 29, 2025 13:34:16",
    "date_time_wti": "Wed, 29 Oct 2025 13:34:16 +0100",
    "date_time_ymd": "2025-10-29T13:34:16+0100",
    "date_time_unix": 1761741256.682,
    "time_24": "13:34:16",
    "time_12": "01:34:16 PM",
    "week": 44,
    "month": 10,
    "year": 2025,
    "year_abbr": "25",
    "is_dst": false,
    "dst_savings": 0,
    "dst_exists": true,
    "dst_start": {
      "utc_time": "2025-03-30 TIME 01",
      "duration": "+1H",
      "gap": true,
      "date_time_after": "2025-03-30 TIME 03",
      "date_time_before": "2025-03-30 TIME 02",
      "overlap": false
    },
    "dst_end": {
      "utc_time": "2025-10-26 TIME 01",
      "duration": "-1H",
      "gap": false,
      "date_time_after": "2025-10-26 TIME 02",
      "date_time_before": "2025-10-26 TIME 03",
      "overlap": true
    }
  }
}
```
### Get Timezone from Location Coordinates
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(lat="48.8566", long="2.3522")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "time_zone": {
    "name": "Europe/Paris",
    "offset": 1,
    "offset_with_dst": 1,
    "date": "2025-10-29",
    "date_time": "2025-10-29 13:35:03",
    "date_time_txt": "Wednesday, October 29, 2025 13:35:03",
    "date_time_wti": "Wed, 29 Oct 2025 13:35:03 +0100",
    "date_time_ymd": "2025-10-29T13:35:03+0100",
    "date_time_unix": 1761741303.683,
    "time_24": "13:35:03",
    "time_12": "01:35:03 PM",
    "week": 44,
    "month": 10,
    "year": 2025,
    "year_abbr": "25",
    "is_dst": false,
    "dst_savings": 0,
    "dst_exists": true,
    "dst_start": {
      "utc_time": "2025-03-30 TIME 01",
      "duration": "+1H",
      "gap": true,
      "date_time_after": "2025-03-30 TIME 03",
      "date_time_before": "2025-03-30 TIME 02",
      "overlap": false
    },
    "dst_end": {
      "utc_time": "2025-10-26 TIME 01",
      "duration": "-1H",
      "gap": false,
      "date_time_after": "2025-10-26 TIME 02",
      "date_time_before": "2025-10-26 TIME 03",
      "overlap": true
    }
  }
}
```
### Get Timezone and Airport Details from IATA Code
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(iata_code="ZRH")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "airport_details": {
    "type": "large_airport",
    "name": "Zurich Airport",
    "latitude": "47.45806",
    "longitude": "8.54806",
    "elevation_ft": 1417,
    "continent_code": "EU",
    "country_code": "CH",
    "state_code": "CH-ZH",
    "city": "Zurich",
    "iata_code": "ZRH",
    "icao_code": "LSZH",
    "faa_code": ""
  },
  "time_zone": {
    "name": "Europe/Zurich",
    "offset": 1,
    "offset_with_dst": 1,
    "date": "2025-10-29",
    "date_time": "2025-10-29 13:36:36",
    "date_time_txt": "Wednesday, October 29, 2025 13:36:36",
    "date_time_wti": "Wed, 29 Oct 2025 13:36:36 +0100",
    "date_time_ymd": "2025-10-29T13:36:36+0100",
    "date_time_unix": 1761741396.833,
    "time_24": "13:36:36",
    "time_12": "01:36:36 PM",
    "week": 44,
    "month": 10,
    "year": 2025,
    "year_abbr": "25",
    "is_dst": false,
    "dst_savings": 0,
    "dst_exists": true,
    "dst_start": {
      "utc_time": "2025-03-30 TIME 01",
      "duration": "+1H",
      "gap": true,
      "date_time_after": "2025-03-30 TIME 03",
      "date_time_before": "2025-03-30 TIME 02",
      "overlap": false
    },
    "dst_end": {
      "utc_time": "2025-10-26 TIME 01",
      "duration": "-1H",
      "gap": false,
      "date_time_after": "2025-10-26 TIME 02",
      "date_time_before": "2025-10-26 TIME 03",
      "overlap": true
    }
  }
}
```
Similarly, you can fetch Airport Details and Timezone from using any ICAO code as well

### Get Timezone and City Details from UN/LOCODE

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(lo_code="ESBCN")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "lo_code_details": {
    "lo_code": "ESBCN",
    "city": "Barcelona",
    "state_code": "",
    "country_code": "ES",
    "country_name": "",
    "location_type": "Port, Rail Terminal, Road Terminal, Airport, Postal Exchange",
    "latitude": "41.38289",
    "longitude": "2.17743"
  },
  "time_zone": {
    "name": "Europe/Madrid",
    "offset": 1,
    "offset_with_dst": 1,
    "date": "2025-10-29",
    "date_time": "2025-10-29 13:37:29",
    "date_time_txt": "Wednesday, October 29, 2025 13:37:29",
    "date_time_wti": "Wed, 29 Oct 2025 13:37:29 +0100",
    "date_time_ymd": "2025-10-29T13:37:29+0100",
    "date_time_unix": 1761741449.725,
    "time_24": "13:37:29",
    "time_12": "01:37:29 PM",
    "week": 44,
    "month": 10,
    "year": 2025,
    "year_abbr": "25",
    "is_dst": false,
    "dst_savings": 0,
    "dst_exists": true,
    "dst_start": {
      "utc_time": "2025-03-30 TIME 01",
      "duration": "+1H",
      "gap": true,
      "date_time_after": "2025-03-30 TIME 03",
      "date_time_before": "2025-03-30 TIME 02",
      "overlap": false
    },
    "dst_end": {
      "utc_time": "2025-10-26 TIME 01",
      "duration": "-1H",
      "gap": false,
      "date_time_after": "2025-10-26 TIME 02",
      "date_time_before": "2025-10-26 TIME 03",
      "overlap": true
    }
  }
}
```
## Timezone Converter Examples

This section provides usage examples of the `convert_time_between_timezones()` method from the SDK. The Timezone Converter API allows you to convert a specific time from one timezone to another using timezone identifiers and optional date/time inputs.

For more details, refer to official documentation: [Timezone Converter API](https://ipgeolocation.io/timezone-api.html#convert-time-bw-time-zones).

### Convert Current Time from One Timezone to Another
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimeConversionApi(client)
    response = api_instance.convert_time_between_timezones(tz_from="America/New_York", tz_to="Asia/Tokyo")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "original_time": "2025-10-29 08:38:11",
  "converted_time": "2025-10-29 21:38:11",
  "diff_hour": 13,
  "diff_min": 780
}
```
Similarly, you can convert time from any timezone to another timezone using location coordinates (Latitude and Longitude), location addresses, IATA codes, ICAO codes and UN/LUCODE .

## User Agent API Examples

This section provides usage examples of the `parse_user_agent_string()` method from the SDK. The User Agent API extracts and classifies information from user agent strings, including browser, engine, device, OS, and type metadata.

For full explanation, visit the [User Agent API documentation](https://ipgeolocation.io/user-agent-api.html#documentation-overview).

### Parse a Basic User Agent String
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.UserAgentApi(client)
    response = api_instance.get_user_agent_details(user_agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "user_agent_string": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
  "name": "Chrome",
  "type": "Browser",
  "version": "125",
  "version_major": "125",
  "device": {
    "name": "Desktop",
    "type": "Desktop",
    "brand": "Unknown",
    "cpu": "Intel x86_64"
  },
  "engine": {
    "name": "Blink",
    "type": "Browser",
    "version": "125",
    "version_major": "125"
  },
  "operating_system": {
    "name": "Windows NT",
    "type": "Desktop",
    "version": "??",
    "version_major": "??",
    "build": "??"
  }
}
```
If you don't pass any userAgentString, the API will return the data of device's user agent.

## Bulk User Agent Parsing Example
The SDK also supports bulk User Agent parsing using the `parse_bulk_user_agent_strings()` method. This allows parsing multiple user agent strings in a single request. All fields available in single-user-agent parsing are returned per entry.
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.UserAgentApi(client)
    bulk_user_agent_string_request = ipgeolocation.ParseBulkUserAgentStringsRequest(uaStrings=[
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36",
        "Mozilla/5.0 (iPhone; CPU iPhone OS 16_0 like Mac OS X) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/16.0 Mobile/15E148 Safari/604.1"
    ])
    response = api_instance.parse_bulk_user_agent_strings(bulk_user_agent_string_request)
    for item in response:
        pprint(item.to_dict())
```
## Astronomy API Examples

This section provides usage examples of the `get_astronomy_details()` method from the SDK, allowing developers to fetch sun and moon timings and position data based on coordinates, IP, or location string.

Refer to the [official Astronomy API documentation](https://ipgeolocation.io/astronomy-api.html#documentation-overview) for more details.

### Lookup Astronomy API by Coordinates
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(lat="40.7128", long="-74.0060")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "location": {
    "country_name": "",
    "state_prov": "New York",
    "city": "New York",
    "locality": "",
    "latitude": "40.71280",
    "longitude": "-74.00600",
    "elevation": "6"
  },
  "astronomy": {
    "date": "2025-10-29",
    "current_time": "08:40:06.713",
    "mid_night": "00:39",
    "night_end": "05:51",
    "morning": {
      "astronomical_twilight_begin": "05:51",
      "astronomical_twilight_end": "06:22",
      "nautical_twilight_begin": "06:22",
      "nautical_twilight_end": "06:55",
      "civil_twilight_begin": "06:55",
      "civil_twilight_end": "07:22",
      "blue_hour_begin": "06:44",
      "blue_hour_end": "07:05",
      "golden_hour_begin": "07:05",
      "golden_hour_end": "08:01"
    },
    "sunrise": "07:22",
    "sunset": "17:56",
    "evening": {
      "golden_hour_begin": "17:17",
      "golden_hour_end": "18:13",
      "blue_hour_begin": "18:13",
      "blue_hour_end": "18:34",
      "civil_twilight_begin": "17:56",
      "civil_twilight_end": "18:24",
      "nautical_twilight_begin": "18:24",
      "nautical_twilight_end": "18:56",
      "astronomical_twilight_begin": "18:56",
      "astronomical_twilight_end": "19:28"
    },
    "night_begin": "19:28",
    "sun_status": "-",
    "solar_noon": "12:39",
    "day_length": "10:33",
    "sun_altitude": 12.448136000966024,
    "sun_distance": 148631813.8153374,
    "sun_azimuth": 120.56184419712855,
    "moon_phase": "FIRST_QUARTER",
    "moonrise": "14:25",
    "moonset": "-:-",
    "moon_status": "-",
    "moon_altitude": -61.30113457212749,
    "moon_distance": 391764.6577677882,
    "moon_azimuth": 58.61773005952898,
    "moon_parallactic_angle": -44.458475700403795,
    "moon_illumination_percentage": "48.42",
    "moon_angle": 88.19322167018869
  }
}
```
### Lookup Astronomy API by IP Address
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(ip="8.8.8.8")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "8.8.8.8",
  "location": {
    "continent_code": "NA",
    "continent_name": "North America",
    "country_code2": "US",
    "country_code3": "USA",
    "country_name": "United States",
    "country_name_official": "United States of America",
    "is_eu": false,
    "state_prov": "California",
    "state_code": "US-CA",
    "district": "Santa Clara",
    "city": "Mountain View",
    "locality": "Charleston Terrace",
    "zipcode": "94043-1351",
    "latitude": "37.42240",
    "longitude": "-122.08421",
    "elevation": "3"
  },
  "astronomy": {
    "date": "2025-10-29",
    "current_time": "05:40:54.149",
    "mid_night": "00:52",
    "night_end": "06:02",
    "morning": {
      "astronomical_twilight_begin": "06:02",
      "astronomical_twilight_end": "06:32",
      "nautical_twilight_begin": "06:32",
      "nautical_twilight_end": "07:03",
      "civil_twilight_begin": "07:03",
      "civil_twilight_end": "07:30",
      "blue_hour_begin": "06:53",
      "blue_hour_end": "07:14",
      "golden_hour_begin": "07:14",
      "golden_hour_end": "08:07"
    },
    "sunrise": "07:30",
    "sunset": "18:13",
    "evening": {
      "golden_hour_begin": "17:36",
      "golden_hour_end": "18:29",
      "blue_hour_begin": "18:29",
      "blue_hour_end": "18:50",
      "civil_twilight_begin": "18:13",
      "civil_twilight_end": "18:40",
      "nautical_twilight_begin": "18:40",
      "nautical_twilight_end": "19:10",
      "astronomical_twilight_begin": "19:10",
      "astronomical_twilight_end": "19:41"
    },
    "night_begin": "19:41",
    "sun_status": "-",
    "solar_noon": "12:51",
    "day_length": "10:43",
    "sun_altitude": -22.275372119240597,
    "sun_distance": 148631813.8153374,
    "sun_azimuth": 90.42154204396991,
    "moon_phase": "FIRST_QUARTER",
    "moonrise": "14:33",
    "moonset": "-:-",
    "moon_status": "-",
    "moon_altitude": -66.20124367819894,
    "moon_distance": 391761.7015893756,
    "moon_azimuth": 302.768681709635,
    "moon_parallactic_angle": 46.284039629615826,
    "moon_illumination_percentage": "48.43",
    "moon_angle": 88.19958116083994
  }
}
```
### Lookup Astronomy API by Location String
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(location="Milan, Italy")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "location": {
    "location_string": "Milan, Italy",
    "country_name": "Italy",
    "state_prov": "Lombardy",
    "city": "Milan",
    "locality": "",
    "latitude": "45.46419",
    "longitude": "9.18963",
    "elevation": "122"
  },
  "astronomy": {
    "date": "2025-10-29",
    "current_time": "13:41:41.772",
    "mid_night": "00:07",
    "night_end": "05:18",
    "morning": {
      "astronomical_twilight_begin": "05:18",
      "astronomical_twilight_end": "05:53",
      "nautical_twilight_begin": "05:53",
      "nautical_twilight_end": "06:28",
      "civil_twilight_begin": "06:28",
      "civil_twilight_end": "06:56",
      "blue_hour_begin": "06:16",
      "blue_hour_end": "06:39",
      "golden_hour_begin": "06:39",
      "golden_hour_end": "07:41"
    },
    "sunrise": "06:56",
    "sunset": "17:16",
    "evening": {
      "golden_hour_begin": "16:32",
      "golden_hour_end": "17:33",
      "blue_hour_begin": "17:33",
      "blue_hour_end": "17:57",
      "civil_twilight_begin": "17:16",
      "civil_twilight_end": "17:45",
      "nautical_twilight_begin": "17:45",
      "nautical_twilight_end": "18:20",
      "astronomical_twilight_begin": "18:20",
      "astronomical_twilight_end": "18:54"
    },
    "night_begin": "18:54",
    "sun_status": "-",
    "solar_noon": "12:06",
    "day_length": "10:20",
    "sun_altitude": 27.13769081211636,
    "sun_distance": 148631813.8153374,
    "sun_azimuth": 206.01750232947694,
    "moon_phase": "FIRST_QUARTER",
    "moonrise": "14:00",
    "moonset": "23:11",
    "moon_status": "-",
    "moon_altitude": -2.9742526309771478,
    "moon_distance": 391758.7335065162,
    "moon_azimuth": 119.56024949439859,
    "moon_parallactic_angle": -41.32141396017013,
    "moon_illumination_percentage": "48.43",
    "moon_angle": 88.20596582035996
  }
}
```
### Lookup Astronomy API for a Specific Date
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(lat="-27.47", long="153.02", var_date="2025-01-01")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "location": {
    "country_name": "Australia",
    "state_prov": "Queensland",
    "city": "Brisbane",
    "locality": "Brisbane",
    "latitude": "-27.47000",
    "longitude": "153.02000",
    "elevation": ""
  },
  "astronomy": {
    "date": "2025-01-01",
    "current_time": "22:43:02.846",
    "mid_night": "23:51",
    "night_end": "03:24",
    "morning": {
      "astronomical_twilight_begin": "03:24",
      "astronomical_twilight_end": "03:57",
      "nautical_twilight_begin": "03:57",
      "nautical_twilight_end": "04:29",
      "civil_twilight_begin": "04:29",
      "civil_twilight_end": "04:56",
      "blue_hour_begin": "04:19",
      "blue_hour_end": "04:40",
      "golden_hour_begin": "04:40",
      "golden_hour_end": "05:30"
    },
    "sunrise": "04:56",
    "sunset": "18:46",
    "evening": {
      "golden_hour_begin": "18:12",
      "golden_hour_end": "19:02",
      "blue_hour_begin": "19:02",
      "blue_hour_end": "19:23",
      "civil_twilight_begin": "18:46",
      "civil_twilight_end": "19:13",
      "nautical_twilight_begin": "19:13",
      "nautical_twilight_end": "19:45",
      "astronomical_twilight_begin": "19:45",
      "astronomical_twilight_end": "20:18"
    },
    "night_begin": "20:18",
    "sun_status": "-",
    "solar_noon": "11:51",
    "day_length": "13:50",
    "sun_altitude": -36.92878445493417,
    "sun_distance": 147102938.88036567,
    "sun_azimuth": 199.8584254941809,
    "moon_phase": "NEW_MOON",
    "moonrise": "05:42",
    "moonset": "20:08",
    "moon_status": "-",
    "moon_altitude": -26.06793971140284,
    "moon_distance": 380199.6748065481,
    "moon_azimuth": 219.86344344944166,
    "moon_parallactic_angle": 141.4485711716647,
    "moon_illumination_percentage": "2.93",
    "moon_angle": 19.702790945717158
  }
}
```
### Lookup Location info in Different Language
You can also get Astronomy Data in other languages as well. Only paid subscriptions can access this feature.
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(ip="1.1.1.1", lang="ru")
    pprint(response.to_dict())
```
Sample Response:
```json
{
  "ip": "1.1.1.1",
  "location": {
    "continent_code": "OC",
    "continent_name": "Океания",
    "country_code2": "AU",
    "country_code3": "AUS",
    "country_name": "Австралия",
    "country_name_official": "",
    "is_eu": false,
    "state_prov": "Квинсленд",
    "state_code": "AU-QLD",
    "district": "Брисбен",
    "city": "Юг Брисбен",
    "locality": "",
    "zipcode": "4101",
    "latitude": "-27.47306",
    "longitude": "153.01421",
    "elevation": ""
  },
  "astronomy": {
    "date": "2025-10-29",
    "current_time": "22:50:12.521",
    "mid_night": "23:31",
    "...": "",
    "moon_angle": 88.27444648710816
  }
}
```

## Documentation For Models
- [ASNConnection](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/ASNConnection.md)
- [ASNResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/ASNResponse.md)
- [ASNDetails](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/ASNDetails.md)
- [Abuse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/Abuse.md)
- [AbuseResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/AbuseResponse.md)
- [Astronomy](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/Astronomy.md)
- [AstronomyEvening](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/AstronomyEvening.md)
- [AstronomyLocation](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/AstronomyLocation.md)
- [AstronomyMorning](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/AstronomyMorning.md)
- [AstronomyResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/AstronomyResponse.md)
- [CountryMetadata](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/CountryMetadata.md)
- [Currency](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/Currency.md)
- [ErrorResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/ErrorResponse.md)
- [GeolocationResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/GeolocationResponse.md)
- [GetBulkIpGeolocationResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/GetBulkIpGeolocationResponse.md)
- [GetBulkIpGeolocationRequest](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/GetBulkIpGeolocationRequest.md)
- [GetBulkIpSecurityInfoResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/GetBulkIpSecurityInfoResponse.md)
- [Location](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/Location.md)
- [LocationMinimal](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/LocationMinimal.md)
- [Network](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/Network.md)
- [NetworkAsn](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/NetworkAsn.md)
- [NetworkCompany](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/NetworkCompany.md)
- [NetworkMinimal](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/NetworkMinimal.md)
- [NetworkMinimalAsn](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/NetworkMinimalAsn.md)
- [NetworkMinimalCompany](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/NetworkMinimalCompany.md)
- [ParseBulkUserAgentStringsRequest](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/ParseBulkUserAgentStringsRequest.md)
- [ParseUserAgentStringRequest](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/ParseUserAgentStringRequest.md)
- [Security](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/Security.md)
- [IPSecurityAPIResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/IPSecurityAPIResponse.md)
- [TimeConversionResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimeConversionResponse.md)
- [TimeSeries](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimeSeries.md)
- [TimeZone](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimeZone.md)
- [TimeZoneDetailedResponse](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimeZoneDetailedResponse.md)
- [TimeZoneDstEnd](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimeZoneDstEnd.md)
- [TimeZoneDstStart](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimeZoneDstStart.md)
- [TimezoneAirport](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimezoneAirport.md)
- [TimezoneDetail](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimezoneDetail.md)
- [TimezoneDetailDstEnd](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimezoneDetailDstEnd.md)
- [TimezoneDetailDstStart](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimezoneDetailDstStart.md)
- [TimezoneLocation](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimezoneLocation.md)
- [TimezoneLocode](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/TimezoneLocode.md)
- [UserAgentData](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/UserAgentData.md)
- [UserAgentDataDevice](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/UserAgentDataDevice.md)
- [UserAgentDataEngine](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/UserAgentDataEngine.md)
- [UserAgentDataOperatingSystem](https://github.com/IPGeolocation/ip-geolocation-api-python-sdk/blob/master/docs/UserAgentDataOperatingSystem.md)

