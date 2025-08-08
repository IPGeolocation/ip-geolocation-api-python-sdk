# GetBulkIpGeolocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** |  | [optional] 
**ip** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**country_metadata** | [**CountryMetadata**](CountryMetadata.md) |  | [optional] 
**network** | [**Network**](Network.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 
**security** | [**Security**](Security.md) |  | [optional] 
**abuse** | [**Abuse**](Abuse.md) |  | [optional] 
**time_zone** | [**TimeZone**](TimeZone.md) |  | [optional] 
**user_agent** | [**UserAgentData**](UserAgentData.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.get_bulk_ip_geolocation_response import GetBulkIpGeolocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBulkIpGeolocationResponse from a JSON string
get_bulk_ip_geolocation_response_instance = GetBulkIpGeolocationResponse.from_json(json)
# print the JSON string representation of the object
print(GetBulkIpGeolocationResponse.to_json())

# convert the object into a dict
get_bulk_ip_geolocation_response_dict = get_bulk_ip_geolocation_response_instance.to_dict()
# create an instance of GetBulkIpGeolocationResponse from a dict
get_bulk_ip_geolocation_response_from_dict = GetBulkIpGeolocationResponse.from_dict(
    get_bulk_ip_geolocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


