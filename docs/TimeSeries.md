# TimeSeries


## Properties

| Name            | Type                                        | Description                                                                                                       | Notes      |
|-----------------|---------------------------------------------|-------------------------------------------------------------------------------------------------------------------|------------|
| **var_date**    | **str**                                     | Provided or current date in the format `yyyy-MM-dd`.                                                              | [optional] |
| **mid_night**   | **str**                                     | Astronomical midnight (nadir) for the given date.                                                                 | [optional] |
| **night_end**   | **str**                                     | End of night / start of astronomical twilight (morning).                                                          | [optional] |
| **morning**     | [**AstronomyMorning**](AstronomyMorning.md) | It has the astronomical twilight period times in the morning.                                                     | [optional] | 
| **sunrise**     | **str**                                     | Time at which sun rises at the extracted location in the format `HH:mm`.                                          | [optional] |
| **sunset**      | **str**                                     | Time at which sun sets at the extracted location in the format `HH:mm`.                                           | [optional] |
| **evening**     | [**AstronomyEvening**](AstronomyEvening.md) | It has the astronomical twilight period times in the evening.                                                     | [optional] | 
| **night_begin** | **str**                                     | Start of night / end of astronomical twilight (evening).                                                          | [optional] |
| **sun_status**  | **str**                                     | Represents the sun rise and sun set status.                                                                       | [optional] |
| **solar_noon**  | **str**                                     | The time of day when the sun is at its highest point in the sky, in the format `HH:mm`.                           | [optional] |
| **day_length**  | **str**                                     | The total length of daylight for the current day in format `HH:mm`, representing the time from sunrise to sunset. | [optional] |
| **moon_phase**  | **str**                                     | The current phase of the moon (e.g., `WAXING_CRESCENT`), indicating its position in the lunar cycle.              | [optional] |
| **moonrise**    | **str**                                     | Time at which moon rises at the extracted location in the format `HH:mm`.                                         | [optional] |
| **moonset**     | **str**                                     | Time at which moon sets at the extracted location in the format `HH:mm`.                                          | [optional] |
| **moon_status** | **str**                                     | Represents the moon rise and moon set status.                                                                     | [optional] |

## Example

```python
from ipgeolocation.models.time_series import TimeSeries

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeries from a JSON string
time_series_instance = TimeSeries.from_json(json)
# print the JSON string representation of the object
print(TimeSeries.to_json())

# convert the object into a dict
time_series_dict = time_series_instance.to_dict()
# create an instance of TimeSeries from a dict
time_series_from_dict = TimeSeries.from_dict(time_series_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


