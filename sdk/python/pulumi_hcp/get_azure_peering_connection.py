# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAzurePeeringConnectionResult',
    'AwaitableGetAzurePeeringConnectionResult',
    'get_azure_peering_connection',
    'get_azure_peering_connection_output',
]

@pulumi.output_type
class GetAzurePeeringConnectionResult:
    """
    A collection of values returned by getAzurePeeringConnection.
    """
    def __init__(__self__, application_id=None, azure_peering_id=None, created_at=None, expires_at=None, hvn_link=None, id=None, organization_id=None, peer_resource_group_name=None, peer_subscription_id=None, peer_tenant_id=None, peer_vnet_name=None, peer_vnet_region=None, peering_id=None, project_id=None, self_link=None, wait_for_active_state=None):
        if application_id and not isinstance(application_id, str):
            raise TypeError("Expected argument 'application_id' to be a str")
        pulumi.set(__self__, "application_id", application_id)
        if azure_peering_id and not isinstance(azure_peering_id, str):
            raise TypeError("Expected argument 'azure_peering_id' to be a str")
        pulumi.set(__self__, "azure_peering_id", azure_peering_id)
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if expires_at and not isinstance(expires_at, str):
            raise TypeError("Expected argument 'expires_at' to be a str")
        pulumi.set(__self__, "expires_at", expires_at)
        if hvn_link and not isinstance(hvn_link, str):
            raise TypeError("Expected argument 'hvn_link' to be a str")
        pulumi.set(__self__, "hvn_link", hvn_link)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if peer_resource_group_name and not isinstance(peer_resource_group_name, str):
            raise TypeError("Expected argument 'peer_resource_group_name' to be a str")
        pulumi.set(__self__, "peer_resource_group_name", peer_resource_group_name)
        if peer_subscription_id and not isinstance(peer_subscription_id, str):
            raise TypeError("Expected argument 'peer_subscription_id' to be a str")
        pulumi.set(__self__, "peer_subscription_id", peer_subscription_id)
        if peer_tenant_id and not isinstance(peer_tenant_id, str):
            raise TypeError("Expected argument 'peer_tenant_id' to be a str")
        pulumi.set(__self__, "peer_tenant_id", peer_tenant_id)
        if peer_vnet_name and not isinstance(peer_vnet_name, str):
            raise TypeError("Expected argument 'peer_vnet_name' to be a str")
        pulumi.set(__self__, "peer_vnet_name", peer_vnet_name)
        if peer_vnet_region and not isinstance(peer_vnet_region, str):
            raise TypeError("Expected argument 'peer_vnet_region' to be a str")
        pulumi.set(__self__, "peer_vnet_region", peer_vnet_region)
        if peering_id and not isinstance(peering_id, str):
            raise TypeError("Expected argument 'peering_id' to be a str")
        pulumi.set(__self__, "peering_id", peering_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)
        if wait_for_active_state and not isinstance(wait_for_active_state, bool):
            raise TypeError("Expected argument 'wait_for_active_state' to be a bool")
        pulumi.set(__self__, "wait_for_active_state", wait_for_active_state)

    @property
    @pulumi.getter(name="applicationId")
    def application_id(self) -> str:
        """
        The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
        """
        return pulumi.get(self, "application_id")

    @property
    @pulumi.getter(name="azurePeeringId")
    def azure_peering_id(self) -> str:
        """
        The peering connection ID used by Azure.
        """
        return pulumi.get(self, "azure_peering_id")

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time that the peering connection was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> str:
        """
        The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter(name="hvnLink")
    def hvn_link(self) -> str:
        """
        The `self_link` of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_link")

    @property
    @pulumi.getter
    def id(self) -> str:
        """
        The provider-assigned unique ID for this managed resource.
        """
        return pulumi.get(self, "id")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> str:
        """
        The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="peerResourceGroupName")
    def peer_resource_group_name(self) -> str:
        """
        The resource group name of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_resource_group_name")

    @property
    @pulumi.getter(name="peerSubscriptionId")
    def peer_subscription_id(self) -> str:
        """
        The subscription ID of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_subscription_id")

    @property
    @pulumi.getter(name="peerTenantId")
    def peer_tenant_id(self) -> str:
        """
        The tenant ID of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_tenant_id")

    @property
    @pulumi.getter(name="peerVnetName")
    def peer_vnet_name(self) -> str:
        """
        The name of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_vnet_name")

    @property
    @pulumi.getter(name="peerVnetRegion")
    def peer_vnet_region(self) -> str:
        """
        The region of the peer VNet in Azure.
        """
        return pulumi.get(self, "peer_vnet_region")

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> str:
        """
        The ID of the peering connection.
        """
        return pulumi.get(self, "peering_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        A unique URL identifying the peering connection
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter(name="waitForActiveState")
    def wait_for_active_state(self) -> Optional[bool]:
        return pulumi.get(self, "wait_for_active_state")


class AwaitableGetAzurePeeringConnectionResult(GetAzurePeeringConnectionResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAzurePeeringConnectionResult(
            application_id=self.application_id,
            azure_peering_id=self.azure_peering_id,
            created_at=self.created_at,
            expires_at=self.expires_at,
            hvn_link=self.hvn_link,
            id=self.id,
            organization_id=self.organization_id,
            peer_resource_group_name=self.peer_resource_group_name,
            peer_subscription_id=self.peer_subscription_id,
            peer_tenant_id=self.peer_tenant_id,
            peer_vnet_name=self.peer_vnet_name,
            peer_vnet_region=self.peer_vnet_region,
            peering_id=self.peering_id,
            project_id=self.project_id,
            self_link=self.self_link,
            wait_for_active_state=self.wait_for_active_state)


def get_azure_peering_connection(hvn_link: Optional[str] = None,
                                 peering_id: Optional[str] = None,
                                 wait_for_active_state: Optional[bool] = None,
                                 opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAzurePeeringConnectionResult:
    """
    > **Note:** Azure support coming soon. This data source is currently in internal preview only.

    The Azure peering connection data source provides information about a peering connection between an HVN and a peer Azure VNet.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    test = hcp.get_azure_peering_connection(hvn_id=var["hvn_id"],
        peering_id=var["peering_id"],
        wait_for_active_state=True)
    ```


    :param str hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
    :param str peering_id: The ID of the peering connection.
    """
    __args__ = dict()
    __args__['hvnLink'] = hvn_link
    __args__['peeringId'] = peering_id
    __args__['waitForActiveState'] = wait_for_active_state
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
    __ret__ = pulumi.runtime.invoke('hcp:index/getAzurePeeringConnection:getAzurePeeringConnection', __args__, opts=opts, typ=GetAzurePeeringConnectionResult).value

    return AwaitableGetAzurePeeringConnectionResult(
        application_id=__ret__.application_id,
        azure_peering_id=__ret__.azure_peering_id,
        created_at=__ret__.created_at,
        expires_at=__ret__.expires_at,
        hvn_link=__ret__.hvn_link,
        id=__ret__.id,
        organization_id=__ret__.organization_id,
        peer_resource_group_name=__ret__.peer_resource_group_name,
        peer_subscription_id=__ret__.peer_subscription_id,
        peer_tenant_id=__ret__.peer_tenant_id,
        peer_vnet_name=__ret__.peer_vnet_name,
        peer_vnet_region=__ret__.peer_vnet_region,
        peering_id=__ret__.peering_id,
        project_id=__ret__.project_id,
        self_link=__ret__.self_link,
        wait_for_active_state=__ret__.wait_for_active_state)


@_utilities.lift_output_func(get_azure_peering_connection)
def get_azure_peering_connection_output(hvn_link: Optional[pulumi.Input[str]] = None,
                                        peering_id: Optional[pulumi.Input[str]] = None,
                                        wait_for_active_state: Optional[pulumi.Input[Optional[bool]]] = None,
                                        opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAzurePeeringConnectionResult]:
    """
    > **Note:** Azure support coming soon. This data source is currently in internal preview only.

    The Azure peering connection data source provides information about a peering connection between an HVN and a peer Azure VNet.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    test = hcp.get_azure_peering_connection(hvn_id=var["hvn_id"],
        peering_id=var["peering_id"],
        wait_for_active_state=True)
    ```


    :param str hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
    :param str peering_id: The ID of the peering connection.
    """
    ...