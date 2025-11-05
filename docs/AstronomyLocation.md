# AstronomyLocation


## Properties

| Name                      | Type         | Description                                           | Notes       |
|---------------------------|--------------|-------------------------------------------------------|-------------|
| **location_string**       | **str**      | Location is the string, you provided for searching    | [optional]  |
| **continent_code**        | **str**      | 2-letter code of the continent.                       | [optional]  |
| **continent_name**        | **str**      | Name of the continent.                                | [optional]  |
| **country_code2**         | **str**      | Country code (ISO 3166-1 alpha-2) of the country.     | [optional]  |
| **country_code3**         | **str**      | Country code (ISO 3166-1 alpha-3) of the country.     | [optional]  |
| **country_name**          | **str**      | Name of the country.                                  | [optional]  |
| **country_name_official** | **str**      | Formal name of the country.                           | [optional]  |
| **is_eu**                 | **bool**     | Is the country belong to European Union?              | [optional]  |
| **state_prov**            | **str**      | Name of the state/province/region.                    | [optional]  |
| **state_code**            | **str**      | Code of the state/province/region.                    | [optional]  |
| **district**              | **str**      | Name of the district or county.                       | [optional]  |
| **city**                  | **str**      | Name of the city.                                     | [optional]  |
| **locality**              | **str**      | Smaller area, part or region of a city.               | [optional]  |
| **zipcode**               | **str**      | ZIP/Postal code of the place.                         | [optional]  |
| **latitude**              | **str**      | Latitude of the place.                                | [optional]  |
| **longitude**             | **str**      | Longitude of the place.                               | [optional]  |
| **elevation**             | **str**      | Elevation above sea level at the location, in meters. | [optional]  |

## Example

```python
from ipgeolocation.models.astronomy_location import AstronomyLocation

# TODO update the JSON string below
json = "{}"
# create an instance of AstronomyLocation from a JSON string
astronomy_location_instance = AstronomyLocation.from_json(json)
# print the JSON string representation of the object
print(AstronomyLocation.to_json())

# convert the object into a dict
astronomy_location_dict = astronomy_location_instance.to_dict()
# create an instance of AstronomyLocation from a dict
astronomy_location_from_dict = AstronomyLocation.from_dict(astronomy_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


