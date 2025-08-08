# GetBulkIpSecurityInfoResponse


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
**message** | **str** |  | [optional] 

## Example

```python
from ipgeolocation.models.get_bulk_ip_security_info_response import GetBulkIpSecurityInfoResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetBulkIpSecurityInfoResponse from a JSON string
get_bulk_ip_security_info_response_instance = GetBulkIpSecurityInfoResponse.from_json(json)
# print the JSON string representation of the object
print(GetBulkIpSecurityInfoResponse.to_json())

# convert the object into a dict
get_bulk_ip_security_info_response_dict = get_bulk_ip_security_info_response_instance.to_dict()
# create an instance of GetBulkIpSecurityInfoResponse from a dict
get_bulk_ip_security_info_response_from_dict = GetBulkIpSecurityInfoResponse.from_dict(
    get_bulk_ip_security_info_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


