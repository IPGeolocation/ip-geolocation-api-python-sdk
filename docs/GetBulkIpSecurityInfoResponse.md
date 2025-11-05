# GetBulkIpSecurityInfoResponse


## Properties

| Name                 | Type                                      | Description                                                                  | Notes        |
|----------------------|-------------------------------------------|------------------------------------------------------------------------------|--------------|
| **ip**               | **str**                                   | IP address that is used to lookup security information.                      | [optional]   |
| **hostname**         | **str**                                   | Hostname of the IP address used to query IP Security API.                    | [optional]   |
| **security**         | [**Security**](Security.md)               | Security object containing security information.                             | [optional]   |
| **location**         | [**LocationMinimal**](LocationMinimal.md) | Location object containing location information for the IP address provided. | [optional]   |
| **network**          | [**NetworkMinimal**](NetworkMinimal.md)   | Network object containing company and ASN information.                       | [optional]   |
| **time_zone**        | [**TimeZone**](TimeZone.md)               | Timezone details object.                                                     | [optional]   |
| **user_agent**       | [**UserAgentData**](UserAgentData.md)     | User Agent details of the calling machine/Client IP.                         | [optional]   | 
| **country_metadata** | [**CountryMetadata**](CountryMetadata.md) | Country metadata object containing tld, calling code and country languages.  | [optional]   | 
| **currency**         | [**Currency**](Currency.md)               | Currency object containing currency related information.                     | [optional]   |
| **message**          | **str**                                   | If there's something wrong with the given IP address.                        | [optional]   |

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


