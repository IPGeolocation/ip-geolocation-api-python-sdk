# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.parse_user_agent_string_request import ParseUserAgentStringRequest

class TestParseUserAgentStringRequest(unittest.TestCase):
    """ParseUserAgentStringRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParseUserAgentStringRequest:
        """Test ParseUserAgentStringRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParseUserAgentStringRequest`
        """
        model = ParseUserAgentStringRequest()
        if include_optional:
            return ParseUserAgentStringRequest(
                ua_string = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9'
            )
        else:
            return ParseUserAgentStringRequest(
        )
        """

    def testParseUserAgentStringRequest(self):
        """Test ParseUserAgentStringRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
