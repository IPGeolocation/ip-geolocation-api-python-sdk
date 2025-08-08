# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.asn_response import ASNResponse

class TestASNResponse(unittest.TestCase):
    """ASNResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ASNResponse:
        """Test ASNResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ASNResponse`
        """
        model = ASNResponse()
        if include_optional:
            return ASNResponse(
                ip = '81.73.154.79',
                asn = ipgeolocation.models.asn_response_asn.ASNResponse_asn(
                    as_number = 'AS3269', 
                    organization = 'Telecom Italia S.p.A.', 
                    country = 'IT', 
                    asn_name = 'ASN-IBSNAZ', 
                    type = 'ISP', 
                    domain = 'business.telecomitalia.it', 
                    date_allocated = '1994-11-14', 
                    allocation_status = 'allocated', 
                    num_of_ipv4_routes = '490', 
                    num_of_ipv6_routes = '4', 
                    rir = 'RIPE', 
                    routes = ["192.76.177.0/24","216.165.96.0/20","216.165.89.0/24"], 
                    upstreams = [
                        ipgeolocation.models.asn_connection.ASNConnection(
                            as_number = 'AS12779', 
                            description = 'IT.Gate S.p.A.', 
                            country = 'IT', )
                        ], 
                    downstreams = [
                        ipgeolocation.models.asn_connection.ASNConnection(
                            as_number = 'AS12779', 
                            description = 'IT.Gate S.p.A.', 
                            country = 'IT', )
                        ], 
                    peers = [
                        
                        ], 
                    whois_response = 'whois output as a single string...', )
            )
        else:
            return ASNResponse(
        )
        """

    def testASNResponse(self):
        """Test ASNResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
