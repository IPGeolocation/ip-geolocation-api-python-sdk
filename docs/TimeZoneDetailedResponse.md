# TimeZoneDetailedResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**airport_details** | [**TimezoneAirport**](TimezoneAirport.md) |  | [optional] 
**lo_code_details** | [**TimezoneLocode**](TimezoneLocode.md) |  | [optional] 
**location** | [**TimezoneLocation**](TimezoneLocation.md) |  | [optional] 
**time_zone** | [**TimezoneDetail**](TimezoneDetail.md) |  | [optional] 

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


