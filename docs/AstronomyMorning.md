# AstronomyMorning


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**astronomical_twilight_begin** | **str** |  | [optional] 
**astronomical_twilight_end** | **str** |  | [optional] 
**nautical_twilight_begin** | **str** |  | [optional] 
**nautical_twilight_end** | **str** |  | [optional] 
**civil_twilight_begin** | **str** |  | [optional] 
**civil_twilight_end** | **str** |  | [optional] 
**blue_hour_begin** | **str** |  | [optional] 
**blue_hour_end** | **str** |  | [optional] 
**golden_hour_begin** | **str** |  | [optional] 
**golden_hour_end** | **str** |  | [optional] 

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


