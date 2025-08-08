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
from ipgeolocation.models.user_agent_data_device import UserAgentDataDevice
from ipgeolocation.models.user_agent_data_engine import UserAgentDataEngine
from ipgeolocation.models.user_agent_data_operating_system import UserAgentDataOperatingSystem
from typing import Optional, Set
from typing_extensions import Self

class UserAgentXMLDataArray(BaseModel):
    """
    UserAgentXMLDataArray
    """ # noqa: E501
    user_agent_string: Optional[StrictStr] = None
    name: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    version: Optional[StrictStr] = None
    version_major: Optional[StrictStr] = None
    device: Optional[UserAgentDataDevice] = None
    engine: Optional[UserAgentDataEngine] = None
    operating_system: Optional[UserAgentDataOperatingSystem] = None
    __properties: ClassVar[List[str]] = ["user_agent_string", "name", "type", "version", "version_major", "device", "engine", "operating_system"]

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
        """Create an instance of UserAgentXMLDataArray from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of device
        if self.device:
            _dict['device'] = self.device.to_dict()
        # override the default output from pydantic by calling `to_dict()` of engine
        if self.engine:
            _dict['engine'] = self.engine.to_dict()
        # override the default output from pydantic by calling `to_dict()` of operating_system
        if self.operating_system:
            _dict['operating_system'] = self.operating_system.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of UserAgentXMLDataArray from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "user_agent_string": obj.get("user_agent_string"),
            "name": obj.get("name"),
            "type": obj.get("type"),
            "version": obj.get("version"),
            "version_major": obj.get("version_major"),
            "device": UserAgentDataDevice.from_dict(obj["device"]) if obj.get("device") is not None else None,
            "engine": UserAgentDataEngine.from_dict(obj["engine"]) if obj.get("engine") is not None else None,
            "operating_system": UserAgentDataOperatingSystem.from_dict(obj["operating_system"]) if obj.get("operating_system") is not None else None
        })
        return _obj


