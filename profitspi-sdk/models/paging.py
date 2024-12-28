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


class Paging(object):
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
        'current_page': 'int',
        'next_page': 'int',
        'prev_page': 'int',
        'total_pages': 'int',
        'total_count': 'int'
    }

    attribute_map = {
        'current_page': 'current_page',
        'next_page': 'next_page',
        'prev_page': 'prev_page',
        'total_pages': 'total_pages',
        'total_count': 'total_count'
    }

    def __init__(self, current_page=None, next_page=None, prev_page=None, total_pages=None, total_count=None, _configuration=None):  # noqa: E501
        """Paging - a model defined in Swagger"""  # noqa: E501
        if _configuration is None:
            _configuration = Configuration()
        self._configuration = _configuration

        self._current_page = None
        self._next_page = None
        self._prev_page = None
        self._total_pages = None
        self._total_count = None
        self.discriminator = None

        if current_page is not None:
            self.current_page = current_page
        if next_page is not None:
            self.next_page = next_page
        if prev_page is not None:
            self.prev_page = prev_page
        if total_pages is not None:
            self.total_pages = total_pages
        if total_count is not None:
            self.total_count = total_count

    @property
    def current_page(self):
        """Gets the current_page of this Paging.  # noqa: E501


        :return: The current_page of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._current_page

    @current_page.setter
    def current_page(self, current_page):
        """Sets the current_page of this Paging.


        :param current_page: The current_page of this Paging.  # noqa: E501
        :type: int
        """

        self._current_page = current_page

    @property
    def next_page(self):
        """Gets the next_page of this Paging.  # noqa: E501


        :return: The next_page of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._next_page

    @next_page.setter
    def next_page(self, next_page):
        """Sets the next_page of this Paging.


        :param next_page: The next_page of this Paging.  # noqa: E501
        :type: int
        """

        self._next_page = next_page

    @property
    def prev_page(self):
        """Gets the prev_page of this Paging.  # noqa: E501


        :return: The prev_page of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._prev_page

    @prev_page.setter
    def prev_page(self, prev_page):
        """Sets the prev_page of this Paging.


        :param prev_page: The prev_page of this Paging.  # noqa: E501
        :type: int
        """

        self._prev_page = prev_page

    @property
    def total_pages(self):
        """Gets the total_pages of this Paging.  # noqa: E501


        :return: The total_pages of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._total_pages

    @total_pages.setter
    def total_pages(self, total_pages):
        """Sets the total_pages of this Paging.


        :param total_pages: The total_pages of this Paging.  # noqa: E501
        :type: int
        """

        self._total_pages = total_pages

    @property
    def total_count(self):
        """Gets the total_count of this Paging.  # noqa: E501


        :return: The total_count of this Paging.  # noqa: E501
        :rtype: int
        """
        return self._total_count

    @total_count.setter
    def total_count(self, total_count):
        """Sets the total_count of this Paging.


        :param total_count: The total_count of this Paging.  # noqa: E501
        :type: int
        """

        self._total_count = total_count

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
        if issubclass(Paging, dict):
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
        if not isinstance(other, Paging):
            return False

        return self.to_dict() == other.to_dict()

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        if not isinstance(other, Paging):
            return True

        return self.to_dict() != other.to_dict()
