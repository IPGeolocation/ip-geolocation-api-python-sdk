# GeolocationResponse


## Properties

| Name                 | Type                                      | Description                                                                                                                          | Notes      |
|----------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|------------|
| **ip**               | **str**                                   | IP address that is used to lookup geolocation information.                                                                           | [optional] |
| **hostname**         | **str**                                   | Hostname of the IP address used to query IP Geolocation API.                                                                         | [optional] |
| **domain**           | **str**                                   | Domain name that is used to lookup geolocation information. It is not returned if an IP address is used to query IP Geolocation API. | [optional] |
| **location**         | [**Location**](Location.md)               | Location information object.                                                                                                         | [optional] |
| **country_metadata** | [**CountryMetadata**](CountryMetadata.md) | Country metadata object containing tld, calling code and country languages.                                                          | [optional] |
| **network**          | [**Network**](Network.md)                 | Network object containing ISP and asn related information.                                                                           | [optional] |
| **currency**         | [**Currency**](Currency.md)               | Currency object containing currency related information.                                                                             | [optional] |
| **security**         | [**Security**](Security.md)               | Security information object.                                                                                                         | [optional] |
| **abuse**            | [**Abuse**](Abuse.md)                     | IP Abuse contact information object.                                                                                                 | [optional] |
| **time_zone**        | [**TimeZone**](TimeZone.md)               | Timezone details object.                                                                                                             | [optional] |
| **user_agent**       | [**UserAgentData**](UserAgentData.md)     | User Agent details of the calling machine/Client IP.                                                                                 | [optional] |

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


