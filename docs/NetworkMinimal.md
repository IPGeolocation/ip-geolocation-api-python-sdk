# NetworkMinimal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**asn** | [**NetworkMinimalAsn**](NetworkMinimalAsn.md) |  | [optional] 
**company** | [**NetworkMinimalCompany**](NetworkMinimalCompany.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.network_minimal import NetworkMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkMinimal from a JSON string
network_minimal_instance = NetworkMinimal.from_json(json)
# print the JSON string representation of the object
print(NetworkMinimal.to_json())

# convert the object into a dict
network_minimal_dict = network_minimal_instance.to_dict()
# create an instance of NetworkMinimal from a dict
network_minimal_from_dict = NetworkMinimal.from_dict(network_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


