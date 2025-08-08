# TimezoneLocation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**location_string** | **str** |  | [optional] 
**continent_code** | **str** |  | [optional] 
**continent_name** | **str** |  | [optional] 
**country_code2** | **str** |  | [optional] 
**country_code3** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**country_name_official** | **str** |  | [optional] 
**is_eu** | **bool** |  | [optional] 
**state_prov** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**locality** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 

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


