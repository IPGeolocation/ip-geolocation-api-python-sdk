# ASNDetails


## Properties

| Name                    | Type                                         | Description                                                                                     | Notes      |
|-------------------------|----------------------------------------------|-------------------------------------------------------------------------------------------------|------------|
|  **as_number**          | **str**                                      | Autonomous System Number that was looked up.                                                    | [optional] |
|  **organization**       | **str**                                      | The name of the organization to which that ASN is assigned.                                     | [optional] | 
|  **country**            | **str**                                      | The two-letter country code where the organization is registered.                               | [optional] | 
|  **asn_name**           | **str**                                      | The official ASN handle.                                                                        | [optional] | 
|  **type**               | **str**                                      | Type of the ASN (e.g., “isp”, “hosting”).                                                       | [optional] | 
|  **domain**             | **str**                                      | The domain associated with the ASN.                                                             | [optional] | 
|  **date_allocated**     | **str**                                      | The date the ASN was originally allocated.                                                      | [optional] | 
|  **allocation_status**  | **str**                                      | Current status of the ASN (“assigned”, “allocated”, etc.).                                      | [optional] | 
|  **num_of_ipv4_routes** | **str**                                      | Number of distinct IPv4 prefixes announced by this ASN.                                         | [optional] | 
|  **num_of_ipv6_routes** | **str**                                      | Number of distinct IPv6 prefixes announced by this ASN.                                         | [optional] | 
|  **rir**                | **str**                                      | Directly connected ASes (with containing object of AS Number, description, country).            | [optional] | 
|  **routes**             | **List[str]**                                | It will only be included in the response, if you set include&#x3D;routes in the request         | [optional] | 
|  **upstreams**          | [**List[ASNConnection]**](ASNConnection.md)  | It will only be included in the response, if you set include&#x3D;upstreams in the request      | [optional] | 
|  **downstreams**        | [**List[ASNConnection]**](ASNConnection.md)  | It will only be included in the response, if you set include&#x3D;downstreams in the request    | [optional] | 
|  **peers**              | [**List[ASNConnection]**](ASNConnection.md)  | It will only be included in the response, if you set include&#x3D;peers in the request          | [optional] | 
|  **whois_response**     | **str**                                      | It will only be included in the response, if you set include&#x3D;whois_response in the request | [optional] | 

## Example

```python
from ipgeolocation.models.asn_details import ASNDetails

# TODO update the JSON string below
json = "{}"
# create an instance of ASNDetails from a JSON string
asn_details_instance = ASNDetails.from_json(json)
# print the JSON string representation of the object
print(ASNDetails.to_json())

# convert the object into a dict
asn_details_dict = asn_details_instance.to_dict()
# create an instance of ASNDetails from a dict
asn_details_from_dict = ASNDetails.from_dict(asn_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


