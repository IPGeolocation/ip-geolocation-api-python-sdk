# UserAgentDataDevice


## Properties

| Name      | Type    | Description       | Notes      |
|-----------|---------|-------------------|------------|
| **name**  | **str** | Device Name.      | [optional] | 
| **type**  | **str** | Device Type.      | [optional] |
| **brand** | **str** | Device Brand.     | [optional] |
| **cpu**   | **str** | Device CPU Model. | [optional] |

## Example

```python
from ipgeolocation.models.user_agent_data_device import UserAgentDataDevice

# TODO update the JSON string below
json = "{}"
# create an instance of UserAgentDataDevice from a JSON string
user_agent_data_device_instance = UserAgentDataDevice.from_json(json)
# print the JSON string representation of the object
print(UserAgentDataDevice.to_json())

# convert the object into a dict
user_agent_data_device_dict = user_agent_data_device_instance.to_dict()
# create an instance of UserAgentDataDevice from a dict
user_agent_data_device_from_dict = UserAgentDataDevice.from_dict(user_agent_data_device_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


