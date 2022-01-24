# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = [
    'GetAwsNetworkPeeringResult',
    'AwaitableGetAwsNetworkPeeringResult',
    'get_aws_network_peering',
    'get_aws_network_peering_output',
]

@pulumi.output_type
class GetAwsNetworkPeeringResult:
    """
    A collection of values returned by getAwsNetworkPeering.
    """
    def __init__(__self__, created_at=None, expires_at=None, hvn_id=None, id=None, organization_id=None, peer_account_id=None, peer_vpc_id=None, peer_vpc_region=None, peering_id=None, project_id=None, provider_peering_id=None, self_link=None):
        if created_at and not isinstance(created_at, str):
            raise TypeError("Expected argument 'created_at' to be a str")
        pulumi.set(__self__, "created_at", created_at)
        if expires_at and not isinstance(expires_at, str):
            raise TypeError("Expected argument 'expires_at' to be a str")
        pulumi.set(__self__, "expires_at", expires_at)
        if hvn_id and not isinstance(hvn_id, str):
            raise TypeError("Expected argument 'hvn_id' to be a str")
        pulumi.set(__self__, "hvn_id", hvn_id)
        if id and not isinstance(id, str):
            raise TypeError("Expected argument 'id' to be a str")
        pulumi.set(__self__, "id", id)
        if organization_id and not isinstance(organization_id, str):
            raise TypeError("Expected argument 'organization_id' to be a str")
        pulumi.set(__self__, "organization_id", organization_id)
        if peer_account_id and not isinstance(peer_account_id, str):
            raise TypeError("Expected argument 'peer_account_id' to be a str")
        pulumi.set(__self__, "peer_account_id", peer_account_id)
        if peer_vpc_id and not isinstance(peer_vpc_id, str):
            raise TypeError("Expected argument 'peer_vpc_id' to be a str")
        pulumi.set(__self__, "peer_vpc_id", peer_vpc_id)
        if peer_vpc_region and not isinstance(peer_vpc_region, str):
            raise TypeError("Expected argument 'peer_vpc_region' to be a str")
        pulumi.set(__self__, "peer_vpc_region", peer_vpc_region)
        if peering_id and not isinstance(peering_id, str):
            raise TypeError("Expected argument 'peering_id' to be a str")
        pulumi.set(__self__, "peering_id", peering_id)
        if project_id and not isinstance(project_id, str):
            raise TypeError("Expected argument 'project_id' to be a str")
        pulumi.set(__self__, "project_id", project_id)
        if provider_peering_id and not isinstance(provider_peering_id, str):
            raise TypeError("Expected argument 'provider_peering_id' to be a str")
        pulumi.set(__self__, "provider_peering_id", provider_peering_id)
        if self_link and not isinstance(self_link, str):
            raise TypeError("Expected argument 'self_link' to be a str")
        pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> str:
        """
        The time that the network peering was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> str:
        """
        The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter(name="hvnId")
    def hvn_id(self) -> str:
        """
        The ID of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_id")

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
        The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="peerAccountId")
    def peer_account_id(self) -> str:
        """
        The account ID of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_account_id")

    @property
    @pulumi.getter(name="peerVpcId")
    def peer_vpc_id(self) -> str:
        """
        The ID of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_vpc_id")

    @property
    @pulumi.getter(name="peerVpcRegion")
    def peer_vpc_region(self) -> str:
        """
        The region of the peer VPC in AWS.
        """
        return pulumi.get(self, "peer_vpc_region")

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> str:
        """
        The ID of the network peering.
        """
        return pulumi.get(self, "peering_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> str:
        """
        The ID of the HCP project where the network peering is located. Always matches the HVN's project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="providerPeeringId")
    def provider_peering_id(self) -> str:
        """
        The peering connection ID used by AWS.
        """
        return pulumi.get(self, "provider_peering_id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> str:
        """
        A unique URL identifying the network peering.
        """
        return pulumi.get(self, "self_link")


class AwaitableGetAwsNetworkPeeringResult(GetAwsNetworkPeeringResult):
    # pylint: disable=using-constant-test
    def __await__(self):
        if False:
            yield self
        return GetAwsNetworkPeeringResult(
            created_at=self.created_at,
            expires_at=self.expires_at,
            hvn_id=self.hvn_id,
            id=self.id,
            organization_id=self.organization_id,
            peer_account_id=self.peer_account_id,
            peer_vpc_id=self.peer_vpc_id,
            peer_vpc_region=self.peer_vpc_region,
            peering_id=self.peering_id,
            project_id=self.project_id,
            provider_peering_id=self.provider_peering_id,
            self_link=self.self_link)


def get_aws_network_peering(hvn_id: Optional[str] = None,
                            peering_id: Optional[str] = None,
                            opts: Optional[pulumi.InvokeOptions] = None) -> AwaitableGetAwsNetworkPeeringResult:
    """
    The AWS network peering data source provides information about an existing network peering between an HVN and a peer AWS VPC.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    test = hcp.get_aws_network_peering(hvn_id=var["hvn_id"],
        peering_id=var["peering_id"])
    ```


    :param str hvn_id: The ID of the HashiCorp Virtual Network (HVN).
    :param str peering_id: The ID of the network peering.
    """
    __args__ = dict()
    __args__['hvnId'] = hvn_id
    __args__['peeringId'] = peering_id
    if opts is None:
        opts = pulumi.InvokeOptions()
    if opts.version is None:
        opts.version = _utilities.get_version()
    __ret__ = pulumi.runtime.invoke('hcp:index/getAwsNetworkPeering:getAwsNetworkPeering', __args__, opts=opts, typ=GetAwsNetworkPeeringResult).value

    return AwaitableGetAwsNetworkPeeringResult(
        created_at=__ret__.created_at,
        expires_at=__ret__.expires_at,
        hvn_id=__ret__.hvn_id,
        id=__ret__.id,
        organization_id=__ret__.organization_id,
        peer_account_id=__ret__.peer_account_id,
        peer_vpc_id=__ret__.peer_vpc_id,
        peer_vpc_region=__ret__.peer_vpc_region,
        peering_id=__ret__.peering_id,
        project_id=__ret__.project_id,
        provider_peering_id=__ret__.provider_peering_id,
        self_link=__ret__.self_link)


@_utilities.lift_output_func(get_aws_network_peering)
def get_aws_network_peering_output(hvn_id: Optional[pulumi.Input[str]] = None,
                                   peering_id: Optional[pulumi.Input[str]] = None,
                                   opts: Optional[pulumi.InvokeOptions] = None) -> pulumi.Output[GetAwsNetworkPeeringResult]:
    """
    The AWS network peering data source provides information about an existing network peering between an HVN and a peer AWS VPC.

    ## Example Usage

    ```python
    import pulumi
    import pulumi_hcp as hcp

    test = hcp.get_aws_network_peering(hvn_id=var["hvn_id"],
        peering_id=var["peering_id"])
    ```


    :param str hvn_id: The ID of the HashiCorp Virtual Network (HVN).
    :param str peering_id: The ID of the network peering.
    """
    ...
