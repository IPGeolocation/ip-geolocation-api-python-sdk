# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.error_response import ErrorResponse

class TestErrorResponse(unittest.TestCase):
    """ErrorResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorResponse:
        """Test ErrorResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorResponse`
        """
        model = ErrorResponse()
        if include_optional:
            return ErrorResponse(
                message = 'The message showing the error'
            )
        else:
            return ErrorResponse(
        )
        """

    def testErrorResponse(self):
        """Test ErrorResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
