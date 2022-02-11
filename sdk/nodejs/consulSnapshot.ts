// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The Consul snapshot resource allows users to manage Consul snapshots of an HCP Consul cluster. Snapshots currently have a retention policy of 30 days.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * // Note: Snapshots currently have a retention policy of 30 days. After that time, any Terraform
 * // state refresh will note that a new snapshot resource will be created.
 * const example = new hcp.ConsulSnapshot("example", {
 *     clusterId: "consul-cluster",
 *     snapshotName: "my-snapshot",
 * });
 * ```
 */
export class ConsulSnapshot extends pulumi.CustomResource {
    /**
     * Get an existing ConsulSnapshot resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: ConsulSnapshotState, opts?: pulumi.CustomResourceOptions): ConsulSnapshot {
        return new ConsulSnapshot(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcp:index/consulSnapshot:ConsulSnapshot';

    /**
     * Returns true if the given object is an instance of ConsulSnapshot.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is ConsulSnapshot {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === ConsulSnapshot.__pulumiType;
    }

    /**
     * The ID of the HCP Consul cluster.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The version of Consul at the time of snapshot creation.
     */
    public /*out*/ readonly consulVersion!: pulumi.Output<string>;
    /**
     * The ID of the HCP organization where the project the HCP Consul cluster is located.
     */
    public /*out*/ readonly organizationId!: pulumi.Output<string>;
    /**
     * The ID of the project the HCP Consul cluster is located.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * Timestamp of when the snapshot was restored. If the snapshot has not been restored, this field will be blank.
     */
    public /*out*/ readonly restoredAt!: pulumi.Output<string>;
    /**
     * The size of the snapshot in bytes.
     */
    public /*out*/ readonly size!: pulumi.Output<number>;
    /**
     * The ID of the Consul snapshot
     */
    public /*out*/ readonly snapshotId!: pulumi.Output<string>;
    /**
     * The name of the snapshot.
     */
    public readonly snapshotName!: pulumi.Output<string>;

    /**
     * Create a ConsulSnapshot resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: ConsulSnapshotArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: ConsulSnapshotArgs | ConsulSnapshotState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as ConsulSnapshotState | undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["consulVersion"] = state ? state.consulVersion : undefined;
            resourceInputs["organizationId"] = state ? state.organizationId : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["restoredAt"] = state ? state.restoredAt : undefined;
            resourceInputs["size"] = state ? state.size : undefined;
            resourceInputs["snapshotId"] = state ? state.snapshotId : undefined;
            resourceInputs["snapshotName"] = state ? state.snapshotName : undefined;
        } else {
            const args = argsOrState as ConsulSnapshotArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            if ((!args || args.snapshotName === undefined) && !opts.urn) {
                throw new Error("Missing required property 'snapshotName'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["snapshotName"] = args ? args.snapshotName : undefined;
            resourceInputs["consulVersion"] = undefined /*out*/;
            resourceInputs["organizationId"] = undefined /*out*/;
            resourceInputs["projectId"] = undefined /*out*/;
            resourceInputs["restoredAt"] = undefined /*out*/;
            resourceInputs["size"] = undefined /*out*/;
            resourceInputs["snapshotId"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(ConsulSnapshot.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering ConsulSnapshot resources.
 */
export interface ConsulSnapshotState {
    /**
     * The ID of the HCP Consul cluster.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The version of Consul at the time of snapshot creation.
     */
    consulVersion?: pulumi.Input<string>;
    /**
     * The ID of the HCP organization where the project the HCP Consul cluster is located.
     */
    organizationId?: pulumi.Input<string>;
    /**
     * The ID of the project the HCP Consul cluster is located.
     */
    projectId?: pulumi.Input<string>;
    /**
     * Timestamp of when the snapshot was restored. If the snapshot has not been restored, this field will be blank.
     */
    restoredAt?: pulumi.Input<string>;
    /**
     * The size of the snapshot in bytes.
     */
    size?: pulumi.Input<number>;
    /**
     * The ID of the Consul snapshot
     */
    snapshotId?: pulumi.Input<string>;
    /**
     * The name of the snapshot.
     */
    snapshotName?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a ConsulSnapshot resource.
 */
export interface ConsulSnapshotArgs {
    /**
     * The ID of the HCP Consul cluster.
     */
    clusterId: pulumi.Input<string>;
    /**
     * The name of the snapshot.
     */
    snapshotName: pulumi.Input<string>;
}
