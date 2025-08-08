# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import os
import unittest
from dotenv import load_dotenv

from ipgeolocation import UserAgentApi, ApiClient, ApiException, Configuration, ParseBulkUserAgentStringsRequest, \
    ParseUserAgentStringRequest

load_dotenv()

class TestUserAgentApi(unittest.TestCase):
    """UserAgentApi unit test"""

    def setUp(self) -> None:
        api_key = os.getenv("API_KEY")
        if not api_key:
            self.skipTest("API_KEY not set in environment")

        configuration = Configuration(
            host="https://api.ipgeolocation.io/v2"
        )
        configuration.api_key["ApiKeyAuth"] = api_key
        self.client = ApiClient(configuration)
        self.api = UserAgentApi(self.client)

    def test_get_user_agent_details(self) -> None:
        """Test case for get_user_agent_details
        Get details of user-agent
        """
        try:
            api_response = self.api.get_user_agent_details(user_agent="Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9")
            print(api_response.to_dict())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_parse_bulk_user_agent_strings(self) -> None:
        """Test case for parse_bulk_user_agent_strings
        Handle multiple user-agent string lookups
        """
        try:
            parse_bulk_user_agent_strings_request = ParseBulkUserAgentStringsRequest.from_dict({"uaStrings": [
                "Mozilla/5.0 (Linux; Android 8.0.0; SM-G960F Build/R16NW) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.84 Mobile Safari/537.36",
                "Mozilla/5.0 (X11; U; Linux armv7l like Android; en-us) AppleWebKit/531.2+ (KHTML, like Gecko) Version/5.0 Safari/533.2+ Kindle/3.0+"
            ]})
            api_response = self.api.parse_bulk_user_agent_strings(parse_bulk_user_agent_strings_request)
            for item in api_response:
                print(item.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_parse_user_agent_string(self) -> None:
        """Test case for parse_user_agent_string
        Handle single User-Agent string
        """
        try:
            parse_user_agent_strings_request = ParseUserAgentStringRequest(uaString="User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9")
            api_response = self.api.parse_user_agent_string(parse_user_agent_strings_request)
            print(api_response.to_json())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")


if __name__ == '__main__':
    unittest.main()
