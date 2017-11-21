# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AddGetRefreshStatus(Model):
    """Add and Get status response properties.

    :param code: Status code.
    :type code: float
    :param description: Status description.
    :type description: str
    :param exception: Exception status.
    :type exception: str
    """

    _attribute_map = {
        'code': {'key': 'code', 'type': 'float'},
        'description': {'key': 'description', 'type': 'str'},
        'exception': {'key': 'exception', 'type': 'str'},
    }

    def __init__(self, code=None, description=None, exception=None):
        self.code = code
        self.description = description
        self.exception = exception
