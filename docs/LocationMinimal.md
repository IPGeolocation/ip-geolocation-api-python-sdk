# LocationMinimal


## Properties

| Name                      | Type     | Description                                       | Notes       |
|---------------------------|----------|---------------------------------------------------|-------------|
| **continent_code**        | **str**  | 2-letter code of the continent.                   | [optional]  |
| **continent_name**        | **str**  | Name of the continent.                            | [optional]  |
| **country_code2**         | **str**  | Country code (ISO 3166-1 alpha-2) of the country. | [optional]  |
| **country_code3**         | **str**  | Country code (ISO 3166-1 alpha-3) of the country. | [optional]  |
| **country_name**          | **str**  | Name of the country.                              | [optional]  |
| **country_name_official** | **str**  | Official name (ISO 3166) of the country.          | [optional]  |
| **country_capital**       | **str**  | Name of the country’s capital.                    | [optional]  |
| **state_prov**            | **str**  | Name of the state/province/region.                | [optional]  |
| **state_code**            | **str**  | Code of the state/province/region.                | [optional]  |
| **district**              | **str**  | Name of the district or county.                   | [optional]  |
| **city**                  | **str**  | Name of the city.                                 | [optional]  |
| **zipcode**               | **str**  | ZIP/Postal code of the place.                     | [optional]  |
| **latitude**              | **str**  | Latitude of the place.                            | [optional]  |
| **longitude**             | **str**  | Longitude of the place.                           | [optional]  |
| **is_eu**                 | **bool** | Is the country belong to European Union?          | [optional]  |
| **country_flag**          | **str**  | URL to get the country flag.                      | [optional]  |
| **geoname_id**            | **str**  | Geoname ID of the place from geonames.org         | [optional]  |
| **country_emoji**         | **str**  | Emoji of the Country flag.                        | [optional]  |

## Example

```python
from ipgeolocation.models.location_minimal import LocationMinimal

# TODO update the JSON string below
json = "{}"
# create an instance of LocationMinimal from a JSON string
location_minimal_instance = LocationMinimal.from_json(json)
# print the JSON string representation of the object
print(LocationMinimal.to_json())

# convert the object into a dict
location_minimal_dict = location_minimal_instance.to_dict()
# create an instance of LocationMinimal from a dict
location_minimal_from_dict = LocationMinimal.from_dict(location_minimal_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


