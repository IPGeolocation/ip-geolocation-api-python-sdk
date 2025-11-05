# TimezoneDetailDstStart


## Properties

| Name                 | Type       | Description                                                                       | Notes      |
|----------------------|------------|-----------------------------------------------------------------------------------|------------|
| **utc_time**         | **str**    | The date and time in UTC when DST begins.                                         | [optional] |
| **duration**         | **str**    | The time change that occurs when DST starts.                                      | [optional] |
| **gap**              | **bool**   | Is there is a missing hour (DST forward transition)?                              | [optional] |
| **date_time_after**  | **str**    | The local date and time that immediately follows the start of DST.                | [optional] |
| **date_time_before** | **str**    | The local date and time immediately before DST begins.                            | [optional] |
| **overlap**          | **bool**   | Whether there is an overlap of time due to clocks being set back when DST starts. | [optional] |

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


