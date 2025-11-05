# Astronomy


## Properties

| Name                             | Type                                        | Description                                                                                                                | Notes      |
|----------------------------------|---------------------------------------------|----------------------------------------------------------------------------------------------------------------------------|------------|
| **time_zone**                    | **str**                                     | Appears (with the provided value) only when the user includes a `time_zone` in the query to specify which time to observe. | [optional] |
| **date**                         | **str**                                     | Provided or current date in the format `yyyy-MM-dd`.                                                                       | [optional] |
| **current_time**                 | **str**                                     | Current time of the extracted location in the format `HH:mm:ss.SSS`.                                                       | [optional] |
| **mid_night**                    | **str**                                     | Astronomical midnight (nadir) for the given date.                                                                          | [optional] |
| **night_end**                    | **str**                                     | End of night / start of astronomical twilight (morning).                                                                   | [optional] |
| **night_begin**                  | **str**                                     | Start of night / end of astronomical twilight (evening).                                                                   | [optional] |
| **morning**                      | [**AstronomyMorning**](AstronomyMorning.md) | It has the astronomical twilight period times in the morning.                                                              | [optional] |
| **sunrise**                      | **str**                                     | Time at which sun rises at the extracted location in the format `HH:mm`.                                                   | [optional] |
| **sunset**                       | **str**                                     | Time at which sun sets at the extracted location in the format `HH:mm`.                                                    | [optional] |
| **evening**                      | [**AstronomyEvening**](AstronomyEvening.md) | It has the astronomical twilight period times in the evening.                                                              | [optional] |
| **sun_status**                   | **str**                                     | Represents the sun rise and sun set status.                                                                                | [optional] |
| **solar_noon**                   | **str**                                     | The time of day when the sun is at its highest point in the sky, in the format `HH:mm`.                                    | [optional] |
| **day_length**                   | **str**                                     | The total length of daylight for the current day in format `HH:mm`, representing the time from sunrise to sunset.          | [optional] |
| **sun_altitude**                 | **float**                                   | The sun's altitude angle above the horizon at `current_time`, measured in degrees.                                         | [optional] |
| **sun_distance**                 | **float**                                   | The distance from Earth to the sun at `current_time`, in kilometers.                                                       | [optional] |
| **sun_azimuth**                  | **float**                                   | The azimuth angle of the sun at `current_time`, indicating its compass direction in degrees.                               | [optional] |
| **moon_phase**                   | **str**                                     | The current phase of the moon (e.g., `WAXING_CRESCENT`), indicating its position in the lunar cycle.                       | [optional] |
| **moonrise**                     | **str**                                     | Time at which moon rises at the extracted location in the format `HH:mm`.                                                  | [optional] |
| **moonset**                      | **str**                                     | Time at which moon sets at the extracted location in the format `HH:mm`.                                                   | [optional] |
| **moon_status**                  | **str**                                     | Represents the moon rise and moon set status.                                                                              | [optional] |
| **moon_altitude**                | **float**                                   | The moon's altitude angle above the horizon at `current_time`, measured in degrees.                                        | [optional] |
| **moon_distance**                | **float**                                   | The distance from Earth to the moon at `current_time`, in kilometers.                                                      | [optional] |
| **moon_azimuth**                 | **float**                                   | The azimuth angle of the moon at `current_time`, indicating its compass direction in degrees.                              | [optional] |
| **moon_parallactic_angle**       | **float**                                   | The angle between the celestial pole and the moon's position relative to the location, measured in degrees.                | [optional] |
| **moon_illumination_percentage** | **str**                                     | The percentage of the moon's surface that is illuminated by sunlight, as viewed from Earth.                                | [optional] |
| **moon_angle**                   | **float**                                   | The angular diameter of the moon as observed from Earth, measured in degrees.                                              | [optional] |

## Example

```python
from ipgeolocation.models.astronomy import Astronomy

# TODO update the JSON string below
json = "{}"
# create an instance of Astronomy from a JSON string
astronomy_instance = Astronomy.from_json(json)
# print the JSON string representation of the object
print(Astronomy.to_json())

# convert the object into a dict
astronomy_dict = astronomy_instance.to_dict()
# create an instance of Astronomy from a dict
astronomy_from_dict = Astronomy.from_dict(astronomy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


