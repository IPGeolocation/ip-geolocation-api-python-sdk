# UserAgentDataOperatingSystem


## Properties

| Name              | Type      | Description                                                                | Notes      |
|-------------------|-----------|----------------------------------------------------------------------------|------------|
| **name**          | **str**   | Name of the operating system (e.g., 'Windows', 'iOS', 'Android', 'Linux'). | [optional] | 
| **type**          | **str**   | Operating System Class.                                                    | [optional] |
| **version**       | **str**   | Operating System Version.                                                  | [optional] |
| **version_major** | **str**   | Operating System Version Major.                                            | [optional] |
| **build**         | **str**   | Operating System Version Major.                                            | [optional] |

## Example

```python
from ipgeolocation.models.user_agent_data_operating_system import UserAgentDataOperatingSystem

# TODO update the JSON string below
json = "{}"
# create an instance of UserAgentDataOperatingSystem from a JSON string
user_agent_data_operating_system_instance = UserAgentDataOperatingSystem.from_json(json)
# print the JSON string representation of the object
print(UserAgentDataOperatingSystem.to_json())

# convert the object into a dict
user_agent_data_operating_system_dict = user_agent_data_operating_system_instance.to_dict()
# create an instance of UserAgentDataOperatingSystem from a dict
user_agent_data_operating_system_from_dict = UserAgentDataOperatingSystem.from_dict(user_agent_data_operating_system_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


