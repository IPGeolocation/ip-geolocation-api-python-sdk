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
from typing import Optional, Set
from typing_extensions import Self

class TimezoneLocode(BaseModel):
    """
    TimezoneLocode
    """ # noqa: E501
    lo_code: Optional[StrictStr] = None
    city: Optional[StrictStr] = None
    state_code: Optional[StrictStr] = None
    country_code: Optional[StrictStr] = None
    country_name: Optional[StrictStr] = None
    location_type: Optional[StrictStr] = None
    latitude: Optional[StrictStr] = None
    longitude: Optional[StrictStr] = None
    __properties: ClassVar[List[str]] = ["lo_code", "city", "state_code", "country_code", "country_name", "location_type", "latitude", "longitude"]

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
        """Create an instance of TimezoneLocode from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TimezoneLocode from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lo_code": obj.get("lo_code"),
            "city": obj.get("city"),
            "state_code": obj.get("state_code"),
            "country_code": obj.get("country_code"),
            "country_name": obj.get("country_name"),
            "location_type": obj.get("location_type"),
            "latitude": obj.get("latitude"),
            "longitude": obj.get("longitude")
        })
        return _obj


