# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.astronomy_morning import AstronomyMorning

class TestAstronomyMorning(unittest.TestCase):
    """AstronomyMorning unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AstronomyMorning:
        """Test AstronomyMorning
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AstronomyMorning`
        """
        model = AstronomyMorning()
        if include_optional:
            return AstronomyMorning(
                astronomical_twilight_begin = '03:40',
                astronomical_twilight_end = '04:27',
                nautical_twilight_begin = '04:27',
                nautical_twilight_end = '05:07',
                civil_twilight_begin = '05:07',
                civil_twilight_end = '05:39',
                blue_hour_begin = '04:54',
                blue_hour_end = '05:20',
                golden_hour_begin = '05:20',
                golden_hour_end = '06:19'
            )
        else:
            return AstronomyMorning(
        )
        """

    def testAstronomyMorning(self):
        """Test AstronomyMorning"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
