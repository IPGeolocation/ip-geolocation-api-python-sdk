# TimeSeriesXmlResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**location** | [**AstronomyLocation**](AstronomyLocation.md) |  | [optional] 
**astronomy** | [**List[TimeSeries]**](TimeSeries.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.time_series_xml_response import TimeSeriesXmlResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeSeriesXmlResponse from a JSON string
time_series_xml_response_instance = TimeSeriesXmlResponse.from_json(json)
# print the JSON string representation of the object
print(TimeSeriesXmlResponse.to_json())

# convert the object into a dict
time_series_xml_response_dict = time_series_xml_response_instance.to_dict()
# create an instance of TimeSeriesXmlResponse from a dict
time_series_xml_response_from_dict = TimeSeriesXmlResponse.from_dict(time_series_xml_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


