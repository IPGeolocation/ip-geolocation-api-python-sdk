# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.time_zone import TimeZone

class TestTimeZone(unittest.TestCase):
    """TimeZone unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimeZone:
        """Test TimeZone
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimeZone`
        """
        model = TimeZone()
        if include_optional:
            return TimeZone(
                name = 'America/Los_Angeles',
                offset = -8,
                offset_with_dst = -7,
                current_time = '2025-04-22 06:19:40.951-0700',
                current_time_unix = 1745327980.951,
                is_dst = True,
                dst_savings = 1,
                dst_exists = True,
                dst_start = ipgeolocation.models.time_zone_dst_start.TimeZoneDstStart(
                    utc_time = '2025-03-09 TIME 10', 
                    duration = '+1H', 
                    gap = True, 
                    date_time_after = '2025-03-09 TIME 03', 
                    date_time_before = '2025-03-09 TIME 02', 
                    overlap = False, ),
                dst_end = ipgeolocation.models.time_zone_dst_end.TimeZoneDstEnd(
                    utc_time = '2025-11-02 TIME 09', 
                    duration = '-1H', 
                    gap = False, 
                    date_time_after = '2025-11-02 TIME 01', 
                    date_time_before = '2025-11-02 TIME 02', 
                    overlap = True, )
            )
        else:
            return TimeZone(
        )
        """

    def testTimeZone(self):
        """Test TimeZone"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
