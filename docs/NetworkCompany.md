# NetworkCompany


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**domain** | **str** |  | [optional] 

## Example

```python
from ipgeolocation.models.network_company import NetworkCompany

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkCompany from a JSON string
network_company_instance = NetworkCompany.from_json(json)
# print the JSON string representation of the object
print(NetworkCompany.to_json())

# convert the object into a dict
network_company_dict = network_company_instance.to_dict()
# create an instance of NetworkCompany from a dict
network_company_from_dict = NetworkCompany.from_dict(network_company_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


