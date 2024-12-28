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


class Screen(object):
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
        'screen_id': 'int',
        'name': 'str',
        'criteria_definition': 'Screencriteria',
        'additional_resultitems_definition': 'Additionalresultitems',
        'screen_results': 'Screenresults'
    }

    attribute_map = {
        'screen_id': 'screen_id',
        'name': 'name',
        'criteria_definition': 'criteria_definition',
        'additional_resultitems_definition': 'additional_resultitems_definition',
        'screen_results': 'screen_results'
    }

    def __init__(self, screen_id=None, name=None, criteria_definition=None, additional_resultitems_definition=None, screen_results=None, _configuration=None):  # noqa: E501
        """Screen - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._screen_id = None
        self._name = None
        self._criteria_definition = None
        self._additional_resultitems_definition = None
        self._screen_results = None
        self.discriminator = None

        if screen_id is not None:
            self.screen_id = screen_id
        if name is not None:
            self.name = name
        if criteria_definition is not None:
            self.criteria_definition = criteria_definition
        if additional_resultitems_definition is not None:
            self.additional_resultitems_definition = additional_resultitems_definition
        if screen_results is not None:
            self.screen_results = screen_results

    @property
    def screen_id(self):
        """Gets the screen_id of this Screen.  # noqa: E501


        :return: The screen_id of this Screen.  # noqa: E501
        :rtype: int
        """
        return self._screen_id

    @screen_id.setter
    def screen_id(self, screen_id):
        """Sets the screen_id of this Screen.


        :param screen_id: The screen_id of this Screen.  # noqa: E501
        :type: int
        """

        self._screen_id = screen_id

    @property
    def name(self):
        """Gets the name of this Screen.  # noqa: E501

        This is the Screen name.  # noqa: E501

        :return: The name of this Screen.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Screen.

        This is the Screen name.  # noqa: E501

        :param name: The name of this Screen.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def criteria_definition(self):
        """Gets the criteria_definition of this Screen.  # noqa: E501


        :return: The criteria_definition of this Screen.  # noqa: E501
        :rtype: Screencriteria
        """
        return self._criteria_definition

    @criteria_definition.setter
    def criteria_definition(self, criteria_definition):
        """Sets the criteria_definition of this Screen.


        :param criteria_definition: The criteria_definition of this Screen.  # noqa: E501
        :type: Screencriteria
        """

        self._criteria_definition = criteria_definition

    @property
    def additional_resultitems_definition(self):
        """Gets the additional_resultitems_definition of this Screen.  # noqa: E501


        :return: The additional_resultitems_definition of this Screen.  # noqa: E501
        :rtype: Additionalresultitems
        """
        return self._additional_resultitems_definition

    @additional_resultitems_definition.setter
    def additional_resultitems_definition(self, additional_resultitems_definition):
        """Sets the additional_resultitems_definition of this Screen.


        :param additional_resultitems_definition: The additional_resultitems_definition of this Screen.  # noqa: E501
        :type: Additionalresultitems
        """

        self._additional_resultitems_definition = additional_resultitems_definition

    @property
    def screen_results(self):
        """Gets the screen_results of this Screen.  # noqa: E501


        :return: The screen_results of this Screen.  # noqa: E501
        :rtype: Screenresults
        """
        return self._screen_results

    @screen_results.setter
    def screen_results(self, screen_results):
        """Sets the screen_results of this Screen.


        :param screen_results: The screen_results of this Screen.  # noqa: E501
        :type: Screenresults
        """

        self._screen_results = screen_results

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
        if issubclass(Screen, dict):
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
        if not isinstance(other, Screen):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Screen):
            return True

        return self.to_dict() != other.to_dict()
