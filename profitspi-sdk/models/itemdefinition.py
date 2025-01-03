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


class Itemdefinition(object):
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
        'description': 'str',
        'datatype': 'str',
        'item_calculations': 'list[Itemcalculation]'
    }

    attribute_map = {
        'description': 'description',
        'datatype': 'datatype',
        'item_calculations': 'item_calculations'
    }

    def __init__(self, description=None, datatype=None, item_calculations=None, _configuration=None):  # noqa: E501
        """Itemdefinition - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._description = None
        self._datatype = None
        self._item_calculations = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if datatype is not None:
            self.datatype = datatype
        if item_calculations is not None:
            self.item_calculations = item_calculations

    @property
    def description(self):
        """Gets the description of this Itemdefinition.  # noqa: E501


        :return: The description of this Itemdefinition.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Itemdefinition.


        :param description: The description of this Itemdefinition.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def datatype(self):
        """Gets the datatype of this Itemdefinition.  # noqa: E501


        :return: The datatype of this Itemdefinition.  # noqa: E501
        :rtype: str
        """
        return self._datatype

    @datatype.setter
    def datatype(self, datatype):
        """Sets the datatype of this Itemdefinition.


        :param datatype: The datatype of this Itemdefinition.  # noqa: E501
        :type: str
        """

        self._datatype = datatype

    @property
    def item_calculations(self):
        """Gets the item_calculations of this Itemdefinition.  # noqa: E501


        :return: The item_calculations of this Itemdefinition.  # noqa: E501
        :rtype: list[Itemcalculation]
        """
        return self._item_calculations

    @item_calculations.setter
    def item_calculations(self, item_calculations):
        """Sets the item_calculations of this Itemdefinition.


        :param item_calculations: The item_calculations of this Itemdefinition.  # noqa: E501
        :type: list[Itemcalculation]
        """

        self._item_calculations = item_calculations

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
        if issubclass(Itemdefinition, dict):
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
        if not isinstance(other, Itemdefinition):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Itemdefinition):
            return True

        return self.to_dict() != other.to_dict()
