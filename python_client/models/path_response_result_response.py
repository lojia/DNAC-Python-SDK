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

from python_client.models.flow_analysis_list_output_response import FlowAnalysisListOutputResponse  # noqa: F401,E501
from python_client.models.path_response_result_response_detailed_status import PathResponseResultResponseDetailedStatus  # noqa: F401,E501
from python_client.models.path_response_result_response_network_elements import PathResponseResultResponseNetworkElements  # noqa: F401,E501
from python_client.models.path_response_result_response_network_elements_info import PathResponseResultResponseNetworkElementsInfo  # noqa: F401,E501


class PathResponseResultResponse(object):
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
        'detailed_status': 'PathResponseResultResponseDetailedStatus',
        'last_update': 'str',
        'network_elements': 'list[PathResponseResultResponseNetworkElements]',
        'network_elements_info': 'list[PathResponseResultResponseNetworkElementsInfo]',
        'properties': 'list[str]',
        'request': 'FlowAnalysisListOutputResponse'
    }

    attribute_map = {
        'detailed_status': 'detailedStatus',
        'last_update': 'lastUpdate',
        'network_elements': 'networkElements',
        'network_elements_info': 'networkElementsInfo',
        'properties': 'properties',
        'request': 'request'
    }

    def __init__(self, detailed_status=None, last_update=None, network_elements=None, network_elements_info=None, properties=None, request=None):  # noqa: E501
        """PathResponseResultResponse - a model defined in Swagger"""  # noqa: E501

        self._detailed_status = None
        self._last_update = None
        self._network_elements = None
        self._network_elements_info = None
        self._properties = None
        self._request = None
        self.discriminator = None

        if detailed_status is not None:
            self.detailed_status = detailed_status
        if last_update is not None:
            self.last_update = last_update
        if network_elements is not None:
            self.network_elements = network_elements
        if network_elements_info is not None:
            self.network_elements_info = network_elements_info
        if properties is not None:
            self.properties = properties
        if request is not None:
            self.request = request

    @property
    def detailed_status(self):
        """Gets the detailed_status of this PathResponseResultResponse.  # noqa: E501


        :return: The detailed_status of this PathResponseResultResponse.  # noqa: E501
        :rtype: PathResponseResultResponseDetailedStatus
        """
        return self._detailed_status

    @detailed_status.setter
    def detailed_status(self, detailed_status):
        """Sets the detailed_status of this PathResponseResultResponse.


        :param detailed_status: The detailed_status of this PathResponseResultResponse.  # noqa: E501
        :type: PathResponseResultResponseDetailedStatus
        """

        self._detailed_status = detailed_status

    @property
    def last_update(self):
        """Gets the last_update of this PathResponseResultResponse.  # noqa: E501


        :return: The last_update of this PathResponseResultResponse.  # noqa: E501
        :rtype: str
        """
        return self._last_update

    @last_update.setter
    def last_update(self, last_update):
        """Sets the last_update of this PathResponseResultResponse.


        :param last_update: The last_update of this PathResponseResultResponse.  # noqa: E501
        :type: str
        """

        self._last_update = last_update

    @property
    def network_elements(self):
        """Gets the network_elements of this PathResponseResultResponse.  # noqa: E501


        :return: The network_elements of this PathResponseResultResponse.  # noqa: E501
        :rtype: list[PathResponseResultResponseNetworkElements]
        """
        return self._network_elements

    @network_elements.setter
    def network_elements(self, network_elements):
        """Sets the network_elements of this PathResponseResultResponse.


        :param network_elements: The network_elements of this PathResponseResultResponse.  # noqa: E501
        :type: list[PathResponseResultResponseNetworkElements]
        """

        self._network_elements = network_elements

    @property
    def network_elements_info(self):
        """Gets the network_elements_info of this PathResponseResultResponse.  # noqa: E501


        :return: The network_elements_info of this PathResponseResultResponse.  # noqa: E501
        :rtype: list[PathResponseResultResponseNetworkElementsInfo]
        """
        return self._network_elements_info

    @network_elements_info.setter
    def network_elements_info(self, network_elements_info):
        """Sets the network_elements_info of this PathResponseResultResponse.


        :param network_elements_info: The network_elements_info of this PathResponseResultResponse.  # noqa: E501
        :type: list[PathResponseResultResponseNetworkElementsInfo]
        """

        self._network_elements_info = network_elements_info

    @property
    def properties(self):
        """Gets the properties of this PathResponseResultResponse.  # noqa: E501


        :return: The properties of this PathResponseResultResponse.  # noqa: E501
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this PathResponseResultResponse.


        :param properties: The properties of this PathResponseResultResponse.  # noqa: E501
        :type: list[str]
        """

        self._properties = properties

    @property
    def request(self):
        """Gets the request of this PathResponseResultResponse.  # noqa: E501


        :return: The request of this PathResponseResultResponse.  # noqa: E501
        :rtype: FlowAnalysisListOutputResponse
        """
        return self._request

    @request.setter
    def request(self, request):
        """Sets the request of this PathResponseResultResponse.


        :param request: The request of this PathResponseResultResponse.  # noqa: E501
        :type: FlowAnalysisListOutputResponse
        """

        self._request = request

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
        if not isinstance(other, PathResponseResultResponse):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other