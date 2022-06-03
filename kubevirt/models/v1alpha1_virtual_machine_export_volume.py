# coding: utf-8

"""
    KubeVirt API

    This is KubeVirt API an add-on for Kubernetes.

    OpenAPI spec version: 1.0.0
    Contact: kubevirt-dev@googlegroups.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class V1alpha1VirtualMachineExportVolume(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
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
        'formats': 'list[V1alpha1VirtualMachineExportVolumeFormat]',
        'name': 'str'
    }

    attribute_map = {
        'formats': 'formats',
        'name': 'name'
    }

    def __init__(self, formats=None, name=None):
        """
        V1alpha1VirtualMachineExportVolume - a model defined in Swagger
        """

        self._formats = None
        self._name = None

        if formats is not None:
          self.formats = formats
        self.name = name

    @property
    def formats(self):
        """
        Gets the formats of this V1alpha1VirtualMachineExportVolume.

        :return: The formats of this V1alpha1VirtualMachineExportVolume.
        :rtype: list[V1alpha1VirtualMachineExportVolumeFormat]
        """
        return self._formats

    @formats.setter
    def formats(self, formats):
        """
        Sets the formats of this V1alpha1VirtualMachineExportVolume.

        :param formats: The formats of this V1alpha1VirtualMachineExportVolume.
        :type: list[V1alpha1VirtualMachineExportVolumeFormat]
        """

        self._formats = formats

    @property
    def name(self):
        """
        Gets the name of this V1alpha1VirtualMachineExportVolume.
        Name is the name of the exported volume

        :return: The name of this V1alpha1VirtualMachineExportVolume.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this V1alpha1VirtualMachineExportVolume.
        Name is the name of the exported volume

        :param name: The name of this V1alpha1VirtualMachineExportVolume.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
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
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, V1alpha1VirtualMachineExportVolume):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
