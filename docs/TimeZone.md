# TimeZone


## Properties

| Name                  | Type                                        | Description                                                                                                                                                                | Notes      |
|-----------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **name**              | **str**                                     | Name (ISO 8601) of the time zone.                                                                                                                                          | [optional] |
| **offset**            | **int**                                     | Time zone offset from UTC.                                                                                                                                                 | [optional] |
| **offset_with_dst**   | **int**                                     | Time zone with DST offset from UTC.                                                                                                                                        | [optional] |
| **current_time**      | **str**                                     | Current time in `yyyy-MM-dd HH:mm:ss.SSS±ZZZ` format.                                                                                                                      | [optional] |
| **current_time_unix** | **float**                                   | Current time in seconds since 1970.                                                                                                                                        | [optional] |
| **is_dst**            | **bool**                                    | Is the time zone in daylight savings?                                                                                                                                      | [optional] |
| **dst_savings**       | **int**                                     | Total daylight savings.                                                                                                                                                    | [optional] |
| **dst_exists**        | **bool**                                    | Indicates whether Daylight Saving Time (DST) is observed in the region. If `true`, the `dst_start` and `dst_end` objects will include detailed DST transition information. | [optional] |
| **dst_start**         | [**TimeZoneDstStart**](TimeZoneDstStart.md) | DST start detailed information.                                                                                                                                            | [optional] | 
| **dst_end**           | [**TimeZoneDstEnd**](TimeZoneDstEnd.md)     | DST end detailed information.                                                                                                                                              | [optional] |

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


