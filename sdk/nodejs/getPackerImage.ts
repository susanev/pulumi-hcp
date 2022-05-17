// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The Packer Image data source iteration gets the most recent iteration (or build) of an image, given an iteration id.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as hcp from "@pulumi/hcp";
 *
 * const hardened-source = hcp.getPackerIteration({
 *     bucketName: "hardened-ubuntu-16-04",
 *     channel: "production",
 * });
 * const foo = hardened_source.then(hardened_source => hcp.getPackerImage({
 *     bucketName: "hardened-ubuntu-16-04",
 *     cloudProvider: "aws",
 *     iterationId: hardened_source.ulid,
 *     region: "us-east-1",
 * }));
 * export const packer_registry_ubuntu = foo.then(foo => foo.cloudImageId);
 * ```
 *
 * > **Note:** This data source only returns the first found image's metadata filtered by the given schema values, from the returned list of images associated with the specified iteration. Therefore, if multiple images exist in the same region, it will only pick one of them. If that's the case, you may consider separating your builds into different buckets.
 */
export function getPackerImage(args: GetPackerImageArgs, opts?: pulumi.InvokeOptions): Promise<GetPackerImageResult> {
    if (!opts) {
        opts = {}
    }

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
    return pulumi.runtime.invoke("hcp:index/getPackerImage:getPackerImage", {
        "bucketName": args.bucketName,
        "cloudProvider": args.cloudProvider,
        "iterationId": args.iterationId,
        "region": args.region,
    }, opts);
}

/**
 * A collection of arguments for invoking getPackerImage.
 */
export interface GetPackerImageArgs {
    bucketName: string;
    cloudProvider: string;
    iterationId: string;
    region: string;
}

/**
 * A collection of values returned by getPackerImage.
 */
export interface GetPackerImageResult {
    readonly bucketName: string;
    readonly buildId: string;
    readonly cloudImageId: string;
    readonly cloudProvider: string;
    readonly componentType: string;
    readonly createdAt: string;
    /**
     * The provider-assigned unique ID for this managed resource.
     */
    readonly id: string;
    readonly iterationId: string;
    readonly labels: {[key: string]: any};
    readonly organizationId: string;
    readonly packerRunUuid: string;
    readonly projectId: string;
    readonly region: string;
}

export function getPackerImageOutput(args: GetPackerImageOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetPackerImageResult> {
    return pulumi.output(args).apply(a => getPackerImage(a, opts))
}

/**
 * A collection of arguments for invoking getPackerImage.
 */
export interface GetPackerImageOutputArgs {
    bucketName: pulumi.Input<string>;
    cloudProvider: pulumi.Input<string>;
    iterationId: pulumi.Input<string>;
    region: pulumi.Input<string>;
}
