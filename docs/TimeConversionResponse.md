# TimeConversionResponse


## Properties

| Name               | Type      | Description                                                                                                                    | Notes      |
|--------------------|-----------|--------------------------------------------------------------------------------------------------------------------------------|------------|
| **original_time**  | **str**   | The original date and time before any conversion, presented in the format 'yyyy-MM-dd HH:mm:ss' (e.g., "2024-03-11 14:47:32"). | [optional] |
| **converted_time** | **str**   | The date and time after conversion, in the format 'yyyy-MM-dd HH:mm:ss' (e.g., "2024-03-11 02:47:32").                         | [optional] |
| **diff_hour**      | **float** | The difference in hours between the `original_time` and the `converted_time`.                                                  | [optional] |
| **diff_min**       | **int**   | The difference in minutes between the `original_time` and the `converted_time`.                                                | [optional] |

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


