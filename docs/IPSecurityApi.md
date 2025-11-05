# ipgeolocation.IPSecurityApi

All URIs are relative to *https://api.ipgeolocation.io/v2*

| Method                                                                      | HTTP request            | Description                                                       |
|-----------------------------------------------------------------------------|-------------------------|-------------------------------------------------------------------|
| [**get_bulk_ip_security_info**](IPSecurityApi.md#get_bulk_ip_security_info) | **POST** /security-bulk | To get the security information of multiple IP addresses at once. |
| [**get_ip_security_info**](IPSecurityApi.md#get_ip_security_info)           | **GET** /security       | To get the security information of an IP address.                 | 


# **get_bulk_ip_security_info**
> List[GetBulkIpSecurityInfoResponse] get_bulk_ip_security_info(get_bulk_ip_geolocation_request, include=include, fields=fields, excludes=excludes, output=output, lang=lang)

The Bulk IP Security Lookup API can provide security details for up to `50,000` bulk IPs. This API also has parameters to customize the response, just like the single IP Security Lookup API.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipgeolocation
from ipgeolocation.models.get_bulk_ip_geolocation_request import GetBulkIpGeolocationRequest
from ipgeolocation.models.get_bulk_ip_security_info_response import GetBulkIpSecurityInfoResponse
from ipgeolocation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ipgeolocation.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ipgeolocation.Configuration(
    host="https://api.ipgeolocation.io/v2"
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
    api_instance = ipgeolocation.IPSecurityApi(api_client)
    get_bulk_ip_geolocation_request = ipgeolocation.GetBulkIpGeolocationRequest()  # GetBulkIpGeolocationRequest | 
    include = 'location,network,currency,time_zone,user_agent,country_metadata,hostname'  # str | Include optional objects like `location`, `network`.  Use comma-separated values. Example: include=location,network  (optional)
    fields = 'security.is_tor, location,'  # str | Get specific fields, objects from the response. (optional)
    excludes = 'security.is_cloud_provider'  # str | Exclude specific fields, objects from the response. (optional)
    output = 'json'  # str | Desired output format. (optional)
    lang = 'en'  # str | By default, the API responds in English. You can change the response language by passing the language code as a query parameter `lang`. Multi language feature is available only for `paid users`. (optional)

    try:
        api_response = api_instance.get_bulk_ip_security_info(get_bulk_ip_geolocation_request, include=include,
                                                              fields=fields, excludes=excludes, output=output,
                                                              lang=lang)
        print("The response of IPSecurityApi->get_bulk_ip_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPSecurityApi->get_bulk_ip_security_info: %s\n" % e)
```



### Parameters


| Name                                | Type                                                              | Description                                                                                                                                                                                                            | Notes      |
|-------------------------------------|-------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **get_bulk_ip_geolocation_request** | [**GetBulkIpGeolocationRequest**](GetBulkIpGeolocationRequest.md) | To create a bulk request object for ipgeolocation api.                                                                                                                                                                 |            | 
| **include**                         | **str**                                                           | Include optional objects like &#x60;location&#x60;, &#x60;network&#x60;.  Use comma-separated values. Example: include&#x3D;location,network                                                                           | [optional] |
| **fields**                          | **str**                                                           | Get specific fields, objects from the response.                                                                                                                                                                        | [optional] |
| **excludes**                        | **str**                                                           | Exclude specific fields, objects from the response.                                                                                                                                                                    | [optional] |
| **output**                          | **str**                                                           | Desired output format.                                                                                                                                                                                                 | [optional] |
| **lang**                            | **str**                                                           | By default, the API responds in English. You can change the response language by passing the language code as a query parameter &#x60;lang&#x60;. Multi language feature is available only for &#x60;paid users&#x60;. | [optional] |

### Return type

[**List[GetBulkIpSecurityInfoResponse]**](GetBulkIpSecurityInfoResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                     | Response headers |
|-------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
**200** | Get the security details of bulk IPs. It may include the following information  subjecting to the availability of query parameters  - If include&#x3D;network, it will include network object  - If include&#x3D;location, it will include location object  - If include&#x3D;location,network, it will include both objects  - To get specific fields/object, use fields&#x3D;field_name e.g., security.is_tor - to exclude fields, same can be done                                                                                                                                                                                                                                                                                                           |  -  |
**400** | Bad Request – Possible reasons include:   - If the provided IPv4, IPv6 address, or domain name is invalid.    - If special character(s) ( ) [ ] { } \| ^ &#x60; is passed in the API URL either as paramter or its value. Specially in case of API key.      - If the IP addresses JSON list is empty, or the provided JSON does not have &#39;ips&#39; field while querying /security-bulk endpoint.      - If more than 50,000 IP addresses are provided while quering from /security-bulk endpoint.                                                                                                                                                                                                                                                          |  -  |
**401** | Unauthorized – Possible reasons include:   - Missing or invalid API key   - Account unverified, locked, or disabled   - Accessing API with an unauthorized key   - Subscription expired or downgraded   - If your account has been disabled or locked to use by the admin due to abuse or illegal activity.   - When the request to IP Security API is made using API key for a database subscription   - When the request to IP Security API is made on the &#39;paused&#39; subscription.   - If you’re making API requests after your subscription trial has been expired.   - If your active until date has passed and you need to upgrade your account.   - If bulk IP to security look-ups endpoint is called &#x60;using free subscription API key&#x60;. |  -  |
**403** | Forbidden - Possible reasons include:   - If IP to security look-up for a domain name is done using a free subscription API key.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                |  -  |
**404** | Not Found – Possible reasons include:   - If the IPv4, IPv6, or domain name does not not exists in our database.    - If the IPv4, IPv6, or domain name is passed as a path variable, instead of url parameter as ip&#x3D;.      - If the wrong endpoint is called, that does not exists in our API.                                                                                                                                                                                                                                                                                                                                                                                                                                                            |  -  |
**405** | Method Not Allowed – Only POST method is allowed for &#x60;/security-bulk&#x60; endpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                        |  -  |
**413** | Content Too Large – Possible reasons include:   - If the passed data in the POST requests is more than the limit of the API.                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    |  -  |
**429** | Too Many Requests – Possible reasons include:   - If the API usage limit has reached for the free subscriptions, or paid subscriptions with the status &#39;past due&#39;, &#39;deleted&#39; or &#39;trial expired&#39;.    - If the surcharge API usage limit has reached against the subscribed plan.                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  -  |
**499** | Client Closed Request – Client terminated connection before completion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          |  -  |
**500** | Internal Server Error – Something went wrong on our end                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_ip_security_info**
> IPSecurityAPIResponse get_ip_security_info(ip=ip, include=include, fields=fields, excludes=excludes, output=output, lang=lang)

IP Security API provides security details of a given IP. It detects whether the IP is proxy, tor or bot. It also shows the proxy types of the IP (like VPN, PROXY, RELAY etc.) with it's VPN/proxy service provider making our API powerful VPN checker. It finds the IPs that are involved in spam activities. It also checks whether the IP links to a cloud provider and includes the provider's name.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipgeolocation
from ipgeolocation.models.ip_security_api_response import IPSecurityAPIResponse
from ipgeolocation.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://api.ipgeolocation.io/v2
# See configuration.py for a list of all supported configuration parameters.
configuration = ipgeolocation.Configuration(
    host="https://api.ipgeolocation.io/v2"
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
    api_instance = ipgeolocation.IPSecurityApi(api_client)
    ip = '8.8.8.8'  # str | query parameter 'ip'. If not provided, will be your network IP (optional)
    include = 'location,network,currency,time_zone,user_agent,country_metadata,hostname'  # str | Include optional details like location and/or network. (optional)
    fields = 'security.is_tor, location,'  # str | Get specific fields, objects from the response. (optional)
    excludes = 'security.is_cloud_provider'  # str | Exclude specific fields, objects from the response. (optional)
    output = 'json'  # str | Desired output format (json or xml). (optional)
    lang = 'en'  # str | By default, the API responds in English. You can change the response language by passing the language code as a query parameter `lang`. Multi language feature is available only for `paid users`. (optional)

    try:
        api_response = api_instance.get_ip_security_info(ip=ip, include=include, fields=fields, excludes=excludes,
                                                         output=output, lang=lang)
        print("The response of IPSecurityApi->get_ip_security_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IPSecurityApi->get_ip_security_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **ip** | **str**| query parameter &#39;ip&#39;. If not provided, will be your network IP | [optional] 
 **include** | **str**| Include optional details like location and/or network. | [optional] 
 **fields** | **str**| Get specific fields, objects from the response. | [optional] 
 **excludes** | **str**| Exclude specific fields, objects from the response. | [optional] 
 **output** | **str**| Desired output format (json or xml). | [optional] 
 **lang** | **str**| By default, the API responds in English. You can change the response language by passing the language code as a query parameter &#x60;lang&#x60;. Multi language feature is available only for &#x60;paid users&#x60;. | [optional] 

### Return type

[**IPSecurityAPIResponse**](IPSecurityAPIResponse.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  | Response headers |
|-------------|--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------------|
**200** | Get the security details of the ip. It may include the following information  subjecting to the availability of query parameters  - If include&#x3D;network, it will include network object  - If include&#x3D;location, it will include location object  - If include&#x3D;location,network, it will include both objects  - To get specific fields/object, use fields&#x3D;field_name e.g., security.is_tor - to exclude fields, same can be done                                                                                                                                                                                                          |  -  |
**400** | Bad Request – Possible reasons include:   - If the provided IPv4, IPv6 address is invalid.    - If special character(s) ( ) [ ] { } \| ^ &#x60; is passed in the API URL either as paramter or its value. Specially in case of API key.                                                                                                                                                                                                                                                                                                                                                                                                                      |  -  |
**401** | Unauthorized – Possible reasons include:   - Missing or invalid API key   - Account unverified, locked, or disabled   - Accessing API with an unauthorized key   - Subscription expired or downgraded   - If your account has been disabled or locked to use by the admin due to abuse or illegal activity.   - When the request to IP Security API is made using API key for a database subscription   - When the request to IP Security API is made on the &#39;paused&#39; subscription.   - If you’re making API requests after your subscription trial has been expired.   - If your active until date has passed and you need to upgrade your account. |  -  |
**404** | Not Found – Possible reasons include:   - If the IPv4, IPv6, or domain name does not exist in our database.    - If the IPv4, IPv6, or domain name is passed as a path variable, instead of url parameter as ip&#x3D;.      - If the wrong endpoint is called, that does not exist in our API.                                                                                                                                                                                                                                                                                                                                                               |  -  |
**405** | Method Not Allowed – Only GET is allowed for &#x60;/security&#x60; endpoint                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                  |  -  |
**429** | Too Many Requests – Possible reasons include:   - If the API usage limit has reached for the free subscriptions, or paid subscriptions with the status &#39;past due&#39;, &#39;deleted&#39; or &#39;trial expired&#39;.    - If the surcharge API usage limit has reached against the subscribed plan.                                                                                                                                                                                                                                                                                                                                                      |  -  |
**499** | Client Closed Request – Client terminated connection before completion                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       |  -  |
**500** | Internal Server Error – Something went wrong on our end                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

