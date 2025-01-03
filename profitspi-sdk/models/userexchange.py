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


class Userexchange(object):
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
        'exchange_id': 'str',
        'exchange': 'str',
        'exchange_description': 'str',
        'exchange_has_subtypes': 'bool',
        'is_corporate_exchange': 'bool'
    }

    attribute_map = {
        'exchange_id': 'exchange_id',
        'exchange': 'exchange',
        'exchange_description': 'exchange_description',
        'exchange_has_subtypes': 'exchange_has_subtypes',
        'is_corporate_exchange': 'is_corporate_exchange'
    }

    def __init__(self, exchange_id=None, exchange=None, exchange_description=None, exchange_has_subtypes=None, is_corporate_exchange=None, _configuration=None):  # noqa: E501
        """Userexchange - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._exchange_id = None
        self._exchange = None
        self._exchange_description = None
        self._exchange_has_subtypes = None
        self._is_corporate_exchange = None
        self.discriminator = None

        if exchange_id is not None:
            self.exchange_id = exchange_id
        if exchange is not None:
            self.exchange = exchange
        if exchange_description is not None:
            self.exchange_description = exchange_description
        if exchange_has_subtypes is not None:
            self.exchange_has_subtypes = exchange_has_subtypes
        if is_corporate_exchange is not None:
            self.is_corporate_exchange = is_corporate_exchange

    @property
    def exchange_id(self):
        """Gets the exchange_id of this Userexchange.  # noqa: E501


        :return: The exchange_id of this Userexchange.  # noqa: E501
        :rtype: str
        """
        return self._exchange_id

    @exchange_id.setter
    def exchange_id(self, exchange_id):
        """Sets the exchange_id of this Userexchange.


        :param exchange_id: The exchange_id of this Userexchange.  # noqa: E501
        :type: str
        """

        self._exchange_id = exchange_id

    @property
    def exchange(self):
        """Gets the exchange of this Userexchange.  # noqa: E501


        :return: The exchange of this Userexchange.  # noqa: E501
        :rtype: str
        """
        return self._exchange

    @exchange.setter
    def exchange(self, exchange):
        """Sets the exchange of this Userexchange.


        :param exchange: The exchange of this Userexchange.  # noqa: E501
        :type: str
        """

        self._exchange = exchange

    @property
    def exchange_description(self):
        """Gets the exchange_description of this Userexchange.  # noqa: E501


        :return: The exchange_description of this Userexchange.  # noqa: E501
        :rtype: str
        """
        return self._exchange_description

    @exchange_description.setter
    def exchange_description(self, exchange_description):
        """Sets the exchange_description of this Userexchange.


        :param exchange_description: The exchange_description of this Userexchange.  # noqa: E501
        :type: str
        """

        self._exchange_description = exchange_description

    @property
    def exchange_has_subtypes(self):
        """Gets the exchange_has_subtypes of this Userexchange.  # noqa: E501


        :return: The exchange_has_subtypes of this Userexchange.  # noqa: E501
        :rtype: bool
        """
        return self._exchange_has_subtypes

    @exchange_has_subtypes.setter
    def exchange_has_subtypes(self, exchange_has_subtypes):
        """Sets the exchange_has_subtypes of this Userexchange.


        :param exchange_has_subtypes: The exchange_has_subtypes of this Userexchange.  # noqa: E501
        :type: bool
        """

        self._exchange_has_subtypes = exchange_has_subtypes

    @property
    def is_corporate_exchange(self):
        """Gets the is_corporate_exchange of this Userexchange.  # noqa: E501


        :return: The is_corporate_exchange of this Userexchange.  # noqa: E501
        :rtype: bool
        """
        return self._is_corporate_exchange

    @is_corporate_exchange.setter
    def is_corporate_exchange(self, is_corporate_exchange):
        """Sets the is_corporate_exchange of this Userexchange.


        :param is_corporate_exchange: The is_corporate_exchange of this Userexchange.  # noqa: E501
        :type: bool
        """

        self._is_corporate_exchange = is_corporate_exchange

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
        if issubclass(Userexchange, dict):
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
        if not isinstance(other, Userexchange):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Userexchange):
            return True

        return self.to_dict() != other.to_dict()
