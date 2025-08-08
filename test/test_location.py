# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.location import Location

class TestLocation(unittest.TestCase):
    """Location unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Location:
        """Test Location
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Location`
        """
        model = Location()
        if include_optional:
            return Location(
                continent_code = 'NA',
                continent_name = 'North America',
                country_code2 = 'US',
                country_code3 = 'USA',
                country_name = 'United States',
                country_name_official = 'United States of America',
                country_capital = 'Washington, D.C.',
                state_prov = 'California',
                state_code = 'US-CA',
                district = 'Santa Clara',
                city = 'Mountain View',
                zipcode = '94043-1351',
                latitude = '37.42240',
                longitude = '-122.08421',
                is_eu = False,
                country_flag = 'https://ipgeolocation.io/static/flags/us_64.png',
                geoname_id = '6301403',
                country_emoji = '',
                accuracy_radius = '1000',
                locality = 'Mountain View',
                dma_code = '807'
            )
        else:
            return Location(
        )
        """

    def testLocation(self):
        """Test Location"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
