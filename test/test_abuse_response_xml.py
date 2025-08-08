# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.abuse_response_xml import AbuseResponseXML

class TestAbuseResponseXML(unittest.TestCase):
    """AbuseResponseXML unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> AbuseResponseXML:
        """Test AbuseResponseXML
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `AbuseResponseXML`
        """
        model = AbuseResponseXML()
        if include_optional:
            return AbuseResponseXML(
                ip = '8.8.8.8',
                abuse = ipgeolocation.models.abuse.Abuse(
                    route = '8.8.8.0/24', 
                    country = 'US', 
                    handle = 'ABUSE5250-ARIN', 
                    name = 'Abuse', 
                    organization = 'Abuse', 
                    role = 'abuse', 
                    kind = 'group', 
                    address = '1600 Amphitheatre Parkway
Mountain View
CA
94043
United States', 
                    emails = ["network-abuse@google.com"], 
                    phone_numbers = ["+1-650-253-0000"], )
            )
        else:
            return AbuseResponseXML(
        )
        """

    def testAbuseResponseXML(self):
        """Test AbuseResponseXML"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
