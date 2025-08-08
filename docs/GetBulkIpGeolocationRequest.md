# GetBulkIpGeolocationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ips** | **List[str]** |  | [optional] 

## Example

```python
from ipgeolocation.models.get_bulk_ip_geolocation_request import GetBulkIpGeolocationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GetBulkIpGeolocationRequest from a JSON string
get_bulk_ip_geolocation_request_instance = GetBulkIpGeolocationRequest.from_json(json)
# print the JSON string representation of the object
print(GetBulkIpGeolocationRequest.to_json())

# convert the object into a dict
get_bulk_ip_geolocation_request_dict = get_bulk_ip_geolocation_request_instance.to_dict()
# create an instance of GetBulkIpGeolocationRequest from a dict
get_bulk_ip_geolocation_request_from_dict = GetBulkIpGeolocationRequest.from_dict(get_bulk_ip_geolocation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


