# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.security import Security

class TestSecurity(unittest.TestCase):
    """Security unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Security:
        """Test Security
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Security`
        """
        model = Security()
        if include_optional:
            return Security(
                threat_score = 80,
                is_tor = False,
                is_proxy = True,
                proxy_type = 'VPN',
                proxy_provider = '',
                is_anonymous = True,
                is_known_attacker = True,
                is_spam = False,
                is_bot = False,
                is_cloud_provider = False,
                cloud_provider = ''
            )
        else:
            return Security(
        )
        """

    def testSecurity(self):
        """Test Security"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
