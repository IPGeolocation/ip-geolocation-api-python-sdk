# Abuse


## Properties

| Name                | Type          | Description                                                          | Notes      |
|---------------------|---------------|----------------------------------------------------------------------|------------|
| **route**           | **str**       | The IP range or route associated with the IP address.                | [optional] |
| **country**         | **str**       | Two-letter country code where the abuse contact is registered.       | [optional] |
| **handle**          | **str**       | The abuse handle or reference ID for the responsible organization.   | [optional] |
| **name**            | **str**       | The name/title of the abuse contact role or team.                    | [optional] |
| **organization**    | **str**       | The name of the organization managing provided IP Address.           | [optional] |
| **role**            | **str**       | Role of the contact (e.g., abuse, administrative, registrant, etc.). | [optional] |
| **kind**            | **str**       | Type of contact: individual, team, or organization.                  | [optional] |
| **address**         | **str**       | Physical mailing address of the responsible entity.                  | [optional] |
| **emails**          | **List[str]** | Email address(es) of the abuse contact.                              | [optional] |
| **phone_numbers**   | **List[str]** | Phone number(s) in international format for the abuse contact.       | [optional] |

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
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#api-endpoints) [[Back to README]](../README.md)


