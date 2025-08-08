# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.time_conversion_response import TimeConversionResponse

class TestTimeConversionResponse(unittest.TestCase):
    """TimeConversionResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeConversionResponse:
        """Test TimeConversionResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeConversionResponse`
        """
        model = TimeConversionResponse()
        if include_optional:
            return TimeConversionResponse(
                original_time = '2024-12-08 11:00',
                converted_time = '2024-12-08 18:30:00',
                diff_hour = 7.5,
                diff_min = 450
            )
        else:
            return TimeConversionResponse(
        )
        """

    def testTimeConversionResponse(self):
        """Test TimeConversionResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
