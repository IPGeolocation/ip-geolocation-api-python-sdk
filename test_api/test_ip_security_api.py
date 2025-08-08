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

from ipgeolocation import IPSecurityApi, ApiException, ApiClient, Configuration, \
    GetBulkIpGeolocationRequest, IPSecurityAPIResponse

load_dotenv()

class TestIPSecurityApi(unittest.TestCase):
    """IPSecurityApi unit test"""
    def setUp(self) -> None:
        api_key = os.getenv("SEC_API_KEY")
        if not api_key:
            self.skipTest("API_KEY not set in environment")

        configuration = Configuration(
            host="https://api.ipgeolocation.io/v2"
        )
        configuration.api_key["ApiKeyAuth"] = api_key
        self.client = ApiClient(configuration)
        self.api = IPSecurityApi(self.client)

    def test_get_ip_security_info(self) -> None:
        """Test case for get_ip_security_info
        """
        try:
            api_response = self.api.get_ip_security_info(ip="219.100.37.55", include="location,network,currency,time_zone,country_metadata,hostname")
            print(api_response.to_str())
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")

    def test_get_bulk_ip_security_info(self) -> None:
        """Test case for get_bulk_ip_security_info
        """
        try:
            bulk_security_request = GetBulkIpGeolocationRequest(ips=["2.56.188.34", "2.56.188.35", "wrong-ip"])
            api_response = self.api.get_bulk_ip_security_info(bulk_security_request, include="location,network", fields="location.city,network.asn.as_number")
            for item in api_response:
                instance = item.actual_instance
                if isinstance(instance, IPSecurityAPIResponse):
                    print(instance.to_json())
                else:
                    print(instance.message)
        except ApiException as e:
            self.fail(f"API call failed with exception: {e}")


if __name__ == '__main__':
    unittest.main()
