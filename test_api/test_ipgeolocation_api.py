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

from ipgeolocation import Configuration, ApiClient, ApiException, \
    IPGeolocationApi, GetBulkIpGeolocationRequest, GeolocationResponse, ErrorResponse

load_dotenv()

class TestIPGeolocationApi(unittest.TestCase):
    """IPGeolocationApi unit test"""

    def setUp(self) -> None:
        api_key = os.getenv("API_KEY")
        if not api_key:
            self.skipTest("API_KEY not set in environment")

        configuration = Configuration(
            host="https://api.ipgeolocation.io/v2"
        )
        configuration.api_key["ApiKeyAuth"] = api_key
        self.client = ApiClient(configuration)
        self.api = IPGeolocationApi(self.client)

    def test_get_ip_geolocation_by_ip(self) -> None:
        """Test case for get_ip_geolocation
        """
        try:
            api_response = self.api.get_ip_geolocation(ip="1.1.1.1")
            print(api_response.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_ip_geolocation_include_timezone(self) -> None:
        """Test case for get_ip_geolocation include timezone with location specific fields
        """
        try:
            api_response = self.api.get_ip_geolocation(ip="8.8.8.8", fields="location.country_name" ,include="time_zone")
            print(api_response.ip)
            print(api_response.location.country_name)
            print(api_response.time_zone.to_dict())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_ip_geolocation_include_security(self) -> None:
        """Test case for get_ip_geolocation include security
        """
        try:
            api_response = self.api.get_ip_geolocation(ip="2.56.188.34", fields="location", include="security", output="xml")
            print(api_response.location.city, api_response.location.country_name)
            print(api_response.security.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_bulk_ip_geolocation(self) -> None:
        """Test case for get_bulk_ip_geolocation to query multiple ip addresses at once.
        """
        try:
            bulk_ipgeolocation_request = GetBulkIpGeolocationRequest(ips=["1.1.1.1", "8.8.8.8", "invalid-ip"])
            api_response = self.api.get_bulk_ip_geolocation(bulk_ipgeolocation_request, include="time_zone,abuse")
            for item in api_response:
                instance = item.actual_instance
                if isinstance(instance, GeolocationResponse):
                    print(instance.to_str())
                elif isinstance(instance, ErrorResponse):
                    print(instance.message)
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_bulk_ip_geolocation_currency_info(self) -> None:
        """Test case for get_bulk_ip_geolocation to get currency info along with geolocation
        """
        try:
            bulk_ipgeolocation_request = GetBulkIpGeolocationRequest.from_dict({"ips": ["google.com", "1.1.0.0"]})
            api_response = self.api.get_bulk_ip_geolocation(bulk_ipgeolocation_request, fields="location,currency")
            for item in api_response:
                instance = item.actual_instance
                if isinstance(instance, GeolocationResponse):
                    print(instance.location.to_str(), instance.currency.to_str())
                elif isinstance(instance, ErrorResponse):
                    print(instance.message)
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

if __name__ == '__main__':
    unittest.main()
