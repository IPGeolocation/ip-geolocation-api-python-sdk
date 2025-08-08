# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.astronomy_location import AstronomyLocation

class TestAstronomyLocation(unittest.TestCase):
    """AstronomyLocation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AstronomyLocation:
        """Test AstronomyLocation
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AstronomyLocation`
        """
        model = AstronomyLocation()
        if include_optional:
            return AstronomyLocation(
                location_string = 'Londong, UK',
                continent_code = 'OC',
                continent_name = 'Oceania',
                country_code2 = 'AU',
                country_code3 = 'AUS',
                country_name = 'Australia',
                country_name_official = 'Commonwealth of Australia',
                is_eu = False,
                state_prov = 'Queensland',
                state_code = 'AU-QLD',
                district = 'South Brisbane',
                city = 'Brisbane',
                locality = '',
                zipcode = '4101',
                latitude = '-27.47306',
                longitude = '153.01421',
                elevation = '36.6'
            )
        else:
            return AstronomyLocation(
        )
        """

    def testAstronomyLocation(self):
        """Test AstronomyLocation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
