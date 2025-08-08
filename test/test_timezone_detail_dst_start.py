# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.timezone_detail_dst_start import TimezoneDetailDstStart

class TestTimezoneDetailDstStart(unittest.TestCase):
    """TimezoneDetailDstStart unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimezoneDetailDstStart:
        """Test TimezoneDetailDstStart
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimezoneDetailDstStart`
        """
        model = TimezoneDetailDstStart()
        if include_optional:
            return TimezoneDetailDstStart(
                utc_time = '2025-03-09 TIME 10',
                duration = '+1H',
                gap = True,
                date_time_after = '2025-03-09 TIME 03',
                date_time_before = '2025-03-09 TIME 02',
                overlap = True
            )
        else:
            return TimezoneDetailDstStart(
        )
        """

    def testTimezoneDetailDstStart(self):
        """Test TimezoneDetailDstStart"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
