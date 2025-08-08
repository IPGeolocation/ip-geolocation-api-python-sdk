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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from ipgeolocation.models.asn_connection import ASNConnection
from typing import Optional, Set
from typing_extensions import Self

class ASNDetails(BaseModel):
    """
    ASNDetails
    """ # noqa: E501
    as_number: Optional[StrictStr] = None
    organization: Optional[StrictStr] = None
    country: Optional[StrictStr] = None
    asn_name: Optional[StrictStr] = None
    type: Optional[StrictStr] = None
    domain: Optional[StrictStr] = None
    date_allocated: Optional[StrictStr] = None
    allocation_status: Optional[StrictStr] = None
    num_of_ipv4_routes: Optional[StrictStr] = None
    num_of_ipv6_routes: Optional[StrictStr] = None
    rir: Optional[StrictStr] = None
    routes: Optional[List[StrictStr]] = Field(default=None, description="It will only be included in the response, if you set include=routes in the request")
    upstreams: Optional[List[ASNConnection]] = Field(default=None, description="It will only be included in the response, if you set include=upstreams in the request")
    downstreams: Optional[List[ASNConnection]] = Field(default=None, description="It will only be included in the response, if you set include=downstreams in the request")
    peers: Optional[List[ASNConnection]] = Field(default=None, description="It will only be included in the response, if you set include=peers in the request")
    whois_response: Optional[StrictStr] = Field(default=None, description="It will only be included in the response, if you set include=whois_response in the request")
    __properties: ClassVar[List[str]] = ["as_number", "organization", "country", "asn_name", "type", "domain", "date_allocated", "allocation_status", "num_of_ipv4_routes", "num_of_ipv6_routes", "rir", "routes", "upstreams", "downstreams", "peers", "whois_response"]

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
        """Create an instance of ASNDetails from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in upstreams (list)
        _items = []
        if self.upstreams:
            for _item_upstreams in self.upstreams:
                if _item_upstreams:
                    _items.append(_item_upstreams.to_dict())
            _dict['upstreams'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in downstreams (list)
        _items = []
        if self.downstreams:
            for _item_downstreams in self.downstreams:
                if _item_downstreams:
                    _items.append(_item_downstreams.to_dict())
            _dict['downstreams'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in peers (list)
        _items = []
        if self.peers:
            for _item_peers in self.peers:
                if _item_peers:
                    _items.append(_item_peers.to_dict())
            _dict['peers'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ASNDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "as_number": obj.get("as_number"),
            "organization": obj.get("organization"),
            "country": obj.get("country"),
            "asn_name": obj.get("asn_name"),
            "type": obj.get("type"),
            "domain": obj.get("domain"),
            "date_allocated": obj.get("date_allocated"),
            "allocation_status": obj.get("allocation_status"),
            "num_of_ipv4_routes": obj.get("num_of_ipv4_routes"),
            "num_of_ipv6_routes": obj.get("num_of_ipv6_routes"),
            "rir": obj.get("rir"),
            "routes": obj.get("routes"),
            "upstreams": [ASNConnection.from_dict(_item) for _item in obj["upstreams"]] if obj.get("upstreams") is not None else None,
            "downstreams": [ASNConnection.from_dict(_item) for _item in obj["downstreams"]] if obj.get("downstreams") is not None else None,
            "peers": [ASNConnection.from_dict(_item) for _item in obj["peers"]] if obj.get("peers") is not None else None,
            "whois_response": obj.get("whois_response")
        })
        return _obj


