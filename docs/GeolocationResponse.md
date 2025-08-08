# GeolocationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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
from ipgeolocation.models.geolocation_response import GeolocationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GeolocationResponse from a JSON string
geolocation_response_instance = GeolocationResponse.from_json(json)
# print the JSON string representation of the object
print(GeolocationResponse.to_json())

# convert the object into a dict
geolocation_response_dict = geolocation_response_instance.to_dict()
# create an instance of GeolocationResponse from a dict
geolocation_response_from_dict = GeolocationResponse.from_dict(geolocation_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


