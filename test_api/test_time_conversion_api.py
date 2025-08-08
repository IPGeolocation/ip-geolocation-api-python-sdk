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
from pprint import pprint

from ipgeolocation import TimeConversionApi, ApiException, ApiClient, Configuration

load_dotenv()

class TestTimeConversionApi(unittest.TestCase):
    """TimeConversionApi unit test"""
    def setUp(self) -> None:
        api_key = os.getenv("API_KEY")
        if not api_key:
            self.skipTest("API_KEY not set in environment")

        configuration = Configuration(
            host="https://api.ipgeolocation.io/v2"
        )
        configuration.api_key["ApiKeyAuth"] = api_key
        self.client = ApiClient(configuration)
        self.api = TimeConversionApi(self.client)

    def test_convert_time_between_timezones_using_tz(self) -> None:
        """Test case for convert_time_between_timezones using time zone names
        """
        try:
            api_response = self.api.convert_time_between_timezones(tz_from="Europe/Rome", tz_to="Asia/Dubai")
            print(api_response.to_json())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")


    def test_convert_time_between_timezones_using_location_addr(self) -> None:
        """Test case for convert_time_between_timezones using location address
        """
        try:
            api_response = self.api.convert_time_between_timezones(location_from="London, United Kingdom", location_to="New York, United States")
            print(api_response.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_convert_time_between_timezones_using_ICAO_CODE(self) -> None:
        """Test case for convert_time_between_timezones using ICAO code
        """
        try:
            api_response = self.api.convert_time_between_timezones(icao_from="YSSY", icao_to="ZBAA")
            print(api_response.to_json())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
