# TimezoneDetailDstStart


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
from ipgeolocation.models.timezone_detail_dst_start import TimezoneDetailDstStart

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneDetailDstStart from a JSON string
timezone_detail_dst_start_instance = TimezoneDetailDstStart.from_json(json)
# print the JSON string representation of the object
print(TimezoneDetailDstStart.to_json())

# convert the object into a dict
timezone_detail_dst_start_dict = timezone_detail_dst_start_instance.to_dict()
# create an instance of TimezoneDetailDstStart from a dict
timezone_detail_dst_start_from_dict = TimezoneDetailDstStart.from_dict(timezone_detail_dst_start_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


