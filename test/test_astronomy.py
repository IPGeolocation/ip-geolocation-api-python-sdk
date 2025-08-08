# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.astronomy import Astronomy

class TestAstronomy(unittest.TestCase):
    """Astronomy unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Astronomy:
        """Test Astronomy
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Astronomy`
        """
        model = Astronomy()
        if include_optional:
            return Astronomy(
                time_zone = 'America/Los_Angeles',
                var_date = '2025-07-17',
                current_time = '08:03:36.532',
                mid_night = '01:02',
                night_end = '03:40',
                morning = ipgeolocation.models.astronomy_morning.Astronomy_morning(
                    astronomical_twilight_begin = '03:40', 
                    astronomical_twilight_end = '04:27', 
                    nautical_twilight_begin = '04:27', 
                    nautical_twilight_end = '05:07', 
                    civil_twilight_begin = '05:07', 
                    civil_twilight_end = '05:39', 
                    blue_hour_begin = '04:54', 
                    blue_hour_end = '05:20', 
                    golden_hour_begin = '05:20', 
                    golden_hour_end = '06:19', ),
                sunrise = '05:39',
                sunset = '20:24',
                evening = ipgeolocation.models.astronomy_evening.Astronomy_evening(
                    golden_hour_begin = '19:44', 
                    golden_hour_end = '20:44', 
                    blue_hour_begin = '20:44', 
                    blue_hour_end = '21:09', 
                    civil_twilight_begin = '20:24', 
                    civil_twilight_end = '20:56', 
                    nautical_twilight_begin = '20:56', 
                    nautical_twilight_end = '21:37', 
                    astronomical_twilight_begin = '21:37', 
                    astronomical_twilight_end = '22:23', ),
                night_begin = '22:23',
                sun_status = '-',
                solar_noon = '13:02',
                day_length = '14:45',
                sun_altitude = 24.957683470850487,
                sun_distance = 152059278.3394745,
                sun_azimuth = 82.93803947255543,
                moon_phase = 'LAST_QUARTER',
                moonrise = '-:-',
                moonset = '13:04',
                moon_status = '-',
                moon_altitude = 50.865120808868284,
                moon_distance = 371690.2207058187,
                moon_azimuth = 224.27457358894264,
                moon_parallactic_angle = 32.4113797557535,
                moon_illumination_percentage = '-55.99',
                moon_angle = 263.11859022190265
            )
        else:
            return Astronomy(
        )
        """

    def testAstronomy(self):
        """Test Astronomy"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
