// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * > Consul on Azure is now available in public beta. [Get started with end-to-end deployment configuration](https://learn.hashicorp.com/tutorials/cloud/consul-end-to-end-overview).
 *
 * The Consul cluster resource allows you to manage an HCP Consul cluster.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as pulumi_hcp from "@grapl/pulumi-hcp";
 *
 * const exampleHvn = new hcp.Hvn("exampleHvn", {
 *     hvnId: "hvn",
 *     cloudProvider: "aws",
 *     region: "us-west-2",
 *     cidrBlock: "172.25.16.0/20",
 * });
 * const exampleConsulCluster = new hcp.ConsulCluster("exampleConsulCluster", {
 *     clusterId: "consul-cluster",
 *     hvnId: exampleHvn.hvnId,
 *     tier: "development",
 * });
 * ```
 *
 * ## Import
 *
 * # The import ID is {cluster_id}
 *
 * ```sh
 *  $ pulumi import hcp:index/consulCluster:ConsulCluster example consul-cluster
 * ```
 */
export class ConsulCluster extends pulumi.CustomResource {
    /**
     * Get an existing ConsulCluster resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConsulClusterState, opts?: pulumi.CustomResourceOptions): ConsulCluster {
        return new ConsulCluster(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcp:index/consulCluster:ConsulCluster';

    /**
     * Returns true if the given object is an instance of ConsulCluster.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConsulCluster {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConsulCluster.__pulumiType;
    }

    /**
     * Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
     * auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
     * defines the HVN resources that are allowed to communicate with each other.
     */
    public readonly autoHvnToHvnPeering!: pulumi.Output<boolean>;
    /**
     * The provider where the HCP Consul cluster is located.
     */
    public /*out*/ readonly cloudProvider!: pulumi.Output<string>;
    /**
     * The ID of the HCP Consul cluster.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * Denotes the Consul connect feature should be enabled for this cluster. Default to true.
     */
    public readonly connectEnabled!: pulumi.Output<boolean | undefined>;
    /**
     * Denotes that automatic Consul upgrades are enabled.
     */
    public /*out*/ readonly consulAutomaticUpgrades!: pulumi.Output<boolean>;
    /**
     * The cluster CA file encoded as a Base64 string.
     */
    public /*out*/ readonly consulCaFile!: pulumi.Output<string>;
    /**
     * The cluster config encoded as a Base64 string.
     */
    public /*out*/ readonly consulConfigFile!: pulumi.Output<string>;
    /**
     * The private URL for the Consul UI.
     */
    public /*out*/ readonly consulPrivateEndpointUrl!: pulumi.Output<string>;
    /**
     * The public URL for the Consul UI. This will be empty if `public_endpoint` is `false`.
     */
    public /*out*/ readonly consulPublicEndpointUrl!: pulumi.Output<string>;
    /**
     * The accessor ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using
     * the `hcp_consul_root_token` resource, this field is no longer valid.
     */
    public /*out*/ readonly consulRootTokenAccessorId!: pulumi.Output<string>;
    /**
     * The secret ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the
     * `hcp_consul_root_token` resource, this field is no longer valid.
     */
    public /*out*/ readonly consulRootTokenSecretId!: pulumi.Output<string>;
    /**
     * The Consul snapshot interval.
     */
    public /*out*/ readonly consulSnapshotInterval!: pulumi.Output<string>;
    /**
     * The retention policy for Consul snapshots.
     */
    public /*out*/ readonly consulSnapshotRetention!: pulumi.Output<string>;
    /**
     * The Consul version of the cluster.
     */
    public /*out*/ readonly consulVersion!: pulumi.Output<string>;
    /**
     * The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
     */
    public readonly datacenter!: pulumi.Output<string>;
    /**
     * The ID of the HVN this HCP Consul cluster is associated to.
     */
    public readonly hvnId!: pulumi.Output<string>;
    /**
     * The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
     * recommended by HCP.
     */
    public readonly minConsulVersion!: pulumi.Output<string | undefined>;
    /**
     * The ID of the organization this HCP Consul cluster is located in.
     */
    public /*out*/ readonly organizationId!: pulumi.Output<string>;
    /**
     * The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
     * not specified, it is a standalone cluster.
     */
    public readonly primaryLink!: pulumi.Output<string | undefined>;
    /**
     * The ID of the project this HCP Consul cluster is located in.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
     */
    public readonly publicEndpoint!: pulumi.Output<boolean | undefined>;
    /**
     * The region where the HCP Consul cluster is located.
     */
    public /*out*/ readonly region!: pulumi.Output<string>;
    /**
     * The number of Consul server nodes in the cluster.
     */
    public /*out*/ readonly scale!: pulumi.Output<number>;
    /**
     * A unique URL identifying the HCP Consul cluster.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;
    /**
     * The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
     * development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
     * https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
     */
    public readonly size!: pulumi.Output<string>;
    /**
     * The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
     * this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
     */
    public readonly tier!: pulumi.Output<string>;

    /**
     * Create a ConsulCluster resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConsulClusterArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConsulClusterArgs | ConsulClusterState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ConsulClusterState | undefined;
            resourceInputs["autoHvnToHvnPeering"] = state ? state.autoHvnToHvnPeering : undefined;
            resourceInputs["cloudProvider"] = state ? state.cloudProvider : undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["connectEnabled"] = state ? state.connectEnabled : undefined;
            resourceInputs["consulAutomaticUpgrades"] = state ? state.consulAutomaticUpgrades : undefined;
            resourceInputs["consulCaFile"] = state ? state.consulCaFile : undefined;
            resourceInputs["consulConfigFile"] = state ? state.consulConfigFile : undefined;
            resourceInputs["consulPrivateEndpointUrl"] = state ? state.consulPrivateEndpointUrl : undefined;
            resourceInputs["consulPublicEndpointUrl"] = state ? state.consulPublicEndpointUrl : undefined;
            resourceInputs["consulRootTokenAccessorId"] = state ? state.consulRootTokenAccessorId : undefined;
            resourceInputs["consulRootTokenSecretId"] = state ? state.consulRootTokenSecretId : undefined;
            resourceInputs["consulSnapshotInterval"] = state ? state.consulSnapshotInterval : undefined;
            resourceInputs["consulSnapshotRetention"] = state ? state.consulSnapshotRetention : undefined;
            resourceInputs["consulVersion"] = state ? state.consulVersion : undefined;
            resourceInputs["datacenter"] = state ? state.datacenter : undefined;
            resourceInputs["hvnId"] = state ? state.hvnId : undefined;
            resourceInputs["minConsulVersion"] = state ? state.minConsulVersion : undefined;
            resourceInputs["organizationId"] = state ? state.organizationId : undefined;
            resourceInputs["primaryLink"] = state ? state.primaryLink : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["publicEndpoint"] = state ? state.publicEndpoint : undefined;
            resourceInputs["region"] = state ? state.region : undefined;
            resourceInputs["scale"] = state ? state.scale : undefined;
            resourceInputs["selfLink"] = state ? state.selfLink : undefined;
            resourceInputs["size"] = state ? state.size : undefined;
            resourceInputs["tier"] = state ? state.tier : undefined;
        } else {
            const args = argsOrState as ConsulClusterArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.hvnId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hvnId'");
            }
            if ((!args || args.tier === undefined) && !opts.urn) {
                throw new Error("Missing required property 'tier'");
            }
            resourceInputs["autoHvnToHvnPeering"] = args ? args.autoHvnToHvnPeering : undefined;
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["connectEnabled"] = args ? args.connectEnabled : undefined;
            resourceInputs["datacenter"] = args ? args.datacenter : undefined;
            resourceInputs["hvnId"] = args ? args.hvnId : undefined;
            resourceInputs["minConsulVersion"] = args ? args.minConsulVersion : undefined;
            resourceInputs["primaryLink"] = args ? args.primaryLink : undefined;
            resourceInputs["publicEndpoint"] = args ? args.publicEndpoint : undefined;
            resourceInputs["size"] = args ? args.size : undefined;
            resourceInputs["tier"] = args ? args.tier : undefined;
            resourceInputs["cloudProvider"] = undefined /*out*/;
            resourceInputs["consulAutomaticUpgrades"] = undefined /*out*/;
            resourceInputs["consulCaFile"] = undefined /*out*/;
            resourceInputs["consulConfigFile"] = undefined /*out*/;
            resourceInputs["consulPrivateEndpointUrl"] = undefined /*out*/;
            resourceInputs["consulPublicEndpointUrl"] = undefined /*out*/;
            resourceInputs["consulRootTokenAccessorId"] = undefined /*out*/;
            resourceInputs["consulRootTokenSecretId"] = undefined /*out*/;
            resourceInputs["consulSnapshotInterval"] = undefined /*out*/;
            resourceInputs["consulSnapshotRetention"] = undefined /*out*/;
            resourceInputs["consulVersion"] = undefined /*out*/;
            resourceInputs["organizationId"] = undefined /*out*/;
            resourceInputs["projectId"] = undefined /*out*/;
            resourceInputs["region"] = undefined /*out*/;
            resourceInputs["scale"] = undefined /*out*/;
            resourceInputs["selfLink"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ConsulCluster.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ConsulCluster resources.
 */
export interface ConsulClusterState {
    /**
     * Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
     * auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
     * defines the HVN resources that are allowed to communicate with each other.
     */
    autoHvnToHvnPeering?: pulumi.Input<boolean>;
    /**
     * The provider where the HCP Consul cluster is located.
     */
    cloudProvider?: pulumi.Input<string>;
    /**
     * The ID of the HCP Consul cluster.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * Denotes the Consul connect feature should be enabled for this cluster. Default to true.
     */
    connectEnabled?: pulumi.Input<boolean>;
    /**
     * Denotes that automatic Consul upgrades are enabled.
     */
    consulAutomaticUpgrades?: pulumi.Input<boolean>;
    /**
     * The cluster CA file encoded as a Base64 string.
     */
    consulCaFile?: pulumi.Input<string>;
    /**
     * The cluster config encoded as a Base64 string.
     */
    consulConfigFile?: pulumi.Input<string>;
    /**
     * The private URL for the Consul UI.
     */
    consulPrivateEndpointUrl?: pulumi.Input<string>;
    /**
     * The public URL for the Consul UI. This will be empty if `public_endpoint` is `false`.
     */
    consulPublicEndpointUrl?: pulumi.Input<string>;
    /**
     * The accessor ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using
     * the `hcp_consul_root_token` resource, this field is no longer valid.
     */
    consulRootTokenAccessorId?: pulumi.Input<string>;
    /**
     * The secret ID of the root ACL token that is generated upon cluster creation. If a new root token is generated using the
     * `hcp_consul_root_token` resource, this field is no longer valid.
     */
    consulRootTokenSecretId?: pulumi.Input<string>;
    /**
     * The Consul snapshot interval.
     */
    consulSnapshotInterval?: pulumi.Input<string>;
    /**
     * The retention policy for Consul snapshots.
     */
    consulSnapshotRetention?: pulumi.Input<string>;
    /**
     * The Consul version of the cluster.
     */
    consulVersion?: pulumi.Input<string>;
    /**
     * The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
     */
    datacenter?: pulumi.Input<string>;
    /**
     * The ID of the HVN this HCP Consul cluster is associated to.
     */
    hvnId?: pulumi.Input<string>;
    /**
     * The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
     * recommended by HCP.
     */
    minConsulVersion?: pulumi.Input<string>;
    /**
     * The ID of the organization this HCP Consul cluster is located in.
     */
    organizationId?: pulumi.Input<string>;
    /**
     * The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
     * not specified, it is a standalone cluster.
     */
    primaryLink?: pulumi.Input<string>;
    /**
     * The ID of the project this HCP Consul cluster is located in.
     */
    projectId?: pulumi.Input<string>;
    /**
     * Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
     */
    publicEndpoint?: pulumi.Input<boolean>;
    /**
     * The region where the HCP Consul cluster is located.
     */
    region?: pulumi.Input<string>;
    /**
     * The number of Consul server nodes in the cluster.
     */
    scale?: pulumi.Input<number>;
    /**
     * A unique URL identifying the HCP Consul cluster.
     */
    selfLink?: pulumi.Input<string>;
    /**
     * The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
     * development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
     * https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
     */
    size?: pulumi.Input<string>;
    /**
     * The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
     * this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
     */
    tier?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ConsulCluster resource.
 */
export interface ConsulClusterArgs {
    /**
     * Enables automatic HVN to HVN peering when creating a secondary cluster in a federation. The alternative to using the
     * auto-accept feature is to create an [`hcp_hvn_peering_connection`](hvn_peering_connection.md) resource that explicitly
     * defines the HVN resources that are allowed to communicate with each other.
     */
    autoHvnToHvnPeering?: pulumi.Input<boolean>;
    /**
     * The ID of the HCP Consul cluster.
     */
    clusterId: pulumi.Input<string>;
    /**
     * Denotes the Consul connect feature should be enabled for this cluster. Default to true.
     */
    connectEnabled?: pulumi.Input<boolean>;
    /**
     * The Consul data center name of the cluster. If not specified, it is defaulted to the value of `cluster_id`.
     */
    datacenter?: pulumi.Input<string>;
    /**
     * The ID of the HVN this HCP Consul cluster is associated to.
     */
    hvnId: pulumi.Input<string>;
    /**
     * The minimum Consul version of the cluster. If not specified, it is defaulted to the version that is currently
     * recommended by HCP.
     */
    minConsulVersion?: pulumi.Input<string>;
    /**
     * The `self_link` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If
     * not specified, it is a standalone cluster.
     */
    primaryLink?: pulumi.Input<string>;
    /**
     * Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
     */
    publicEndpoint?: pulumi.Input<boolean>;
    /**
     * The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for
     * development tier - `x_small`. Valid options for other tiers - `small`, `medium`, `large`. For more details -
     * https://cloud.hashicorp.com/pricing/consul. Upgrading the size of a cluster after creation is allowed.
     */
    size?: pulumi.Input<string>;
    /**
     * The tier that the HCP Consul cluster will be provisioned as. Only `development`, `standard` and `plus` are available at
     * this time. See [pricing information](https://cloud.hashicorp.com/pricing/consul).
     */
    tier: pulumi.Input<string>;
}
