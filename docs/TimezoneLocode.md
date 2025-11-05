# TimezoneLocode


## Properties

| Name              | Type    | Description                                                                                                         | Notes      |
|-------------------|---------|---------------------------------------------------------------------------------------------------------------------|------------|
| **lo_code**       | **str** | A unique identifier for the location, often used in logistics and shipping (e.g., "USNYC").                         | [optional] | 
| **city**          | **str** | The name of the city or location associated with the `lo_code`.                                                     | [optional] | 
| **state_code**    | **str** | The code for the state, province or region.                                                                         | [optional] | 
| **country_code**  | **str** | The ISO 3166-1 alpha-2 country code (e.g., "US").                                                                   | [optional] | 
| **country_name**  | **str** | The name of the country in an administrative context.                                                               | [optional] | 
| **location_type** | **str** | The type of the location as comma separated list of facilities (e.g., Port, Rail Terminal, Road Terminal, Airport). | [optional] | 
| **latitude**      | **str** | The latitude coordinate of the location.                                                                            | [optional] | 
| **longitude**     | **str** | The longitude coordinate of the location.                                                                           | [optional] | 

## Example

```python
from ipgeolocation.models.timezone_locode import TimezoneLocode

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneLocode from a JSON string
timezone_locode_instance = TimezoneLocode.from_json(json)
# print the JSON string representation of the object
print(TimezoneLocode.to_json())

# convert the object into a dict
timezone_locode_dict = timezone_locode_instance.to_dict()
# create an instance of TimezoneLocode from a dict
timezone_locode_from_dict = TimezoneLocode.from_dict(timezone_locode_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


