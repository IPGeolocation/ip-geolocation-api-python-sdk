# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.timezone_locode import TimezoneLocode

class TestTimezoneLocode(unittest.TestCase):
    """TimezoneLocode unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimezoneLocode:
        """Test TimezoneLocode
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimezoneLocode`
        """
        model = TimezoneLocode()
        if include_optional:
            return TimezoneLocode(
                lo_code = 'DEBER',
                city = 'Berlin',
                state_code = 'BE',
                country_code = 'DE',
                country_name = '',
                location_type = 'Port, Rail Terminal, Road Terminal, Airport, Postal Exchange',
                latitude = '52.51667',
                longitude = '13.38333'
            )
        else:
            return TimezoneLocode(
        )
        """

    def testTimezoneLocode(self):
        """Test TimezoneLocode"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
