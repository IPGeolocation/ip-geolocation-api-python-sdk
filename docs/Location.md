# Location


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**continent_code** | **str** |  | [optional] 
**continent_name** | **str** |  | [optional] 
**country_code2** | **str** |  | [optional] 
**country_code3** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**country_name_official** | **str** |  | [optional] 
**country_capital** | **str** |  | [optional] 
**state_prov** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**district** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**zipcode** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 
**is_eu** | **bool** |  | [optional] 
**country_flag** | **str** |  | [optional] 
**geoname_id** | **str** |  | [optional] 
**country_emoji** | **str** |  | [optional] 
**accuracy_radius** | **str** |  | [optional] 
**locality** | **str** |  | [optional] 
**dma_code** | **str** |  | [optional] 

## Example

```python
from ipgeolocation.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


