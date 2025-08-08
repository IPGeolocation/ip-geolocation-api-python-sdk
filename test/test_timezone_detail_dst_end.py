# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.timezone_detail_dst_end import TimezoneDetailDstEnd

class TestTimezoneDetailDstEnd(unittest.TestCase):
    """TimezoneDetailDstEnd unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> TimezoneDetailDstEnd:
        """Test TimezoneDetailDstEnd
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `TimezoneDetailDstEnd`
        """
        model = TimezoneDetailDstEnd()
        if include_optional:
            return TimezoneDetailDstEnd(
                utc_time = '2025-11-02 TIME 09',
                duration = '-1H',
                gap = True,
                date_time_after = '2025-11-02 TIME 01',
                date_time_before = '2025-11-02 TIME 02',
                overlap = True
            )
        else:
            return TimezoneDetailDstEnd(
        )
        """

    def testTimezoneDetailDstEnd(self):
        """Test TimezoneDetailDstEnd"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
