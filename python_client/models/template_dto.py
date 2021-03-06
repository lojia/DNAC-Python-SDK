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

from python_client.models.template_dto_device_types import TemplateDTODeviceTypes  # noqa: F401,E501
from python_client.models.template_dto_rollback_template_params import TemplateDTORollbackTemplateParams  # noqa: F401,E501


class TemplateDTO(object):
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
        'author': 'str',
        'create_time': 'int',
        'description': 'str',
        'device_types': 'list[TemplateDTODeviceTypes]',
        'id': 'str',
        'last_update_time': 'int',
        'name': 'str',
        'parent_template_id': 'str',
        'project_id': 'str',
        'project_name': 'str',
        'rollback_template_content': 'str',
        'rollback_template_params': 'list[TemplateDTORollbackTemplateParams]',
        'software_type': 'str',
        'software_variant': 'str',
        'software_version': 'str',
        'tags': 'list[str]',
        'template_content': 'str',
        'template_params': 'list[TemplateDTORollbackTemplateParams]',
        'version': 'str'
    }

    attribute_map = {
        'author': 'author',
        'create_time': 'createTime',
        'description': 'description',
        'device_types': 'deviceTypes',
        'id': 'id',
        'last_update_time': 'lastUpdateTime',
        'name': 'name',
        'parent_template_id': 'parentTemplateId',
        'project_id': 'projectId',
        'project_name': 'projectName',
        'rollback_template_content': 'rollbackTemplateContent',
        'rollback_template_params': 'rollbackTemplateParams',
        'software_type': 'softwareType',
        'software_variant': 'softwareVariant',
        'software_version': 'softwareVersion',
        'tags': 'tags',
        'template_content': 'templateContent',
        'template_params': 'templateParams',
        'version': 'version'
    }

    def __init__(self, author=None, create_time=None, description=None, device_types=None, id=None, last_update_time=None, name=None, parent_template_id=None, project_id=None, project_name=None, rollback_template_content=None, rollback_template_params=None, software_type=None, software_variant=None, software_version=None, tags=None, template_content=None, template_params=None, version=None):  # noqa: E501
        """TemplateDTO - a model defined in Swagger"""  # noqa: E501

        self._author = None
        self._create_time = None
        self._description = None
        self._device_types = None
        self._id = None
        self._last_update_time = None
        self._name = None
        self._parent_template_id = None
        self._project_id = None
        self._project_name = None
        self._rollback_template_content = None
        self._rollback_template_params = None
        self._software_type = None
        self._software_variant = None
        self._software_version = None
        self._tags = None
        self._template_content = None
        self._template_params = None
        self._version = None
        self.discriminator = None

        if author is not None:
            self.author = author
        if create_time is not None:
            self.create_time = create_time
        if description is not None:
            self.description = description
        if device_types is not None:
            self.device_types = device_types
        if id is not None:
            self.id = id
        if last_update_time is not None:
            self.last_update_time = last_update_time
        if name is not None:
            self.name = name
        if parent_template_id is not None:
            self.parent_template_id = parent_template_id
        if project_id is not None:
            self.project_id = project_id
        if project_name is not None:
            self.project_name = project_name
        if rollback_template_content is not None:
            self.rollback_template_content = rollback_template_content
        if rollback_template_params is not None:
            self.rollback_template_params = rollback_template_params
        if software_type is not None:
            self.software_type = software_type
        if software_variant is not None:
            self.software_variant = software_variant
        if software_version is not None:
            self.software_version = software_version
        if tags is not None:
            self.tags = tags
        if template_content is not None:
            self.template_content = template_content
        if template_params is not None:
            self.template_params = template_params
        if version is not None:
            self.version = version

    @property
    def author(self):
        """Gets the author of this TemplateDTO.  # noqa: E501


        :return: The author of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._author

    @author.setter
    def author(self, author):
        """Sets the author of this TemplateDTO.


        :param author: The author of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._author = author

    @property
    def create_time(self):
        """Gets the create_time of this TemplateDTO.  # noqa: E501


        :return: The create_time of this TemplateDTO.  # noqa: E501
        :rtype: int
        """
        return self._create_time

    @create_time.setter
    def create_time(self, create_time):
        """Sets the create_time of this TemplateDTO.


        :param create_time: The create_time of this TemplateDTO.  # noqa: E501
        :type: int
        """

        self._create_time = create_time

    @property
    def description(self):
        """Gets the description of this TemplateDTO.  # noqa: E501


        :return: The description of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this TemplateDTO.


        :param description: The description of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._description = description

    @property
    def device_types(self):
        """Gets the device_types of this TemplateDTO.  # noqa: E501


        :return: The device_types of this TemplateDTO.  # noqa: E501
        :rtype: list[TemplateDTODeviceTypes]
        """
        return self._device_types

    @device_types.setter
    def device_types(self, device_types):
        """Sets the device_types of this TemplateDTO.


        :param device_types: The device_types of this TemplateDTO.  # noqa: E501
        :type: list[TemplateDTODeviceTypes]
        """

        self._device_types = device_types

    @property
    def id(self):
        """Gets the id of this TemplateDTO.  # noqa: E501


        :return: The id of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TemplateDTO.


        :param id: The id of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._id = id

    @property
    def last_update_time(self):
        """Gets the last_update_time of this TemplateDTO.  # noqa: E501


        :return: The last_update_time of this TemplateDTO.  # noqa: E501
        :rtype: int
        """
        return self._last_update_time

    @last_update_time.setter
    def last_update_time(self, last_update_time):
        """Sets the last_update_time of this TemplateDTO.


        :param last_update_time: The last_update_time of this TemplateDTO.  # noqa: E501
        :type: int
        """

        self._last_update_time = last_update_time

    @property
    def name(self):
        """Gets the name of this TemplateDTO.  # noqa: E501


        :return: The name of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TemplateDTO.


        :param name: The name of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._name = name

    @property
    def parent_template_id(self):
        """Gets the parent_template_id of this TemplateDTO.  # noqa: E501


        :return: The parent_template_id of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._parent_template_id

    @parent_template_id.setter
    def parent_template_id(self, parent_template_id):
        """Sets the parent_template_id of this TemplateDTO.


        :param parent_template_id: The parent_template_id of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._parent_template_id = parent_template_id

    @property
    def project_id(self):
        """Gets the project_id of this TemplateDTO.  # noqa: E501


        :return: The project_id of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_id

    @project_id.setter
    def project_id(self, project_id):
        """Sets the project_id of this TemplateDTO.


        :param project_id: The project_id of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._project_id = project_id

    @property
    def project_name(self):
        """Gets the project_name of this TemplateDTO.  # noqa: E501


        :return: The project_name of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._project_name

    @project_name.setter
    def project_name(self, project_name):
        """Sets the project_name of this TemplateDTO.


        :param project_name: The project_name of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._project_name = project_name

    @property
    def rollback_template_content(self):
        """Gets the rollback_template_content of this TemplateDTO.  # noqa: E501


        :return: The rollback_template_content of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._rollback_template_content

    @rollback_template_content.setter
    def rollback_template_content(self, rollback_template_content):
        """Sets the rollback_template_content of this TemplateDTO.


        :param rollback_template_content: The rollback_template_content of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._rollback_template_content = rollback_template_content

    @property
    def rollback_template_params(self):
        """Gets the rollback_template_params of this TemplateDTO.  # noqa: E501


        :return: The rollback_template_params of this TemplateDTO.  # noqa: E501
        :rtype: list[TemplateDTORollbackTemplateParams]
        """
        return self._rollback_template_params

    @rollback_template_params.setter
    def rollback_template_params(self, rollback_template_params):
        """Sets the rollback_template_params of this TemplateDTO.


        :param rollback_template_params: The rollback_template_params of this TemplateDTO.  # noqa: E501
        :type: list[TemplateDTORollbackTemplateParams]
        """

        self._rollback_template_params = rollback_template_params

    @property
    def software_type(self):
        """Gets the software_type of this TemplateDTO.  # noqa: E501


        :return: The software_type of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._software_type

    @software_type.setter
    def software_type(self, software_type):
        """Sets the software_type of this TemplateDTO.


        :param software_type: The software_type of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._software_type = software_type

    @property
    def software_variant(self):
        """Gets the software_variant of this TemplateDTO.  # noqa: E501


        :return: The software_variant of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._software_variant

    @software_variant.setter
    def software_variant(self, software_variant):
        """Sets the software_variant of this TemplateDTO.


        :param software_variant: The software_variant of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._software_variant = software_variant

    @property
    def software_version(self):
        """Gets the software_version of this TemplateDTO.  # noqa: E501


        :return: The software_version of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._software_version

    @software_version.setter
    def software_version(self, software_version):
        """Sets the software_version of this TemplateDTO.


        :param software_version: The software_version of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._software_version = software_version

    @property
    def tags(self):
        """Gets the tags of this TemplateDTO.  # noqa: E501


        :return: The tags of this TemplateDTO.  # noqa: E501
        :rtype: list[str]
        """
        return self._tags

    @tags.setter
    def tags(self, tags):
        """Sets the tags of this TemplateDTO.


        :param tags: The tags of this TemplateDTO.  # noqa: E501
        :type: list[str]
        """

        self._tags = tags

    @property
    def template_content(self):
        """Gets the template_content of this TemplateDTO.  # noqa: E501


        :return: The template_content of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._template_content

    @template_content.setter
    def template_content(self, template_content):
        """Sets the template_content of this TemplateDTO.


        :param template_content: The template_content of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._template_content = template_content

    @property
    def template_params(self):
        """Gets the template_params of this TemplateDTO.  # noqa: E501


        :return: The template_params of this TemplateDTO.  # noqa: E501
        :rtype: list[TemplateDTORollbackTemplateParams]
        """
        return self._template_params

    @template_params.setter
    def template_params(self, template_params):
        """Sets the template_params of this TemplateDTO.


        :param template_params: The template_params of this TemplateDTO.  # noqa: E501
        :type: list[TemplateDTORollbackTemplateParams]
        """

        self._template_params = template_params

    @property
    def version(self):
        """Gets the version of this TemplateDTO.  # noqa: E501


        :return: The version of this TemplateDTO.  # noqa: E501
        :rtype: str
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TemplateDTO.


        :param version: The version of this TemplateDTO.  # noqa: E501
        :type: str
        """

        self._version = version

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
        if not isinstance(other, TemplateDTO):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """Returns true if both objects are not equal"""
        return not self == other
