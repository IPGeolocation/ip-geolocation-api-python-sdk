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

from ipgeolocation import Configuration, ApiException, ApiClient
from ipgeolocation.api.astronomy_api import AstronomyApi
load_dotenv()

class TestAstronomyApi(unittest.TestCase):
    """AstronomyApi unit test """

    def setUp(self) -> None:
        api_key = os.getenv("API_KEY")
        if not api_key:
            self.skipTest("API_KEY not set in environment")

        configuration = Configuration(
            host="https://api.ipgeolocation.io/v2"
        )
        configuration.api_key["ApiKeyAuth"] = api_key
        self.client = ApiClient(configuration)
        self.api = AstronomyApi(self.client)

    def test_get_astronomy_details_by_ip(self) -> None:
        """Test case for get_astronomy_details by IP address
        """
        try:
            api_response = self.api.get_astronomy_details(ip="187.19.222.189")
            print(api_response.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_astronomy_details_by_location_str(self) -> None:
        """Test case for get_astronomy_details by location str
        """
        try:
            api_response = self.api.get_astronomy_details(location="London, GB")
            print(api_response.to_dict())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_astronomy_details_by_coordinates(self) -> None:
        """Test case for get_astronomy_details by coordinates
        """
        try:
            api_response = self.api.get_astronomy_details(lat="40.76473", long="-74.00084")
            print(api_response.to_json())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_astronomy_details_by_time_zone(self) -> None:
        """Test case for get_astronomy_details by time_zone with the provided date
        """
        try:
            api_response = self.api.get_astronomy_details(time_zone="Europe/London")
            print(api_response.to_json())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_time_series_lookup(self) -> None:
        """Test case for get_time_series_lookup
        """
        try:
            api_response = self.api.get_time_series_lookup(ip="187.19.222.189", date_start="2025-08-05", date_end="2025-08-08")
            print(api_response.to_str())
            for item in api_response.astronomy:
                print(item.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")


if __name__ == '__main__':
    unittest.main()
