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
load_dotenv()

from ipgeolocation import ApiException, Configuration, ApiClient
from ipgeolocation.api.abuse_contact_api import AbuseContactApi


class TestAbuseContactApi(unittest.TestCase):
    """AbuseContactApi unit test """

    def setUp(self) -> None:
        api_key = os.getenv("API_KEY")
        if not api_key:
            self.skipTest("API_KEY not set in environment")

        configuration = Configuration(
            host="https://api.ipgeolocation.io/v2"
        )
        configuration.api_key["ApiKeyAuth"] = api_key
        self.client = ApiClient(configuration)
        self.api = AbuseContactApi(self.client)

    def test_get_abuse_contact_info(self) -> None:
        """Test case for get_abuse_contact_info
        """
        try:
            api_response = self.api.get_abuse_contact_info(ip="8.8.8.8")
            print(api_response.to_json())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_address_field_get_abuse_contact_info(self) -> None:
        """Test case for get_abuse_contact_info to get abuse address only
        """
        try:
            api_response = self.api.get_abuse_contact_info(ip="1.1.1.1")
            print(api_response.ip)
            print(api_response.abuse.address)
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")


if __name__ == '__main__':
    unittest.main()
