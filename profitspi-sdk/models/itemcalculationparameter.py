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


class Itemcalculationparameter(object):
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
        'parameter_name': 'str',
        'parameter_value': 'str',
        'datatype': 'str'
    }

    attribute_map = {
        'parameter_name': 'parameter_name',
        'parameter_value': 'parameter_value',
        'datatype': 'datatype'
    }

    def __init__(self, parameter_name=None, parameter_value=None, datatype=None, _configuration=None):  # noqa: E501
        """Itemcalculationparameter - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._parameter_name = None
        self._parameter_value = None
        self._datatype = None
        self.discriminator = None

        if parameter_name is not None:
            self.parameter_name = parameter_name
        if parameter_value is not None:
            self.parameter_value = parameter_value
        if datatype is not None:
            self.datatype = datatype

    @property
    def parameter_name(self):
        """Gets the parameter_name of this Itemcalculationparameter.  # noqa: E501


        :return: The parameter_name of this Itemcalculationparameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """Sets the parameter_name of this Itemcalculationparameter.


        :param parameter_name: The parameter_name of this Itemcalculationparameter.  # noqa: E501
        :type: str
        """

        self._parameter_name = parameter_name

    @property
    def parameter_value(self):
        """Gets the parameter_value of this Itemcalculationparameter.  # noqa: E501


        :return: The parameter_value of this Itemcalculationparameter.  # noqa: E501
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        """Sets the parameter_value of this Itemcalculationparameter.


        :param parameter_value: The parameter_value of this Itemcalculationparameter.  # noqa: E501
        :type: str
        """

        self._parameter_value = parameter_value

    @property
    def datatype(self):
        """Gets the datatype of this Itemcalculationparameter.  # noqa: E501


        :return: The datatype of this Itemcalculationparameter.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this Itemcalculationparameter.


        :param datatype: The datatype of this Itemcalculationparameter.  # noqa: E501
        :type: str
        """

        self._datatype = datatype

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
        if issubclass(Itemcalculationparameter, dict):
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
        if not isinstance(other, Itemcalculationparameter):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Itemcalculationparameter):
            return True

        return self.to_dict() != other.to_dict()
