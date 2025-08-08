# TimeConversionResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**original_time** | **str** |  | [optional] 
**converted_time** | **str** |  | [optional] 
**diff_hour** | **float** |  | [optional] 
**diff_min** | **int** |  | [optional] 

## Example

```python
from ipgeolocation.models.time_conversion_response import TimeConversionResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeConversionResponse from a JSON string
time_conversion_response_instance = TimeConversionResponse.from_json(json)
# print the JSON string representation of the object
print(TimeConversionResponse.to_json())

# convert the object into a dict
time_conversion_response_dict = time_conversion_response_instance.to_dict()
# create an instance of TimeConversionResponse from a dict
time_conversion_response_from_dict = TimeConversionResponse.from_dict(time_conversion_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


