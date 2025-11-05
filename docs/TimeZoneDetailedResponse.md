# TimeZoneDetailedResponse


## Properties

| Name                | Type                                        | Description                                                                                                         | Notes      |
|---------------------|---------------------------------------------|---------------------------------------------------------------------------------------------------------------------|------------|
| **ip**              | **str**                                     | The IP address used for the timezone lookup. Returned when queried using the `ip=` parameter or with no parameters. | [optional] | 
| **airport_details** | [**TimezoneAirport**](TimezoneAirport.md)   | Airport details object.                                                                                             | [optional] | 
| **lo_code_details** | [**TimezoneLocode**](TimezoneLocode.md)     | UN/LOCODE details object.                                                                                           | [optional] | 
| **location**        | [**TimezoneLocation**](TimezoneLocation.md) | Location object.                                                                                                    | [optional] | 
| **time_zone**       | [**TimezoneDetail**](TimezoneDetail.md)     | Timezone object.                                                                                                    | [optional] | 

## Example

```python
from ipgeolocation.models.time_zone_detailed_response import TimeZoneDetailedResponse

# TODO update the JSON string below
json = "{}"
# create an instance of TimeZoneDetailedResponse from a JSON string
time_zone_detailed_response_instance = TimeZoneDetailedResponse.from_json(json)
# print the JSON string representation of the object
print(TimeZoneDetailedResponse.to_json())

# convert the object into a dict
time_zone_detailed_response_dict = time_zone_detailed_response_instance.to_dict()
# create an instance of TimeZoneDetailedResponse from a dict
time_zone_detailed_response_from_dict = TimeZoneDetailedResponse.from_dict(time_zone_detailed_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


