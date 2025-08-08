# UserAgentData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user_agent_string** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**version** | **str** |  | [optional] 
**version_major** | **str** |  | [optional] 
**device** | [**UserAgentDataDevice**](UserAgentDataDevice.md) |  | [optional] 
**engine** | [**UserAgentDataEngine**](UserAgentDataEngine.md) |  | [optional] 
**operating_system** | [**UserAgentDataOperatingSystem**](UserAgentDataOperatingSystem.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.user_agent_data import UserAgentData

# TODO update the JSON string below
json = "{}"
# create an instance of UserAgentData from a JSON string
user_agent_data_instance = UserAgentData.from_json(json)
# print the JSON string representation of the object
print(UserAgentData.to_json())

# convert the object into a dict
user_agent_data_dict = user_agent_data_instance.to_dict()
# create an instance of UserAgentData from a dict
user_agent_data_from_dict = UserAgentData.from_dict(user_agent_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


