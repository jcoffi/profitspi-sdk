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


class Userinstrumentsplit(object):
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
        'instrument': 'str',
        'split_date': 'datetime',
        'split_factor': 'float'
    }

    attribute_map = {
        'instrument': 'instrument',
        'split_date': 'split_date',
        'split_factor': 'split_factor'
    }

    def __init__(self, instrument=None, split_date=None, split_factor=None, _configuration=None):  # noqa: E501
        """Userinstrumentsplit - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instrument = None
        self._split_date = None
        self._split_factor = None
        self.discriminator = None

        if instrument is not None:
            self.instrument = instrument
        if split_date is not None:
            self.split_date = split_date
        if split_factor is not None:
            self.split_factor = split_factor

    @property
    def instrument(self):
        """Gets the instrument of this Userinstrumentsplit.  # noqa: E501


        :return: The instrument of this Userinstrumentsplit.  # noqa: E501
        :rtype: str
        """
        return self._instrument

    @instrument.setter
    def instrument(self, instrument):
        """Sets the instrument of this Userinstrumentsplit.


        :param instrument: The instrument of this Userinstrumentsplit.  # noqa: E501
        :type: str
        """

        self._instrument = instrument

    @property
    def split_date(self):
        """Gets the split_date of this Userinstrumentsplit.  # noqa: E501


        :return: The split_date of this Userinstrumentsplit.  # noqa: E501
        :rtype: datetime
        """
        return self._split_date

    @split_date.setter
    def split_date(self, split_date):
        """Sets the split_date of this Userinstrumentsplit.


        :param split_date: The split_date of this Userinstrumentsplit.  # noqa: E501
        :type: datetime
        """

        self._split_date = split_date

    @property
    def split_factor(self):
        """Gets the split_factor of this Userinstrumentsplit.  # noqa: E501


        :return: The split_factor of this Userinstrumentsplit.  # noqa: E501
        :rtype: float
        """
        return self._split_factor

    @split_factor.setter
    def split_factor(self, split_factor):
        """Sets the split_factor of this Userinstrumentsplit.


        :param split_factor: The split_factor of this Userinstrumentsplit.  # noqa: E501
        :type: float
        """

        self._split_factor = split_factor

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
        if issubclass(Userinstrumentsplit, dict):
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
        if not isinstance(other, Userinstrumentsplit):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Userinstrumentsplit):
            return True

        return self.to_dict() != other.to_dict()
