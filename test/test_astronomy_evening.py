# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.astronomy_evening import AstronomyEvening

class TestAstronomyEvening(unittest.TestCase):
    """AstronomyEvening unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AstronomyEvening:
        """Test AstronomyEvening
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AstronomyEvening`
        """
        model = AstronomyEvening()
        if include_optional:
            return AstronomyEvening(
                golden_hour_begin = '19:44',
                golden_hour_end = '20:44',
                blue_hour_begin = '20:44',
                blue_hour_end = '21:09',
                civil_twilight_begin = '20:24',
                civil_twilight_end = '20:56',
                nautical_twilight_begin = '20:56',
                nautical_twilight_end = '21:37',
                astronomical_twilight_begin = '21:37',
                astronomical_twilight_end = '22:23'
            )
        else:
            return AstronomyEvening(
        )
        """

    def testAstronomyEvening(self):
        """Test AstronomyEvening"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
