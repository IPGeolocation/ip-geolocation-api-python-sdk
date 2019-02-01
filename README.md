# IP Geolocation API Python SDK

## Introduction

[IPGeolocation API](https://ipgeolocation.io) is the solution to identify country code (ISO2 and ISO3 standard), country name, continent code, continent name, country capital, state/province, district, city, zip code, latitude and longitude of city, is country belongs to Europian Union, calling code, top level domain (TLD), languages, country flag, internet service provider (ISP), connection type, organization, geoname ID, currency code, currency name, time zone ID, time zone offset, current time in the time zone, is time zone in daylight saving time, and total daylight savings. This document provides important information to help you get up to speed with IPGeolocation API using IP Geolocation API Typescript SDK.

Developers can use this Typescript SDK for software and web projects related to, but not limited to:

1. Display native language and currency
2. Redirect based on the country
3. Digital rights management
4. Web log stats and analysis
5. Auto-selection of country, state/province and city on forms
6. Filter access from countries you do not do business with
7. Geo-targeting for increased sales and click-through

## Quick Start Guide

You need a valid 'IPGeolocation API key' to use this SDK. [Sign up](https://ipgeolocation.io/signup) here and get your free API key if you don't have one.

## System Requirements

Internet connection is required to run this component. This SDK uses ```requests``` module that you need to install before it. Here is the command to install ```requests``` module:

```bash
pip install requests --upgrade --user
```

## Basic Usage

### Setup API

```python
from IPGeolocation import IPGeolocationAPI

# Create IPGeolocationAPI object. Constructor takes one parameter.
# 1) API key ()
ipgeolocationAPI = IPGeolocationAPI("YOUR_API_KEY")
```

### Geolocation Lookup

```python
from IPGeolocation import GeolocationParams

# Get complete geolocation for the calling machine's IP address
geolocation = ipgeolocationApi.getGeolocation()
print(geolocation)

# Get complete geolocation in Russian** for IP address (1.1.1.1)
geolocationParams = GeolocationParams()
geolocationParams.setIPAddress("1.1.1.1")
geolocationParams.setLang("ru")

# getGeolocation method returns valid JSON that contains IPGeolocation API response
geolocation = ipgeolocationAPI.getGeolocation(geolocationParams)

# Get custom geolocation (only "geo, time_zone and currency" fields/objects) for an IP address (1.1.1.1)
geolocationParams = GeolocationParams()
geolocationParams.setIPAddress("1.1.1.1")
geolocationParams.setFields("geo,time_zone,currency")

geolocation = ipgeolocationAPI.getGeolocation(geolocationParams)

# Exclude fields/obejects from complete geolocation in Italian language
geolocationParams = GeolocationParams()
geolocationParams.setExcludes("continent_name,country_code3,time_zone")
geolocationParams.setLang("it")

geolocation = ipgeolocationAPI.getGeolocation(geolocationParams)
```

### Bulk Geolocations Lookup

```python
# Query geolocation in German** for multiple IP addresses and all fields
geolocationParams = GeolocationParams()
geolocationParams.setLang("de")
geolocationParams.setIPAddresses(["1.1.1.1", "2.2.2.2", "3.3.3.3"])

geolocations = ipgeolocationAPI.getGeolocation(geolocationParams)
print(geolocations)

# Specify the required fields/objects for multiple IP addresses
geolocationParams = GeolocationParams()
geolocationParams.setIPAddresses(["1.1.1.1", "2.2.2.2", "3.3.3.3"])
geolocationParams.setFields("geo")

geolocations = ipgeolocationAPI.getGeolocation(geolocationParams)
```

### Timezone API

```python
from IPGeolocation import TimezoneParams

# Get time zone information by time zone ID
timezoneParams = TimezoneParams()
timezoneParams.setTimezone("America/Los_Angeles")

timezone = ipgeolocationAPI.getTimezone(timezoneParams)
print(timezone)

# Get time zone information by latitude and longitude of the location
timezoneParams = TimezoneParams()
timezoneParams.setCoordinates(37.1838139, -123.8105225)

timezone = ipgeolocationAPI.getTimezone(timezoneParams)

# Get time zone information for IP address (1.1.1.1) and geolocation information Japanese**
timezoneParams = TimezoneParams()
timezoneParams.setIPAddress("1.1.1.1")

timezone = ipgeolocationAPI.getTimezone(timezoneParams)

# Query time zone information for calling machine's IP address
timezone = ipgeolocationAPI.getTimezone()
```

** IPGeolocation provides geolocation information in the following languages:

* English (en)
* German (de)
* Russian (ru)
* Japanese (ja)
* French (fr)
* Chinese Simplified (cn)
* Spanish (es)
* Czech (cs)
* Italian (it)

By default, geolocation information is returned in English. Response in a language other than English is available to paid users only.