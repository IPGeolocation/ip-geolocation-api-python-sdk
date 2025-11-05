# AstronomyMorning


## Properties

| Name                            | Type          | Description                                                                         | Notes        |
|---------------------------------|---------------|-------------------------------------------------------------------------------------|--------------|
| **astronomical_twilight_begin** | **str**       | Start of astronomical twilight (pre‑dawn) in the morning.                           | [optional]   |
| **astronomical_twilight_end**   | **str**       | End of astronomical twilight in the morning.                                        | [optional]   |
| **nautical_twilight_begin**     | **str**       | Start of nautical twilight (when the horizon first becomes visible) in the morning. | [optional]   |
| **nautical_twilight_end**       | **str**       | End of nautical twilight in the morning.                                            | [optional]   |
| **civil_twilight_begin**        | **str**       | Start of civil twilight (enough light for outdoor activities) in the morning.       | [optional]   |
| **civil_twilight_end**          | **str**       | End of civil twilight in the morning.                                               | [optional]   |
| **blue_hour_begin**             | **str**       | Start of blue hour (soft, diffused light) before sunrise.                           | [optional]   |
| **blue_hour_end**               | **str**       | End of blue hour before sunrise.                                                    | [optional]   |
| **golden_hour_begin**           | **str**       | Start of golden hour (warm, low‑angle light) before sunrise.                        | [optional]   |
| **golden_hour_end**             | **str**       | End of golden hour before sunrise.                                                  | [optional]   |

## Example

```python
from ipgeolocation.models.astronomy_morning import AstronomyMorning

# TODO update the JSON string below
json = "{}"
# create an instance of AstronomyMorning from a JSON string
astronomy_morning_instance = AstronomyMorning.from_json(json)
# print the JSON string representation of the object
print(AstronomyMorning.to_json())

# convert the object into a dict
astronomy_morning_dict = astronomy_morning_instance.to_dict()
# create an instance of AstronomyMorning from a dict
astronomy_morning_from_dict = AstronomyMorning.from_dict(astronomy_morning_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


