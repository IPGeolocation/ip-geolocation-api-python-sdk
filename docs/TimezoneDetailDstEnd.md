# TimezoneDetailDstEnd


## Properties

| Name                 | Type     | Description                                                                     | Notes      |
|----------------------|----------|---------------------------------------------------------------------------------|------------|
| **utc_time**         | **str**  | The date and time in UTC when DST ends.                                         | [optional] | 
| **duration**         | **str**  | The time change that occurs when DST ends.                                      | [optional] | 
| **gap**              | **bool** | Is there is no gap (DST backward transition)?                                   | [optional] | 
| **date_time_after**  | **str**  | The local date and time that immediately follows the ends of DST.               | [optional] | 
| **date_time_before** | **str**  | The local date and time immediately before DST ends.                            | [optional] | 
| **overlap**          | **bool** | Whether there is an overlap of time due to clocks being set back when DST ends. | [optional] | 

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


