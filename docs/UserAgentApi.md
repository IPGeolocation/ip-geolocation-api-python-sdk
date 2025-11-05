# ipgeolocation.UserAgentApi

All URIs are relative to *https://api.ipgeolocation.io/v2*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_user_agent_details**](UserAgentApi.md#get_user_agent_details) | **GET** /user-agent | Get details of user-agent
[**parse_bulk_user_agent_strings**](UserAgentApi.md#parse_bulk_user_agent_strings) | **POST** /user-agent-bulk | Handle multiple user-agent string lookups
[**parse_user_agent_string**](UserAgentApi.md#parse_user_agent_string) | **POST** /user-agent | Handle single User-Agent string


# **get_user_agent_details**
> UserAgentData get_user_agent_details(user_agent=user_agent, output=output)

Get details of user-agent

User Agent Parser API provides the accurate browser, device, and operating system
details from a User Agent String. It also provides information about crawlers and attack sources. You can use these details to customize user experience, prevent crawlers and attackers from accessing your website.


### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipgeolocation
from ipgeolocation.models.user_agent_data import UserAgentData
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
    api_instance = ipgeolocation.UserAgentApi(api_client)
    user_agent = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9' # str |  (optional)
    output = 'json' # str | Desired output format (json or xml). (optional)

    try:
        # Get details of user-agent
        api_response = api_instance.get_user_agent_details(user_agent=user_agent, output=output)
        print("The response of UserAgentApi->get_user_agent_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAgentApi->get_user_agent_details: %s\n" % e)
```



### Parameters


Name | Type | Description                          | Notes
------------- | ------------- |--------------------------------------| -------------
 **user_agent** | **str**| User Agent String to parse.          | [optional] 
 **output** | **str**| Desired output format (json or xml). | [optional] 

### Return type

[**UserAgentData**](UserAgentData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | successful response |  -  |
**400** | Bad Request – Possible reasons include:   - If the user-agent string is empty/null.  |  -  |
**401** | Unauthorized – Possible reasons include:   - If API key (as apiKey URL parameter) is missing from the request to User Agent API.    - If the provided API key is not valid.   - If your account has been disabled or locked by admin because of any illegal activity.   - If you’re making requests after your subscription trial has been expired.   - If you’ve exceeded your requests limit.   - If your subscription is paused or is not active.   - If you’re accessing a paid feature on free subscription.  |  -  |
**405** | If wrong HTTP request method is used for calling the endpoints. Only GET and POST methods are allowed. |  -  |
**429** | Too Many Requests – API usage limits exceeded for current plan |  -  |
**499** | Client Closed Request – Client terminated connection before completion |  -  |
**500** | Internal Server Error – Something went wrong on our end |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_bulk_user_agent_strings**
> List[UserAgentData] parse_bulk_user_agent_strings(output=output, parse_bulk_user_agent_strings_request=parse_bulk_user_agent_strings_request)

Handle multiple user-agent string lookups

This endpoint allows you to perform the parsing of multiple User-Angent strings (max. 50,000) at the same time. The requests count per round is equal to total User-Agent strings passed. This feature is `only available for paid plans`.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipgeolocation
from ipgeolocation.models.parse_bulk_user_agent_strings_request import ParseBulkUserAgentStringsRequest
from ipgeolocation.models.user_agent_data import UserAgentData
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
    api_instance = ipgeolocation.UserAgentApi(api_client)
    output = 'json' # str | Desired output format (json or xml). (optional)
    parse_bulk_user_agent_strings_request = ipgeolocation.ParseBulkUserAgentStringsRequest() # ParseBulkUserAgentStringsRequest |  (optional)

    try:
        # Handle multiple user-agent string lookups
        api_response = api_instance.parse_bulk_user_agent_strings(output=output, parse_bulk_user_agent_strings_request=parse_bulk_user_agent_strings_request)
        print("The response of UserAgentApi->parse_bulk_user_agent_strings:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAgentApi->parse_bulk_user_agent_strings: %s\n" % e)
```



### Parameters


Name | Type | Description                               | Notes
------------- | ------------- |-------------------------------------------| -------------
 **output** | **str**| Desired output format (json or xml).      | [optional] 
 **parse_bulk_user_agent_strings_request** | [**ParseBulkUserAgentStringsRequest**](ParseBulkUserAgentStringsRequest.md)| User Agent String request object to pass. | [optional] 

### Return type

[**List[UserAgentData]**](UserAgentData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad Request – Possible reasons include:   - If the user-agent string is empty/null.   - If the User Agent Strings JSON list is empty, or the provided JSON does not have &#39;uaStrings&#39; field while querying /user-agent-bulk endpoint.   - If more than 50,000 user agent strings are provided while quering from /user-agent-bulk endpoint.  |  -  |
**401** | Unauthorized – Possible reasons include:   - If API key (as apiKey URL parameter) is missing from the request to User Agent API.    - If the provided API key is not valid.   - If your account has been disabled or locked by admin because of any illegal activity.   - If you’re making requests after your subscription trial has been expired.   - If you’ve exceeded your requests limit.   - If your subscription is paused or is not active.   - If you’re accessing a paid feature on free subscription.   - If bulk user agent parsing endpoint is called using free subscription API key.  |  -  |
**405** | If wrong HTTP request method is used for calling the endpoints. Only POST method is allowed. |  -  |
**429** | Too Many Requests – API usage limits exceeded for current plan |  -  |
**499** | Client Closed Request – Client terminated connection before completion |  -  |
**500** | Internal Server Error – Something went wrong on our end |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **parse_user_agent_string**
> UserAgentData parse_user_agent_string(output=output, parse_user_agent_string_request=parse_user_agent_string_request)

Handle single User-Agent string

You can also provide custom User-Agent string to parse in JSON payload. This endpoint is meant to be called from server-side and is available for paid subscriptions only.

### Example

* Api Key Authentication (ApiKeyAuth):

```python
import ipgeolocation
from ipgeolocation.models.parse_user_agent_string_request import ParseUserAgentStringRequest
from ipgeolocation.models.user_agent_data import UserAgentData
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
    api_instance = ipgeolocation.UserAgentApi(api_client)
    output = 'json' # str | Desired output format (json or xml). (optional)
    parse_user_agent_string_request = ipgeolocation.ParseUserAgentStringRequest() # ParseUserAgentStringRequest |  (optional)

    try:
        # Handle single User-Agent string
        api_response = api_instance.parse_user_agent_string(output=output, parse_user_agent_string_request=parse_user_agent_string_request)
        print("The response of UserAgentApi->parse_user_agent_string:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UserAgentApi->parse_user_agent_string: %s\n" % e)
```



### Parameters


Name | Type | Description                                    | Notes
------------- | ------------- |------------------------------------------------| -------------
 **output** | **str**| Desired output format (json or xml).           | [optional] 
 **parse_user_agent_string_request** | [**ParseUserAgentStringRequest**](ParseUserAgentStringRequest.md)| User Agent String object to pass as parameter. | [optional] 

### Return type

[**UserAgentData**](UserAgentData.md)

### Authorization

[ApiKeyAuth](../README.md#ApiKeyAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json, application/xml

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Successful request |  -  |
**400** | Bad Request – Possible reasons include:   - If the user-agent string is empty/null.  |  -  |
**401** | Unauthorized – Possible reasons include:   - If API key (as apiKey URL parameter) is missing from the request to User Agent API.    - If the provided API key is not valid.   - If your account has been disabled or locked by admin because of any illegal activity.   - If you’re making requests after your subscription trial has been expired.   - If you’ve exceeded your requests limit.   - If your subscription is paused or is not active.   - If you’re accessing a paid feature on free subscription.  |  -  |
**405** | If wrong HTTP request method is used for calling the endpoints. Only POST Method is acceptable for this endpoint |  -  |
**429** | Too Many Requests – API usage limits exceeded for current plan |  -  |
**499** | Client Closed Request – Client terminated connection before completion |  -  |
**500** | Internal Server Error – Something went wrong on our end |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

