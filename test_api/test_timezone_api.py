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

from ipgeolocation import Configuration, ApiClient, ApiException, TimezoneApi

load_dotenv()

class TestTimezoneApi(unittest.TestCase):
    """TimezoneApi unit test"""

    def setUp(self) -> None:
        api_key = os.getenv("API_KEY")
        if not api_key:
            self.skipTest("API_KEY not set in environment")

        configuration = Configuration(
            host="https://api.ipgeolocation.io/v2"
        )
        configuration.api_key["ApiKeyAuth"] = api_key
        self.client = ApiClient(configuration)
        self.api = TimezoneApi(self.client)

    def test_get_timezone_info_by_ip(self) -> None:
        """Test case for get_timezone_info by ip address
        Timezone information details
        """
        try:
            api_response = self.api.get_timezone_info(ip="1.1.1.1")
            print(api_response.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_timezone_info_by_tz(self) -> None:
        """Test case for get_timezone_info by IANA time zone name
        """
        try:
            api_response = self.api.get_timezone_info(tz="America/Los_Angeles")
            print(api_response.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_timezone_info_by_coordinates(self) -> None:
        """Test case for get_timezone_info by coordinates
        """
        try:
            api_response = self.api.get_timezone_info(lat="51.5", long="-0.1")
            print(api_response.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_timezone_info_by_IATA_CODE(self) -> None:
        """Test case for get_timezone_info by the IATA CODE
        """
        try:
            api_response = self.api.get_timezone_info(iata_code="DXB")
            print(api_response.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_timezone_info_by_UN_LO_CODE(self) -> None:
        """Test case for get_timezone_info by the UN/LO CODE
        """
        try:
            api_response = self.api.get_timezone_info(lo_code="USNYC")
            print(api_response.to_json())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")


if __name__ == '__main__':
    unittest.main()
