# LocationMinimal


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


