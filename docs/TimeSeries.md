# TimeSeries


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_date** | **str** |  | [optional] 
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
**moon_phase** | **str** |  | [optional] 
**moonrise** | **str** |  | [optional] 
**moonset** | **str** |  | [optional] 
**moon_status** | **str** |  | [optional] 

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


