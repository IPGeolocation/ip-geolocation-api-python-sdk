# TimezoneDetailDstEnd


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
from ipgeolocation.models.timezone_detail_dst_end import TimezoneDetailDstEnd

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneDetailDstEnd from a JSON string
timezone_detail_dst_end_instance = TimezoneDetailDstEnd.from_json(json)
# print the JSON string representation of the object
print(TimezoneDetailDstEnd.to_json())

# convert the object into a dict
timezone_detail_dst_end_dict = timezone_detail_dst_end_instance.to_dict()
# create an instance of TimezoneDetailDstEnd from a dict
timezone_detail_dst_end_from_dict = TimezoneDetailDstEnd.from_dict(timezone_detail_dst_end_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


