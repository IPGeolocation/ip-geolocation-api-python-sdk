# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.network_minimal import NetworkMinimal

class TestNetworkMinimal(unittest.TestCase):
    """NetworkMinimal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkMinimal:
        """Test NetworkMinimal
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkMinimal`
        """
        model = NetworkMinimal()
        if include_optional:
            return NetworkMinimal(
                asn = ipgeolocation.models.network_minimal_asn.NetworkMinimal_asn(
                    as_number = 'AS15169', 
                    organization = 'Google LLC', 
                    country = 'US', ),
                company = ipgeolocation.models.network_minimal_company.NetworkMinimal_company(
                    name = 'Google LLC', )
            )
        else:
            return NetworkMinimal(
        )
        """

    def testNetworkMinimal(self):
        """Test NetworkMinimal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
