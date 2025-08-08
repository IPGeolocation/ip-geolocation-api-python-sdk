# ASNConnection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**as_number** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**country** | **str** |  | [optional] 

## Example

```python
from ipgeolocation.models.asn_connection import ASNConnection

# TODO update the JSON string below
json = "{}"
# create an instance of ASNConnection from a JSON string
asn_connection_instance = ASNConnection.from_json(json)
# print the JSON string representation of the object
print(ASNConnection.to_json())

# convert the object into a dict
asn_connection_dict = asn_connection_instance.to_dict()
# create an instance of ASNConnection from a dict
asn_connection_from_dict = ASNConnection.from_dict(asn_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


