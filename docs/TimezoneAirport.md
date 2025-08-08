# TimezoneAirport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 
**elevation_ft** | **int** |  | [optional] 
**continent_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**iata_code** | **str** |  | [optional] 
**icao_code** | **str** |  | [optional] 
**faa_code** | **str** |  | [optional] 

## Example

```python
from ipgeolocation.models.timezone_airport import TimezoneAirport

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneAirport from a JSON string
timezone_airport_instance = TimezoneAirport.from_json(json)
# print the JSON string representation of the object
print(TimezoneAirport.to_json())

# convert the object into a dict
timezone_airport_dict = timezone_airport_instance.to_dict()
# create an instance of TimezoneAirport from a dict
timezone_airport_from_dict = TimezoneAirport.from_dict(timezone_airport_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


