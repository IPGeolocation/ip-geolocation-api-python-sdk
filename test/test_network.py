# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.network import Network

class TestNetwork(unittest.TestCase):
    """Network unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Network:
        """Test Network
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Network`
        """
        model = Network()
        if include_optional:
            return Network(
                asn = ipgeolocation.models.network_asn.NetworkAsn(
                    as_number = 'AS15169', 
                    organization = 'Google LLC', 
                    country = 'US', 
                    asn_name = 'GOOGLE', 
                    type = 'isp', 
                    domain = 'about.google', 
                    date_allocated = '', 
                    allocation_status = 'Assigned', 
                    num_of_ipv4_routes = '1099', 
                    num_of_ipv6_routes = '107', 
                    rir = 'ARIN', ),
                connection_type = 'wired',
                company = ipgeolocation.models.network_company.NetworkCompany(
                    name = 'Google LLC', 
                    type = 'hosting', 
                    domain = 'google.com', )
            )
        else:
            return Network(
        )
        """

    def testNetwork(self):
        """Test Network"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
