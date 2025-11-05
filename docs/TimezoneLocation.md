# TimezoneLocation


## Properties

| Name                      | Type     | Description                                                               | Notes      |
|---------------------------|----------|---------------------------------------------------------------------------|------------|
| **location_string**       | **str**  | The provided location parameter as `location`.                            | [optional] | 
| **continent_code**        | **str**  | The two-letter code of the continent (e.g., "NA").                        | [optional] | 
| **continent_name**        | **str**  | The full name of the continent (e.g., "North America").                   | [optional] | 
| **country_code2**         | **str**  | The ISO 3166-1 alpha-2 two-letter country code (e.g., "US").              | [optional] | 
| **country_code3**         | **str**  | The ISO 3166-1 alpha-3 three-letter country code (e.g., "USA").           | [optional] | 
| **country_name**          | **str**  | The common name of the country (e.g., "United States").                   | [optional] | 
| **country_name_official** | **str**  | The official full name of the country (e.g., "United States of America"). | [optional] | 
| **is_eu**                 | **bool** | Is the country belong to European Union?                                  | [optional] | 
| **state_prov**            | **str**  | Name of the state/province/region.                                        | [optional] | 
| **state_code**            | **str**  | Code of the state/province/region.                                        | [optional] | 
| **district**              | **str**  | Name of the district or county.                                           | [optional] | 
| **city**                  | **str**  | Name of the city.                                                         | [optional] | 
| **locality**              | **str**  | Smaller area, part or region of a city.                                   | [optional] | 
| **zipcode**               | **str**  | ZIP/Postal code of the place.                                             | [optional] | 
| **latitude**              | **str**  | The geographic latitude of the location.                                  | [optional] | 
| **longitude**             | **str**  | The geographic longitude of the location.                                 | [optional] | 

## Example

```python
from ipgeolocation.models.timezone_location import TimezoneLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneLocation from a JSON string
timezone_location_instance = TimezoneLocation.from_json(json)
# print the JSON string representation of the object
print(TimezoneLocation.to_json())

# convert the object into a dict
timezone_location_dict = timezone_location_instance.to_dict()
# create an instance of TimezoneLocation from a dict
timezone_location_from_dict = TimezoneLocation.from_dict(timezone_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


