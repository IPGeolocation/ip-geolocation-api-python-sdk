# TimezoneDetail


## Properties

| Name                | Type                                                    | Description                                                                                                                                                                | Notes      |
|---------------------|---------------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------------------------------------------------|------------|
| **name**            | **str**                                                 | The IANA timezone name/identifier for the location.                                                                                                                        | [optional] |
| **offset**          | **int**                                                 | The Standard time zone offset from UTC in hours.                                                                                                                           | [optional] |
| **offset_with_dst** | **int**                                                 | The time zone offset from UTC in hours, accounting for daylight saving time (DST) if found.                                                                                | [optional] |
| **date**            | **str**                                                 | The current date in 'YYYY-MM-DD' format.                                                                                                                                   | [optional] |
| **date_time**       | **str**                                                 | The current date and time in 'YYYY-MM-DD HH:mm:ss' format.                                                                                                                 | [optional] |
| **date_time_txt**   | **str**                                                 | The current date and time in descriptive format for easy reading, formatted as 'EEEE, MMMM dd, yyyy HH:mm:ss'. (e.g., "Friday, November 08, 2024 08:44:26")                | [optional] |
| **date_time_wti**   | **str**                                                 | The date and time with time zone information in 'EEE, dd MMM yyyy HH:mm:ss Z' format. (e.g., "Fri, 08 Nov 2024 08:44:26 -0500")                                            | [optional] |
| **date_time_ymd**   | **str**                                                 | The date and time with timezone offset in ISO 8601 format 'YYYY-MM-DDTHH:mm:ss±HHMM'. (e.g., "2024-11-08T08:44:26-0500")                                                   | [optional] |
| **date_time_unix**  | **float**                                               | The Unix timestamp representing the date and time in seconds (e.g., 1731073466.073).                                                                                       | [optional] |
| **time_24**         | **str**                                                 | The current time in 24-hour format 'HH:mm:ss'.                                                                                                                             | [optional] |
| **time_12**         | **str**                                                 | The current time in 12-hour format with AM/PM notation, formatted as 'HH:mm:ss AM/PM'.                                                                                     | [optional] |
| **week**            | **int**                                                 | The week number of the year (1-52).                                                                                                                                        | [optional] |
| **month**           | **int**                                                 | The current month as a number (1-12).                                                                                                                                      | [optional] |
| **year**            | **int**                                                 | The four-digit current year (e.g., 2024).                                                                                                                                  | [optional] |
| **year_abbr**       | **str**                                                 | The two-digit abbreviation for the year (e.g., "24").                                                                                                                      | [optional] |
| **is_dst**          | **bool**                                                | Is the time zone in daylight savings?                                                                                                                                      | [optional] |
| **dst_savings**     | **int**                                                 | The amount of time added for daylight saving (in hours).                                                                                                                   | [optional] |
| **dst_exists**      | **bool**                                                | Indicates whether Daylight Saving Time (DST) is observed in the region. If `true`, the `dst_start` and `dst_end` objects will include detailed DST transition information. | [optional] |
| **dst_start**       | [**TimezoneDetailDstStart**](TimezoneDetailDstStart.md) | Timezone DST start details.                                                                                                                                                | [optional] |
| **dst_end**         | [**TimezoneDetailDstEnd**](TimezoneDetailDstEnd.md)     | Timezone DST end details.                                                                                                                                                  | [optional] |

## Example

```python
from ipgeolocation.models.timezone_detail import TimezoneDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneDetail from a JSON string
timezone_detail_instance = TimezoneDetail.from_json(json)
# print the JSON string representation of the object
print(TimezoneDetail.to_json())

# convert the object into a dict
timezone_detail_dict = timezone_detail_instance.to_dict()
# create an instance of TimezoneDetail from a dict
timezone_detail_from_dict = TimezoneDetail.from_dict(timezone_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


