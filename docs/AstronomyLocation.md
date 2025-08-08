# AstronomyLocation


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
**elevation** | **str** |  | [optional] 

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


