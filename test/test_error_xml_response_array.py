# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.error_xml_response_array import ErrorXMLResponseArray

class TestErrorXMLResponseArray(unittest.TestCase):
    """ErrorXMLResponseArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorXMLResponseArray:
        """Test ErrorXMLResponseArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorXMLResponseArray`
        """
        model = ErrorXMLResponseArray()
        if include_optional:
            return ErrorXMLResponseArray(
                message = 'The Message showing the error'
            )
        else:
            return ErrorXMLResponseArray(
        )
        """

    def testErrorXMLResponseArray(self):
        """Test ErrorXMLResponseArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
