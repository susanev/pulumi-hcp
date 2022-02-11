# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union, overload
from . import _utilities

__all__ = ['ConsulSnapshotArgs', 'ConsulSnapshot']

@pulumi.input_type
class ConsulSnapshotArgs:
    def __init__(__self__, *,
                 cluster_id: pulumi.Input[str],
                 snapshot_name: pulumi.Input[str]):
        """
        The set of arguments for constructing a ConsulSnapshot resource.
        :param pulumi.Input[str] cluster_id: The ID of the HCP Consul cluster.
        :param pulumi.Input[str] snapshot_name: The name of the snapshot.
        """
        pulumi.set(__self__, "cluster_id", cluster_id)
        pulumi.set(__self__, "snapshot_name", snapshot_name)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Input[str]:
        """
        The ID of the HCP Consul cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: pulumi.Input[str]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Input[str]:
        """
        The name of the snapshot.
        """
        return pulumi.get(self, "snapshot_name")

    @snapshot_name.setter
    def snapshot_name(self, value: pulumi.Input[str]):
        pulumi.set(self, "snapshot_name", value)


@pulumi.input_type
class _ConsulSnapshotState:
    def __init__(__self__, *,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 consul_version: Optional[pulumi.Input[str]] = None,
                 organization_id: Optional[pulumi.Input[str]] = None,
                 project_id: Optional[pulumi.Input[str]] = None,
                 restored_at: Optional[pulumi.Input[str]] = None,
                 size: Optional[pulumi.Input[int]] = None,
                 snapshot_id: Optional[pulumi.Input[str]] = None,
                 snapshot_name: Optional[pulumi.Input[str]] = None):
        """
        Input properties used for looking up and filtering ConsulSnapshot resources.
        :param pulumi.Input[str] cluster_id: The ID of the HCP Consul cluster.
        :param pulumi.Input[str] consul_version: The version of Consul at the time of snapshot creation.
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the project the HCP Consul cluster is located.
        :param pulumi.Input[str] project_id: The ID of the project the HCP Consul cluster is located.
        :param pulumi.Input[str] restored_at: Timestamp of when the snapshot was restored. If the snapshot has not been restored, this field will be blank.
        :param pulumi.Input[int] size: The size of the snapshot in bytes.
        :param pulumi.Input[str] snapshot_id: The ID of the Consul snapshot
        :param pulumi.Input[str] snapshot_name: The name of the snapshot.
        """
        if cluster_id is not None:
            pulumi.set(__self__, "cluster_id", cluster_id)
        if consul_version is not None:
            pulumi.set(__self__, "consul_version", consul_version)
        if organization_id is not None:
            pulumi.set(__self__, "organization_id", organization_id)
        if project_id is not None:
            pulumi.set(__self__, "project_id", project_id)
        if restored_at is not None:
            pulumi.set(__self__, "restored_at", restored_at)
        if size is not None:
            pulumi.set(__self__, "size", size)
        if snapshot_id is not None:
            pulumi.set(__self__, "snapshot_id", snapshot_id)
        if snapshot_name is not None:
            pulumi.set(__self__, "snapshot_name", snapshot_name)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP Consul cluster.
        """
        return pulumi.get(self, "cluster_id")

    @cluster_id.setter
    def cluster_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "cluster_id", value)

    @property
    @pulumi.getter(name="consulVersion")
    def consul_version(self) -> Optional[pulumi.Input[str]]:
        """
        The version of Consul at the time of snapshot creation.
        """
        return pulumi.get(self, "consul_version")

    @consul_version.setter
    def consul_version(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "consul_version", value)

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the HCP organization where the project the HCP Consul cluster is located.
        """
        return pulumi.get(self, "organization_id")

    @organization_id.setter
    def organization_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "organization_id", value)

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the project the HCP Consul cluster is located.
        """
        return pulumi.get(self, "project_id")

    @project_id.setter
    def project_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "project_id", value)

    @property
    @pulumi.getter(name="restoredAt")
    def restored_at(self) -> Optional[pulumi.Input[str]]:
        """
        Timestamp of when the snapshot was restored. If the snapshot has not been restored, this field will be blank.
        """
        return pulumi.get(self, "restored_at")

    @restored_at.setter
    def restored_at(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "restored_at", value)

    @property
    @pulumi.getter
    def size(self) -> Optional[pulumi.Input[int]]:
        """
        The size of the snapshot in bytes.
        """
        return pulumi.get(self, "size")

    @size.setter
    def size(self, value: Optional[pulumi.Input[int]]):
        pulumi.set(self, "size", value)

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> Optional[pulumi.Input[str]]:
        """
        The ID of the Consul snapshot
        """
        return pulumi.get(self, "snapshot_id")

    @snapshot_id.setter
    def snapshot_id(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_id", value)

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> Optional[pulumi.Input[str]]:
        """
        The name of the snapshot.
        """
        return pulumi.get(self, "snapshot_name")

    @snapshot_name.setter
    def snapshot_name(self, value: Optional[pulumi.Input[str]]):
        pulumi.set(self, "snapshot_name", value)


class ConsulSnapshot(pulumi.CustomResource):
    @overload
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 snapshot_name: Optional[pulumi.Input[str]] = None,
                 __props__=None):
        """
        The Consul snapshot resource allows users to manage Consul snapshots of an HCP Consul cluster. Snapshots currently have a retention policy of 30 days.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        # Note: Snapshots currently have a retention policy of 30 days. After that time, any Terraform
        # state refresh will note that a new snapshot resource will be created.
        example = hcp.ConsulSnapshot("example",
            cluster_id="consul-cluster",
            snapshot_name="my-snapshot")
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the HCP Consul cluster.
        :param pulumi.Input[str] snapshot_name: The name of the snapshot.
        """
        ...
    @overload
    def __init__(__self__,
                 resource_name: str,
                 args: ConsulSnapshotArgs,
                 opts: Optional[pulumi.ResourceOptions] = None):
        """
        The Consul snapshot resource allows users to manage Consul snapshots of an HCP Consul cluster. Snapshots currently have a retention policy of 30 days.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_hcp as hcp

        # Note: Snapshots currently have a retention policy of 30 days. After that time, any Terraform
        # state refresh will note that a new snapshot resource will be created.
        example = hcp.ConsulSnapshot("example",
            cluster_id="consul-cluster",
            snapshot_name="my-snapshot")
        ```

        :param str resource_name: The name of the resource.
        :param ConsulSnapshotArgs args: The arguments to use to populate this resource's properties.
        :param pulumi.ResourceOptions opts: Options for the resource.
        """
        ...
    def __init__(__self__, resource_name: str, *args, **kwargs):
        resource_args, opts = _utilities.get_resource_args_opts(ConsulSnapshotArgs, pulumi.ResourceOptions, *args, **kwargs)
        if resource_args is not None:
            __self__._internal_init(resource_name, opts, **resource_args.__dict__)
        else:
            __self__._internal_init(resource_name, *args, **kwargs)

    def _internal_init(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 cluster_id: Optional[pulumi.Input[str]] = None,
                 snapshot_name: Optional[pulumi.Input[str]] = None,
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
            __props__ = ConsulSnapshotArgs.__new__(ConsulSnapshotArgs)

            if cluster_id is None and not opts.urn:
                raise TypeError("Missing required property 'cluster_id'")
            __props__.__dict__["cluster_id"] = cluster_id
            if snapshot_name is None and not opts.urn:
                raise TypeError("Missing required property 'snapshot_name'")
            __props__.__dict__["snapshot_name"] = snapshot_name
            __props__.__dict__["consul_version"] = None
            __props__.__dict__["organization_id"] = None
            __props__.__dict__["project_id"] = None
            __props__.__dict__["restored_at"] = None
            __props__.__dict__["size"] = None
            __props__.__dict__["snapshot_id"] = None
        super(ConsulSnapshot, __self__).__init__(
            'hcp:index/consulSnapshot:ConsulSnapshot',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            cluster_id: Optional[pulumi.Input[str]] = None,
            consul_version: Optional[pulumi.Input[str]] = None,
            organization_id: Optional[pulumi.Input[str]] = None,
            project_id: Optional[pulumi.Input[str]] = None,
            restored_at: Optional[pulumi.Input[str]] = None,
            size: Optional[pulumi.Input[int]] = None,
            snapshot_id: Optional[pulumi.Input[str]] = None,
            snapshot_name: Optional[pulumi.Input[str]] = None) -> 'ConsulSnapshot':
        """
        Get an existing ConsulSnapshot resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[str] cluster_id: The ID of the HCP Consul cluster.
        :param pulumi.Input[str] consul_version: The version of Consul at the time of snapshot creation.
        :param pulumi.Input[str] organization_id: The ID of the HCP organization where the project the HCP Consul cluster is located.
        :param pulumi.Input[str] project_id: The ID of the project the HCP Consul cluster is located.
        :param pulumi.Input[str] restored_at: Timestamp of when the snapshot was restored. If the snapshot has not been restored, this field will be blank.
        :param pulumi.Input[int] size: The size of the snapshot in bytes.
        :param pulumi.Input[str] snapshot_id: The ID of the Consul snapshot
        :param pulumi.Input[str] snapshot_name: The name of the snapshot.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = _ConsulSnapshotState.__new__(_ConsulSnapshotState)

        __props__.__dict__["cluster_id"] = cluster_id
        __props__.__dict__["consul_version"] = consul_version
        __props__.__dict__["organization_id"] = organization_id
        __props__.__dict__["project_id"] = project_id
        __props__.__dict__["restored_at"] = restored_at
        __props__.__dict__["size"] = size
        __props__.__dict__["snapshot_id"] = snapshot_id
        __props__.__dict__["snapshot_name"] = snapshot_name
        return ConsulSnapshot(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter(name="clusterId")
    def cluster_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP Consul cluster.
        """
        return pulumi.get(self, "cluster_id")

    @property
    @pulumi.getter(name="consulVersion")
    def consul_version(self) -> pulumi.Output[str]:
        """
        The version of Consul at the time of snapshot creation.
        """
        return pulumi.get(self, "consul_version")

    @property
    @pulumi.getter(name="organizationId")
    def organization_id(self) -> pulumi.Output[str]:
        """
        The ID of the HCP organization where the project the HCP Consul cluster is located.
        """
        return pulumi.get(self, "organization_id")

    @property
    @pulumi.getter(name="projectId")
    def project_id(self) -> pulumi.Output[str]:
        """
        The ID of the project the HCP Consul cluster is located.
        """
        return pulumi.get(self, "project_id")

    @property
    @pulumi.getter(name="restoredAt")
    def restored_at(self) -> pulumi.Output[str]:
        """
        Timestamp of when the snapshot was restored. If the snapshot has not been restored, this field will be blank.
        """
        return pulumi.get(self, "restored_at")

    @property
    @pulumi.getter
    def size(self) -> pulumi.Output[int]:
        """
        The size of the snapshot in bytes.
        """
        return pulumi.get(self, "size")

    @property
    @pulumi.getter(name="snapshotId")
    def snapshot_id(self) -> pulumi.Output[str]:
        """
        The ID of the Consul snapshot
        """
        return pulumi.get(self, "snapshot_id")

    @property
    @pulumi.getter(name="snapshotName")
    def snapshot_name(self) -> pulumi.Output[str]:
        """
        The name of the snapshot.
        """
        return pulumi.get(self, "snapshot_name")

