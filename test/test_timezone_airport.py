# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.timezone_airport import TimezoneAirport

class TestTimezoneAirport(unittest.TestCase):
    """TimezoneAirport unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimezoneAirport:
        """Test TimezoneAirport
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimezoneAirport`
        """
        model = TimezoneAirport()
        if include_optional:
            return TimezoneAirport(
                type = 'large_airport',
                name = 'Hartsfield Jackson Atlanta International Airport',
                latitude = '33.63670',
                longitude = '-84.42810',
                elevation_ft = 1026,
                continent_code = 'NA',
                country_code = 'US',
                state_code = 'US-GA',
                city = 'Atlanta',
                iata_code = 'ATL',
                icao_code = 'KATL',
                faa_code = ''
            )
        else:
            return TimezoneAirport(
        )
        """

    def testTimezoneAirport(self):
        """Test TimezoneAirport"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
