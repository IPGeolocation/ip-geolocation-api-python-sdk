# ipgeolocation.TimeConversionApi

All URIs are relative to *https://api.ipgeolocation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**convert_time_between_timezones**](TimeConversionApi.md#convert_time_between_timezones) | **GET** /timezone/convert | 


# **convert_time_between_timezones**
> TimeConversionResponse convert_time_between_timezones(time=time, tz_from=tz_from, tz_to=tz_to, lat_from=lat_from, long_from=long_from, lat_to=lat_to, long_to=long_to, location_from=location_from, location_to=location_to, icao_from=icao_from, icao_to=icao_to, iata_from=iata_from, iata_to=iata_to, locode_from=locode_from, locode_to=locode_to)

You can convert a timestamp provided as a query paramter time from one time zone to another time zone.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipgeolocation
from ipgeolocation.models.time_conversion_response import TimeConversionResponse
from ipgeolocation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ipgeolocation.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ipgeolocation.Configuration(
    host = "https://api.ipgeolocation.io/v2"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: ApiKeyAuth
configuration.api_key['ApiKeyAuth'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['ApiKeyAuth'] = 'Bearer'

# Enter a context with an instance of the API client
with ipgeolocation.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = ipgeolocation.TimeConversionApi(api_client)
    time = '2025-02-28 9:00:00' # str | time parameter takes the input in the following two formats: i) 'yyyy-MM-dd HH:mm', and ii) 'yyyy-MM-dd HH:mm:ss'. This parameter is optional and you can omit it to convert the current time between two coordinates, time zones or locations. (optional)
    tz_from = 'America/Argentina/Catamarca' # str | timezone to convert from (optional)
    tz_to = 'Asia/Kabul' # str | timezone to convert to (optional)
    lat_from = 34.0207305 # float | latitude to convert from (optional)
    long_from = -118.691916 # float | longitude to convert from (optional)
    lat_to = 53.473682 # float | latitude to convert to (optional)
    long_to = -77.397706 # float | longitude to convert to (optional)
    location_from = 'New York, USA' # str | location to convert from (optional)
    location_to = 'Lahore, Pakistan' # str | location to convert to (optional)
    icao_from = 'YSSY' # str | location to convert from (optional)
    icao_to = 'ZBAA' # str | location to convert to (optional)
    iata_from = 'DXB' # str | location to convert from (optional)
    iata_to = 'LHR' # str | location to convert to (optional)
    locode_from = 'PKISB' # str | location to convert from (optional)
    locode_to = 'USNYC' # str | location to convert to (optional)

    try:
        api_response = api_instance.convert_time_between_timezones(time=time, tz_from=tz_from, tz_to=tz_to, lat_from=lat_from, long_from=long_from, lat_to=lat_to, long_to=long_to, location_from=location_from, location_to=location_to, icao_from=icao_from, icao_to=icao_to, iata_from=iata_from, iata_to=iata_to, locode_from=locode_from, locode_to=locode_to)
        print("The response of TimeConversionApi->convert_time_between_timezones:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TimeConversionApi->convert_time_between_timezones: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **time** | **str**| time parameter takes the input in the following two formats: i) &#39;yyyy-MM-dd HH:mm&#39;, and ii) &#39;yyyy-MM-dd HH:mm:ss&#39;. This parameter is optional and you can omit it to convert the current time between two coordinates, time zones or locations. | [optional] 
 **tz_from** | **str**| timezone to convert from | [optional] 
 **tz_to** | **str**| timezone to convert to | [optional] 
 **lat_from** | **float**| latitude to convert from | [optional] 
 **long_from** | **float**| longitude to convert from | [optional] 
 **lat_to** | **float**| latitude to convert to | [optional] 
 **long_to** | **float**| longitude to convert to | [optional] 
 **location_from** | **str**| location to convert from | [optional] 
 **location_to** | **str**| location to convert to | [optional] 
 **icao_from** | **str**| location to convert from | [optional] 
 **icao_to** | **str**| location to convert to | [optional] 
 **iata_from** | **str**| location to convert from | [optional] 
 **iata_to** | **str**| location to convert to | [optional] 
 **locode_from** | **str**| location to convert from | [optional] 
 **locode_to** | **str**| location to convert to | [optional] 

### Return type

[**TimeConversionResponse**](TimeConversionResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request – Possible reasons include:   - If one of the query paramters tz_from and tz_to is provided and other is missing, for time conversion.    - If one of the query paramters location_from and location_to is provided and other is missing, for time conversion.      - If one of the query paramters lat_from, long_from, lat_to, and long_to is provided and other(s) is/are missing, for time conversion.      - If the location address provided to one of the paramters location_from and location_to is invalid, for time conversion. City or state level address must be provided.      - If the geographic coordinates provided to one of the paramters lat_from, long_from, lat_to, and long_to is/are not numbers, or the values fall outside the acceptable latitude and longitude ranges. The valid range for latitude is between -90 and 90, and for longitude, it is between -180 and 180.      - If the time zone names provided to one of the paramters tz_from and tz_to is/are wrong or not registered in the IANA time zone database.      - If none of the query parameter combination is provided for time conversion. tz_from and tz_to or location_from and location_to or lat_from, long_from, lat_to, long_to combination must be provided.  |  -  |
**401** | Unauthorized – Possible reasons include:   - Missing or invalid API key   - Account unverified, locked, or disabled   - Accessing API with an unauthorized key   - Subscription expired or downgraded   - If your account has been disabled or locked to use by the admin due to abuse or illegal activity.   - When the request to IP Geolocation API is made using API key for a database subscription   - When the request to IP Geolocation API is made on the &#39;paused&#39; subscription.   - If you’re making API requests after your subscription trial has been expired.   - If your active until date has passed and you need to upgrade your account.  |  -  |
**404** | Not Found – Possible reasons include:   - If the IPv4, IPv6, or domain name does not not exists in our database.    - If the IPv4, IPv6, or domain name is passed as a path variable, instead of url parameter as ip&#x3D;.      - If the location address provided to the request paramters location is invalid. City or state level address must be provided.      - If the provided ICAO code to the request paramter icao_code is not in the format as four letter code AAAA.      - If the provided UN/LOCODE, IATA code or ICAO code to the query paramters lo_code, iata_code, or icao_code does not exists in our database.      - If the wrong endpoint is called, that does not exists in our API.  |  -  |
**405** | Method Not Allowed – Only GET is allowed for &#x60;/timezone/convert&#x60; endpoint |  -  |
**429** | Too Many Requests – Possible reasons include:   - If the API usage limit has reached for the free subscriptions, or paid subscriptions with the status &#39;past due&#39;, &#39;deleted&#39; or &#39;trial expired&#39;.    - If the surcharge API usage limit has reached against the subscribed plan.     |  -  |
**499** | Client Closed Request – Client terminated connection before completion |  -  |
**500** | Internal Server Error – Something went wrong on our end |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

