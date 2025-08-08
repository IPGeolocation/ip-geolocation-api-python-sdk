# TimezoneLocode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**lo_code** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**state_code** | **str** |  | [optional] 
**country_code** | **str** |  | [optional] 
**country_name** | **str** |  | [optional] 
**location_type** | **str** |  | [optional] 
**latitude** | **str** |  | [optional] 
**longitude** | **str** |  | [optional] 

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


