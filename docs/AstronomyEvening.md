# AstronomyEvening


## Properties

| Name                            | Type          | Description                                                                   | Notes        |
|---------------------------------|---------------|-------------------------------------------------------------------------------|--------------|
| **golden_hour_begin**           | **str**       | Start of golden hour (warm, low‑angle light) after sunset.                    | [optional]   |
| **golden_hour_end**             | **str**       | End of golden hour after sunset.                                              | [optional]   |
| **blue_hour_begin**             | **str**       | Start of blue hour (soft, diffused light) after sunset.                       | [optional]   |
| **blue_hour_end**               | **str**       | End of blue hour after sunset.                                                | [optional]   |
| **civil_twilight_begin**        | **str**       | Start of civil twilight (enough light for outdoor activities) in the evening. | [optional]   |
| **civil_twilight_end**          | **str**       | End of civil twilight in the evening.                                         | [optional]   |
| **nautical_twilight_begin**     | **str**       | Start of nautical twilight (horizon still visible) in the evening.            | [optional]   |
| **nautical_twilight_end**       | **str**       | End of nautical twilight in the evening.                                      | [optional]   |
| **astronomical_twilight_begin** | **str**       | Start of astronomical twilight (night sky begins) in the evening.             | [optional]   |
| **astronomical_twilight_end**   | **str**       | End of astronomical twilight in the evening.                                  | [optional]   |

## Example

```python
from ipgeolocation.models.astronomy_evening import AstronomyEvening

# TODO update the JSON string below
json = "{}"
# create an instance of AstronomyEvening from a JSON string
astronomy_evening_instance = AstronomyEvening.from_json(json)
# print the JSON string representation of the object
print(AstronomyEvening.to_json())

# convert the object into a dict
astronomy_evening_dict = astronomy_evening_instance.to_dict()
# create an instance of AstronomyEvening from a dict
astronomy_evening_from_dict = AstronomyEvening.from_dict(astronomy_evening_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


