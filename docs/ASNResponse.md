# ASNResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ip** | **str** | IP address for which ASN information is returned. Present if the &#39;ip&#39; query parameter is used or no IP is specified (defaults to requester&#39;s IP). | [optional] 
**asn** | [**ASNDetails**](ASNDetails.md) |  | [optional] 

## Example

```python
from ipgeolocation.models.asn_response import ASNResponse

# TODO update the JSON string below
json = "{}"
# create an instance of ASNResponse from a JSON string
asn_response_instance = ASNResponse.from_json(json)
# print the JSON string representation of the object
print(ASNResponse.to_json())

# convert the object into a dict
asn_response_dict = asn_response_instance.to_dict()
# create an instance of ASNResponse from a dict
asn_response_from_dict = ASNResponse.from_dict(asn_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


