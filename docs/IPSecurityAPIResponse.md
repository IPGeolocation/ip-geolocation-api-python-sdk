# IPSecurityAPIResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**security** | [**Security**](Security.md) |  | [optional] 
**location** | [**LocationMinimal**](LocationMinimal.md) |  | [optional] 
**network** | [**NetworkMinimal**](NetworkMinimal.md) |  | [optional] 
**time_zone** | [**TimeZone**](TimeZone.md) |  | [optional] 
**user_agent** | [**UserAgentData**](UserAgentData.md) |  | [optional] 
**country_metadata** | [**CountryMetadata**](CountryMetadata.md) |  | [optional] 
**currency** | [**Currency**](Currency.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.ip_security_api_response import IPSecurityAPIResponse

# TODO update the JSON string below
json = "{}"
# create an instance of IPSecurityAPIResponse from a JSON string
ip_security_api_response_instance = IPSecurityAPIResponse.from_json(json)
# print the JSON string representation of the object
print(IPSecurityAPIResponse.to_json())

# convert the object into a dict
ip_security_api_response_dict = ip_security_api_response_instance.to_dict()
# create an instance of IPSecurityAPIResponse from a dict
ip_security_api_response_from_dict = IPSecurityAPIResponse.from_dict(ip_security_api_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


