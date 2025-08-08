# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.parse_bulk_user_agent_strings_request import ParseBulkUserAgentStringsRequest

class TestParseBulkUserAgentStringsRequest(unittest.TestCase):
    """ParseBulkUserAgentStringsRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ParseBulkUserAgentStringsRequest:
        """Test ParseBulkUserAgentStringsRequest
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ParseBulkUserAgentStringsRequest`
        """
        model = ParseBulkUserAgentStringsRequest()
        if include_optional:
            return ParseBulkUserAgentStringsRequest(
                ua_strings = ["Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36","Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+","Mozilla/5.0 (Linux; U; en-US) AppleWebKit/528.5+ (KHTML, like Gecko, Safari/528.5+) Version/4.0 Kindle/3.0 (screen 600x800; rotate)"]
            )
        else:
            return ParseBulkUserAgentStringsRequest(
        )
        """

    def testParseBulkUserAgentStringsRequest(self):
        """Test ParseBulkUserAgentStringsRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
