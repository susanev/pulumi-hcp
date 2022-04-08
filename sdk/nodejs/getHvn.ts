// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The HVN data source provides information about an existing HashiCorp Virtual Network.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const example = hcp.getHvn({
 *     hvnId: _var.hvn_id,
 * });
 * ```
 */
export function getHvn(args: GetHvnArgs, opts?: pulumi.InvokeOptions): Promise<GetHvnResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("hcp:index/getHvn:getHvn", {
        "hvnId": args.hvnId,
    }, opts);
}

/**
 * A collection of arguments for invoking getHvn.
 */
export interface GetHvnArgs {
    /**
     * The ID of the HashiCorp Virtual Network (HVN).
     */
    hvnId: string;
}

/**
 * A collection of values returned by getHvn.
 */
export interface GetHvnResult {
    /**
     * The CIDR range of the HVN.
     */
    readonly cidrBlock: string;
    /**
     * The provider where the HVN is located.
     */
    readonly cloudProvider: string;
    /**
     * The time that the HVN was created.
     */
    readonly createdAt: string;
    /**
     * The ID of the HashiCorp Virtual Network (HVN).
     */
    readonly hvnId: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    /**
     * The ID of the HCP organization where the HVN is located.
     */
    readonly organizationId: string;
    /**
     * The ID of the HCP project where the HVN is located.
     */
    readonly projectId: string;
    /**
     * The provider account ID where the HVN is located.
     */
    readonly providerAccountId: string;
    /**
     * The region where the HVN is located.
     */
    readonly region: string;
    /**
     * A unique URL identifying the HVN.
     */
    readonly selfLink: string;
}

export function getHvnOutput(args: GetHvnOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetHvnResult> {
    return pulumi.output(args).apply(a => getHvn(a, opts))
}

/**
 * A collection of arguments for invoking getHvn.
 */
export interface GetHvnOutputArgs {
    /**
     * The ID of the HashiCorp Virtual Network (HVN).
     */
    hvnId: pulumi.Input<string>;
}
