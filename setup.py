# coding: utf-8

"""
    IPGeolocation.io - IP intelligence products

    Ipgeolocation provides a set of APIs to make ip based decisions.

    Creat a free account by signing up here:
    https://app.ipgeolocation.io/signup

    Do not edit the class manually.
"""  # noqa: E501


from setuptools import setup, find_packages  # noqa: H301

# To install the library, run the following
#
# python setup.py install
#
# prerequisite: setuptools
# http://pypi.python.org/pypi/setuptools
NAME = "ipgeolocationio"
VERSION = "1.0.0"
PYTHON_REQUIRES = ">= 3.9"
REQUIRES = [
    "urllib3 >= 2.1.0, < 3.0.0",
    "python-dateutil >= 2.8.2",
    "pydantic >= 2",
    "typing-extensions >= 4.7.1",
]

setup(
    name=NAME,
    version=VERSION,
    description="IPGeolocation.io - IP intelligence products",
    author="IPGeolocation.io Teams",
    author_email="support@ipgeolocation.io",
    url="",
    keywords=["ipgeolocation", "ip location api", "location api", "IPGeolocation.io - IP intelligence products"],
    install_requires=REQUIRES,
    packages=find_packages(exclude=["test", "test_api"]),
    include_package_data=True,
    long_description_content_type='text/markdown',
    long_description="""\
    Ipgeolocation provides a set of APIs to make ip based decisions.
    """,  # noqa: E501
    package_data={"ipgeolocation": ["py.typed"]},
)