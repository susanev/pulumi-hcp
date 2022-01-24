// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

export class VaultClusterAdminToken extends pulumi.CustomResource {
    /**
     * Get an existing VaultClusterAdminToken resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: VaultClusterAdminTokenState, opts?: pulumi.CustomResourceOptions): VaultClusterAdminToken {
        return new VaultClusterAdminToken(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcp:index/vaultClusterAdminToken:VaultClusterAdminToken';

    /**
     * Returns true if the given object is an instance of VaultClusterAdminToken.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is VaultClusterAdminToken {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === VaultClusterAdminToken.__pulumiType;
    }

    /**
     * The ID of the HCP Vault cluster.
     */
    public readonly clusterId!: pulumi.Output<string>;
    /**
     * The time that the admin token was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The admin token of this HCP Vault cluster.
     */
    public /*out*/ readonly token!: pulumi.Output<string>;

    /**
     * Create a VaultClusterAdminToken resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: VaultClusterAdminTokenArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: VaultClusterAdminTokenArgs | VaultClusterAdminTokenState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as VaultClusterAdminTokenState | undefined;
            resourceInputs["clusterId"] = state ? state.clusterId : undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["token"] = state ? state.token : undefined;
        } else {
            const args = argsOrState as VaultClusterAdminTokenArgs | undefined;
            if ((!args || args.clusterId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'clusterId'");
            }
            resourceInputs["clusterId"] = args ? args.clusterId : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["token"] = undefined /*out*/;
        }
        if (!opts.version) {
            opts = pulumi.mergeOptions(opts, { version: utilities.getVersion()});
        }
        super(VaultClusterAdminToken.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering VaultClusterAdminToken resources.
 */
export interface VaultClusterAdminTokenState {
    /**
     * The ID of the HCP Vault cluster.
     */
    clusterId?: pulumi.Input<string>;
    /**
     * The time that the admin token was created.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * The admin token of this HCP Vault cluster.
     */
    token?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a VaultClusterAdminToken resource.
 */
export interface VaultClusterAdminTokenArgs {
    /**
     * The ID of the HCP Vault cluster.
     */
    clusterId: pulumi.Input<string>;
}
