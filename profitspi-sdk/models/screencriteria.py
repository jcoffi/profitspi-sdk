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


class Screencriteria(object):
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
        'instrument_group_text': 'str',
        'include_instrument_group_id': 'str',
        'include_instrument_group': 'str',
        'include_instrument_group_item_ids': 'str',
        'include_instrument_group_item_subtype_id': 'str',
        'include_instrument_group_item_subtype': 'str',
        'exclude_instrument_group_id': 'str',
        'exclude_instrument_group': 'str',
        'exclude_instrument_group_item_ids': 'str',
        'criteria_text': 'str',
        'criteria_pairs': 'list[Criteriapair]',
        'criteria_items': 'list[Criteriaitem]'
    }

    attribute_map = {
        'instrument_group_text': 'instrument_group_text',
        'include_instrument_group_id': 'include_instrument_group_id',
        'include_instrument_group': 'include_instrument_group',
        'include_instrument_group_item_ids': 'include_instrument_group_item_ids',
        'include_instrument_group_item_subtype_id': 'include_instrument_group_item_subtype_id',
        'include_instrument_group_item_subtype': 'include_instrument_group_item_subtype',
        'exclude_instrument_group_id': 'exclude_instrument_group_id',
        'exclude_instrument_group': 'exclude_instrument_group',
        'exclude_instrument_group_item_ids': 'exclude_instrument_group_item_ids',
        'criteria_text': 'criteria_text',
        'criteria_pairs': 'criteria_pairs',
        'criteria_items': 'criteria_items'
    }

    def __init__(self, instrument_group_text=None, include_instrument_group_id=None, include_instrument_group=None, include_instrument_group_item_ids=None, include_instrument_group_item_subtype_id=None, include_instrument_group_item_subtype=None, exclude_instrument_group_id=None, exclude_instrument_group=None, exclude_instrument_group_item_ids=None, criteria_text=None, criteria_pairs=None, criteria_items=None, _configuration=None):  # noqa: E501
        """Screencriteria - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._instrument_group_text = None
        self._include_instrument_group_id = None
        self._include_instrument_group = None
        self._include_instrument_group_item_ids = None
        self._include_instrument_group_item_subtype_id = None
        self._include_instrument_group_item_subtype = None
        self._exclude_instrument_group_id = None
        self._exclude_instrument_group = None
        self._exclude_instrument_group_item_ids = None
        self._criteria_text = None
        self._criteria_pairs = None
        self._criteria_items = None
        self.discriminator = None

        if instrument_group_text is not None:
            self.instrument_group_text = instrument_group_text
        if include_instrument_group_id is not None:
            self.include_instrument_group_id = include_instrument_group_id
        if include_instrument_group is not None:
            self.include_instrument_group = include_instrument_group
        if include_instrument_group_item_ids is not None:
            self.include_instrument_group_item_ids = include_instrument_group_item_ids
        if include_instrument_group_item_subtype_id is not None:
            self.include_instrument_group_item_subtype_id = include_instrument_group_item_subtype_id
        if include_instrument_group_item_subtype is not None:
            self.include_instrument_group_item_subtype = include_instrument_group_item_subtype
        if exclude_instrument_group_id is not None:
            self.exclude_instrument_group_id = exclude_instrument_group_id
        if exclude_instrument_group is not None:
            self.exclude_instrument_group = exclude_instrument_group
        if exclude_instrument_group_item_ids is not None:
            self.exclude_instrument_group_item_ids = exclude_instrument_group_item_ids
        if criteria_text is not None:
            self.criteria_text = criteria_text
        if criteria_pairs is not None:
            self.criteria_pairs = criteria_pairs
        if criteria_items is not None:
            self.criteria_items = criteria_items

    @property
    def instrument_group_text(self):
        """Gets the instrument_group_text of this Screencriteria.  # noqa: E501


        :return: The instrument_group_text of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._instrument_group_text

    @instrument_group_text.setter
    def instrument_group_text(self, instrument_group_text):
        """Sets the instrument_group_text of this Screencriteria.


        :param instrument_group_text: The instrument_group_text of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._instrument_group_text = instrument_group_text

    @property
    def include_instrument_group_id(self):
        """Gets the include_instrument_group_id of this Screencriteria.  # noqa: E501


        :return: The include_instrument_group_id of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._include_instrument_group_id

    @include_instrument_group_id.setter
    def include_instrument_group_id(self, include_instrument_group_id):
        """Sets the include_instrument_group_id of this Screencriteria.


        :param include_instrument_group_id: The include_instrument_group_id of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._include_instrument_group_id = include_instrument_group_id

    @property
    def include_instrument_group(self):
        """Gets the include_instrument_group of this Screencriteria.  # noqa: E501


        :return: The include_instrument_group of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._include_instrument_group

    @include_instrument_group.setter
    def include_instrument_group(self, include_instrument_group):
        """Sets the include_instrument_group of this Screencriteria.


        :param include_instrument_group: The include_instrument_group of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._include_instrument_group = include_instrument_group

    @property
    def include_instrument_group_item_ids(self):
        """Gets the include_instrument_group_item_ids of this Screencriteria.  # noqa: E501


        :return: The include_instrument_group_item_ids of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._include_instrument_group_item_ids

    @include_instrument_group_item_ids.setter
    def include_instrument_group_item_ids(self, include_instrument_group_item_ids):
        """Sets the include_instrument_group_item_ids of this Screencriteria.


        :param include_instrument_group_item_ids: The include_instrument_group_item_ids of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._include_instrument_group_item_ids = include_instrument_group_item_ids

    @property
    def include_instrument_group_item_subtype_id(self):
        """Gets the include_instrument_group_item_subtype_id of this Screencriteria.  # noqa: E501


        :return: The include_instrument_group_item_subtype_id of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._include_instrument_group_item_subtype_id

    @include_instrument_group_item_subtype_id.setter
    def include_instrument_group_item_subtype_id(self, include_instrument_group_item_subtype_id):
        """Sets the include_instrument_group_item_subtype_id of this Screencriteria.


        :param include_instrument_group_item_subtype_id: The include_instrument_group_item_subtype_id of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._include_instrument_group_item_subtype_id = include_instrument_group_item_subtype_id

    @property
    def include_instrument_group_item_subtype(self):
        """Gets the include_instrument_group_item_subtype of this Screencriteria.  # noqa: E501


        :return: The include_instrument_group_item_subtype of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._include_instrument_group_item_subtype

    @include_instrument_group_item_subtype.setter
    def include_instrument_group_item_subtype(self, include_instrument_group_item_subtype):
        """Sets the include_instrument_group_item_subtype of this Screencriteria.


        :param include_instrument_group_item_subtype: The include_instrument_group_item_subtype of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._include_instrument_group_item_subtype = include_instrument_group_item_subtype

    @property
    def exclude_instrument_group_id(self):
        """Gets the exclude_instrument_group_id of this Screencriteria.  # noqa: E501


        :return: The exclude_instrument_group_id of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._exclude_instrument_group_id

    @exclude_instrument_group_id.setter
    def exclude_instrument_group_id(self, exclude_instrument_group_id):
        """Sets the exclude_instrument_group_id of this Screencriteria.


        :param exclude_instrument_group_id: The exclude_instrument_group_id of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._exclude_instrument_group_id = exclude_instrument_group_id

    @property
    def exclude_instrument_group(self):
        """Gets the exclude_instrument_group of this Screencriteria.  # noqa: E501


        :return: The exclude_instrument_group of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._exclude_instrument_group

    @exclude_instrument_group.setter
    def exclude_instrument_group(self, exclude_instrument_group):
        """Sets the exclude_instrument_group of this Screencriteria.


        :param exclude_instrument_group: The exclude_instrument_group of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._exclude_instrument_group = exclude_instrument_group

    @property
    def exclude_instrument_group_item_ids(self):
        """Gets the exclude_instrument_group_item_ids of this Screencriteria.  # noqa: E501


        :return: The exclude_instrument_group_item_ids of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._exclude_instrument_group_item_ids

    @exclude_instrument_group_item_ids.setter
    def exclude_instrument_group_item_ids(self, exclude_instrument_group_item_ids):
        """Sets the exclude_instrument_group_item_ids of this Screencriteria.


        :param exclude_instrument_group_item_ids: The exclude_instrument_group_item_ids of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._exclude_instrument_group_item_ids = exclude_instrument_group_item_ids

    @property
    def criteria_text(self):
        """Gets the criteria_text of this Screencriteria.  # noqa: E501


        :return: The criteria_text of this Screencriteria.  # noqa: E501
        :rtype: str
        """
        return self._criteria_text

    @criteria_text.setter
    def criteria_text(self, criteria_text):
        """Sets the criteria_text of this Screencriteria.


        :param criteria_text: The criteria_text of this Screencriteria.  # noqa: E501
        :type: str
        """

        self._criteria_text = criteria_text

    @property
    def criteria_pairs(self):
        """Gets the criteria_pairs of this Screencriteria.  # noqa: E501


        :return: The criteria_pairs of this Screencriteria.  # noqa: E501
        :rtype: list[Criteriapair]
        """
        return self._criteria_pairs

    @criteria_pairs.setter
    def criteria_pairs(self, criteria_pairs):
        """Sets the criteria_pairs of this Screencriteria.


        :param criteria_pairs: The criteria_pairs of this Screencriteria.  # noqa: E501
        :type: list[Criteriapair]
        """

        self._criteria_pairs = criteria_pairs

    @property
    def criteria_items(self):
        """Gets the criteria_items of this Screencriteria.  # noqa: E501


        :return: The criteria_items of this Screencriteria.  # noqa: E501
        :rtype: list[Criteriaitem]
        """
        return self._criteria_items

    @criteria_items.setter
    def criteria_items(self, criteria_items):
        """Sets the criteria_items of this Screencriteria.


        :param criteria_items: The criteria_items of this Screencriteria.  # noqa: E501
        :type: list[Criteriaitem]
        """

        self._criteria_items = criteria_items

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
        if issubclass(Screencriteria, dict):
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
        if not isinstance(other, Screencriteria):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Screencriteria):
            return True

        return self.to_dict() != other.to_dict()
