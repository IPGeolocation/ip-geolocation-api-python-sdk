# NetworkMinimalAsn


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from ipgeolocation.models.network_minimal_asn import NetworkMinimalAsn

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkMinimalAsn from a JSON string
network_minimal_asn_instance = NetworkMinimalAsn.from_json(json)
# print the JSON string representation of the object
print(NetworkMinimalAsn.to_json())

# convert the object into a dict
network_minimal_asn_dict = network_minimal_asn_instance.to_dict()
# create an instance of NetworkMinimalAsn from a dict
network_minimal_asn_from_dict = NetworkMinimalAsn.from_dict(network_minimal_asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


