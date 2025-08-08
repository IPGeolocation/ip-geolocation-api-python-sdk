# Astronomy


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**time_zone** | **str** |  | [optional] 
**date**  | **str** |  | [optional] 
**current_time** | **str** |  | [optional] 
**mid_night** | **str** |  | [optional] 
**night_end** | **str** |  | [optional] 
**morning** | [**AstronomyMorning**](AstronomyMorning.md) |  | [optional] 
**sunrise** | **str** |  | [optional] 
**sunset** | **str** |  | [optional] 
**evening** | [**AstronomyEvening**](AstronomyEvening.md) |  | [optional] 
**night_begin** | **str** |  | [optional] 
**sun_status** | **str** |  | [optional] 
**solar_noon** | **str** |  | [optional] 
**day_length** | **str** |  | [optional] 
**sun_altitude** | **float** |  | [optional] 
**sun_distance** | **float** |  | [optional] 
**sun_azimuth** | **float** |  | [optional] 
**moon_phase** | **str** |  | [optional] 
**moonrise** | **str** |  | [optional] 
**moonset** | **str** |  | [optional] 
**moon_status** | **str** |  | [optional] 
**moon_altitude** | **float** |  | [optional] 
**moon_distance** | **float** |  | [optional] 
**moon_azimuth** | **float** |  | [optional] 
**moon_parallactic_angle** | **float** |  | [optional] 
**moon_illumination_percentage** | **str** |  | [optional] 
**moon_angle** | **float** |  | [optional] 

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


