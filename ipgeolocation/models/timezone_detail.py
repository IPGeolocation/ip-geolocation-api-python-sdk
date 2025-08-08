# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ipgeolocation.models.timezone_detail_dst_end import TimezoneDetailDstEnd
from ipgeolocation.models.timezone_detail_dst_start import TimezoneDetailDstStart
from typing import Optional, Set
from typing_extensions import Self

class TimezoneDetail(BaseModel):
    """
    TimezoneDetail
    """ # noqa: E501
    name: Optional[StrictStr] = None
    offset: Optional[StrictInt] = None
    offset_with_dst: Optional[StrictInt] = None
    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    date_time: Optional[StrictStr] = None
    date_time_txt: Optional[StrictStr] = None
    date_time_wti: Optional[StrictStr] = None
    date_time_ymd: Optional[StrictStr] = None
    date_time_unix: Optional[Union[StrictFloat, StrictInt]] = None
    time_24: Optional[StrictStr] = None
    time_12: Optional[StrictStr] = None
    week: Optional[StrictInt] = None
    month: Optional[StrictInt] = None
    year: Optional[StrictInt] = None
    year_abbr: Optional[StrictStr] = None
    is_dst: Optional[StrictBool] = None
    dst_savings: Optional[StrictInt] = None
    dst_exists: Optional[StrictBool] = None
    dst_start: Optional[TimezoneDetailDstStart] = None
    dst_end: Optional[TimezoneDetailDstEnd] = None
    __properties: ClassVar[List[str]] = ["name", "offset", "offset_with_dst", "date", "date_time", "date_time_txt", "date_time_wti", "date_time_ymd", "date_time_unix", "time_24", "time_12", "week", "month", "year", "year_abbr", "is_dst", "dst_savings", "dst_exists", "dst_start", "dst_end"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of TimezoneDetail from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of dst_start
        if self.dst_start:
            _dict['dst_start'] = self.dst_start.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dst_end
        if self.dst_end:
            _dict['dst_end'] = self.dst_end.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimezoneDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "name": obj.get("name"),
            "offset": obj.get("offset"),
            "offset_with_dst": obj.get("offset_with_dst"),
            "date": obj.get("date"),
            "date_time": obj.get("date_time"),
            "date_time_txt": obj.get("date_time_txt"),
            "date_time_wti": obj.get("date_time_wti"),
            "date_time_ymd": obj.get("date_time_ymd"),
            "date_time_unix": obj.get("date_time_unix"),
            "time_24": obj.get("time_24"),
            "time_12": obj.get("time_12"),
            "week": obj.get("week"),
            "month": obj.get("month"),
            "year": obj.get("year"),
            "year_abbr": obj.get("year_abbr"),
            "is_dst": obj.get("is_dst"),
            "dst_savings": obj.get("dst_savings"),
            "dst_exists": obj.get("dst_exists"),
            "dst_start": TimezoneDetailDstStart.from_dict(obj["dst_start"]) if obj.get("dst_start") is not None else None,
            "dst_end": TimezoneDetailDstEnd.from_dict(obj["dst_end"]) if obj.get("dst_end") is not None else None
        })
        return _obj


