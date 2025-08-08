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

from pydantic import BaseModel, ConfigDict, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ipgeolocation.models.timezone_airport import TimezoneAirport
from ipgeolocation.models.timezone_detail import TimezoneDetail
from ipgeolocation.models.timezone_location import TimezoneLocation
from ipgeolocation.models.timezone_locode import TimezoneLocode
from typing import Optional, Set
from typing_extensions import Self

class TimeZoneDetailedXMLResponse(BaseModel):
    """
    TimeZoneDetailedXMLResponse
    """ # noqa: E501
    ip: Optional[StrictStr] = None
    airport_details: Optional[TimezoneAirport] = None
    lo_code_details: Optional[TimezoneLocode] = None
    location: Optional[TimezoneLocation] = None
    time_zone: Optional[TimezoneDetail] = None
    __properties: ClassVar[List[str]] = ["ip", "airport_details", "lo_code_details", "location", "time_zone"]

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
        """Create an instance of TimeZoneDetailedXMLResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of airport_details
        if self.airport_details:
            _dict['airport_details'] = self.airport_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of lo_code_details
        if self.lo_code_details:
            _dict['lo_code_details'] = self.lo_code_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_zone
        if self.time_zone:
            _dict['time_zone'] = self.time_zone.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimeZoneDetailedXMLResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ip": obj.get("ip"),
            "airport_details": TimezoneAirport.from_dict(obj["airport_details"]) if obj.get("airport_details") is not None else None,
            "lo_code_details": TimezoneLocode.from_dict(obj["lo_code_details"]) if obj.get("lo_code_details") is not None else None,
            "location": TimezoneLocation.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "time_zone": TimezoneDetail.from_dict(obj["time_zone"]) if obj.get("time_zone") is not None else None
        })
        return _obj


