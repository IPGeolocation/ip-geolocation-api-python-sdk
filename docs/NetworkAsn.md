# NetworkAsn


## Properties

| Name                   | Type    | Description                                                                                 | Notes      |
|------------------------|---------|---------------------------------------------------------------------------------------------|------------|
| **as_number**          | **str** | Autonomous system number of the autonomous system, to which IP address belongs to.          | [optional] |
| **organization**       | **str** | Legal Full Name of AS organization holding the IP address.                                  | [optional] |
| **country**            | **str** | Name of the country, ASN is residing.                                                       | [optional] |
| **asn_name**           | **str** | Name associated with the Autonomous System, usually representing organization.              | [optional] |
| **type**               | **str** | Type of the ASN, whether ISP, Business, etc.                                                | [optional] |
| **domain**             | **str** | Domain name associated with the ASN holding the IP address.                                 | [optional] |
| **date_allocated**     | **str** | Last date, when the IP address assigned to the ASN. e.g., in format `1st June 2001`         | [optional] |
| **allocation_status**  | **str** | Whether the IP address is currently assigned to the ASN or not.                             | [optional] |
| **num_of_ipv4_routes** | **str** | Total number of IPv4 routes, held by the ASN. These Routes can be queried from our ASN API. | [optional] |
| **num_of_ipv6_routes** | **str** | Total number of IPv6 routes, held by the ASN. These Routes can be queried from our ASN API. | [optional] |
| **rir**                | **str** | Name of the Regional Internet Registry (RIR) that allocated the AS number.                  | [optional] |

## Example

```python
from ipgeolocation.models.network_asn import NetworkAsn

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkAsn from a JSON string
network_asn_instance = NetworkAsn.from_json(json)
# print the JSON string representation of the object
print(NetworkAsn.to_json())

# convert the object into a dict
network_asn_dict = network_asn_instance.to_dict()
# create an instance of NetworkAsn from a dict
network_asn_from_dict = NetworkAsn.from_dict(network_asn_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


