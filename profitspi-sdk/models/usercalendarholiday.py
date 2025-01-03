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


class Usercalendarholiday(object):
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
        'calendar_id': 'int',
        'holiday_date': 'datetime',
        'is_not_auto_maintained': 'bool'
    }

    attribute_map = {
        'calendar_id': 'calendar_id',
        'holiday_date': 'holiday_date',
        'is_not_auto_maintained': 'is_not_auto_maintained'
    }

    def __init__(self, calendar_id=None, holiday_date=None, is_not_auto_maintained=None, _configuration=None):  # noqa: E501
        """Usercalendarholiday - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._calendar_id = None
        self._holiday_date = None
        self._is_not_auto_maintained = None
        self.discriminator = None

        if calendar_id is not None:
            self.calendar_id = calendar_id
        if holiday_date is not None:
            self.holiday_date = holiday_date
        if is_not_auto_maintained is not None:
            self.is_not_auto_maintained = is_not_auto_maintained

    @property
    def calendar_id(self):
        """Gets the calendar_id of this Usercalendarholiday.  # noqa: E501


        :return: The calendar_id of this Usercalendarholiday.  # noqa: E501
        :rtype: int
        """
        return self._calendar_id

    @calendar_id.setter
    def calendar_id(self, calendar_id):
        """Sets the calendar_id of this Usercalendarholiday.


        :param calendar_id: The calendar_id of this Usercalendarholiday.  # noqa: E501
        :type: int
        """

        self._calendar_id = calendar_id

    @property
    def holiday_date(self):
        """Gets the holiday_date of this Usercalendarholiday.  # noqa: E501


        :return: The holiday_date of this Usercalendarholiday.  # noqa: E501
        :rtype: datetime
        """
        return self._holiday_date

    @holiday_date.setter
    def holiday_date(self, holiday_date):
        """Sets the holiday_date of this Usercalendarholiday.


        :param holiday_date: The holiday_date of this Usercalendarholiday.  # noqa: E501
        :type: datetime
        """

        self._holiday_date = holiday_date

    @property
    def is_not_auto_maintained(self):
        """Gets the is_not_auto_maintained of this Usercalendarholiday.  # noqa: E501


        :return: The is_not_auto_maintained of this Usercalendarholiday.  # noqa: E501
        :rtype: bool
        """
        return self._is_not_auto_maintained

    @is_not_auto_maintained.setter
    def is_not_auto_maintained(self, is_not_auto_maintained):
        """Sets the is_not_auto_maintained of this Usercalendarholiday.


        :param is_not_auto_maintained: The is_not_auto_maintained of this Usercalendarholiday.  # noqa: E501
        :type: bool
        """

        self._is_not_auto_maintained = is_not_auto_maintained

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
        if issubclass(Usercalendarholiday, dict):
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
        if not isinstance(other, Usercalendarholiday):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Usercalendarholiday):
            return True

        return self.to_dict() != other.to_dict()
