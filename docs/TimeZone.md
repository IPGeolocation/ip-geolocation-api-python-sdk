# TimeZone


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**offset** | **int** |  | [optional] 
**offset_with_dst** | **int** |  | [optional] 
**current_time** | **str** |  | [optional] 
**current_time_unix** | **float** |  | [optional] 
**is_dst** | **bool** |  | [optional] 
**dst_savings** | **int** |  | [optional] 
**dst_exists** | **bool** |  | [optional] 
**dst_start** | [**TimeZoneDstStart**](TimeZoneDstStart.md) |  | [optional] 
**dst_end** | [**TimeZoneDstEnd**](TimeZoneDstEnd.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.time_zone import TimeZone

# TODO update the JSON string below
json = "{}"
# create an instance of TimeZone from a JSON string
time_zone_instance = TimeZone.from_json(json)
# print the JSON string representation of the object
print(TimeZone.to_json())

# convert the object into a dict
time_zone_dict = time_zone_instance.to_dict()
# create an instance of TimeZone from a dict
time_zone_from_dict = TimeZone.from_dict(time_zone_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


