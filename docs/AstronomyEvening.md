# AstronomyEvening


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**golden_hour_begin** | **str** |  | [optional] 
**golden_hour_end** | **str** |  | [optional] 
**blue_hour_begin** | **str** |  | [optional] 
**blue_hour_end** | **str** |  | [optional] 
**civil_twilight_begin** | **str** |  | [optional] 
**civil_twilight_end** | **str** |  | [optional] 
**nautical_twilight_begin** | **str** |  | [optional] 
**nautical_twilight_end** | **str** |  | [optional] 
**astronomical_twilight_begin** | **str** |  | [optional] 
**astronomical_twilight_end** | **str** |  | [optional] 

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


