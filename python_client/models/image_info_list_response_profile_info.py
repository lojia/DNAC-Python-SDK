# coding: utf-8

"""
    Swagger

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


import pprint
import re  # noqa: F401

import six


class ImageInfoListResponseProfileInfo(object):
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
        'extended_attributes': 'object',
        'memory': 'int',
        'product_type': 'str',
        'profile_name': 'str',
        'shares': 'int',
        'v_cpu': 'int'
    }

    attribute_map = {
        'description': 'description',
        'extended_attributes': 'extendedAttributes',
        'memory': 'memory',
        'product_type': 'productType',
        'profile_name': 'profileName',
        'shares': 'shares',
        'v_cpu': 'vCpu'
    }

    def __init__(self, description=None, extended_attributes=None, memory=None, product_type=None, profile_name=None, shares=None, v_cpu=None):  # noqa: E501
        """ImageInfoListResponseProfileInfo - a model defined in Swagger"""  # noqa: E501

        self._description = None
        self._extended_attributes = None
        self._memory = None
        self._product_type = None
        self._profile_name = None
        self._shares = None
        self._v_cpu = None
        self.discriminator = None

        if description is not None:
            self.description = description
        if extended_attributes is not None:
            self.extended_attributes = extended_attributes
        if memory is not None:
            self.memory = memory
        if product_type is not None:
            self.product_type = product_type
        if profile_name is not None:
            self.profile_name = profile_name
        if shares is not None:
            self.shares = shares
        if v_cpu is not None:
            self.v_cpu = v_cpu

    @property
    def description(self):
        """Gets the description of this ImageInfoListResponseProfileInfo.  # noqa: E501


        :return: The description of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ImageInfoListResponseProfileInfo.


        :param description: The description of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def extended_attributes(self):
        """Gets the extended_attributes of this ImageInfoListResponseProfileInfo.  # noqa: E501


        :return: The extended_attributes of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :rtype: object
        """
        return self._extended_attributes

    @extended_attributes.setter
    def extended_attributes(self, extended_attributes):
        """Sets the extended_attributes of this ImageInfoListResponseProfileInfo.


        :param extended_attributes: The extended_attributes of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :type: object
        """

        self._extended_attributes = extended_attributes

    @property
    def memory(self):
        """Gets the memory of this ImageInfoListResponseProfileInfo.  # noqa: E501


        :return: The memory of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :rtype: int
        """
        return self._memory

    @memory.setter
    def memory(self, memory):
        """Sets the memory of this ImageInfoListResponseProfileInfo.


        :param memory: The memory of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :type: int
        """

        self._memory = memory

    @property
    def product_type(self):
        """Gets the product_type of this ImageInfoListResponseProfileInfo.  # noqa: E501


        :return: The product_type of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._product_type

    @product_type.setter
    def product_type(self, product_type):
        """Sets the product_type of this ImageInfoListResponseProfileInfo.


        :param product_type: The product_type of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :type: str
        """

        self._product_type = product_type

    @property
    def profile_name(self):
        """Gets the profile_name of this ImageInfoListResponseProfileInfo.  # noqa: E501


        :return: The profile_name of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """Sets the profile_name of this ImageInfoListResponseProfileInfo.


        :param profile_name: The profile_name of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :type: str
        """

        self._profile_name = profile_name

    @property
    def shares(self):
        """Gets the shares of this ImageInfoListResponseProfileInfo.  # noqa: E501


        :return: The shares of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :rtype: int
        """
        return self._shares

    @shares.setter
    def shares(self, shares):
        """Sets the shares of this ImageInfoListResponseProfileInfo.


        :param shares: The shares of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :type: int
        """

        self._shares = shares

    @property
    def v_cpu(self):
        """Gets the v_cpu of this ImageInfoListResponseProfileInfo.  # noqa: E501


        :return: The v_cpu of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :rtype: int
        """
        return self._v_cpu

    @v_cpu.setter
    def v_cpu(self, v_cpu):
        """Sets the v_cpu of this ImageInfoListResponseProfileInfo.


        :param v_cpu: The v_cpu of this ImageInfoListResponseProfileInfo.  # noqa: E501
        :type: int
        """

        self._v_cpu = v_cpu

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

        return result

    def to_str(self):
        """Returns the string representation of the model"""
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        """For `print` and `pprint`"""
        return self.to_str()

    def __eq__(self, other):
        """Returns true if both objects are equal"""
        if not isinstance(other, ImageInfoListResponseProfileInfo):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
