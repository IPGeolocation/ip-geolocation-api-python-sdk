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
from ipgeolocation.models.country_metadata import CountryMetadata
from ipgeolocation.models.currency import Currency
from ipgeolocation.models.location_minimal import LocationMinimal
from ipgeolocation.models.network_minimal import NetworkMinimal
from ipgeolocation.models.security import Security
from ipgeolocation.models.time_zone import TimeZone
from ipgeolocation.models.user_agent_data import UserAgentData
from typing import Optional, Set
from typing_extensions import Self

class IPSecurityAPIXMLResponse(BaseModel):
    """
    IPSecurityAPIXMLResponse
    """ # noqa: E501
    ip: Optional[StrictStr] = None
    hostname: Optional[StrictStr] = None
    security: Optional[Security] = None
    location: Optional[LocationMinimal] = None
    network: Optional[NetworkMinimal] = None
    time_zone: Optional[TimeZone] = None
    user_agent: Optional[UserAgentData] = None
    country_metadata: Optional[CountryMetadata] = None
    currency: Optional[Currency] = None
    __properties: ClassVar[List[str]] = ["ip", "hostname", "security", "location", "network", "time_zone", "user_agent", "country_metadata", "currency"]

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
        """Create an instance of IPSecurityAPIXMLResponse from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of security
        if self.security:
            _dict['security'] = self.security.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict['network'] = self.network.to_dict()
        # override the default output from pydantic by calling `to_dict()` of time_zone
        if self.time_zone:
            _dict['time_zone'] = self.time_zone.to_dict()
        # override the default output from pydantic by calling `to_dict()` of user_agent
        if self.user_agent:
            _dict['user_agent'] = self.user_agent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of country_metadata
        if self.country_metadata:
            _dict['country_metadata'] = self.country_metadata.to_dict()
        # override the default output from pydantic by calling `to_dict()` of currency
        if self.currency:
            _dict['currency'] = self.currency.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of IPSecurityAPIXMLResponse from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "ip": obj.get("ip"),
            "hostname": obj.get("hostname"),
            "security": Security.from_dict(obj["security"]) if obj.get("security") is not None else None,
            "location": LocationMinimal.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "network": NetworkMinimal.from_dict(obj["network"]) if obj.get("network") is not None else None,
            "time_zone": TimeZone.from_dict(obj["time_zone"]) if obj.get("time_zone") is not None else None,
            "user_agent": UserAgentData.from_dict(obj["user_agent"]) if obj.get("user_agent") is not None else None,
            "country_metadata": CountryMetadata.from_dict(obj["country_metadata"]) if obj.get("country_metadata") is not None else None,
            "currency": Currency.from_dict(obj["currency"]) if obj.get("currency") is not None else None
        })
        return _obj


