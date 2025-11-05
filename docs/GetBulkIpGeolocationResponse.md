# GetBulkIpGeolocationResponse


## Properties

| Name                 | Type                                      | Description                                                                                                                          | Notes      |
|----------------------|-------------------------------------------|--------------------------------------------------------------------------------------------------------------------------------------|------------|
| **message**          | **str**                                   | Error message related to the IP address, if it is wrong.                                                                             | [optional] |
| **ip**               | **str**                                   | IP address which is provided in the request list.                                                                                    | [optional] |
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


