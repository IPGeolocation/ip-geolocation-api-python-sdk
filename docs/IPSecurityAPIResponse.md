# IPSecurityAPIResponse


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


