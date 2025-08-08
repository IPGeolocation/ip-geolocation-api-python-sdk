# AstronomyResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** |  | [optional] 
**location** | [**AstronomyLocation**](AstronomyLocation.md) |  | [optional] 
**astronomy** | [**Astronomy**](Astronomy.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.astronomy_response import AstronomyResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AstronomyResponse from a JSON string
astronomy_response_instance = AstronomyResponse.from_json(json)
# print the JSON string representation of the object
print(AstronomyResponse.to_json())

# convert the object into a dict
astronomy_response_dict = astronomy_response_instance.to_dict()
# create an instance of AstronomyResponse from a dict
astronomy_response_from_dict = AstronomyResponse.from_dict(astronomy_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


