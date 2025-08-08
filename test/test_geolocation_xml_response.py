# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.geolocation_xml_response import GeolocationXMLResponse

class TestGeolocationXMLResponse(unittest.TestCase):
    """GeolocationXMLResponse unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> GeolocationXMLResponse:
        """Test GeolocationXMLResponse
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `GeolocationXMLResponse`
        """
        model = GeolocationXMLResponse()
        if include_optional:
            return GeolocationXMLResponse(
                ip = '8.8.8.8',
                hostname = 'dns.google',
                domain = 'google.com',
                location = ipgeolocation.models.location.Location(
                    continent_code = 'NA', 
                    continent_name = 'North America', 
                    country_code2 = 'US', 
                    country_code3 = 'USA', 
                    country_name = 'United States', 
                    country_name_official = 'United States of America', 
                    country_capital = 'Washington, D.C.', 
                    state_prov = 'California', 
                    state_code = 'US-CA', 
                    district = 'Santa Clara', 
                    city = 'Mountain View', 
                    zipcode = '94043-1351', 
                    latitude = '37.42240', 
                    longitude = '-122.08421', 
                    is_eu = False, 
                    country_flag = 'https://ipgeolocation.io/static/flags/us_64.png', 
                    geoname_id = '6301403', 
                    country_emoji = '', 
                    accuracy_radius = '1000', 
                    locality = 'Mountain View', 
                    dma_code = '807', ),
                country_metadata = ipgeolocation.models.country_metadata.CountryMetadata(
                    calling_code = '+1', 
                    tld = '.us', 
                    languages = ["en-US","es-US","haw","fr"], ),
                network = ipgeolocation.models.network.Network(
                    asn = ipgeolocation.models.network_asn.NetworkAsn(
                        as_number = 'AS15169', 
                        organization = 'Google LLC', 
                        country = 'US', 
                        asn_name = 'GOOGLE', 
                        type = 'isp', 
                        domain = 'about.google', 
                        date_allocated = '', 
                        allocation_status = 'Assigned', 
                        num_of_ipv4_routes = '1099', 
                        num_of_ipv6_routes = '107', 
                        rir = 'ARIN', ), 
                    connection_type = 'wired', 
                    company = ipgeolocation.models.network_company.NetworkCompany(
                        name = 'Google LLC', 
                        type = 'hosting', 
                        domain = 'google.com', ), ),
                currency = ipgeolocation.models.currency.Currency(
                    code = 'USD', 
                    name = 'US Dollar', 
                    symbol = '$', ),
                security = ipgeolocation.models.security.Security(
                    threat_score = 80, 
                    is_tor = False, 
                    is_proxy = True, 
                    proxy_type = 'VPN', 
                    proxy_provider = '', 
                    is_anonymous = True, 
                    is_known_attacker = True, 
                    is_spam = False, 
                    is_bot = False, 
                    is_cloud_provider = False, 
                    cloud_provider = '', ),
                abuse = ipgeolocation.models.abuse.Abuse(
                    route = '8.8.8.0/24', 
                    country = 'US', 
                    handle = 'ABUSE5250-ARIN', 
                    name = 'Abuse', 
                    organization = 'Abuse', 
                    role = 'abuse', 
                    kind = 'group', 
                    address = '1600 Amphitheatre Parkway
Mountain View
CA
94043
United States', 
                    emails = ["network-abuse@google.com"], 
                    phone_numbers = ["+1-650-253-0000"], ),
                time_zone = ipgeolocation.models.time_zone.TimeZone(
                    name = 'America/Los_Angeles', 
                    offset = -8, 
                    offset_with_dst = -7, 
                    current_time = '2025-04-22 06:19:40.951-0700', 
                    current_time_unix = 1745327980.951, 
                    is_dst = True, 
                    dst_savings = 1, 
                    dst_exists = True, 
                    dst_start = ipgeolocation.models.time_zone_dst_start.TimeZoneDstStart(
                        utc_time = '2025-03-09 TIME 10', 
                        duration = '+1H', 
                        gap = True, 
                        date_time_after = '2025-03-09 TIME 03', 
                        date_time_before = '2025-03-09 TIME 02', 
                        overlap = False, ), 
                    dst_end = ipgeolocation.models.time_zone_dst_end.TimeZoneDstEnd(
                        utc_time = '2025-11-02 TIME 09', 
                        duration = '-1H', 
                        gap = False, 
                        date_time_after = '2025-11-02 TIME 01', 
                        date_time_before = '2025-11-02 TIME 02', 
                        overlap = True, ), ),
                user_agent = {"user_agent_string":"Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_2) AppleWebKit/601.3.9 (KHTML, like Gecko) Version/9.0.2 Safari/601.3.9","name":"Safari","type":"Browser","version":"9.0.2","version_major":"9","device":{"name":"Apple Macintosh","type":"Desktop","brand":"Apple","cpu":"Intel"},"engine":{"name":"AppleWebKit","type":"Browser","version":"601.3.9","version_major":"601"},"operating_system":{"name":"Mac OS","type":"Desktop","version":"10.11.2","version_major":"10.11","build":"??"}}
            )
        else:
            return GeolocationXMLResponse(
        )
        """

    def testGeolocationXMLResponse(self):
        """Test GeolocationXMLResponse"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
