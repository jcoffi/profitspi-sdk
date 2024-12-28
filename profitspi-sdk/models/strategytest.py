# coding: utf-8

"""
    Profitspi API v1

    <div><p>Welcome to the Profitspi.com API v1 Beta. Here you will find a complete description of all the current APIs. Please check back regularly as we continue to roll-out new functions.</p><p>For example, to retrieve the list of default screens use https://www.profitspi.com/api/v1/defaultscreens?api_key={api_key}&user_id={user_id}.</p> <p>Functions will return JSON or XML depending on an Accept header setting of 'application/json' or 'application/xml' respectively, with JSON being the default. The Instruments functions can also return CSV for an Accept header setting of 'text/csv'. As an alternative to an Accept header add a query parameter of 'format='JSON|XML|CSV'.</p></div>  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six

from profitspi-sdk.configuration import Configuration


class Strategytest(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    """

    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'strategy_id': 'int',
        'test_num': 'int',
        'name': 'str',
        'run_datetime': 'datetime',
        'test_status': 'str',
        'percent_complete': 'float',
        'criteria_definition': 'Strategytestcriteria',
        'test_settings': 'Strategytestsettings',
        'test_results': 'Strategytestresults'
    }

    attribute_map = {
        'strategy_id': 'strategy_id',
        'test_num': 'test_num',
        'name': 'name',
        'run_datetime': 'run_datetime',
        'test_status': 'test_status',
        'percent_complete': 'percent_complete',
        'criteria_definition': 'criteria_definition',
        'test_settings': 'test_settings',
        'test_results': 'test_results'
    }

    def __init__(self, strategy_id=None, test_num=None, name=None, run_datetime=None, test_status=None, percent_complete=None, criteria_definition=None, test_settings=None, test_results=None, _configuration=None):  # noqa: E501
        """Strategytest - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._strategy_id = None
        self._test_num = None
        self._name = None
        self._run_datetime = None
        self._test_status = None
        self._percent_complete = None
        self._criteria_definition = None
        self._test_settings = None
        self._test_results = None
        self.discriminator = None

        if strategy_id is not None:
            self.strategy_id = strategy_id
        if test_num is not None:
            self.test_num = test_num
        if name is not None:
            self.name = name
        if run_datetime is not None:
            self.run_datetime = run_datetime
        if test_status is not None:
            self.test_status = test_status
        if percent_complete is not None:
            self.percent_complete = percent_complete
        if criteria_definition is not None:
            self.criteria_definition = criteria_definition
        if test_settings is not None:
            self.test_settings = test_settings
        if test_results is not None:
            self.test_results = test_results

    @property
    def strategy_id(self):
        """Gets the strategy_id of this Strategytest.  # noqa: E501


        :return: The strategy_id of this Strategytest.  # noqa: E501
        :rtype: int
        """
        return self._strategy_id

    @strategy_id.setter
    def strategy_id(self, strategy_id):
        """Sets the strategy_id of this Strategytest.


        :param strategy_id: The strategy_id of this Strategytest.  # noqa: E501
        :type: int
        """

        self._strategy_id = strategy_id

    @property
    def test_num(self):
        """Gets the test_num of this Strategytest.  # noqa: E501


        :return: The test_num of this Strategytest.  # noqa: E501
        :rtype: int
        """
        return self._test_num

    @test_num.setter
    def test_num(self, test_num):
        """Sets the test_num of this Strategytest.


        :param test_num: The test_num of this Strategytest.  # noqa: E501
        :type: int
        """

        self._test_num = test_num

    @property
    def name(self):
        """Gets the name of this Strategytest.  # noqa: E501


        :return: The name of this Strategytest.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Strategytest.


        :param name: The name of this Strategytest.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def run_datetime(self):
        """Gets the run_datetime of this Strategytest.  # noqa: E501


        :return: The run_datetime of this Strategytest.  # noqa: E501
        :rtype: datetime
        """
        return self._run_datetime

    @run_datetime.setter
    def run_datetime(self, run_datetime):
        """Sets the run_datetime of this Strategytest.


        :param run_datetime: The run_datetime of this Strategytest.  # noqa: E501
        :type: datetime
        """

        self._run_datetime = run_datetime

    @property
    def test_status(self):
        """Gets the test_status of this Strategytest.  # noqa: E501


        :return: The test_status of this Strategytest.  # noqa: E501
        :rtype: str
        """
        return self._test_status

    @test_status.setter
    def test_status(self, test_status):
        """Sets the test_status of this Strategytest.


        :param test_status: The test_status of this Strategytest.  # noqa: E501
        :type: str
        """

        self._test_status = test_status

    @property
    def percent_complete(self):
        """Gets the percent_complete of this Strategytest.  # noqa: E501


        :return: The percent_complete of this Strategytest.  # noqa: E501
        :rtype: float
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """Sets the percent_complete of this Strategytest.


        :param percent_complete: The percent_complete of this Strategytest.  # noqa: E501
        :type: float
        """

        self._percent_complete = percent_complete

    @property
    def criteria_definition(self):
        """Gets the criteria_definition of this Strategytest.  # noqa: E501


        :return: The criteria_definition of this Strategytest.  # noqa: E501
        :rtype: Strategytestcriteria
        """
        return self._criteria_definition

    @criteria_definition.setter
    def criteria_definition(self, criteria_definition):
        """Sets the criteria_definition of this Strategytest.


        :param criteria_definition: The criteria_definition of this Strategytest.  # noqa: E501
        :type: Strategytestcriteria
        """

        self._criteria_definition = criteria_definition

    @property
    def test_settings(self):
        """Gets the test_settings of this Strategytest.  # noqa: E501


        :return: The test_settings of this Strategytest.  # noqa: E501
        :rtype: Strategytestsettings
        """
        return self._test_settings

    @test_settings.setter
    def test_settings(self, test_settings):
        """Sets the test_settings of this Strategytest.


        :param test_settings: The test_settings of this Strategytest.  # noqa: E501
        :type: Strategytestsettings
        """

        self._test_settings = test_settings

    @property
    def test_results(self):
        """Gets the test_results of this Strategytest.  # noqa: E501


        :return: The test_results of this Strategytest.  # noqa: E501
        :rtype: Strategytestresults
        """
        return self._test_results

    @test_results.setter
    def test_results(self, test_results):
        """Sets the test_results of this Strategytest.


        :param test_results: The test_results of this Strategytest.  # noqa: E501
        :type: Strategytestresults
        """

        self._test_results = test_results

    def to_dict(self):
        """Returns the model properties as a dict"""
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value
        if issubclass(Strategytest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, Strategytest):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Strategytest):
            return True

        return self.to_dict() != other.to_dict()
