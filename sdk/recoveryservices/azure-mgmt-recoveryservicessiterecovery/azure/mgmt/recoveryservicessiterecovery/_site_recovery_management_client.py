# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

from typing import TYPE_CHECKING

from azure.mgmt.core import ARMPipelineClient
from msrest import Deserializer, Serializer

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from typing import Any, Optional

    from azure.core.credentials import TokenCredential
    from azure.core.pipeline.transport import HttpRequest, HttpResponse

from ._configuration import SiteRecoveryManagementClientConfiguration
from .operations import Operations
from .operations import ReplicationAlertSettingsOperations
from .operations import ReplicationEligibilityResultsOperations
from .operations import ReplicationEventsOperations
from .operations import ReplicationFabricsOperations
from .operations import ReplicationLogicalNetworksOperations
from .operations import ReplicationNetworksOperations
from .operations import ReplicationNetworkMappingsOperations
from .operations import ReplicationProtectionContainersOperations
from .operations import ReplicationMigrationItemsOperations
from .operations import MigrationRecoveryPointsOperations
from .operations import ReplicationProtectableItemsOperations
from .operations import ReplicationProtectedItemsOperations
from .operations import RecoveryPointsOperations
from .operations import TargetComputeSizesOperations
from .operations import ReplicationProtectionContainerMappingsOperations
from .operations import ReplicationRecoveryServicesProvidersOperations
from .operations import ReplicationStorageClassificationsOperations
from .operations import ReplicationStorageClassificationMappingsOperations
from .operations import ReplicationvCentersOperations
from .operations import ReplicationJobsOperations
from .operations import ReplicationPoliciesOperations
from .operations import ReplicationProtectionIntentsOperations
from .operations import ReplicationRecoveryPlansOperations
from .operations import SupportedOperatingSystemsOperations
from .operations import ReplicationVaultHealthOperations
from .operations import ReplicationVaultSettingOperations
from . import models


class SiteRecoveryManagementClient(object):
    """SiteRecoveryManagementClient.

    :ivar operations: Operations operations
    :vartype operations: azure.mgmt.recoveryservicessiterecovery.operations.Operations
    :ivar replication_alert_settings: ReplicationAlertSettingsOperations operations
    :vartype replication_alert_settings: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationAlertSettingsOperations
    :ivar replication_eligibility_results: ReplicationEligibilityResultsOperations operations
    :vartype replication_eligibility_results: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationEligibilityResultsOperations
    :ivar replication_events: ReplicationEventsOperations operations
    :vartype replication_events: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationEventsOperations
    :ivar replication_fabrics: ReplicationFabricsOperations operations
    :vartype replication_fabrics: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationFabricsOperations
    :ivar replication_logical_networks: ReplicationLogicalNetworksOperations operations
    :vartype replication_logical_networks: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationLogicalNetworksOperations
    :ivar replication_networks: ReplicationNetworksOperations operations
    :vartype replication_networks: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationNetworksOperations
    :ivar replication_network_mappings: ReplicationNetworkMappingsOperations operations
    :vartype replication_network_mappings: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationNetworkMappingsOperations
    :ivar replication_protection_containers: ReplicationProtectionContainersOperations operations
    :vartype replication_protection_containers: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationProtectionContainersOperations
    :ivar replication_migration_items: ReplicationMigrationItemsOperations operations
    :vartype replication_migration_items: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationMigrationItemsOperations
    :ivar migration_recovery_points: MigrationRecoveryPointsOperations operations
    :vartype migration_recovery_points: azure.mgmt.recoveryservicessiterecovery.operations.MigrationRecoveryPointsOperations
    :ivar replication_protectable_items: ReplicationProtectableItemsOperations operations
    :vartype replication_protectable_items: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationProtectableItemsOperations
    :ivar replication_protected_items: ReplicationProtectedItemsOperations operations
    :vartype replication_protected_items: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationProtectedItemsOperations
    :ivar recovery_points: RecoveryPointsOperations operations
    :vartype recovery_points: azure.mgmt.recoveryservicessiterecovery.operations.RecoveryPointsOperations
    :ivar target_compute_sizes: TargetComputeSizesOperations operations
    :vartype target_compute_sizes: azure.mgmt.recoveryservicessiterecovery.operations.TargetComputeSizesOperations
    :ivar replication_protection_container_mappings: ReplicationProtectionContainerMappingsOperations operations
    :vartype replication_protection_container_mappings: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationProtectionContainerMappingsOperations
    :ivar replication_recovery_services_providers: ReplicationRecoveryServicesProvidersOperations operations
    :vartype replication_recovery_services_providers: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationRecoveryServicesProvidersOperations
    :ivar replication_storage_classifications: ReplicationStorageClassificationsOperations operations
    :vartype replication_storage_classifications: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationStorageClassificationsOperations
    :ivar replication_storage_classification_mappings: ReplicationStorageClassificationMappingsOperations operations
    :vartype replication_storage_classification_mappings: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationStorageClassificationMappingsOperations
    :ivar replicationv_centers: ReplicationvCentersOperations operations
    :vartype replicationv_centers: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationvCentersOperations
    :ivar replication_jobs: ReplicationJobsOperations operations
    :vartype replication_jobs: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationJobsOperations
    :ivar replication_policies: ReplicationPoliciesOperations operations
    :vartype replication_policies: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationPoliciesOperations
    :ivar replication_protection_intents: ReplicationProtectionIntentsOperations operations
    :vartype replication_protection_intents: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationProtectionIntentsOperations
    :ivar replication_recovery_plans: ReplicationRecoveryPlansOperations operations
    :vartype replication_recovery_plans: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationRecoveryPlansOperations
    :ivar supported_operating_systems: SupportedOperatingSystemsOperations operations
    :vartype supported_operating_systems: azure.mgmt.recoveryservicessiterecovery.operations.SupportedOperatingSystemsOperations
    :ivar replication_vault_health: ReplicationVaultHealthOperations operations
    :vartype replication_vault_health: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationVaultHealthOperations
    :ivar replication_vault_setting: ReplicationVaultSettingOperations operations
    :vartype replication_vault_setting: azure.mgmt.recoveryservicessiterecovery.operations.ReplicationVaultSettingOperations
    :param credential: Credential needed for the client to connect to Azure.
    :type credential: ~azure.core.credentials.TokenCredential
    :param subscription_id: The subscription Id.
    :type subscription_id: str
    :param resource_group_name: The name of the resource group where the recovery services vault is present.
    :type resource_group_name: str
    :param resource_name: The name of the recovery services vault.
    :type resource_name: str
    :param str base_url: Service URL
    :keyword int polling_interval: Default waiting time between two polls for LRO operations if no Retry-After header is present.
    """

    def __init__(
        self,
        credential,  # type: "TokenCredential"
        subscription_id,  # type: str
        resource_group_name,  # type: str
        resource_name,  # type: str
        base_url=None,  # type: Optional[str]
        **kwargs  # type: Any
    ):
        # type: (...) -> None
        if not base_url:
            base_url = 'https://management.azure.com'
        self._config = SiteRecoveryManagementClientConfiguration(credential, subscription_id, resource_group_name, resource_name, **kwargs)
        self._client = ARMPipelineClient(base_url=base_url, config=self._config, **kwargs)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self._serialize = Serializer(client_models)
        self._serialize.client_side_validation = False
        self._deserialize = Deserializer(client_models)

        self.operations = Operations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_alert_settings = ReplicationAlertSettingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_eligibility_results = ReplicationEligibilityResultsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_events = ReplicationEventsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_fabrics = ReplicationFabricsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_logical_networks = ReplicationLogicalNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_networks = ReplicationNetworksOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_network_mappings = ReplicationNetworkMappingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_protection_containers = ReplicationProtectionContainersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_migration_items = ReplicationMigrationItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.migration_recovery_points = MigrationRecoveryPointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_protectable_items = ReplicationProtectableItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_protected_items = ReplicationProtectedItemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.recovery_points = RecoveryPointsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.target_compute_sizes = TargetComputeSizesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_protection_container_mappings = ReplicationProtectionContainerMappingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_recovery_services_providers = ReplicationRecoveryServicesProvidersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_storage_classifications = ReplicationStorageClassificationsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_storage_classification_mappings = ReplicationStorageClassificationMappingsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replicationv_centers = ReplicationvCentersOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_jobs = ReplicationJobsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_policies = ReplicationPoliciesOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_protection_intents = ReplicationProtectionIntentsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_recovery_plans = ReplicationRecoveryPlansOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.supported_operating_systems = SupportedOperatingSystemsOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_vault_health = ReplicationVaultHealthOperations(
            self._client, self._config, self._serialize, self._deserialize)
        self.replication_vault_setting = ReplicationVaultSettingOperations(
            self._client, self._config, self._serialize, self._deserialize)

    def _send_request(self, http_request, **kwargs):
        # type: (HttpRequest, Any) -> HttpResponse
        """Runs the network request through the client's chained policies.

        :param http_request: The network request you want to make. Required.
        :type http_request: ~azure.core.pipeline.transport.HttpRequest
        :keyword bool stream: Whether the response payload will be streamed. Defaults to True.
        :return: The response of your network call. Does not do error handling on your response.
        :rtype: ~azure.core.pipeline.transport.HttpResponse
        """
        path_format_arguments = {
            'subscriptionId': self._serialize.url("self._config.subscription_id", self._config.subscription_id, 'str'),
            'resourceGroupName': self._serialize.url("self._config.resource_group_name", self._config.resource_group_name, 'str'),
            'resourceName': self._serialize.url("self._config.resource_name", self._config.resource_name, 'str'),
        }
        http_request.url = self._client.format_url(http_request.url, **path_format_arguments)
        stream = kwargs.pop("stream", True)
        pipeline_response = self._client._pipeline.run(http_request, stream=stream, **kwargs)
        return pipeline_response.http_response

    def close(self):
        # type: () -> None
        self._client.close()

    def __enter__(self):
        # type: () -> SiteRecoveryManagementClient
        self._client.__enter__()
        return self

    def __exit__(self, *exc_details):
        # type: (Any) -> None
        self._client.__exit__(*exc_details)
