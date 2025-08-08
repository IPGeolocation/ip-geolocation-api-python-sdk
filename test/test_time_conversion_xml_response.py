# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.time_conversion_xml_response import TimeConversionXMLResponse

class TestTimeConversionXMLResponse(unittest.TestCase):
    """TimeConversionXMLResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeConversionXMLResponse:
        """Test TimeConversionXMLResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeConversionXMLResponse`
        """
        model = TimeConversionXMLResponse()
        if include_optional:
            return TimeConversionXMLResponse(
                original_time = '2024-12-08 11:00',
                converted_time = '2024-12-08 18:30:00',
                diff_hour = 7.5,
                diff_min = 450
            )
        else:
            return TimeConversionXMLResponse(
        )
        """

    def testTimeConversionXMLResponse(self):
        """Test TimeConversionXMLResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
