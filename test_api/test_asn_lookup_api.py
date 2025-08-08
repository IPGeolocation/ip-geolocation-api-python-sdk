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

from ipgeolocation import Configuration, ApiClient, ApiException
from ipgeolocation.api.asn_lookup_api import ASNLookupApi

load_dotenv()

class TestASNLookupApi(unittest.TestCase):
    """ASNLookupApi unit test"""

    def setUp(self) -> None:
        api_key = os.getenv("API_KEY")
        if not api_key:
            self.skipTest("API_KEY not set in environment")

        configuration = Configuration(
            host="https://api.ipgeolocation.io/v2"
        )
        configuration.api_key["ApiKeyAuth"] = api_key
        self.client = ApiClient(configuration)
        self.api = ASNLookupApi(self.client)

    def test_get_asn_info(self) -> None:
        """Test case for get_asn_info
        """
        try:
            api_response = self.api.get_asn_info(ip="112.16.31.10")
            print(api_response.to_json())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")


if __name__ == '__main__':
    unittest.main()
