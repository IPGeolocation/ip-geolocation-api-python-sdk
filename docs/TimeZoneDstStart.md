# TimeZoneDstStart


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**utc_time** | **str** |  | [optional] 
**duration** | **str** |  | [optional] 
**gap** | **bool** |  | [optional] 
**date_time_after** | **str** |  | [optional] 
**date_time_before** | **str** |  | [optional] 
**overlap** | **bool** |  | [optional] 

## Example

```python
from ipgeolocation.models.time_zone_dst_start import TimeZoneDstStart

# TODO update the JSON string below
json = "{}"
# create an instance of TimeZoneDstStart from a JSON string
time_zone_dst_start_instance = TimeZoneDstStart.from_json(json)
# print the JSON string representation of the object
print(TimeZoneDstStart.to_json())

# convert the object into a dict
time_zone_dst_start_dict = time_zone_dst_start_instance.to_dict()
# create an instance of TimeZoneDstStart from a dict
time_zone_dst_start_from_dict = TimeZoneDstStart.from_dict(time_zone_dst_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


