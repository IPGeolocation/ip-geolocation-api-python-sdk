# ipgeolocation.AstronomyApi

All URIs are relative to *https://api.ipgeolocation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_astronomy_details**](AstronomyApi.md#get_astronomy_details) | **GET** /astronomy | 
[**get_time_series_lookup**](AstronomyApi.md#get_time_series_lookup) | **GET** /astronomy/timeSeries |


# **get_astronomy_details**
> AstronomyResponse get_astronomy_details(ip=ip, location=location, lat=lat, long=long, time_zone=time_zone, var_date=var_date, elevation=elevation, output=output, lang=lang)

The Astronomy API provides the location-based rise and set times for the Sun and Moon along with the current position, distance from earth, and azimuth of the Sun and the Moon for a specific date at the queried time.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipgeolocation
from ipgeolocation.models.astronomy_response import AstronomyResponse
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
    api_instance = ipgeolocation.AstronomyApi(api_client)
    ip = '8.8.8.8' # str | query paramter 'ip'. If not provided, will be your network IP (optional)
    location = 'New York, US' # str | query paramter 'location'. If not provided, will be your ip location (optional)
    lat = '40.76473' # str | query paramter 'lat'. (optional)
    long = '-74.00084' # str | query paramter 'long'. (optional)
    time_zone = 'Europe/London' # str |  (optional)
    var_date = '2025-04-22' # str | The date (YYYY-MM-DD) to lookup for. default will be the current date (optional)
    elevation = 9 # float | query parameter 'elevation' (optional)
    output = 'json' # str | Desired output format. (optional)
    lang = 'en' # str | By default, the API responds in English. You can change the response language by passing the language code as a query parameter `lang`. Multi language feature is available only for `paid users`. (optional)

    try:
        api_response = api_instance.get_astronomy_details(ip=ip, location=location, lat=lat, long=long, time_zone=time_zone, var_date=var_date, elevation=elevation, output=output, lang=lang)
        print("The response of AstronomyApi->get_astronomy_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AstronomyApi->get_astronomy_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| query paramter &#39;ip&#39;. If not provided, will be your network IP | [optional] 
 **location** | **str**| query paramter &#39;location&#39;. If not provided, will be your ip location | [optional] 
 **lat** | **str**| query paramter &#39;lat&#39;. | [optional] 
 **long** | **str**| query paramter &#39;long&#39;. | [optional] 
 **time_zone** | **str**|  | [optional] 
 **date** | **str**| The date (YYYY-MM-DD) to lookup for. default will be the current date | [optional] 
 **elevation** | **float**| query parameter &#39;elevation&#39; | [optional] 
 **output** | **str**| Desired output format. | [optional] 
 **lang** | **str**| By default, the API responds in English. You can change the response language by passing the language code as a query parameter &#x60;lang&#x60;. Multi language feature is available only for &#x60;paid users&#x60;. | [optional] 

### Return type

[**AstronomyResponse**](AstronomyResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request – Possible reasons include:   - Invalid or not found location/address   - Special characters in API key or value   - Invalid date format (expected: yyyy-MM-dd)   - IP not found in the database  |  -  |
**401** | Unauthorized – Possible reasons include:   - Missing or invalid API key   - Account unverified, locked, or disabled   - Accessing API with an unauthorized key   - Subscription expired or downgraded  |  -  |
**405** | Method Not Allowed – Only GET is allowed for &#x60;/astronomy&#x60; endpoint |  -  |
**429** | Too Many Requests – API usage limits exceeded for current plan |  -  |
**499** | Client Closed Request – Client terminated connection before completion |  -  |
**500** | Internal Server Error – Something went wrong on our end |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_time_series_lookup**
> TimeSeriesResponse get_time_series_lookup(date_start, date_end, ip=ip, location=location, lat=lat, long=long, output=output, lang=lang)

You can look up astronomy details for any location by providing a starting and
ending date for the time series. The API allows a maximum 90-day lookup period, whether for future or past dates.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipgeolocation
from ipgeolocation.models.time_series_response import TimeSeriesResponse
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
    api_instance = ipgeolocation.AstronomyApi(api_client)
    date_start = '2025-06-23' # str | To lookup astronomy details from this date in YYYY-MM-DD format
    date_end = '2025-06-24' # str | To lookup astronomy details from start date to this end date. (YYYY-MM-DD)
    ip = '8.8.8.8' # str | query parameter 'ip'. (optional)
    location = 'New York, US' # str | query paramter 'location'. If not provided, will be your ip location (optional)
    lat = '40.76473' # str | query paramter 'lat'. (optional)
    long = '-74.00084' # str | query paramter 'long'. (optional)
    output = 'json' # str | Desired output format. (optional)
    lang = 'en' # str | By default, the API responds in English. You can change the response language by passing the language code as a query parameter `lang`. Multi language feature is available only for `paid users`. (optional)

    try:
        api_response = api_instance.get_time_series_lookup(date_start, date_end, ip=ip, location=location, lat=lat, long=long, output=output, lang=lang)
        print("The response of AstronomyApi->get_time_series_lookup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AstronomyApi->get_time_series_lookup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **date_start** | **str**| To lookup astronomy details from this date in YYYY-MM-DD format | 
 **date_end** | **str**| To lookup astronomy details from start date to this end date. (YYYY-MM-DD) | 
 **ip** | **str**| query parameter &#39;ip&#39;. | [optional] 
 **location** | **str**| query paramter &#39;location&#39;. If not provided, will be your ip location | [optional] 
 **lat** | **str**| query paramter &#39;lat&#39;. | [optional] 
 **long** | **str**| query paramter &#39;long&#39;. | [optional] 
 **output** | **str**| Desired output format. | [optional] 
 **lang** | **str**| By default, the API responds in English. You can change the response language by passing the language code as a query parameter &#x60;lang&#x60;. Multi language feature is available only for &#x60;paid users&#x60;. | [optional] 

### Return type

[**TimeSeriesResponse**](TimeSeriesResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful response |  -  |
**400** | Bad Request – Possible reasons include:   - Invalid or not found location/address   - Special characters in API key or value   - Invalid date format (expected: yyyy-MM-dd)   - IP not found in the database  |  -  |
**401** | Unauthorized – Possible reasons include:   - Missing or invalid API key   - Account unverified, locked, or disabled   - Accessing API with an unauthorized key   - Subscription expired or downgraded  |  -  |
**405** | Method Not Allowed – Only GET is allowed for &#x60;/astronomy/timeSeries&#x60; endpoint |  -  |
**429** | Too Many Requests – API usage limits exceeded for current plan |  -  |
**499** | Client Closed Request – Client terminated connection before completion |  -  |
**500** | Internal Server Error – Something went wrong on our end |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

