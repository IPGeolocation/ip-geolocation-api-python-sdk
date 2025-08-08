# UserAgentDataEngine


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**version_major** | **str** |  | [optional] 

## Example

```python
from ipgeolocation.models.user_agent_data_engine import UserAgentDataEngine

# TODO update the JSON string below
json = "{}"
# create an instance of UserAgentDataEngine from a JSON string
user_agent_data_engine_instance = UserAgentDataEngine.from_json(json)
# print the JSON string representation of the object
print(UserAgentDataEngine.to_json())

# convert the object into a dict
user_agent_data_engine_dict = user_agent_data_engine_instance.to_dict()
# create an instance of UserAgentDataEngine from a dict
user_agent_data_engine_from_dict = UserAgentDataEngine.from_dict(user_agent_data_engine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


