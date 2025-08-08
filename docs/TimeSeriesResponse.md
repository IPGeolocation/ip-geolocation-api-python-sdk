# TimeSeriesResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**location** | [**AstronomyLocation**](AstronomyLocation.md) |  | [optional] 
**astronomy** | [**List[TimeSeries]**](TimeSeries.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.time_series_response import TimeSeriesResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesResponse from a JSON string
time_series_response_instance = TimeSeriesResponse.from_json(json)
# print the JSON string representation of the object
print(TimeSeriesResponse.to_json())

# convert the object into a dict
time_series_response_dict = time_series_response_instance.to_dict()
# create an instance of TimeSeriesResponse from a dict
time_series_response_from_dict = TimeSeriesResponse.from_dict(time_series_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


