# TimezoneAirport


## Properties

| Name               | Type    | Description                                                                                       | Notes      |
|--------------------|---------|---------------------------------------------------------------------------------------------------|------------|
| **type**           | **str** | Classification of the airport based on size and traffic.                                          | [optional] | 
| **name**           | **str** | The full name of the airport.                                                                     | [optional] | 
| **latitude**       | **str** | The latitude coordinate of the airport.                                                           | [optional] | 
| **longitude**      | **str** | The longitude coordinate of the airport.                                                          | [optional] | 
| **elevation_ft**   | **int** | The elevation of the airport above sea level, measured in feet.                                   | [optional] | 
| **continent_code** | **str** | The two-letter code of the continent.                                                             | [optional] | 
| **country_code**   | **str** | The ISO 3166-1 alpha-2 code for the country where the airport is located.                         | [optional] | 
| **state_code**     | **str** | Code of the state/province/region where the airport is located.                                   | [optional] | 
| **city**           | **str** | The city or administrative region that the airport serves.                                        | [optional] | 
| **iata_code**      | **str** | The three-letter IATA airport code (e.g., "LHR").                                                 | [optional] | 
| **icao_code**      | **str** | The four-letter ICAO airport code (e.g., "EGLL").                                                 | [optional] | 
| **faa_code**       | **str** | The FAA location identifier, used primarily in the United States. May be empty if not applicable. | [optional] | 

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


