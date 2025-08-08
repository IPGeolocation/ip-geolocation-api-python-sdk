# ParseBulkUserAgentStringsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ua_strings** | **List[str]** |  | [optional] 

## Example

```python
from ipgeolocation.models.parse_bulk_user_agent_strings_request import ParseBulkUserAgentStringsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ParseBulkUserAgentStringsRequest from a JSON string
parse_bulk_user_agent_strings_request_instance = ParseBulkUserAgentStringsRequest.from_json(json)
# print the JSON string representation of the object
print(ParseBulkUserAgentStringsRequest.to_json())

# convert the object into a dict
parse_bulk_user_agent_strings_request_dict = parse_bulk_user_agent_strings_request_instance.to_dict()
# create an instance of ParseBulkUserAgentStringsRequest from a dict
parse_bulk_user_agent_strings_request_from_dict = ParseBulkUserAgentStringsRequest.from_dict(parse_bulk_user_agent_strings_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


