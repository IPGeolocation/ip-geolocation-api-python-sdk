# Abuse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**route** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**handle** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization** | **str** |  | [optional] 
**role** | **str** |  | [optional] 
**kind** | **str** |  | [optional] 
**address** | **str** |  | [optional] 
**emails** | **List[str]** |  | [optional] 
**phone_numbers** | **List[str]** |  | [optional] 

## Example

```python
from ipgeolocation.models.abuse import Abuse

# TODO update the JSON string below
json = "{}"
# create an instance of Abuse from a JSON string
abuse_instance = Abuse.from_json(json)
# print the JSON string representation of the object
print(Abuse.to_json())

# convert the object into a dict
abuse_dict = abuse_instance.to_dict()
# create an instance of Abuse from a dict
abuse_from_dict = Abuse.from_dict(abuse_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


