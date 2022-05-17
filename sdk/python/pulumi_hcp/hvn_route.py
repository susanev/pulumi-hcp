# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['HvnRouteArgs', 'HvnRoute']

@pulumi.input_type
class HvnRouteArgs:
    def __init__(__self__, *,
                 destination_cidr: pulumi.Input[str],
                 hvn_link: pulumi.Input[str],
                 hvn_route_id: pulumi.Input[str],
                 target_link: pulumi.Input[str]):
        """
        The set of arguments for constructing a HvnRoute resource.
        :param pulumi.Input[str] destination_cidr: The destination CIDR of the HVN route.
        :param pulumi.Input[str] hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] hvn_route_id: The ID of the HVN route.
        :param pulumi.Input[str] target_link: A unique URL identifying the target of the HVN route. Examples of the target:
               [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
        """
        pulumi.set(__self__, "destination_cidr", destination_cidr)
        pulumi.set(__self__, "hvn_link", hvn_link)
        pulumi.set(__self__, "hvn_route_id", hvn_route_id)
        pulumi.set(__self__, "target_link", target_link)

    @property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> pulumi.Input[str]:
        """
        The destination CIDR of the HVN route.
        """
        return pulumi.get(self, "destination_cidr")

    @destination_cidr.setter
    def destination_cidr(self, value: pulumi.Input[str]):
        pulumi.set(self, "destination_cidr", value)

    @property
    @pulumi.getter(name="hvnLink")
    def hvn_link(self) -> pulumi.Input[str]:
        """
        The `self_link` of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_link")

    @hvn_link.setter
    def hvn_link(self, value: pulumi.Input[str]):
        pulumi.set(self, "hvn_link", value)

    @property
    @pulumi.getter(name="hvnRouteId")
    def hvn_route_id(self) -> pulumi.Input[str]:
        """
        The ID of the HVN route.
        """
        return pulumi.get(self, "hvn_route_id")

    @hvn_route_id.setter
    def hvn_route_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "hvn_route_id", value)

    @property
    @pulumi.getter(name="targetLink")
    def target_link(self) -> pulumi.Input[str]:
        """
        A unique URL identifying the target of the HVN route. Examples of the target:
        [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
        """
        return pulumi.get(self, "target_link")

    @target_link.setter
    def target_link(self, value: pulumi.Input[str]):
        pulumi.set(self, "target_link", value)


@pulumi.input_type
class _HvnRouteState:
    def __init__(__self__, *,
                 created_at: Optional[pulumi.Input[str]] = None,
                 destination_cidr: Optional[pulumi.Input[str]] = None,
                 hvn_link: Optional[pulumi.Input[str]] = None,
                 hvn_route_id: Optional[pulumi.Input[str]] = None,
                 self_link: Optional[pulumi.Input[str]] = None,
                 state: Optional[pulumi.Input[str]] = None,
                 target_link: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering HvnRoute resources.
        :param pulumi.Input[str] created_at: The time that the HVN route was created.
        :param pulumi.Input[str] destination_cidr: The destination CIDR of the HVN route.
        :param pulumi.Input[str] hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] hvn_route_id: The ID of the HVN route.
        :param pulumi.Input[str] self_link: A unique URL identifying the HVN route.
        :param pulumi.Input[str] state: The state of the HVN route.
        :param pulumi.Input[str] target_link: A unique URL identifying the target of the HVN route. Examples of the target:
               [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
        """
        if created_at is not None:
            pulumi.set(__self__, "created_at", created_at)
        if destination_cidr is not None:
            pulumi.set(__self__, "destination_cidr", destination_cidr)
        if hvn_link is not None:
            pulumi.set(__self__, "hvn_link", hvn_link)
        if hvn_route_id is not None:
            pulumi.set(__self__, "hvn_route_id", hvn_route_id)
        if self_link is not None:
            pulumi.set(__self__, "self_link", self_link)
        if state is not None:
            pulumi.set(__self__, "state", state)
        if target_link is not None:
            pulumi.set(__self__, "target_link", target_link)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> Optional[pulumi.Input[str]]:
        """
        The time that the HVN route was created.
        """
        return pulumi.get(self, "created_at")

    @created_at.setter
    def created_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "created_at", value)

    @property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> Optional[pulumi.Input[str]]:
        """
        The destination CIDR of the HVN route.
        """
        return pulumi.get(self, "destination_cidr")

    @destination_cidr.setter
    def destination_cidr(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "destination_cidr", value)

    @property
    @pulumi.getter(name="hvnLink")
    def hvn_link(self) -> Optional[pulumi.Input[str]]:
        """
        The `self_link` of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_link")

    @hvn_link.setter
    def hvn_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hvn_link", value)

    @property
    @pulumi.getter(name="hvnRouteId")
    def hvn_route_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HVN route.
        """
        return pulumi.get(self, "hvn_route_id")

    @hvn_route_id.setter
    def hvn_route_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "hvn_route_id", value)

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL identifying the HVN route.
        """
        return pulumi.get(self, "self_link")

    @self_link.setter
    def self_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "self_link", value)

    @property
    @pulumi.getter
    def state(self) -> Optional[pulumi.Input[str]]:
        """
        The state of the HVN route.
        """
        return pulumi.get(self, "state")

    @state.setter
    def state(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "state", value)

    @property
    @pulumi.getter(name="targetLink")
    def target_link(self) -> Optional[pulumi.Input[str]]:
        """
        A unique URL identifying the target of the HVN route. Examples of the target:
        [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
        """
        return pulumi.get(self, "target_link")

    @target_link.setter
    def target_link(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "target_link", value)


class HvnRoute(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_cidr: Optional[pulumi.Input[str]] = None,
                 hvn_link: Optional[pulumi.Input[str]] = None,
                 hvn_route_id: Optional[pulumi.Input[str]] = None,
                 target_link: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_hcp as hcp

        main = hcp.Hvn("main",
            hvn_id="main-hvn",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.25.16.0/20")
        # Creating a peering and a route for it.
        peer_vpc = aws.ec2.Vpc("peerVpc", cidr_block="192.168.0.0/20")
        example = hcp.AwsNetworkPeering("example",
            peering_id="peer-example",
            hvn_id=main.hvn_id,
            peer_vpc_id=peer_vpc.id,
            peer_account_id=peer_vpc.owner_id,
            peer_vpc_region="us-west-2")
        peer_vpc_peering_connection_accepter = aws.ec2.VpcPeeringConnectionAccepter("peerVpcPeeringConnectionAccepter",
            vpc_peering_connection_id=example.provider_peering_id,
            auto_accept=True)
        example_peering_route = hcp.HvnRoute("example-peering-route",
            hvn_link=main.self_link,
            hvn_route_id="peering-route",
            destination_cidr=peer_vpc.cidr_block,
            target_link=example.self_link)
        ```

        ## Import

        # The import ID is {hvn_id}:{hvn_route_id}

        ```sh
         $ pulumi import hcp:index/hvnRoute:HvnRoute example main-hvn:example-hvn-route
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] destination_cidr: The destination CIDR of the HVN route.
        :param pulumi.Input[str] hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] hvn_route_id: The ID of the HVN route.
        :param pulumi.Input[str] target_link: A unique URL identifying the target of the HVN route. Examples of the target:
               [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: HvnRouteArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        ## Example Usage

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_hcp as hcp

        main = hcp.Hvn("main",
            hvn_id="main-hvn",
            cloud_provider="aws",
            region="us-west-2",
            cidr_block="172.25.16.0/20")
        # Creating a peering and a route for it.
        peer_vpc = aws.ec2.Vpc("peerVpc", cidr_block="192.168.0.0/20")
        example = hcp.AwsNetworkPeering("example",
            peering_id="peer-example",
            hvn_id=main.hvn_id,
            peer_vpc_id=peer_vpc.id,
            peer_account_id=peer_vpc.owner_id,
            peer_vpc_region="us-west-2")
        peer_vpc_peering_connection_accepter = aws.ec2.VpcPeeringConnectionAccepter("peerVpcPeeringConnectionAccepter",
            vpc_peering_connection_id=example.provider_peering_id,
            auto_accept=True)
        example_peering_route = hcp.HvnRoute("example-peering-route",
            hvn_link=main.self_link,
            hvn_route_id="peering-route",
            destination_cidr=peer_vpc.cidr_block,
            target_link=example.self_link)
        ```

        ## Import

        # The import ID is {hvn_id}:{hvn_route_id}

        ```sh
         $ pulumi import hcp:index/hvnRoute:HvnRoute example main-hvn:example-hvn-route
        ```

        :param str resource_name: The name of the resource.
        :param HvnRouteArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(HvnRouteArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 destination_cidr: Optional[pulumi.Input[str]] = None,
                 hvn_link: Optional[pulumi.Input[str]] = None,
                 hvn_route_id: Optional[pulumi.Input[str]] = None,
                 target_link: Optional[pulumi.Input[str]] = None,
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
            __props__ = HvnRouteArgs.__new__(HvnRouteArgs)

            if destination_cidr is None and not opts.urn:
                raise TypeError("Missing required property 'destination_cidr'")
            __props__.__dict__["destination_cidr"] = destination_cidr
            if hvn_link is None and not opts.urn:
                raise TypeError("Missing required property 'hvn_link'")
            __props__.__dict__["hvn_link"] = hvn_link
            if hvn_route_id is None and not opts.urn:
                raise TypeError("Missing required property 'hvn_route_id'")
            __props__.__dict__["hvn_route_id"] = hvn_route_id
            if target_link is None and not opts.urn:
                raise TypeError("Missing required property 'target_link'")
            __props__.__dict__["target_link"] = target_link
            __props__.__dict__["created_at"] = None
            __props__.__dict__["self_link"] = None
            __props__.__dict__["state"] = None
        super(HvnRoute, __self__).__init__(
            'hcp:index/hvnRoute:HvnRoute',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            created_at: Optional[pulumi.Input[str]] = None,
            destination_cidr: Optional[pulumi.Input[str]] = None,
            hvn_link: Optional[pulumi.Input[str]] = None,
            hvn_route_id: Optional[pulumi.Input[str]] = None,
            self_link: Optional[pulumi.Input[str]] = None,
            state: Optional[pulumi.Input[str]] = None,
            target_link: Optional[pulumi.Input[str]] = None) -> 'HvnRoute':
        """
        Get an existing HvnRoute resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] created_at: The time that the HVN route was created.
        :param pulumi.Input[str] destination_cidr: The destination CIDR of the HVN route.
        :param pulumi.Input[str] hvn_link: The `self_link` of the HashiCorp Virtual Network (HVN).
        :param pulumi.Input[str] hvn_route_id: The ID of the HVN route.
        :param pulumi.Input[str] self_link: A unique URL identifying the HVN route.
        :param pulumi.Input[str] state: The state of the HVN route.
        :param pulumi.Input[str] target_link: A unique URL identifying the target of the HVN route. Examples of the target:
               [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _HvnRouteState.__new__(_HvnRouteState)

        __props__.__dict__["created_at"] = created_at
        __props__.__dict__["destination_cidr"] = destination_cidr
        __props__.__dict__["hvn_link"] = hvn_link
        __props__.__dict__["hvn_route_id"] = hvn_route_id
        __props__.__dict__["self_link"] = self_link
        __props__.__dict__["state"] = state
        __props__.__dict__["target_link"] = target_link
        return HvnRoute(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="createdAt")
    def created_at(self) -> pulumi.Output[str]:
        """
        The time that the HVN route was created.
        """
        return pulumi.get(self, "created_at")

    @property
    @pulumi.getter(name="destinationCidr")
    def destination_cidr(self) -> pulumi.Output[str]:
        """
        The destination CIDR of the HVN route.
        """
        return pulumi.get(self, "destination_cidr")

    @property
    @pulumi.getter(name="hvnLink")
    def hvn_link(self) -> pulumi.Output[str]:
        """
        The `self_link` of the HashiCorp Virtual Network (HVN).
        """
        return pulumi.get(self, "hvn_link")

    @property
    @pulumi.getter(name="hvnRouteId")
    def hvn_route_id(self) -> pulumi.Output[str]:
        """
        The ID of the HVN route.
        """
        return pulumi.get(self, "hvn_route_id")

    @property
    @pulumi.getter(name="selfLink")
    def self_link(self) -> pulumi.Output[str]:
        """
        A unique URL identifying the HVN route.
        """
        return pulumi.get(self, "self_link")

    @property
    @pulumi.getter
    def state(self) -> pulumi.Output[str]:
        """
        The state of the HVN route.
        """
        return pulumi.get(self, "state")

    @property
    @pulumi.getter(name="targetLink")
    def target_link(self) -> pulumi.Output[str]:
        """
        A unique URL identifying the target of the HVN route. Examples of the target:
        [`aws_network_peering`](aws_network_peering.md), [`aws_transit_gateway_attachment`](aws_transit_gateway_attachment.md)
        """
        return pulumi.get(self, "target_link")

