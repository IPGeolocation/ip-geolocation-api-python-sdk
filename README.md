# IP Geolocation API Python SDK
IPGeolocation.io – Real-time IP Intelligence, Threat Detection APIs & Database Solutions

- API version: 1.0.0

## IPGeolocation.io Package/SDK for Python
[IPGeolocation API](https://ipgeolocation.io) is the solution to identify country code (ISO2 and ISO3 standard), 
country name, continent code, continent name, country capital, state/province, district, city, zip code, latitude and 
longitude of city, is country belongs to Europian Union, calling code, top level domain (TLD), languages, country flag, 
internet service provider (ISP), connection type, organization, geoname ID, currency code, currency name, time zone ID, 
time zone offset, current time in the time zone, is time zone in daylight saving time, total daylight savings, 
IP security info including is_proxy, is_cloud_provider, is_bot, Abuse Contact info related to an IP address and 
Parse the User Agent String. This document provides important information to help you get up to speed with IPGeolocation API using IP Geolocation 
API Python SDK.

Developers can use this Python SDK for software and web projects related to, but not limited to:

1. Display native language and currency
2. Redirect based on the country
3. Digital rights management
4. Web log stats and analysis
5. Auto-selection of country, state/province and city on forms
6. Filter access from countries you do not do business with
7. Geo-targeting for increased sales and click-through

## Table of Contents
1. [Installation](#installation)
   - [Using Pip](#pip-install)
   - [Manual Installation](#setuptools)
2. [Authentication Setup](#authentication-setup)
   - [1. How to Get Your API Key](#how-to-get-your-api-key)
   - [2. ApiKeyAuth](#apikeyauth)
3. [Tests setup](#tests)
4. [API Endpoints](#api-endpoints)
3. [IP Geolocation Examples](#ip-geolocation-examples)
   - [1. Developer (Free) Plan Examples](#1-developer-plan-examples)
   - [2. Standard Plan Examples](#2-standard-plan-examples)
   - [3. Advanced Plan Examples](#3-advanced-plan-examples)
   - [Bulk IP Geolocation Example](#bulk-ip-geolocation-example)

4. [IP Security Examples](#ip-security-examples)
   - [Basic Request (Minimal Setup)](#basic-request-minimal-setup)
   - [Include Multiple Optional Fields](#include-multiple-optional-fields)
   - [Request with Field Filtering](#request-with-field-filtering)
   - [Bulk IP Security Request](#bulk-ip-security-request)

5. [ASN API Examples](#asn-api-examples)
   - [Get ASN Information by IP Address](#get-asn-information-by-ip-address)
   - [Get ASN Information by ASN Number](#get-asn-information-by-asn-number)
   - [Combine All objects using Include](#combine-all-objects-using-include)
  
6. [Abuse Contact API Examples](#abuse-contact-api-examples)
   - [Lookup Abuse Contact by IP](#lookup-abuse-contact-by-ip)
   - [Lookup Abuse Contact with Specific Fields](#lookup-abuse-contact-with-specific-fields)
   - [Lookup Abuse Contact while Excluding Fields](#lookup-abuse-contact-while-excluding-fields)

7. [Timezone API Examples](#timezone-api-examples)
   - [Get Timezone by IP Address](#get-timezone-by-ip-address)
   - [Get Timezone by Timezone Name](#get-timezone-by-timezone-name)
   - [Get Timezone from Any Address](#get-timezone-from-any-address)
   - [Get Timezone from Location Coordinates](#get-timezone-from-location-coordinates)
   - [Get Timezone and Airport Details from IATA Code](#get-timezone-and-airport-details-from-iata-code)
   - [Get Timezone and City Details from UN/LOCODE](#get-timezone-and-city-details-from-unlocode)

8. [Timezone Converter Examples](#timezone-converter-examples)
   - [Convert Current Time from One Timezone to Another](#convert-current-time-from-one-timezone-to-another)

9. [User Agent API Examples](#user-agent-api-examples)
   - [Parse a Basic User Agent String](#parse-a-basic-user-agent-string)
   - [Bulk User Agent Parsing Example](#bulk-user-agent-parsing-example)
10. [Astronomy API Examples](#astronomy-api-examples)
   - [Astronomy by Coordinates](#astronomy-by-coordinates)
   - [Astronomy by IP Address](#astronomy-by-ip-address)
   - [Astronomy by Location String](#astronomy-by-location-string)
   - [Astronomy for Specific Date](#astronomy-for-specific-date)
   - [Astronomy in Different Language](#astronomy-in-different-language)

11. [Documentation for Models](#documentation-for-models)



# Installation
## Requirements

- Python 3.9+

## pip install

You can install package directly using:

```sh
pip install ipgeolocationio
```
(you may need to run `pip` with root permission: `sudo pip install ipgeolocation`)

Then import the package:
```python
import ipgeolocation
```

### Setuptools

Install via [Setuptools](http://pypi.python.org/pypi/setuptools).

```sh
git clone https://github.com/IPGeolocation/ip-geolocation-api-python-sdk.git
python ip-geolocation-api-python-sdk/setup.py install --user
```
(or `sudo python ip-geolocation-api-python-sdk/setup.py install` to install the package for all users)

Then import the package:
```python
import ipgeolocation
```

# API Endpoints

All URIs are relative to *https://api.ipgeolocation.io/v2*

Class | Method | HTTP request | Description
------------ | ------------- | ------------- | -------------
*ASNLookupApi* | [**get_asn_info**](docs/ASNLookupApi.md#get_asn_info) | **GET** /asn | Get details of any ASN number or associated IP address
*AbuseContactApi* | [**get_abuse_contact_info**](docs/AbuseContactApi.md#get_abuse_contact_info) | **GET** /abuse | Retrieve abuse reporting contact information for a given IP address
*AstronomyApi* | [**get_astronomy_details**](docs/AstronomyApi.md#get_astronomy_details) | **GET** /astronomy | Get sunrise, sunset, moonrise, moonset, and related data for a location
*AstronomyApi* | [**get_time_series_lookup**](docs/AstronomyApi.md#get_time_series_lookup) | **GET** /astronomy/timeSeries | Get astronomy information for given date range at once
*IPGeolocationApi* | [**get_bulk_ip_geolocation**](docs/IPGeolocationApi.md#get_bulk_ip_geolocation) | **POST** /ipgeo-bulk | Get geolocation data for multiple IP addresses in a single API request
*IPGeolocationApi* | [**get_ip_geolocation**](docs/IPGeolocationApi.md#get_ip_geolocation) | **GET** /ipgeo | Get geolocation data for a single IP address
*IPSecurityApi* | [**get_bulk_ip_security_info**](docs/IPSecurityApi.md#get_bulk_ip_security_info) | **POST** /security-bulk | Retrieve security threat intelligence for multiple IPs
*IPSecurityApi* | [**get_ip_security_info**](docs/IPSecurityApi.md#get_ip_security_info) | **GET** /security | Retrieve security information (VPN, TOR, proxy, etc.) for a single IP
*TimeConversionApi* | [**convert_time_between_timezones**](docs/TimeConversionApi.md#convert_time_between_timezones) | **GET** /timezone/convert | Convert time between two specified timezones
*TimezoneApi* | [**get_timezone_info**](docs/TimezoneApi.md#get_timezone_info) | **GET** /timezone | Timezone information details
*UserAgentApi* | [**get_user_agent_details**](docs/UserAgentApi.md#get_user_agent_details) | **GET** /user-agent | Get details of user-agent
*UserAgentApi* | [**parse_bulk_user_agent_strings**](docs/UserAgentApi.md#parse_bulk_user_agent_strings) | **POST** /user-agent-bulk | Handle multiple user-agent string lookups
*UserAgentApi* | [**parse_user_agent_string**](docs/UserAgentApi.md#parse_user_agent_string) | **POST** /user-agent | Handle single User-Agent string

## Authentication Setup
To authenticate API requests, you need an API key from [ipgeolocation.io](https://ipgeolocation.io/).

## How to Get Your API Key

1. **Sign up** here: [https://app.ipgeolocation.io/signup](https://app.ipgeolocation.io/signup)  
2. **Log in** to your account: [https://app.ipgeolocation.io/login](https://app.ipgeolocation.io/login)  
3. After logging in, navigate to your **Dashboard** to find your API key: [https://app.ipgeolocation.io/dashboard](https://app.ipgeolocation.io/dashboard)

## API Plan Tiers and Documentation

The documentation below corresponds to the four available API tier plans:

- **Developer Plan** (Free): [Full Documentation](https://ipgeolocation.io/ip-location-api.html#Free)
- **Standard Plan**: [Full Documentation](https://ipgeolocation.io/ip-location-api.html#Standard)
- **Advance Plan**: [Full Documentation](https://ipgeolocation.io/ip-location-api.html#Advance)
- **Security Plan**: [Full Documentation](https://ipgeolocation.io/ip-security-api.html#documentation-overview)

For a detailed comparison of what each plan offers, visit the [Pricing Page](https://ipgeolocation.io/pricing.html).

<a id="ApiKeyAuth"></a>
## ApiKeyAuth
Once you've obtained the api key, configure your API client as follows:

The client must configure the authentication and authorization parameters in accordance with the API server security 
policy.
```python
import ipgeolocation
import os

# Defining the host is optional and defaults to https://api.ipgeolocation.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ipgeolocation.Configuration(
    host = "https://api.ipgeolocation.io/v2"
)

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.getenv("API_KEY")
```


### Tests

Set the environment variable for `API_KEY` or specify in `.env` file and execute `pytest` to run the tests.


# Example Usage

## IP Geolocation Examples

This section provides usage examples of the `get_ip_geolocation()` method from the package across Free, Standard, and Advanced subscription tiers. Each example highlights different combinations of parameters: `fields`, `include`, and `excludes`.

### Parameters

#### `fields`
Use this parameter to include specific fields in the response.

#### `excludes`
Use this parameter to omit specific fields from the response.

#### `include`
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

### 1. Developer Plan Examples

#### Default Fields
```python
import ipgeolocation
from pprint import pprint

with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="1.1.1.1")
    pprint(response.to_dict()) 
```
Sample Response:
```text
{'country_metadata': {'calling_code': '+61',
                      'languages': ['en-AU'],
                      'tld': '.au'},
 'currency': {'code': 'AUD', 'name': 'Australian Dollar', 'symbol': 'A$'},
 'ip': '1.1.1.1',
 'location': {'city': 'South Brisbane',
              'continent_code': 'OC',
              'continent_name': 'Oceania',
              'country_capital': 'Canberra',
              'country_code2': 'AU',
              'country_code3': 'AUS',
              'country_emoji': '🇦🇺',
              'country_flag': 'https://ipgeolocation.io/static/flags/au_64.png',
              'country_name': 'Australia',
              'country_name_official': 'Commonwealth of Australia',
              'district': 'Brisbane',
              'geoname_id': '10113228',
              'is_eu': False,
              'latitude': '-27.47306',
              'longitude': '153.01421',
              'state_code': 'AU-QLD',
              'state_prov': 'Queensland',
              'zipcode': '4101'}}
```

Filtering Specific Fields from the Response (Use of 'exclude' and 'fields')
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="1.1.1.1", fields="location", excludes="location.continent_code,location.continent_name")
    pprint(response.to_dict())
```

Sample Response:
```text
{'ip': '1.1.1.1',
 'location': {'city': 'South Brisbane',
              'country_capital': 'Canberra',
              'country_code2': 'AU',
              'country_code3': 'AUS',
              'country_emoji': '🇦🇺',
              'country_flag': 'https://ipgeolocation.io/static/flags/au_64.png',
              'country_name': 'Australia',
              'country_name_official': 'Commonwealth of Australia',
              'district': 'Brisbane',
              'geoname_id': '10113228',
              'is_eu': False,
              'latitude': '-27.47306',
              'longitude': '153.01421',
              'state_code': 'AU-QLD',
              'state_prov': 'Queensland',
              'zipcode': '4101'}}
```
### 2. Standard Plan Examples
#### Default Fields

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="8.8.8.8")
    pprint(response.to_json())
```
Sample Response:
```text
{'country_metadata': {'calling_code': '+1',
                      'languages': ['en-US', 'es-US', 'haw', 'fr'],
                      'tld': '.us'},
 'currency': {'code': 'USD', 'name': 'US Dollar', 'symbol': '$'},
 'ip': '8.8.8.8',
 'location': {'city': 'Mountain View',
              'continent_code': 'NA',
              'continent_name': 'North America',
              'country_capital': 'Washington, D.C.',
              'country_code2': 'US',
              'country_code3': 'USA',
              'country_emoji': '🇺🇸',
              'country_flag': 'https://ipgeolocation.io/static/flags/us_64.png',
              'country_name': 'United States',
              'country_name_official': 'United States of America',
              'district': 'Santa Clara',
              'geoname_id': '6301403',
              'is_eu': False,
              'latitude': '37.42240',
              'longitude': '-122.08421',
              'state_code': 'US-CA',
              'state_prov': 'California',
              'zipcode': '94043-1351'},
 'network': {'asn': {'as_number': 'AS15169',
                     'country': 'US',
                     'organization': 'Google LLC'},
             'company': {'name': 'Google LLC'}}}
```

### Retrieving Geolocation Data in Multiple Languages
Here is an example to get the geolocation data for IP address '2001:4230:4890::1' in French language:
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="2001:4230:4890::1", lang="fr")
    pprint(response.to_dict())
```
Sample Response:
```text
{'country_metadata': {'calling_code': '+230',
                      'languages': ['en-MU', 'bho', 'fr'],
                      'tld': '.mu'},
 'currency': {'code': 'MUR', 'name': 'Mauritius Rupee', 'symbol': '₨'},
 'ip': '2001:4230:4890:0:0:0:0:1',
 'location': {'city': 'Quatre Bornes',
              'continent_code': 'AF',
              'continent_name': 'Afrique',
              'country_capital': 'Port Louis',
              'country_code2': 'MU',
              'country_code3': 'MUS',
              'country_emoji': '🇲🇺',
              'country_flag': 'https://ipgeolocation.io/static/flags/mu_64.png',
              'country_name': 'Maurice',
              'country_name_official': '',
              'district': 'Quatre Bornes',
              'geoname_id': '1106777',
              'is_eu': False,
              'latitude': '-20.24304',
              'longitude': '57.49631',
              'state_code': 'MU-PW',
              'state_prov': 'Wilhems des plaines',
              'zipcode': '72201'},
 'network': {'asn': {'as_number': 'AS0', 'country': '', 'organization': ''},
             'company': {'name': 'African Network Information Center AfriNIC '
                                 'Ltd'}}}
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
```text
{'hostname': 'public-vpn-13-15.vpngate.v4.open.ad.jp',
 'ip': '219.100.37.207',
 'location': {'country_capital': 'Tokyo', 'country_name': 'Japan'},
 'time_zone': {'current_time': '2025-08-07 18:47:11.809+0900',
               'current_time_unix': 1754560031.809,
               'dst_end': {},
               'dst_exists': False,
               'dst_savings': 0,
               'dst_start': {},
               'is_dst': False,
               'name': 'Asia/Tokyo',
               'offset': 9,
               'offset_with_dst': 9},
 'user_agent': {'device': {'brand': 'Unknown',
                           'cpu': 'Unknown',
                           'name': 'Unknown',
                           'type': 'Unknown'},
                'engine': {'name': 'Unknown',
                           'type': 'Unknown',
                           'version': '??',
                           'version_major': '??'},
                'name': 'IPGeolocation-API',
                'operating_system': {'build': '??',
                                     'name': 'Unknown',
                                     'type': 'Unknown',
                                     'version': '??',
                                     'version_major': '??'},
                'type': 'Special',
                'user_agent_string': 'IPGeolocation-API/1.0.0/python',
                'version': '1.0.0',
                'version_major': '1'}}
```
**Note on Hostname Parameters**

The IP Geolocation API supports hostname lookup for all paid subscriptions. However, this is not included by default. To enable hostname resolution, use the `include` parameter with one of the following options:

- `hostname`: Performs a quick lookup using the internal hostname database. If no match is found, the IP is returned as-is. This is fast but may produce incomplete results.
- `liveHostname`: Queries live sources for accurate hostname resolution. This may increase response time.
- `hostnameFallbackLive`: Attempts the internal database first, and falls back to live sources if no result is found. This option provides a balance of speed and reliability.

### 3. Advanced Plan Examples
#### Include DMA, Abuse and Security

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPGeolocationApi(client)
    response = api_instance.get_ip_geolocation(ip="8.8.8.8", excludes="location.country_flag,location.country_emoji",
                                               include="dma,abuse,security")
    pprint(response.to_dict())
```
Sample Response:
```text
{'abuse': {'address': '1600 Amphitheatre Parkway\n'
                      'Mountain View\n'
                      'CA\n'
                      '94043\n'
                      'United States',
           'country': '',
           'emails': ['network-abuse@google.com'],
           'handle': 'ABUSE5250-ARIN',
           'kind': 'group',
           'name': 'Abuse',
           'organization': 'Abuse',
           'phone_numbers': ['+1-650-253-0000'],
           'role': 'abuse',
           'route': '8.8.8.0/24'},
 'country_metadata': {'calling_code': '+1',
                      'languages': ['en-US', 'es-US', 'haw', 'fr'],
                      'tld': '.us'},
 'currency': {'code': 'USD', 'name': 'US Dollar', 'symbol': '$'},
 'ip': '8.8.8.8',
 'location': {'accuracy_radius': '',
              'city': 'Mountain View',
              'continent_code': 'NA',
              'continent_name': 'North America',
              'country_capital': 'Washington, D.C.',
              'country_code2': 'US',
              'country_code3': 'USA',
              'country_name': 'United States',
              'country_name_official': 'United States of America',
              'district': 'Santa Clara',
              'dma_code': '807',
              'geoname_id': '6301403',
              'is_eu': False,
              'latitude': '37.42240',
              'locality': 'Mountain View',
              'longitude': '-122.08421',
              'state_code': 'US-CA',
              'state_prov': 'California',
              'zipcode': '94043-1351'},
 'network': {'asn': {'allocation_status': 'assigned',
                     'as_number': 'AS15169',
                     'asn_name': 'GOOGLE',
                     'country': 'US',
                     'date_allocated': '',
                     'domain': 'about.google',
                     'num_of_ipv4_routes': '991',
                     'num_of_ipv6_routes': '104',
                     'organization': 'Google LLC',
                     'rir': 'ARIN',
                     'type': 'BUSINESS'},
             'company': {'domain': '', 'name': 'Google LLC', 'type': ''},
             'connection_type': ''},
 'security': {'cloud_provider': '',
              'is_anonymous': False,
              'is_bot': False,
              'is_cloud_provider': False,
              'is_known_attacker': False,
              'is_proxy': False,
              'is_spam': False,
              'is_tor': False,
              'proxy_provider': '',
              'proxy_type': '',
              'threat_score': 0}}
```

These examples demonstrate typical usage of the IP Geolocation API with different subscription tiers. Use `fields` to specify exactly which data to receive, `include` for optional data like security and user agent, and `excludes` to omit specific keys from the response.

**Note:** All features available in the Free plan are also included in the Standard and Advanced plans. Similarly, all features of the Standard plan are available in the Advanced plan.

## Bulk IP Geolocation Example
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

### Basic Request (Minimal Setup)

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPSecurityApi(client)
    response = api_instance.get_ip_security_info(ip="2.56.188.34")
    pprint(response.to_dict())
```

Sample Response:
```text
{'ip': '2.56.188.34',
 'security': {'cloud_provider': 'Packethub S.A.',
              'is_anonymous': True,
              'is_bot': False,
              'is_cloud_provider': True,
              'is_known_attacker': True,
              'is_proxy': True,
              'is_spam': False,
              'is_tor': False,
              'proxy_provider': 'Nord VPN',
              'proxy_type': 'VPN',
              'threat_score': 80}}
```

### Include Multiple Optional Fields
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPSecurityApi(client)
    response = api_instance.get_ip_security_info(ip="2.56.188.34", include="location,network,currency,time_zone,user_agent,country_metadata,hostname")
    pprint(response.to_dict())
```
Sample Response:
```text
{'country_metadata': {'calling_code': '+1',
                      'languages': ['en-US', 'es-US', 'haw', 'fr'],
                      'tld': '.us'},
 'currency': {'code': 'USD', 'name': 'US Dollar', 'symbol': '$'},
 'hostname': '2.56.188.34',
 'ip': '2.56.188.34',
 'location': {'city': 'Dallas',
              'continent_code': 'NA',
              'continent_name': 'North America',
              'country_capital': 'Washington, D.C.',
              'country_code2': 'US',
              'country_code3': 'USA',
              'country_emoji': '🇺🇸',
              'country_flag': 'https://ipgeolocation.io/static/flags/us_64.png',
              'country_name': 'United States',
              'country_name_official': 'United States of America',
              'district': 'Dallas',
              'geoname_id': '4684902',
              'is_eu': False,
              'latitude': '32.77822',
              'longitude': '-96.79512',
              'state_code': 'US-TX',
              'state_prov': 'Texas',
              'zipcode': '75201'},
 'network': {'asn': {'as_number': 'AS62240',
                     'country': 'GB',
                     'organization': 'Clouvider Limited'},
             'company': {'name': 'Packethub S.A.'}},
 'security': {'cloud_provider': 'Packethub S.A.',
              'is_anonymous': True,
              'is_bot': False,
              'is_cloud_provider': True,
              'is_known_attacker': True,
              'is_proxy': True,
              'is_spam': False,
              'is_tor': False,
              'proxy_provider': 'Nord VPN',
              'proxy_type': 'VPN',
              'threat_score': 80},
 'time_zone': {'current_time': '2025-08-07 14:31:46.086-0500',
               'current_time_unix': 1754595106.086,
               'dst_end': {'date_time_after': '2025-11-02 TIME 01',
                           'date_time_before': '2025-11-02 TIME 02',
                           'duration': '-1H',
                           'gap': False,
                           'overlap': True,
                           'utc_time': '2025-11-02 TIME 07'},
               'dst_exists': True,
               'dst_savings': 1,
               'dst_start': {'date_time_after': '2025-03-09 TIME 03',
                             'date_time_before': '2025-03-09 TIME 02',
                             'duration': '+1H',
                             'gap': True,
                             'overlap': False,
                             'utc_time': '2025-03-09 TIME 08'},
               'is_dst': True,
               'name': 'America/Chicago',
               'offset': -6,
               'offset_with_dst': -5},
 'user_agent': {'device': {'brand': 'Unknown',
                           'cpu': 'Unknown',
                           'name': 'Unknown',
                           'type': 'Unknown'},
                'engine': {'name': 'Unknown',
                           'type': 'Unknown',
                           'version': '??',
                           'version_major': '??'},
                'name': 'IPGeolocation-API',
                'operating_system': {'build': '??',
                                     'name': 'Unknown',
                                     'type': 'Unknown',
                                     'version': '??',
                                     'version_major': '??'},
                'type': 'Special',
                'user_agent_string': 'IPGeolocation-API/1.0.0/python',
                'version': '1.0.0',
                'version_major': '1'}}
```

### Request with Field Filtering
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.IPSecurityApi(client)
    response = api_instance.get_ip_security_info(ip="195.154.221.54", 
                                                 fields="security.is_tor,security.is_proxy,security.is_bot,security.is_spam")
    pprint(response.to_dict())
```
Sample Response:
```text
{'ip': '195.154.221.54',
 'security': {'is_bot': False,
              'is_proxy': True,
              'is_spam': False,
              'is_tor': False}}
```
## Bulk IP Security Request
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

> **Note**: ASN API is only available in the Advanced Plan

Refer to the [ASN API documentation](https://ipgeolocation.io/asn-api.html#documentation-overview) for a detailed list of supported fields and behaviors.

### Get ASN Information by IP Address
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.ASNLookupApi(client)
    response = api_instance.get_asn_info(ip="8.8.8.8")
    pprint(response.to_dict())
```
Sample Response:
```text
{'asn': {'allocation_status': 'assigned',
         'as_number': 'AS15169',
         'asn_name': 'GOOGLE',
         'country': 'US',
         'date_allocated': '',
         'domain': 'about.google',
         'num_of_ipv4_routes': '991',
         'num_of_ipv6_routes': '104',
         'organization': 'Google LLC',
         'rir': 'ARIN',
         'type': 'BUSINESS'},
 'ip': '8.8.8.8'}
```

### Get ASN Information by ASN Number
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.ASNLookupApi(client)
    response = api_instance.get_asn_info(asn="AS15169")
    pprint(response.to_dict())
```
Sample Response:
```text
{'asn': {'allocation_status': 'assigned',
         'as_number': 'AS15169',
         'asn_name': 'GOOGLE',
         'country': 'US',
         'date_allocated': '',
         'domain': 'about.google',
         'num_of_ipv4_routes': '991',
         'num_of_ipv6_routes': '104',
         'organization': 'Google LLC',
         'rir': 'ARIN',
         'type': 'BUSINESS'}}
```

### Combine All objects using Include

```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.ASNLookupApi(client)
    response = api_instance.get_asn_info(asn=12,
                                         include="peers,downstreams,upstreams,routes,whois_response")
    pprint(response.to_dict())
```
Sample Response:
```text
{'asn': {'allocation_status': 'assigned',
         'as_number': 'AS12',
         'asn_name': 'NYU-DOMAIN',
         'country': 'US',
         'date_allocated': '',
         'domain': 'nyu.edu',
         'downstreams': [{'as_number': 'AS394666',
                          'country': 'US',
                          'description': 'NYU Langone Health'},
                         {'as_number': 'AS54965',
                          'country': 'US',
                          'description': 'Polytechnic Institute of NYU'}],
         'num_of_ipv4_routes': '11',
         'num_of_ipv6_routes': '1',
         'organization': 'New York University',
         'peers': [{'as_number': 'AS3269',
                    'country': 'IT',
                    'description': 'Telecom Italia S.p.A.'},
                   {'as_number': 'AS8220',
                    'country': 'GB',
                    'description': 'COLT Technology Services Group Limited'},
                   {'as_number': 'AS394666',
                    'country': 'US',
                    'description': 'NYU Langone Health'},
                   {'as_number': 'AS286',
                    'country': 'NL',
                    'description': 'GTT Communications Inc.'},
                   {'as_number': 'AS286',
                    'country': 'US',
                    'description': 'GTT Communications Inc.'},
                   {'as_number': 'AS3257',
                    'country': 'US',
                    'description': 'GTT Communications Inc.'},
                   {'as_number': 'AS3754',
                    'country': 'US',
                    'description': 'NYSERNet'},
                   {'as_number': 'AS3356',
                    'country': 'US',
                    'description': 'Level 3 Parent, LLC'},
                   {'as_number': 'AS6461',
                    'country': 'US',
                    'description': 'Zayo Bandwidth'},
                   {'as_number': 'AS137',
                    'country': 'IT',
                    'description': 'Consortium GARR'},
                   {'as_number': 'AS54965',
                    'country': 'US',
                    'description': 'Polytechnic Institute of NYU'}],
         'rir': 'ARIN',
         'routes': ['192.76.177.0/24',
                    '216.165.96.0/20',
                    '216.165.89.0/24',
                    '216.165.0.0/18',
                    '2607:f600::/32',
                    '216.165.112.0/21',
                    '128.122.0.0/16',
                    '216.165.102.0/24',
                    '216.165.64.0/19',
                    '216.165.120.0/22',
                    '192.86.139.0/24',
                    '216.165.103.0/24'],
         'type': 'EDUCATION',
         'upstreams': [{'as_number': 'AS3269',
                        'country': 'IT',
                        'description': 'Telecom Italia S.p.A.'},
                       {'as_number': 'AS8220',
                        'country': 'GB',
                        'description': 'COLT Technology Services Group '
                                       'Limited'},
                       {'as_number': 'AS286',
                        'country': 'US',
                        'description': 'GTT Communications Inc.'},
                       {'as_number': 'AS3257',
                        'country': 'US',
                        'description': 'GTT Communications Inc.'},
                       {'as_number': 'AS3754',
                        'country': 'US',
                        'description': 'NYSERNet'},
                       {'as_number': 'AS3356',
                        'country': 'US',
                        'description': 'Level 3 Parent, LLC'},
                       {'as_number': 'AS6461',
                        'country': 'US',
                        'description': 'Zayo Bandwidth'},
                       {'as_number': 'AS137',
                        'country': 'IT',
                        'description': 'Consortium GARR'}],
         'whois_response': '\n'
                           '#\n'
                           '# ARIN WHOIS data and services are subject to the '
                           'Terms of Use\n'
                           '# available at: '
                           'https://www.arin.net/resources/registry/whois/tou/\n'
                           '#\n'
                           '# If you see inaccuracies in the results, please '
                           'report at\n'
                           '# '
                           'https://www.arin.net/resources/registry/whois/inaccuracy_reporting/\n'
                           '#\n'
                           '# Copyright 1997-2025, American Registry for '
                           'Internet Numbers, Ltd.\n'
                           '#\n'
                           '\n'
                           '\n'
                           'ASNumber:       12\n'
                           'ASName:         NYU-DOMAIN\n'
                           'ASHandle:       AS12\n'
                           'RegDate:        1984-07-05\n'
                           'Updated:        2023-05-25    \n'
                           'Ref:            '
                           'https://rdap.arin.net/registry/autnum/12\n'
                           '\n'
                           '\n'
                           'OrgName:        New York University\n'
                           'OrgId:          NYU-Z\n'
                           'Address:        726 Broadway, 8th Floor - ITS\n'
                           'City:           New York\n'
                           'StateProv:      NY\n'
                           'PostalCode:     10003\n'
                           'Country:        US\n'
                           'RegDate:        2023-05-15\n'
                           'Updated:        2023-05-15\n'
                           'Ref:            '
                           'https://rdap.arin.net/registry/entity/NYU-Z\n'
                           '\n'
                           '\n'
                           'OrgTechHandle: COSI-ARIN\n'
                           'OrgTechName:   Communications Operations Services '
                           '- ITS\n'
                           'OrgTechPhone:  +1-212-998-3444 \n'
                           'OrgTechEmail:  noc-cosi-arin@nyu.edu\n'
                           'OrgTechRef:    '
                           'https://rdap.arin.net/registry/entity/COSI-ARIN\n'
                           '\n'
                           'OrgNOCHandle: COSI-ARIN\n'
                           'OrgNOCName:   Communications Operations Services - '
                           'ITS\n'
                           'OrgNOCPhone:  +1-212-998-3444 \n'
                           'OrgNOCEmail:  noc-cosi-arin@nyu.edu\n'
                           'OrgNOCRef:    '
                           'https://rdap.arin.net/registry/entity/COSI-ARIN\n'
                           '\n'
                           'OrgAbuseHandle: OIS9-ARIN\n'
                           'OrgAbuseName:   Office of Information Security\n'
                           'OrgAbusePhone:  +1-212-998-3333 \n'
                           'OrgAbuseEmail:  abuse@nyu.edu\n'
                           'OrgAbuseRef:    '
                           'https://rdap.arin.net/registry/entity/OIS9-ARIN\n'
                           '\n'
                           'RNOCHandle: COSI-ARIN\n'
                           'RNOCName:   Communications Operations Services - '
                           'ITS\n'
                           'RNOCPhone:  +1-212-998-3444 \n'
                           'RNOCEmail:  noc-cosi-arin@nyu.edu\n'
                           'RNOCRef:    '
                           'https://rdap.arin.net/registry/entity/COSI-ARIN\n'
                           '\n'
                           'RTechHandle: COSI-ARIN\n'
                           'RTechName:   Communications Operations Services - '
                           'ITS\n'
                           'RTechPhone:  +1-212-998-3444 \n'
                           'RTechEmail:  noc-cosi-arin@nyu.edu\n'
                           'RTechRef:    '
                           'https://rdap.arin.net/registry/entity/COSI-ARIN\n'
                           '\n'
                           '\n'
                           '#\n'
                           '# ARIN WHOIS data and services are subject to the '
                           'Terms of Use\n'
                           '# available at: '
                           'https://www.arin.net/resources/registry/whois/tou/\n'
                           '#\n'
                           '# If you see inaccuracies in the results, please '
                           'report at\n'
                           '# '
                           'https://www.arin.net/resources/registry/whois/inaccuracy_reporting/\n'
                           '#\n'
                           '# Copyright 1997-2025, American Registry for '
                           'Internet Numbers, Ltd.\n'
                           '#\n'}}
```
## Abuse Contact API Examples
This section demonstrates how to use the `get_abuse_contact_info()` method of the AbuseContact API. This API helps security teams, hosting providers, and compliance professionals quickly identify the correct abuse reporting contacts for any IPv4 or IPv6 address. You can retrieve data like the responsible organization, role, contact emails, phone numbers, and address to take appropriate mitigation action against abusive or malicious activity.
> **Note**: Abuse Contact API is only available in the Advanced Plan

Refer to the official [Abuse Contact API documentation](https://ipgeolocation.io/ip-abuse-contact-api.html#documentation-overview) for details on all available fields.
### Lookup Abuse Contact by IP
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AbuseContactApi(client)
    response = api_instance.get_abuse_contact_info(ip="1.0.1.0")
    pprint(response.to_dict())
```
Sample Response:
```text
{'abuse': {'address': 'No.31 ,jingrong street,beijing\n100032',
           'country': 'CN',
           'emails': ['anti-spam@chinatelecom.cn'],
           'handle': 'IRT-CHINANET-CN',
           'kind': 'group',
           'name': 'IRT-CHINANET-CN',
           'organization': '',
           'phone_numbers': ['+86-591-83371954', ' +86-591-83309761'],
           'role': 'abuse',
           'route': '1.0.1.0/24'},
 'ip': '1.0.1.0'}
```
### Lookup Abuse Contact with Specific Fields
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AbuseContactApi(client)
    response = api_instance.get_abuse_contact_info(ip="2.76.19.0", fields="abuse.role,abuse.emails")
    pprint(response.to_dict())
```
Sample Response:
```text
{'abuse': {'emails': ['abuse@kcell.kz'], 
            'role': 'abuse'}, 
'ip': '2.76.19.0'}
```
### Lookup Abuse Contact while Excluding Fields
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AbuseContactApi(client)
    response = api_instance.get_abuse_contact_info(ip="2.76.19.0", excludes="abuse.handle,abuse.emails")
    pprint(response.to_dict())
```
Sample Response:
```text
{'abuse': {'address': 'MEDEU DISTRICT, Alimzhanov street, house 51\n'
                      '050004\n'
                      'Almaty\n'
                      'KAZAKHSTAN',
           'country': 'KZ',
           'kind': 'group',
           'name': 'Abuse-C Role',
           'organization': '',
           'phone_numbers': ['+77272582755 ext. 1889'],
           'role': 'abuse',
           'route': '2.76.0.0/15'},
 'ip': '2.76.19.0'}
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
```text
{'ip': '8.8.8.8',
 'location': {'city': 'Mountain View',
              'continent_code': 'NA',
              'continent_name': 'North America',
              'country_code2': 'US',
              'country_code3': 'USA',
              'country_name': 'United States',
              'country_name_official': 'United States of America',
              'district': 'Santa Clara',
              'is_eu': False,
              'latitude': '37.42240',
              'longitude': '-122.08421',
              'state_code': 'US-CA',
              'state_prov': 'California',
              'zipcode': '94043-1351'},
 'time_zone': {'date': '2025-08-07',
               'date_time': '2025-08-07 21:39:59',
               'date_time_txt': 'Thursday, August 07, 2025 21:39:59',
               'date_time_unix': 1754627999.594,
               'date_time_wti': 'Thu, 07 Aug 2025 21:39:59 -0700',
               'date_time_ymd': '2025-08-07T21:39:59-0700',
               'dst_end': {'date_time_after': '2025-11-02 TIME 01',
                           'date_time_before': '2025-11-02 TIME 02',
                           'duration': '-1H',
                           'gap': False,
                           'overlap': True,
                           'utc_time': '2025-11-02 TIME 09'},
               'dst_exists': True,
               'dst_savings': 1,
               'dst_start': {'date_time_after': '2025-03-09 TIME 03',
                             'date_time_before': '2025-03-09 TIME 02',
                             'duration': '+1H',
                             'gap': True,
                             'overlap': False,
                             'utc_time': '2025-03-09 TIME 10'},
               'is_dst': True,
               'month': 8,
               'name': 'America/Los_Angeles',
               'offset': -8,
               'offset_with_dst': -7,
               'time_12': '09:39:59 PM',
               'time_24': '21:39:59',
               'week': 32,
               'year': 2025,
               'year_abbr': '25'}}
```
### Get Timezone by Timezone Name
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(tz="Europe/London")
    pprint(response.to_dict())
```
Sample Response:
```text
{'time_zone': {'date': '2025-08-08',
               'date_time': '2025-08-08 05:41:48',
               'date_time_txt': 'Friday, August 08, 2025 05:41:48',
               'date_time_unix': 1754628108.702,
               'date_time_wti': 'Fri, 08 Aug 2025 05:41:48 +0100',
               'date_time_ymd': '2025-08-08T05:41:48+0100',
               'dst_end': {'date_time_after': '2025-10-26 TIME 01',
                           'date_time_before': '2025-10-26 TIME 02',
                           'duration': '-1H',
                           'gap': False,
                           'overlap': True,
                           'utc_time': '2025-10-26 TIME 01'},
               'dst_exists': True,
               'dst_savings': 1,
               'dst_start': {'date_time_after': '2025-03-30 TIME 02',
                             'date_time_before': '2025-03-30 TIME 01',
                             'duration': '+1H',
                             'gap': True,
                             'overlap': False,
                             'utc_time': '2025-03-30 TIME 01'},
               'is_dst': True,
               'month': 8,
               'name': 'Europe/London',
               'offset': 0,
               'offset_with_dst': 1,
               'time_12': '05:41:48 AM',
               'time_24': '05:41:48',
               'week': 32,
               'year': 2025,
               'year_abbr': '25'}}
```
### Get Timezone from Any Address
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(location="Munich, Germany")
    pprint(response.to_dict())
```
Sample Response:
```text
{'location': {'city': 'Munich',
              'country_name': 'Germany',
              'latitude': '48.13711',
              'locality': '',
              'location_string': 'Munich, Germany',
              'longitude': '11.57538',
              'state_prov': 'Bavaria'},
 'time_zone': {'date': '2025-08-08',
               'date_time': '2025-08-08 06:42:54',
               'date_time_txt': 'Friday, August 08, 2025 06:42:54',
               'date_time_unix': 1754628174.007,
               'date_time_wti': 'Fri, 08 Aug 2025 06:42:54 +0200',
               'date_time_ymd': '2025-08-08T06:42:54+0200',
               'dst_end': {'date_time_after': '2025-10-26 TIME 02',
                           'date_time_before': '2025-10-26 TIME 03',
                           'duration': '-1H',
                           'gap': False,
                           'overlap': True,
                           'utc_time': '2025-10-26 TIME 01'},
               'dst_exists': True,
               'dst_savings': 1,
               'dst_start': {'date_time_after': '2025-03-30 TIME 03',
                             'date_time_before': '2025-03-30 TIME 02',
                             'duration': '+1H',
                             'gap': True,
                             'overlap': False,
                             'utc_time': '2025-03-30 TIME 01'},
               'is_dst': True,
               'month': 8,
               'name': 'Europe/Berlin',
               'offset': 1,
               'offset_with_dst': 2,
               'time_12': '06:42:54 AM',
               'time_24': '06:42:54',
               'week': 32,
               'year': 2025,
               'year_abbr': '25'}}
```
### Get Timezone from Location Coordinates
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(lat="48.8566", long="2.3522")
    pprint(response.to_dict())
```
Sample Response:
```text
{'time_zone': {'date': '2025-08-08',
               'date_time': '2025-08-08 06:44:31',
               'date_time_txt': 'Friday, August 08, 2025 06:44:31',
               'date_time_unix': 1754628271.639,
               'date_time_wti': 'Fri, 08 Aug 2025 06:44:31 +0200',
               'date_time_ymd': '2025-08-08T06:44:31+0200',
               'dst_end': {'date_time_after': '2025-10-26 TIME 02',
                           'date_time_before': '2025-10-26 TIME 03',
                           'duration': '-1H',
                           'gap': False,
                           'overlap': True,
                           'utc_time': '2025-10-26 TIME 01'},
               'dst_exists': True,
               'dst_savings': 1,
               'dst_start': {'date_time_after': '2025-03-30 TIME 03',
                             'date_time_before': '2025-03-30 TIME 02',
                             'duration': '+1H',
                             'gap': True,
                             'overlap': False,
                             'utc_time': '2025-03-30 TIME 01'},
               'is_dst': True,
               'month': 8,
               'name': 'Europe/Paris',
               'offset': 1,
               'offset_with_dst': 2,
               'time_12': '06:44:31 AM',
               'time_24': '06:44:31',
               'week': 32,
               'year': 2025,
               'year_abbr': '25'}}
```
### Get Timezone and Airport Details from IATA Code
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.TimezoneApi(client)
    response = api_instance.get_timezone_info(iata_code="ZRH")
    pprint(response.to_dict())
```
Sample Response:
```text
{'airport_details': {'city': 'Zurich',
                     'continent_code': 'EU',
                     'country_code': 'CH',
                     'elevation_ft': 1417,
                     'faa_code': '',
                     'iata_code': 'ZRH',
                     'icao_code': 'LSZH',
                     'latitude': '47.45806',
                     'longitude': '8.54806',
                     'name': 'Zurich Airport',
                     'state_code': 'CH-ZH',
                     'type': 'large_airport'},
 'time_zone': {'date': '2025-08-08',
               'date_time': '2025-08-08 06:46:22',
               'date_time_txt': 'Friday, August 08, 2025 06:46:22',
               'date_time_unix': 1754628382.876,
               'date_time_wti': 'Fri, 08 Aug 2025 06:46:22 +0200',
               'date_time_ymd': '2025-08-08T06:46:22+0200',
               'dst_end': {'date_time_after': '2025-10-26 TIME 02',
                           'date_time_before': '2025-10-26 TIME 03',
                           'duration': '-1H',
                           'gap': False,
                           'overlap': True,
                           'utc_time': '2025-10-26 TIME 01'},
               'dst_exists': True,
               'dst_savings': 1,
               'dst_start': {'date_time_after': '2025-03-30 TIME 03',
                             'date_time_before': '2025-03-30 TIME 02',
                             'duration': '+1H',
                             'gap': True,
                             'overlap': False,
                             'utc_time': '2025-03-30 TIME 01'},
               'is_dst': True,
               'month': 8,
               'name': 'Europe/Zurich',
               'offset': 1,
               'offset_with_dst': 2,
               'time_12': '06:46:22 AM',
               'time_24': '06:46:22',
               'week': 32,
               'year': 2025,
               'year_abbr': '25'}}
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
```text
{'lo_code_details': {'city': 'Barcelona',
                     'country_code': 'ES',
                     'country_name': '',
                     'latitude': '41.38289',
                     'lo_code': 'ESBCN',
                     'location_type': 'Port, Rail Terminal, Road Terminal, '
                                      'Airport, Postal Exchange',
                     'longitude': '2.17743',
                     'state_code': ''},
 'time_zone': {'date': '2025-08-08',
               'date_time': '2025-08-08 06:48:13',
               'date_time_txt': 'Friday, August 08, 2025 06:48:13',
               'date_time_unix': 1754628493.203,
               'date_time_wti': 'Fri, 08 Aug 2025 06:48:13 +0200',
               'date_time_ymd': '2025-08-08T06:48:13+0200',
               'dst_end': {'date_time_after': '2025-10-26 TIME 02',
                           'date_time_before': '2025-10-26 TIME 03',
                           'duration': '-1H',
                           'gap': False,
                           'overlap': True,
                           'utc_time': '2025-10-26 TIME 01'},
               'dst_exists': True,
               'dst_savings': 1,
               'dst_start': {'date_time_after': '2025-03-30 TIME 03',
                             'date_time_before': '2025-03-30 TIME 02',
                             'duration': '+1H',
                             'gap': True,
                             'overlap': False,
                             'utc_time': '2025-03-30 TIME 01'},
               'is_dst': True,
               'month': 8,
               'name': 'Europe/Madrid',
               'offset': 1,
               'offset_with_dst': 2,
               'time_12': '06:48:13 AM',
               'time_24': '06:48:13',
               'week': 32,
               'year': 2025,
               'year_abbr': '25'}}
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
```text
{'converted_time': '2025-08-08 13:50:44',
 'diff_hour': 13,
 'diff_min': 780,
 'original_time': '2025-08-08 00:50:44'}
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
```text
{'device': {'brand': 'Unknown',
            'cpu': 'Intel x86_64',
            'name': 'Desktop',
            'type': 'Desktop'},
 'engine': {'name': 'Blink',
            'type': 'Browser',
            'version': '125',
            'version_major': '125'},
 'name': 'Chrome',
 'operating_system': {'build': '??',
                      'name': 'Windows NT',
                      'type': 'Desktop',
                      'version': '??',
                      'version_major': '??'},
 'type': 'Browser',
 'user_agent_string': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) '
                      'AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 '
                      'Safari/537.36',
 'version': '125',
 'version_major': '125'}
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

### Astronomy by Coordinates
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(lat="40.7128", long="-74.0060")
    pprint(response.to_dict())
```
Sample Response:
```text
{'astronomy': {'current_time': '01:24:34.206',
               'date': '2025-08-08',
               'day_length': '14:03',
               'evening': {'astronomical_twilight_begin': '21:09',
                           'astronomical_twilight_end': '21:49',
                           'blue_hour_begin': '20:21',
                           'blue_hour_end': '20:44',
                           'civil_twilight_begin': '20:03',
                           'civil_twilight_end': '20:32',
                           'golden_hour_begin': '19:24',
                           'golden_hour_end': '20:21',
                           'nautical_twilight_begin': '20:32',
                           'nautical_twilight_end': '21:09'},
               'mid_night': '01:01',
               'moon_altitude': 23.669055866442545,
               'moon_angle': 166.27229987123508,
               'moon_azimuth': 198.75293380735044,
               'moon_distance': 384876.99936538114,
               'moon_illumination_percentage': '98.57',
               'moon_parallactic_angle': 15.390260494111123,
               'moon_phase': 'FULL_MOON',
               'moon_status': '-',
               'moonrise': '20:01',
               'moonset': '04:52',
               'morning': {'astronomical_twilight_begin': '04:13',
                           'astronomical_twilight_end': '04:53',
                           'blue_hour_begin': '05:17',
                           'blue_hour_end': '05:41',
                           'civil_twilight_begin': '05:29',
                           'civil_twilight_end': '05:59',
                           'golden_hour_begin': '05:41',
                           'golden_hour_end': '06:38',
                           'nautical_twilight_begin': '04:53',
                           'nautical_twilight_end': '05:29'},
               'night_begin': '21:49',
               'night_end': '04:13',
               'solar_noon': '13:01',
               'sun_altitude': -32.984922198146315,
               'sun_azimuth': 6.547113802544914,
               'sun_distance': 151721123.19916567,
               'sun_status': '-',
               'sunrise': '05:59',
               'sunset': '20:03'},
 'location': {'city': 'New York',
              'country_name': '',
              'elevation': '6',
              'latitude': '40.71280',
              'locality': '',
              'longitude': '-74.00600',
              'state_prov': 'New York'}}
```
### Astronomy by IP Address
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(ip="8.8.8.8")
    pprint(response.to_dict())
```
Sample Response:
```text
{'astronomy': {'current_time': '22:26:45.166',
               'date': '2025-08-07',
               'day_length': '13:51',
               'evening': {'astronomical_twilight_begin': '21:12',
                           'astronomical_twilight_end': '21:48',
                           'blue_hour_begin': '20:26',
                           'blue_hour_end': '20:49',
                           'civil_twilight_begin': '20:09',
                           'civil_twilight_end': '20:37',
                           'golden_hour_begin': '19:33',
                           'golden_hour_end': '20:26',
                           'nautical_twilight_begin': '20:37',
                           'nautical_twilight_end': '21:12'},
               'mid_night': '01:14',
               'moon_altitude': 23.499956846028425,
               'moon_angle': 166.29082916314508,
               'moon_azimuth': 151.12598145672808,
               'moon_distance': 384870.3937982859,
               'moon_illumination_percentage': '98.58',
               'moon_parallactic_angle': -24.685745972238635,
               'moon_phase': 'FULL_MOON',
               'moon_status': '-',
               'moonrise': '19:35',
               'moonset': '04:15',
               'morning': {'astronomical_twilight_begin': '04:38',
                           'astronomical_twilight_end': '05:15',
                           'blue_hour_begin': '05:38',
                           'blue_hour_end': '06:00',
                           'civil_twilight_begin': '05:49',
                           'civil_twilight_end': '06:17',
                           'golden_hour_begin': '06:00',
                           'golden_hour_end': '06:54',
                           'nautical_twilight_begin': '05:15',
                           'nautical_twilight_end': '05:49'},
               'night_begin': '21:48',
               'night_end': '04:38',
               'solar_noon': '13:14',
               'sun_altitude': -23.622520216576035,
               'sun_azimuth': 315.6208700434932,
               'sun_distance': 151743546.31162292,
               'sun_status': '-',
               'sunrise': '06:17',
               'sunset': '20:09'},
 'ip': '8.8.8.8',
 'location': {'city': 'Mountain View',
              'continent_code': 'NA',
              'continent_name': 'North America',
              'country_code2': 'US',
              'country_code3': 'USA',
              'country_name': 'United States',
              'country_name_official': 'United States of America',
              'district': 'Santa Clara',
              'elevation': '3',
              'is_eu': False,
              'latitude': '37.42240',
              'locality': 'Charleston Terrace',
              'longitude': '-122.08421',
              'state_code': 'US-CA',
              'state_prov': 'California',
              'zipcode': '94043-1351'}}
```
### Astronomy by Location String
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(location="Milan, Italy")
    pprint(response.to_dict())
```
Sample Response:
```text
{'astronomy': {'current_time': '07:27:27.944',
               'date': '2025-08-08',
               'day_length': '14:30',
               'evening': {'astronomical_twilight_begin': '21:55',
                           'astronomical_twilight_end': '22:42',
                           'blue_hour_begin': '21:01',
                           'blue_hour_end': '21:27',
                           'civil_twilight_begin': '20:43',
                           'civil_twilight_end': '21:14',
                           'golden_hour_begin': '19:59',
                           'golden_hour_end': '21:01',
                           'nautical_twilight_begin': '21:14',
                           'nautical_twilight_end': '21:55'},
               'mid_night': '01:29',
               'moon_altitude': -25.010715698704324,
               'moon_angle': 166.29688189098198,
               'moon_azimuth': 261.4389380532827,
               'moon_distance': 384868.236228891,
               'moon_illumination_percentage': '98.58',
               'moon_parallactic_angle': 49.04972415962652,
               'moon_phase': 'FULL_MOON',
               'moon_status': '-',
               'moonrise': '20:35',
               'moonset': '04:46',
               'morning': {'astronomical_twilight_begin': '04:14',
                           'astronomical_twilight_end': '05:01',
                           'blue_hour_begin': '05:29',
                           'blue_hour_end': '05:55',
                           'civil_twilight_begin': '05:42',
                           'civil_twilight_end': '06:13',
                           'golden_hour_begin': '05:55',
                           'golden_hour_end': '06:57',
                           'nautical_twilight_begin': '05:01',
                           'nautical_twilight_end': '05:42'},
               'night_begin': '22:42',
               'night_end': '04:14',
               'solar_noon': '13:28',
               'sun_altitude': 11.11568551252996,
               'sun_azimuth': 78.33676356672913,
               'sun_distance': 151721123.1991657,
               'sun_status': '-',
               'sunrise': '06:13',
               'sunset': '20:43'},
 'location': {'city': 'Milan',
              'country_name': 'Italy',
              'elevation': '122',
              'latitude': '45.46419',
              'locality': '',
              'location_string': 'Milan, Italy',
              'longitude': '9.18963',
              'state_prov': 'Lombardy'}}
```
### Astronomy for Specific Date
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(lat="-27.47", long="153.02", var_date="2025-01-01")
    pprint(response.to_dict())
```
Sample Response:
```text
{'astronomy': {'current_time': '15:37:36.338',
               'date': '2025-01-01',
               'day_length': '13:50',
               'evening': {'astronomical_twilight_begin': '19:45',
                           'astronomical_twilight_end': '20:18',
                           'blue_hour_begin': '19:02',
                           'blue_hour_end': '19:23',
                           'civil_twilight_begin': '18:46',
                           'civil_twilight_end': '19:13',
                           'golden_hour_begin': '18:12',
                           'golden_hour_end': '19:02',
                           'nautical_twilight_begin': '19:13',
                           'nautical_twilight_end': '19:45'},
               'mid_night': '23:51',
               'moon_altitude': 55.581857131320504,
               'moon_angle': 16.006816957603085,
               'moon_azimuth': 264.9032851876516,
               'moon_distance': 381160.8743283583,
               'moon_illumination_percentage': '1.94',
               'moon_parallactic_angle': 102.49215878888498,
               'moon_phase': 'NEW_MOON',
               'moon_status': '-',
               'moonrise': '05:42',
               'moonset': '20:08',
               'morning': {'astronomical_twilight_begin': '03:24',
                           'astronomical_twilight_end': '03:57',
                           'blue_hour_begin': '04:19',
                           'blue_hour_end': '04:40',
                           'civil_twilight_begin': '04:29',
                           'civil_twilight_end': '04:56',
                           'golden_hour_begin': '04:40',
                           'golden_hour_end': '05:30',
                           'nautical_twilight_begin': '03:57',
                           'nautical_twilight_end': '04:29'},
               'night_begin': '20:18',
               'night_end': '03:24',
               'solar_noon': '11:51',
               'sun_altitude': 39.09727912525482,
               'sun_azimuth': 261.6973481428636,
               'sun_distance': 147102938.88036567,
               'sun_status': '-',
               'sunrise': '04:56',
               'sunset': '18:46'},
 'location': {'city': 'Brisbane',
              'country_name': 'Australia',
              'elevation': '',
              'latitude': '-27.47000',
              'locality': 'Brisbane',
              'longitude': '153.02000',
              'state_prov': 'Queensland'}}
```
### Astronomy in Different Language
You can also get Astronomy Data in other languages as well. Only paid subscriptions can access this feature.
```python
with ipgeolocation.ApiClient(configuration) as client:
    api_instance = ipgeolocation.AstronomyApi(client)
    response = api_instance.get_astronomy_details(ip="1.1.1.1", lang="fr")
    pprint(response.to_dict())
```
Sample Response:
```text
{'astronomy': {'current_time': '15:39:12.077',
               'date': '2025-08-08',
               'day_length': '10:58',
               'evening': {'astronomical_twilight_begin': '18:15',
                           'astronomical_twilight_end': '18:42',
                           'blue_hour_begin': '17:38',
                           'blue_hour_end': '17:56',
                           'civil_twilight_begin': '17:23',
                           'civil_twilight_end': '17:47',
                           'golden_hour_begin': '16:50',
                           'golden_hour_end': '17:38',
                           'nautical_twilight_begin': '17:47',
                           'nautical_twilight_end': '18:15'},
               'mid_night': '23:53',
               'moon_altitude': -6.093842643644992,
               'moon_angle': 166.3965211706784,
               'moon_azimuth': 120.25140833908989,
               'moon_distance': 384832.731852605,
               'moon_illumination_percentage': '98.60',
               'moon_parallactic_angle': -123.44281070347506,
               'moon_phase': 'FULL_MOON',
               'moon_status': '-',
               'moonrise': '16:12',
               'moonset': '05:35',
               'morning': {'astronomical_twilight_begin': '05:04',
                           'astronomical_twilight_end': '05:32',
                           'blue_hour_begin': '05:50',
                           'blue_hour_end': '06:09',
                           'civil_twilight_begin': '06:00',
                           'civil_twilight_end': '06:24',
                           'golden_hour_begin': '06:09',
                           'golden_hour_end': '06:57',
                           'nautical_twilight_begin': '05:32',
                           'nautical_twilight_end': '06:00'},
               'night_begin': '18:42',
               'night_end': '05:04',
               'solar_noon': '11:53',
               'sun_altitude': 20.145285015118457,
               'sun_azimuth': 301.51439150528006,
               'sun_distance': 151721123.1991657,
               'sun_status': '-',
               'sunrise': '06:24',
               'sunset': '17:23'},
 'ip': '1.1.1.1',
 'location': {'city': 'Brisbane Sud',
              'continent_code': 'OC',
              'continent_name': 'Océanie',
              'country_code2': 'AU',
              'country_code3': 'AUS',
              'country_name': 'Australie',
              'country_name_official': '',
              'district': 'Brisbane',
              'elevation': '',
              'is_eu': False,
              'latitude': '-27.47306',
              'locality': '',
              'longitude': '153.01421',
              'state_code': 'AU-QLD',
              'state_prov': 'Queensland',
              'zipcode': '4101'}}
```


## Documentation For Models

 - [ASNConnection](docs/ASNConnection.md)
 - [ASNResponse](docs/ASNResponse.md)
 - [ASNDetails](docs/ASNDetails.md)
 - [Abuse](docs/Abuse.md)
 - [AbuseResponse](docs/AbuseResponse.md)
 - [Astronomy](docs/Astronomy.md)
 - [AstronomyEvening](docs/AstronomyEvening.md)
 - [AstronomyLocation](docs/AstronomyLocation.md)
 - [AstronomyMorning](docs/AstronomyMorning.md)
 - [AstronomyResponse](docs/AstronomyResponse.md)
 - [CountryMetadata](docs/CountryMetadata.md)
 - [Currency](docs/Currency.md)
 - [ErrorResponse](docs/ErrorResponse.md)
 - [GeolocationResponse](docs/GeolocationResponse.md)
 - [GetBulkIpGeolocationResponse](docs/GetBulkIpGeolocationResponse.md)
 - [GetBulkIpGeolocationRequest](docs/GetBulkIpGeolocationRequest.md)
 - [GetBulkIpSecurityInfoResponse](docs/GetBulkIpSecurityInfoResponse.md)
 - [Location](docs/Location.md)
 - [LocationMinimal](docs/LocationMinimal.md)
 - [Network](docs/Network.md)
 - [NetworkAsn](docs/NetworkAsn.md)
 - [NetworkCompany](docs/NetworkCompany.md)
 - [NetworkMinimal](docs/NetworkMinimal.md)
 - [NetworkMinimalAsn](docs/NetworkMinimalAsn.md)
 - [NetworkMinimalCompany](docs/NetworkMinimalCompany.md)
 - [ParseBulkUserAgentStringsRequest](docs/ParseBulkUserAgentStringsRequest.md)
 - [ParseUserAgentStringRequest](docs/ParseUserAgentStringRequest.md)
 - [Security](docs/Security.md)
 - [IPSecurityAPIResponse](docs/IPSecurityAPIResponse.md)
 - [TimeConversionResponse](docs/TimeConversionResponse.md)
 - [TimeSeries](docs/TimeSeries.md)
 - [TimeZone](docs/TimeZone.md)
 - [TimeZoneDetailedResponse](docs/TimeZoneDetailedResponse.md)
 - [TimeZoneDstEnd](docs/TimeZoneDstEnd.md)
 - [TimeZoneDstStart](docs/TimeZoneDstStart.md)
 - [TimezoneAirport](docs/TimezoneAirport.md)
 - [TimezoneDetail](docs/TimezoneDetail.md)
 - [TimezoneDetailDstEnd](docs/TimezoneDetailDstEnd.md)
 - [TimezoneDetailDstStart](docs/TimezoneDetailDstStart.md)
 - [TimezoneLocation](docs/TimezoneLocation.md)
 - [TimezoneLocode](docs/TimezoneLocode.md)
 - [UserAgentData](docs/UserAgentData.md)
 - [UserAgentDataDevice](docs/UserAgentDataDevice.md)
 - [UserAgentDataEngine](docs/UserAgentDataEngine.md)
 - [UserAgentDataOperatingSystem](docs/UserAgentDataOperatingSystem.md)


