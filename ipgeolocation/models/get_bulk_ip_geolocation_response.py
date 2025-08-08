# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
import pprint
from pydantic import BaseModel, ConfigDict, Field, StrictStr, ValidationError, field_validator
from typing import Any, List, Optional
from ipgeolocation.models.error_response import ErrorResponse
from ipgeolocation.models.geolocation_response import GeolocationResponse
from pydantic import StrictStr, Field
from typing import Union, List, Set, Optional, Dict
from typing_extensions import Literal, Self

GETBULKIPGEOLOCATIONRESPONSE_ONE_OF_SCHEMAS = ["ErrorResponse", "GeolocationResponse"]

class GetBulkIpGeolocationResponse(BaseModel):
    """
    GetBulkIpGeolocationResponse
    """
    # data type: ErrorResponse
    oneof_schema_1_validator: Optional[ErrorResponse] = None
    # data type: GeolocationResponse
    oneof_schema_2_validator: Optional[GeolocationResponse] = None
    actual_instance: Optional[Union[ErrorResponse, GeolocationResponse]] = None
    one_of_schemas: Set[str] = { "ErrorResponse", "GeolocationResponse" }

    model_config = ConfigDict(
        validate_assignment=True,
        protected_namespaces=(),
    )


    def __init__(self, *args, **kwargs) -> None:
        if args:
            if len(args) > 1:
                raise ValueError("If a position argument is used, only 1 is allowed to set `actual_instance`")
            if kwargs:
                raise ValueError("If a position argument is used, keyword arguments cannot be used.")
            super().__init__(actual_instance=args[0])
        else:
            super().__init__(**kwargs)

    @field_validator('actual_instance')
    def actual_instance_must_validate_oneof(cls, v):
        instance = GetBulkIpGeolocationResponse.model_construct()
        error_messages = []
        match = 0
        # validate data type: ErrorResponse
        if not isinstance(v, ErrorResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `ErrorResponse`")
        else:
            match += 1
        # validate data type: GeolocationResponse
        if not isinstance(v, GeolocationResponse):
            error_messages.append(f"Error! Input type `{type(v)}` is not `GeolocationResponse`")
        else:
            match += 1
        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when setting `actual_instance` in GetBulkIpGeolocationResponse with oneOf schemas: ErrorResponse, GeolocationResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when setting `actual_instance` in GetBulkIpGeolocationResponse with oneOf schemas: ErrorResponse, GeolocationResponse. Details: " + ", ".join(error_messages))
        else:
            return v

    @classmethod
    def from_dict(cls, obj: Union[str, Dict[str, Any]]) -> Self:
        return cls.from_json(json.dumps(obj))

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Returns the object represented by the json string"""
        instance = cls.model_construct()
        error_messages = []
        match = 0

        # deserialize data into ErrorResponse
        try:
            instance.actual_instance = ErrorResponse.from_json(json_str)
            if not instance.actual_instance.message:
                # deserialize data into GeolocationResponse
                try:
                    instance.actual_instance = GeolocationResponse.from_json(json_str)
                    match += 1
                except (ValidationError, ValueError) as e:
                    error_messages.append(str(e))
            else:
                match += 1
        except (ValidationError, ValueError) as e:
            error_messages.append(str(e))
        # deserialize data into GeolocationResponse
        # try:
        #     instance.actual_instance = GeolocationResponse.from_json(json_str)
        #     match += 1
        # except (ValidationError, ValueError) as e:
        #     error_messages.append(str(e))

        if match > 1:
            # more than 1 match
            raise ValueError("Multiple matches found when deserializing the JSON string into GetBulkIpGeolocationResponse with oneOf schemas: ErrorResponse, GeolocationResponse. Details: " + ", ".join(error_messages))
        elif match == 0:
            # no match
            raise ValueError("No match found when deserializing the JSON string into GetBulkIpGeolocationResponse with oneOf schemas: ErrorResponse, GeolocationResponse. Details: " + ", ".join(error_messages))
        else:
            return instance

    def to_json(self) -> str:
        """Returns the JSON representation of the actual instance"""
        if self.actual_instance is None:
            return "null"

        if hasattr(self.actual_instance, "to_json") and callable(self.actual_instance.to_json):
            return self.actual_instance.to_json()
        else:
            return json.dumps(self.actual_instance)

    def to_dict(self) -> Optional[Union[Dict[str, Any], ErrorResponse, GeolocationResponse]]:
        """Returns the dict representation of the actual instance"""
        if self.actual_instance is None:
            return None

        if hasattr(self.actual_instance, "to_dict") and callable(self.actual_instance.to_dict):
            return self.actual_instance.to_dict()
        else:
            # primitive type
            return self.actual_instance

    def to_str(self) -> str:
        """Returns the string representation of the actual instance"""
        return pprint.pformat(self.model_dump())


