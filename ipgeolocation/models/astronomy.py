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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from ipgeolocation.models.astronomy_evening import AstronomyEvening
from ipgeolocation.models.astronomy_morning import AstronomyMorning
from typing import Optional, Set
from typing_extensions import Self

class Astronomy(BaseModel):
    """
    Astronomy
    """ # noqa: E501
    time_zone: Optional[StrictStr] = None
    var_date: Optional[StrictStr] = Field(default=None, alias="date")
    current_time: Optional[StrictStr] = None
    mid_night: Optional[StrictStr] = None
    night_end: Optional[StrictStr] = None
    morning: Optional[AstronomyMorning] = None
    sunrise: Optional[StrictStr] = None
    sunset: Optional[StrictStr] = None
    evening: Optional[AstronomyEvening] = None
    night_begin: Optional[StrictStr] = None
    sun_status: Optional[StrictStr] = None
    solar_noon: Optional[StrictStr] = None
    day_length: Optional[StrictStr] = None
    sun_altitude: Optional[Union[StrictFloat, StrictInt]] = None
    sun_distance: Optional[Union[StrictFloat, StrictInt]] = None
    sun_azimuth: Optional[Union[StrictFloat, StrictInt]] = None
    moon_phase: Optional[StrictStr] = None
    moonrise: Optional[StrictStr] = None
    moonset: Optional[StrictStr] = None
    moon_status: Optional[StrictStr] = None
    moon_altitude: Optional[Union[StrictFloat, StrictInt]] = None
    moon_distance: Optional[Union[StrictFloat, StrictInt]] = None
    moon_azimuth: Optional[Union[StrictFloat, StrictInt]] = None
    moon_parallactic_angle: Optional[Union[StrictFloat, StrictInt]] = None
    moon_illumination_percentage: Optional[StrictStr] = None
    moon_angle: Optional[Union[StrictFloat, StrictInt]] = None
    __properties: ClassVar[List[str]] = ["time_zone", "date", "current_time", "mid_night", "night_end", "morning", "sunrise", "sunset", "evening", "night_begin", "sun_status", "solar_noon", "day_length", "sun_altitude", "sun_distance", "sun_azimuth", "moon_phase", "moonrise", "moonset", "moon_status", "moon_altitude", "moon_distance", "moon_azimuth", "moon_parallactic_angle", "moon_illumination_percentage", "moon_angle"]

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
        """Create an instance of Astronomy from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of morning
        if self.morning:
            _dict['morning'] = self.morning.to_dict()
        # override the default output from pydantic by calling `to_dict()` of evening
        if self.evening:
            _dict['evening'] = self.evening.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Astronomy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "time_zone": obj.get("time_zone"),
            "date": obj.get("date"),
            "current_time": obj.get("current_time"),
            "mid_night": obj.get("mid_night"),
            "night_end": obj.get("night_end"),
            "morning": AstronomyMorning.from_dict(obj["morning"]) if obj.get("morning") is not None else None,
            "sunrise": obj.get("sunrise"),
            "sunset": obj.get("sunset"),
            "evening": AstronomyEvening.from_dict(obj["evening"]) if obj.get("evening") is not None else None,
            "night_begin": obj.get("night_begin"),
            "sun_status": obj.get("sun_status"),
            "solar_noon": obj.get("solar_noon"),
            "day_length": obj.get("day_length"),
            "sun_altitude": obj.get("sun_altitude"),
            "sun_distance": obj.get("sun_distance"),
            "sun_azimuth": obj.get("sun_azimuth"),
            "moon_phase": obj.get("moon_phase"),
            "moonrise": obj.get("moonrise"),
            "moonset": obj.get("moonset"),
            "moon_status": obj.get("moon_status"),
            "moon_altitude": obj.get("moon_altitude"),
            "moon_distance": obj.get("moon_distance"),
            "moon_azimuth": obj.get("moon_azimuth"),
            "moon_parallactic_angle": obj.get("moon_parallactic_angle"),
            "moon_illumination_percentage": obj.get("moon_illumination_percentage"),
            "moon_angle": obj.get("moon_angle")
        })
        return _obj


