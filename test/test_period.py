# coding: utf-8

"""
    Profitspi API v1

    <div><p>Welcome to the Profitspi.com API v1 Beta. Here you will find a complete description of all the current APIs. Please check back regularly as we continue to roll-out new functions.</p><p>For example, to retrieve the list of default screens use https://www.profitspi.com/api/v1/defaultscreens?api_key={api_key}&user_id={user_id}.</p> <p>Functions will return JSON or XML depending on an Accept header setting of 'application/json' or 'application/xml' respectively, with JSON being the default. The Instruments functions can also return CSV for an Accept header setting of 'text/csv'. As an alternative to an Accept header add a query parameter of 'format='JSON|XML|CSV'.</p></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import profitspi-sdk
from profitspi-sdk.models.period import Period  # noqa: E501
from profitspi-sdk.rest import ApiException


class TestPeriod(unittest.TestCase):
    """Period unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testPeriod(self):
        """Test Period"""
        # FIXME: construct object with mandatory attributes with example values
        # model = profitspi-sdk.models.period.Period()  # noqa: E501
        pass


if __name__ == '__main__':
    unittest.main()