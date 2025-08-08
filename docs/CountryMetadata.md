# CountryMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calling_code** | **str** |  | [optional] 
**tld** | **str** |  | [optional] 
**languages** | **List[str]** |  | [optional] 

## Example

```python
from ipgeolocation.models.country_metadata import CountryMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of CountryMetadata from a JSON string
country_metadata_instance = CountryMetadata.from_json(json)
# print the JSON string representation of the object
print(CountryMetadata.to_json())

# convert the object into a dict
country_metadata_dict = country_metadata_instance.to_dict()
# create an instance of CountryMetadata from a dict
country_metadata_from_dict = CountryMetadata.from_dict(country_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


