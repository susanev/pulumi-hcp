# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['HvnPeeringConnectionArgs', 'HvnPeeringConnection']

@pulumi.input_type
class HvnPeeringConnectionArgs:
    def __init__(__self__, *,
                 hvn1: pulumi.Input[str],
                 hvn2: pulumi.Input[str]):
        """
        The set of arguments for constructing a HvnPeeringConnection resource.
        :param pulumi.Input[str] hvn1: The unique URL of one of the HVNs being peered.
        :param pulumi.Input[str] hvn2: The unique URL of one of the HVNs being peered.
        """
        pulumi.set(__self__, "hvn1", hvn1)
        pulumi.set(__self__, "hvn2", hvn2)

    @property
    @pulumi.getter
    def hvn1(self) -> pulumi.Input[str]:
        """
        The unique URL of one of the HVNs being peered.
        """
        return pulumi.get(self, "hvn1")

    @hvn1.setter
    def hvn1(self, value: pulumi.Input[str]):
        pulumi.set(self, "hvn1", value)

    @property
    @pulumi.getter
    def hvn2(self) -> pulumi.Input[str]:
        """
        The unique URL of one of the HVNs being peered.
        """
        return pulumi.get(self, "hvn2")

    @hvn2.setter
    def hvn2(self, value: pulumi.Input[str]):
        pulumi.set(self, "hvn2", value)


@pulumi.input_type
class _HvnPeeringConnectionState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 expires_at: Optional[pulumi.Input[str]] = None,
                 hvn1: Optional[pulumi.Input[str]] = None,
                 hvn2: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 peering_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HvnPeeringConnection resources.
        :param pulumi.Input[str] created_at: The time that the peering connection was created.
        :param pulumi.Input[str] expires_at: The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        :param pulumi.Input[str] hvn1: The unique URL of one of the HVNs being peered.
        :param pulumi.Input[str] hvn2: The unique URL of one of the HVNs being peered.
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
        :param pulumi.Input[str] peering_id: The ID of the peering connection.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
        :param pulumi.Input[str] self_link: A unique URL identifying the peering connection
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if expires_at is not None:
            pulumi.set(__self__, "expires_at", expires_at)
        if hvn1 is not None:
            pulumi.set(__self__, "hvn1", hvn1)
        if hvn2 is not None:
            pulumi.set(__self__, "hvn2", hvn2)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if peering_id is not None:
            pulumi.set(__self__, "peering_id", peering_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time that the peering connection was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @expires_at.setter
    def expires_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "expires_at", value)

    @property
    @pulumi.getter
    def hvn1(self) -> Optional[pulumi.Input[str]]:
        """
        The unique URL of one of the HVNs being peered.
        """
        return pulumi.get(self, "hvn1")

    @hvn1.setter
    def hvn1(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hvn1", value)

    @property
    @pulumi.getter
    def hvn2(self) -> Optional[pulumi.Input[str]]:
        """
        The unique URL of one of the HVNs being peered.
        """
        return pulumi.get(self, "hvn2")

    @hvn2.setter
    def hvn2(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hvn2", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the peering connection.
        """
        return pulumi.get(self, "peering_id")

    @peering_id.setter
    def peering_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "peering_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL identifying the peering connection
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)


class HvnPeeringConnection(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hvn1: Optional[pulumi.Input[str]] = None,
                 hvn2: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The HVN peering connection resource allows you to manage a peering connection between HVNs.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        hvn1 = hcp.Hvn("hvn1",
            hvn_id="hvn-1",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.25.16.0/20")
        hvn2 = hcp.Hvn("hvn2",
            hvn_id="hvn-2",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.18.16.0/20")
        peer1 = hcp.HvnPeeringConnection("peer1",
            hvn1=hvn1.self_link,
            hvn2=hvn2.self_link)
        ```

        ## Import

        # The import ID requires the first HVN ID in the format {hvn_1_id}:{peering_id}

        ```sh
         $ pulumi import hcp:index/hvnPeeringConnection:HvnPeeringConnection peer_1 hvn-1:peer-1
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] hvn1: The unique URL of one of the HVNs being peered.
        :param pulumi.Input[str] hvn2: The unique URL of one of the HVNs being peered.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HvnPeeringConnectionArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The HVN peering connection resource allows you to manage a peering connection between HVNs.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        hvn1 = hcp.Hvn("hvn1",
            hvn_id="hvn-1",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.25.16.0/20")
        hvn2 = hcp.Hvn("hvn2",
            hvn_id="hvn-2",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.18.16.0/20")
        peer1 = hcp.HvnPeeringConnection("peer1",
            hvn1=hvn1.self_link,
            hvn2=hvn2.self_link)
        ```

        ## Import

        # The import ID requires the first HVN ID in the format {hvn_1_id}:{peering_id}

        ```sh
         $ pulumi import hcp:index/hvnPeeringConnection:HvnPeeringConnection peer_1 hvn-1:peer-1
        ```

        :param str resource_name: The name of the resource.
        :param HvnPeeringConnectionArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HvnPeeringConnectionArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 hvn1: Optional[pulumi.Input[str]] = None,
                 hvn2: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.plugin_download_url is None:
            opts.plugin_download_url = _utilities.get_plugin_download_url()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
            __props__ = HvnPeeringConnectionArgs.__new__(HvnPeeringConnectionArgs)

            if hvn1 is None and not opts.urn:
                raise TypeError("Missing required property 'hvn1'")
            __props__.__dict__["hvn1"] = hvn1
            if hvn2 is None and not opts.urn:
                raise TypeError("Missing required property 'hvn2'")
            __props__.__dict__["hvn2"] = hvn2
            __props__.__dict__["created_at"] = None
            __props__.__dict__["expires_at"] = None
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["peering_id"] = None
            __props__.__dict__["project_id"] = None
            __props__.__dict__["self_link"] = None
        super(HvnPeeringConnection, __self__).__init__(
            'hcp:index/hvnPeeringConnection:HvnPeeringConnection',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            expires_at: Optional[pulumi.Input[str]] = None,
            hvn1: Optional[pulumi.Input[str]] = None,
            hvn2: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            peering_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None) -> 'HvnPeeringConnection':
        """
        Get an existing HvnPeeringConnection resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The time that the peering connection was created.
        :param pulumi.Input[str] expires_at: The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        :param pulumi.Input[str] hvn1: The unique URL of one of the HVNs being peered.
        :param pulumi.Input[str] hvn2: The unique URL of one of the HVNs being peered.
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
        :param pulumi.Input[str] peering_id: The ID of the peering connection.
        :param pulumi.Input[str] project_id: The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
        :param pulumi.Input[str] self_link: A unique URL identifying the peering connection
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HvnPeeringConnectionState.__new__(_HvnPeeringConnectionState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["expires_at"] = expires_at
        __props__.__dict__["hvn1"] = hvn1
        __props__.__dict__["hvn2"] = hvn2
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["peering_id"] = peering_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["self_link"] = self_link
        return HvnPeeringConnection(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time that the peering connection was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="expiresAt")
    def expires_at(self) -> pulumi.Output[str]:
        """
        The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        """
        return pulumi.get(self, "expires_at")

    @property
    @pulumi.getter
    def hvn1(self) -> pulumi.Output[str]:
        """
        The unique URL of one of the HVNs being peered.
        """
        return pulumi.get(self, "hvn1")

    @property
    @pulumi.getter
    def hvn2(self) -> pulumi.Output[str]:
        """
        The unique URL of one of the HVNs being peered.
        """
        return pulumi.get(self, "hvn2")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="peeringId")
    def peering_id(self) -> pulumi.Output[str]:
        """
        The ID of the peering connection.
        """
        return pulumi.get(self, "peering_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        A unique URL identifying the peering connection
        """
        return pulumi.get(self, "self_link")

