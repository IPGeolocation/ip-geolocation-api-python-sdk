# AbuseResponse


## Properties

| Name      | Type                  | Description                                                  | Notes         |
|-----------|-----------------------|--------------------------------------------------------------|---------------|
| **ip**    | **str**               | The IP address for which abuse contact details are returned. | [optional]    |
| **abuse** | [**Abuse**](Abuse.md) | Abuse contact information object.                            | [optional]    |

## Example

```python
from ipgeolocation.models.abuse_response import AbuseResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AbuseResponse from a JSON string
abuse_response_instance = AbuseResponse.from_json(json)
# print the JSON string representation of the object
print(AbuseResponse.to_json())

# convert the object into a dict
abuse_response_dict = abuse_response_instance.to_dict()
# create an instance of AbuseResponse from a dict
abuse_response_from_dict = AbuseResponse.from_dict(abuse_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


