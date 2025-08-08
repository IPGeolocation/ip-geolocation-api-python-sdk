# ASNDetails


## Properties

Name | Type                                        | Description | Notes
------------ |---------------------------------------------| ------------- | -------------
**as_number** | **str**                                     |  | [optional] 
**organization** | **str**                                     |  | [optional] 
**country** | **str**                                     |  | [optional] 
**asn_name** | **str**                                     |  | [optional] 
**type** | **str**                                     |  | [optional] 
**domain** | **str**                                     |  | [optional] 
**date_allocated** | **str**                                     |  | [optional] 
**allocation_status** | **str**                                     |  | [optional] 
**num_of_ipv4_routes** | **str**                                     |  | [optional] 
**num_of_ipv6_routes** | **str**                                     |  | [optional] 
**rir** | **str**                                     |  | [optional] 
**routes** | **List[str]**                               | It will only be included in the response, if you set include&#x3D;routes in the request | [optional] 
**upstreams** | [**List[ASNConnection]**](ASNConnection.md) | It will only be included in the response, if you set include&#x3D;upstreams in the request | [optional] 
**downstreams** | [**List[ASNConnection]**](ASNConnection.md) | It will only be included in the response, if you set include&#x3D;downstreams in the request | [optional] 
**peers** | [**List[ASNConnection]**](ASNConnection.md) | It will only be included in the response, if you set include&#x3D;peers in the request | [optional] 
**whois_response** | **str**                                     | It will only be included in the response, if you set include&#x3D;whois_response in the request | [optional] 

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


