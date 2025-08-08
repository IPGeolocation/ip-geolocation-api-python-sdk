# TimezoneDetail


## Properties

| Name                | Type                                                    | Description | Notes      |
|---------------------|---------------------------------------------------------|-------------|------------|
| **name**            | **str**                                                 |             | [optional] |
| **offset**          | **int**                                                 |             | [optional] |
| **offset_with_dst** | **int**                                                 |             | [optional] |
| **date**            | **str**                                                 |             | [optional] |
| **date_time**       | **str**                                                 |             | [optional] |
| **date_time_txt**   | **str**                                                 |             | [optional] |
| **date_time_wti**   | **str**                                                 |             | [optional] |
| **date_time_ymd**   | **str**                                                 |             | [optional] |
| **date_time_unix**  | **float**                                               |             | [optional] |
| **time_24**         | **str**                                                 |             | [optional] |
| **time_12**         | **str**                                                 |             | [optional] |
| **week**            | **int**                                                 |             | [optional] |
| **month**           | **int**                                                 |             | [optional] |
| **year**            | **int**                                                 |             | [optional] |
| **year_abbr**       | **str**                                                 |             | [optional] |
| **is_dst**          | **bool**                                                |             | [optional] |
| **dst_savings**     | **int**                                                 |             | [optional] |
| **dst_exists**      | **bool**                                                |             | [optional] |
| **dst_start**       | [**TimezoneDetailDstStart**](TimezoneDetailDstStart.md) |             | [optional] |
| **dst_end**         | [**TimezoneDetailDstEnd**](TimezoneDetailDstEnd.md)     |             | [optional] |

## Example

```python
from ipgeolocation.models.timezone_detail import TimezoneDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TimezoneDetail from a JSON string
timezone_detail_instance = TimezoneDetail.from_json(json)
# print the JSON string representation of the object
print(TimezoneDetail.to_json())

# convert the object into a dict
timezone_detail_dict = timezone_detail_instance.to_dict()
# create an instance of TimezoneDetail from a dict
timezone_detail_from_dict = TimezoneDetail.from_dict(timezone_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


