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


class Review(Model):
    """The Review object.

    :param review_id: Id of the review.
    :type review_id: str
    :param sub_team: Name of the subteam.
    :type sub_team: str
    :param status: The status string (<Pending, Complete>).
    :type status: str
    :param reviewer_result_tags: Array of KeyValue with Reviewer set Tags.
    :type reviewer_result_tags:
     list[~azure.cognitiveservices.vision.contentmoderator.models.KeyValuePair]
    :param created_by: The reviewer name.
    :type created_by: str
    :param metadata: Array of KeyValue.
    :type metadata:
     list[~azure.cognitiveservices.vision.contentmoderator.models.KeyValuePair]
    :param type: The type of content.
    :type type: str
    :param content: The content value.
    :type content: str
    :param content_id: Id of the content.
    :type content_id: str
    :param callback_endpoint: The callback endpoint.
    :type callback_endpoint: str
    """

    _attribute_map = {
        'review_id': {'key': 'reviewId', 'type': 'str'},
        'sub_team': {'key': 'subTeam', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'reviewer_result_tags': {'key': 'reviewerResultTags', 'type': '[KeyValuePair]'},
        'created_by': {'key': 'createdBy', 'type': 'str'},
        'metadata': {'key': 'metadata', 'type': '[KeyValuePair]'},
        'type': {'key': 'type', 'type': 'str'},
        'content': {'key': 'content', 'type': 'str'},
        'content_id': {'key': 'contentId', 'type': 'str'},
        'callback_endpoint': {'key': 'callbackEndpoint', 'type': 'str'},
    }

    def __init__(self, review_id=None, sub_team=None, status=None, reviewer_result_tags=None, created_by=None, metadata=None, type=None, content=None, content_id=None, callback_endpoint=None):
        self.review_id = review_id
        self.sub_team = sub_team
        self.status = status
        self.reviewer_result_tags = reviewer_result_tags
        self.created_by = created_by
        self.metadata = metadata
        self.type = type
        self.content = content
        self.content_id = content_id
        self.callback_endpoint = callback_endpoint
