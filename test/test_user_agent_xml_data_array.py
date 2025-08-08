# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from ipgeolocation.models.user_agent_xml_data_array import UserAgentXMLDataArray

class TestUserAgentXMLDataArray(unittest.TestCase):
    """UserAgentXMLDataArray unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> UserAgentXMLDataArray:
        """Test UserAgentXMLDataArray
            include_optional is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `UserAgentXMLDataArray`
        """
        model = UserAgentXMLDataArray()
        if include_optional:
            return UserAgentXMLDataArray(
                user_agent_string = '',
                name = '',
                type = '',
                version = '',
                version_major = '',
                device = ipgeolocation.models.user_agent_data_device.UserAgentData_device(
                    name = '', 
                    type = '', 
                    brand = '', 
                    cpu = '', ),
                engine = ipgeolocation.models.user_agent_data_engine.UserAgentData_engine(
                    name = '', 
                    type = '', 
                    version = '', 
                    version_major = '', ),
                operating_system = ipgeolocation.models.user_agent_data_operating_system.UserAgentData_operating_system(
                    name = '', 
                    type = '', 
                    version = '', 
                    version_major = '', 
                    build = '', )
            )
        else:
            return UserAgentXMLDataArray(
        )
        """

    def testUserAgentXMLDataArray(self):
        """Test UserAgentXMLDataArray"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
