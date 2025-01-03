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


class Criteriapair(object):
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
        'is_active': 'bool',
        'and_or': 'str',
        'left_bracket': 'str',
        'left_item': 'Itemdefinition',
        'condition_id': 'str',
        'condition': 'str',
        'right_value': 'str',
        'right_item': 'Itemdefinition',
        'right_bars': 'int',
        'right_bracket': 'str'
    }

    attribute_map = {
        'is_active': 'is_active',
        'and_or': 'and_or',
        'left_bracket': 'left_bracket',
        'left_item': 'left_item',
        'condition_id': 'condition_id',
        'condition': 'condition',
        'right_value': 'right_value',
        'right_item': 'right_item',
        'right_bars': 'right_bars',
        'right_bracket': 'right_bracket'
    }

    def __init__(self, is_active=None, and_or=None, left_bracket=None, left_item=None, condition_id=None, condition=None, right_value=None, right_item=None, right_bars=None, right_bracket=None, _configuration=None):  # noqa: E501
        """Criteriapair - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._is_active = None
        self._and_or = None
        self._left_bracket = None
        self._left_item = None
        self._condition_id = None
        self._condition = None
        self._right_value = None
        self._right_item = None
        self._right_bars = None
        self._right_bracket = None
        self.discriminator = None

        if is_active is not None:
            self.is_active = is_active
        if and_or is not None:
            self.and_or = and_or
        if left_bracket is not None:
            self.left_bracket = left_bracket
        if left_item is not None:
            self.left_item = left_item
        if condition_id is not None:
            self.condition_id = condition_id
        if condition is not None:
            self.condition = condition
        if right_value is not None:
            self.right_value = right_value
        if right_item is not None:
            self.right_item = right_item
        if right_bars is not None:
            self.right_bars = right_bars
        if right_bracket is not None:
            self.right_bracket = right_bracket

    @property
    def is_active(self):
        """Gets the is_active of this Criteriapair.  # noqa: E501


        :return: The is_active of this Criteriapair.  # noqa: E501
        :rtype: bool
        """
        return self._is_active

    @is_active.setter
    def is_active(self, is_active):
        """Sets the is_active of this Criteriapair.


        :param is_active: The is_active of this Criteriapair.  # noqa: E501
        :type: bool
        """

        self._is_active = is_active

    @property
    def and_or(self):
        """Gets the and_or of this Criteriapair.  # noqa: E501


        :return: The and_or of this Criteriapair.  # noqa: E501
        :rtype: str
        """
        return self._and_or

    @and_or.setter
    def and_or(self, and_or):
        """Sets the and_or of this Criteriapair.


        :param and_or: The and_or of this Criteriapair.  # noqa: E501
        :type: str
        """

        self._and_or = and_or

    @property
    def left_bracket(self):
        """Gets the left_bracket of this Criteriapair.  # noqa: E501


        :return: The left_bracket of this Criteriapair.  # noqa: E501
        :rtype: str
        """
        return self._left_bracket

    @left_bracket.setter
    def left_bracket(self, left_bracket):
        """Sets the left_bracket of this Criteriapair.


        :param left_bracket: The left_bracket of this Criteriapair.  # noqa: E501
        :type: str
        """

        self._left_bracket = left_bracket

    @property
    def left_item(self):
        """Gets the left_item of this Criteriapair.  # noqa: E501


        :return: The left_item of this Criteriapair.  # noqa: E501
        :rtype: Itemdefinition
        """
        return self._left_item

    @left_item.setter
    def left_item(self, left_item):
        """Sets the left_item of this Criteriapair.


        :param left_item: The left_item of this Criteriapair.  # noqa: E501
        :type: Itemdefinition
        """

        self._left_item = left_item

    @property
    def condition_id(self):
        """Gets the condition_id of this Criteriapair.  # noqa: E501


        :return: The condition_id of this Criteriapair.  # noqa: E501
        :rtype: str
        """
        return self._condition_id

    @condition_id.setter
    def condition_id(self, condition_id):
        """Sets the condition_id of this Criteriapair.


        :param condition_id: The condition_id of this Criteriapair.  # noqa: E501
        :type: str
        """

        self._condition_id = condition_id

    @property
    def condition(self):
        """Gets the condition of this Criteriapair.  # noqa: E501


        :return: The condition of this Criteriapair.  # noqa: E501
        :rtype: str
        """
        return self._condition

    @condition.setter
    def condition(self, condition):
        """Sets the condition of this Criteriapair.


        :param condition: The condition of this Criteriapair.  # noqa: E501
        :type: str
        """

        self._condition = condition

    @property
    def right_value(self):
        """Gets the right_value of this Criteriapair.  # noqa: E501


        :return: The right_value of this Criteriapair.  # noqa: E501
        :rtype: str
        """
        return self._right_value

    @right_value.setter
    def right_value(self, right_value):
        """Sets the right_value of this Criteriapair.


        :param right_value: The right_value of this Criteriapair.  # noqa: E501
        :type: str
        """

        self._right_value = right_value

    @property
    def right_item(self):
        """Gets the right_item of this Criteriapair.  # noqa: E501


        :return: The right_item of this Criteriapair.  # noqa: E501
        :rtype: Itemdefinition
        """
        return self._right_item

    @right_item.setter
    def right_item(self, right_item):
        """Sets the right_item of this Criteriapair.


        :param right_item: The right_item of this Criteriapair.  # noqa: E501
        :type: Itemdefinition
        """

        self._right_item = right_item

    @property
    def right_bars(self):
        """Gets the right_bars of this Criteriapair.  # noqa: E501


        :return: The right_bars of this Criteriapair.  # noqa: E501
        :rtype: int
        """
        return self._right_bars

    @right_bars.setter
    def right_bars(self, right_bars):
        """Sets the right_bars of this Criteriapair.


        :param right_bars: The right_bars of this Criteriapair.  # noqa: E501
        :type: int
        """

        self._right_bars = right_bars

    @property
    def right_bracket(self):
        """Gets the right_bracket of this Criteriapair.  # noqa: E501


        :return: The right_bracket of this Criteriapair.  # noqa: E501
        :rtype: str
        """
        return self._right_bracket

    @right_bracket.setter
    def right_bracket(self, right_bracket):
        """Sets the right_bracket of this Criteriapair.


        :param right_bracket: The right_bracket of this Criteriapair.  # noqa: E501
        :type: str
        """

        self._right_bracket = right_bracket

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
        if issubclass(Criteriapair, dict):
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
        if not isinstance(other, Criteriapair):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Criteriapair):
            return True

        return self.to_dict() != other.to_dict()
