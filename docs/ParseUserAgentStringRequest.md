# ParseUserAgentStringRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ua_string** | **str** |  | [optional] 

## Example

```python
from ipgeolocation.models.parse_user_agent_string_request import ParseUserAgentStringRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParseUserAgentStringRequest from a JSON string
parse_user_agent_string_request_instance = ParseUserAgentStringRequest.from_json(json)
# print the JSON string representation of the object
print(ParseUserAgentStringRequest.to_json())

# convert the object into a dict
parse_user_agent_string_request_dict = parse_user_agent_string_request_instance.to_dict()
# create an instance of ParseUserAgentStringRequest from a dict
parse_user_agent_string_request_from_dict = ParseUserAgentStringRequest.from_dict(parse_user_agent_string_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


