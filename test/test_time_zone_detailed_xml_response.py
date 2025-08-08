# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.time_zone_detailed_xml_response import TimeZoneDetailedXMLResponse

class TestTimeZoneDetailedXMLResponse(unittest.TestCase):
    """TimeZoneDetailedXMLResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeZoneDetailedXMLResponse:
        """Test TimeZoneDetailedXMLResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeZoneDetailedXMLResponse`
        """
        model = TimeZoneDetailedXMLResponse()
        if include_optional:
            return TimeZoneDetailedXMLResponse(
                ip = '8.8.8.8',
                airport_details = ipgeolocation.models.timezone_airport.TimezoneAirport(
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
                    faa_code = '', ),
                lo_code_details = ipgeolocation.models.timezone_locode.TimezoneLocode(
                    lo_code = 'DEBER', 
                    city = 'Berlin', 
                    state_code = 'BE', 
                    country_code = 'DE', 
                    country_name = '', 
                    location_type = 'Port, Rail Terminal, Road Terminal, Airport, Postal Exchange', 
                    latitude = '52.51667', 
                    longitude = '13.38333', ),
                location = ipgeolocation.models.timezone_location.TimezoneLocation(
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
                    longitude = '153.01421', ),
                time_zone = ipgeolocation.models.timezone_detail.TimezoneDetail(
                    name = 'America/Los_Angeles', 
                    offset = -8, 
                    offset_with_dst = -7, 
                    date = '2025-04-24', 
                    date_time = '2025-04-24 11:30:12', 
                    date_time_txt = 'Thursday, April 24, 2025 11:30:12', 
                    date_time_wti = 'Thu, 24 Apr 2025 11:30:12 -0700', 
                    date_time_ymd = '2025-04-24T11:30:12-0700', 
                    date_time_unix = 1745519412.353, 
                    time_24 = '41412', 
                    time_12 = '11:30:12 AM', 
                    week = 17, 
                    month = 4, 
                    year = 2025, 
                    year_abbr = '25', 
                    is_dst = True, 
                    dst_savings = 56, 
                    dst_exists = True, 
                    dst_start = ipgeolocation.models.timezone_detail_dst_start.TimezoneDetail_dst_start(
                        utc_time = '2025-03-09 TIME 10', 
                        duration = '+1H', 
                        gap = True, 
                        date_time_after = '2025-03-09 TIME 03', 
                        date_time_before = '2025-03-09 TIME 02', 
                        overlap = True, ), 
                    dst_end = ipgeolocation.models.timezone_detail_dst_end.TimezoneDetail_dst_end(
                        utc_time = '2025-11-02 TIME 09', 
                        duration = '-1H', 
                        gap = True, 
                        date_time_after = '2025-11-02 TIME 01', 
                        date_time_before = '2025-11-02 TIME 02', 
                        overlap = True, ), )
            )
        else:
            return TimeZoneDetailedXMLResponse(
        )
        """

    def testTimeZoneDetailedXMLResponse(self):
        """Test TimeZoneDetailedXMLResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
