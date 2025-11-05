# Security


## Properties

| Name                  | Type          | Description                                                                                                         | Notes       |
|-----------------------|---------------|---------------------------------------------------------------------------------------------------------------------|-------------|
| **threat_score**      | **int**       | IP address’ threat score. It ranges from 0 to 100. **100 indicates highest threat** and vice versa for lower score. | [optional]  |
| **is_tor**            | **bool**      | Indicates if the IP address is being consumed on a Tor endpoint.                                                    | [optional]  |
| **is_proxy**          | **bool**      | Indicates whether the IP address is associated with any anonymization network --- VPN, PROXY, or RELAY.             | [optional]  |
| **proxy_type**        | **str**       | Specifies which of the three types (VPN, PROXY, or RELAY) applies when `is_proxy` is true; otherwise remains empty. | [optional]  |
| **proxy_provider**    | **str**       | Name of the proxy provider, if the IP address belongs to a proxy network.                                           | [optional]  |
| **is_anonymous**      | **bool**      | Indicates if the IP address is being used anonymously.                                                              | [optional]  |
| **is_known_attacker** | **bool**      | Indicates if the IP address is enlisted as an attacking IP address.                                                 | [optional]  |
| **is_spam**           | **bool**      | Indicates if the IP address is enlisted as a spam IP address.                                                       | [optional]  |
| **is_bot**            | **bool**      | Indicates if the IP address is enlisted as a bot IP address.                                                        | [optional]  |
| **is_cloud_provider** | **bool**      | Indicates if the IP address belongs to a cloud provider (computing infrastructure providers).                       | [optional]  |
| **cloud_provider**    | **str**       | Name of the Cloud Provider, if the IP address belongs to a cloud provider.                                          | [optional]  |

## Example

```python
from ipgeolocation.models.security import Security

# TODO update the JSON string below
json = "{}"
# create an instance of Security from a JSON string
security_instance = Security.from_json(json)
# print the JSON string representation of the object
print(Security.to_json())

# convert the object into a dict
security_dict = security_instance.to_dict()
# create an instance of Security from a dict
security_from_dict = Security.from_dict(security_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


