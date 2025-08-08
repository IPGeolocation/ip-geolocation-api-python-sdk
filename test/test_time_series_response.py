# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.time_series_response import TimeSeriesResponse

class TestTimeSeriesResponse(unittest.TestCase):
    """TimeSeriesResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeSeriesResponse:
        """Test TimeSeriesResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeSeriesResponse`
        """
        model = TimeSeriesResponse()
        if include_optional:
            return TimeSeriesResponse(
                ip = '8.8.8.8',
                location = ipgeolocation.models.astronomy_location.AstronomyLocation(
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
                    elevation = '36.6', ),
                astronomy = [
                    ipgeolocation.models.time_series.TimeSeries(
                        date = '2025-07-17', 
                        mid_night = '01:02', 
                        night_end = '03:40', 
                        morning = ipgeolocation.models.time_series_morning.TimeSeries_morning(
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
                        evening = ipgeolocation.models.time_series_evening.TimeSeries_evening(
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
                        moon_phase = 'LAST_QUARTER', 
                        moonrise = '-:-', 
                        moonset = '13:04', 
                        moon_status = '-', )
                    ]
            )
        else:
            return TimeSeriesResponse(
        )
        """

    def testTimeSeriesResponse(self):
        """Test TimeSeriesResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
