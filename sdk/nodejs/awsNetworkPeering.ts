// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The AWS network peering resource allows you to manage a network peering between an HVN and a peer AWS VPC.
 *
 * ## Example Usage
 *
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as pulumi_hcp from "@grapl/pulumi-hcp";
 *
 * const main = new hcp.Hvn("main", {
 *     hvnId: "main-hvn",
 *     cloudProvider: "aws",
 *     region: "us-west-2",
 *     cidrBlock: "172.25.16.0/20",
 * });
 * const peerVpc = new aws.ec2.Vpc("peerVpc", {cidrBlock: "172.31.0.0/16"});
 * const peerArn = aws.getArnOutput({
 *     arn: peerVpc.arn,
 * });
 * const dev = new hcp.AwsNetworkPeering("dev", {
 *     hvnId: main.hvnId,
 *     peeringId: "dev",
 *     peerVpcId: peerVpc.id,
 *     peerAccountId: peerVpc.ownerId,
 *     peerVpcRegion: peerArn.apply(peerArn => peerArn.region),
 * });
 * const main_to_dev = new hcp.HvnRoute("main-to-dev", {
 *     hvnLink: main.selfLink,
 *     hvnRouteId: "main-to-dev",
 *     destinationCidr: "172.31.0.0/16",
 *     targetLink: dev.selfLink,
 * });
 * const peerVpcPeeringConnectionAccepter = new aws.ec2.VpcPeeringConnectionAccepter("peerVpcPeeringConnectionAccepter", {
 *     vpcPeeringConnectionId: dev.providerPeeringId,
 *     autoAccept: true,
 * });
 * ```
 *
 * ## Import
 *
 * # The import ID is {hvn_id}:{peering_id}
 *
 * ```sh
 *  $ pulumi import hcp:index/awsNetworkPeering:AwsNetworkPeering peer main-hvn:11eb60b3-d4ec-5eed-aacc-0242ac120015
 * ```
 */
export class AwsNetworkPeering extends pulumi.CustomResource {
    /**
     * Get an existing AwsNetworkPeering resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     * @param opts Optional settings to control the behavior of the CustomResource.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: AwsNetworkPeeringState, opts?: pulumi.CustomResourceOptions): AwsNetworkPeering {
        return new AwsNetworkPeering(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'hcp:index/awsNetworkPeering:AwsNetworkPeering';

    /**
     * Returns true if the given object is an instance of AwsNetworkPeering.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is AwsNetworkPeering {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === AwsNetworkPeering.__pulumiType;
    }

    /**
     * The time that the network peering was created.
     */
    public /*out*/ readonly createdAt!: pulumi.Output<string>;
    /**
     * The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or
     * `ACTIVE` state.
     */
    public /*out*/ readonly expiresAt!: pulumi.Output<string>;
    /**
     * The ID of the HashiCorp Virtual Network (HVN).
     */
    public readonly hvnId!: pulumi.Output<string>;
    /**
     * The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
     */
    public /*out*/ readonly organizationId!: pulumi.Output<string>;
    /**
     * The account ID of the peer VPC in AWS.
     */
    public readonly peerAccountId!: pulumi.Output<string>;
    /**
     * The ID of the peer VPC in AWS.
     */
    public readonly peerVpcId!: pulumi.Output<string>;
    /**
     * The region of the peer VPC in AWS.
     */
    public readonly peerVpcRegion!: pulumi.Output<string>;
    /**
     * The ID of the network peering.
     */
    public readonly peeringId!: pulumi.Output<string>;
    /**
     * The ID of the HCP project where the network peering is located. Always matches the HVN's project.
     */
    public /*out*/ readonly projectId!: pulumi.Output<string>;
    /**
     * The peering connection ID used by AWS.
     */
    public /*out*/ readonly providerPeeringId!: pulumi.Output<string>;
    /**
     * A unique URL identifying the network peering.
     */
    public /*out*/ readonly selfLink!: pulumi.Output<string>;

    /**
     * Create a AwsNetworkPeering resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: AwsNetworkPeeringArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: AwsNetworkPeeringArgs | AwsNetworkPeeringState, opts?: pulumi.CustomResourceOptions) {
        let resourceInputs: pulumi.Inputs = {};
        opts = opts || {};
        if (opts.id) {
            const state = argsOrState as AwsNetworkPeeringState | undefined;
            resourceInputs["createdAt"] = state ? state.createdAt : undefined;
            resourceInputs["expiresAt"] = state ? state.expiresAt : undefined;
            resourceInputs["hvnId"] = state ? state.hvnId : undefined;
            resourceInputs["organizationId"] = state ? state.organizationId : undefined;
            resourceInputs["peerAccountId"] = state ? state.peerAccountId : undefined;
            resourceInputs["peerVpcId"] = state ? state.peerVpcId : undefined;
            resourceInputs["peerVpcRegion"] = state ? state.peerVpcRegion : undefined;
            resourceInputs["peeringId"] = state ? state.peeringId : undefined;
            resourceInputs["projectId"] = state ? state.projectId : undefined;
            resourceInputs["providerPeeringId"] = state ? state.providerPeeringId : undefined;
            resourceInputs["selfLink"] = state ? state.selfLink : undefined;
        } else {
            const args = argsOrState as AwsNetworkPeeringArgs | undefined;
            if ((!args || args.hvnId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'hvnId'");
            }
            if ((!args || args.peerAccountId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerAccountId'");
            }
            if ((!args || args.peerVpcId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerVpcId'");
            }
            if ((!args || args.peerVpcRegion === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peerVpcRegion'");
            }
            if ((!args || args.peeringId === undefined) && !opts.urn) {
                throw new Error("Missing required property 'peeringId'");
            }
            resourceInputs["hvnId"] = args ? args.hvnId : undefined;
            resourceInputs["peerAccountId"] = args ? args.peerAccountId : undefined;
            resourceInputs["peerVpcId"] = args ? args.peerVpcId : undefined;
            resourceInputs["peerVpcRegion"] = args ? args.peerVpcRegion : undefined;
            resourceInputs["peeringId"] = args ? args.peeringId : undefined;
            resourceInputs["createdAt"] = undefined /*out*/;
            resourceInputs["expiresAt"] = undefined /*out*/;
            resourceInputs["organizationId"] = undefined /*out*/;
            resourceInputs["projectId"] = undefined /*out*/;
            resourceInputs["providerPeeringId"] = undefined /*out*/;
            resourceInputs["selfLink"] = undefined /*out*/;
        }
        opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts);
        super(AwsNetworkPeering.__pulumiType, name, resourceInputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering AwsNetworkPeering resources.
 */
export interface AwsNetworkPeeringState {
    /**
     * The time that the network peering was created.
     */
    createdAt?: pulumi.Input<string>;
    /**
     * The time after which the network peering will be considered expired if it hasn't transitioned into `ACCEPTED` or
     * `ACTIVE` state.
     */
    expiresAt?: pulumi.Input<string>;
    /**
     * The ID of the HashiCorp Virtual Network (HVN).
     */
    hvnId?: pulumi.Input<string>;
    /**
     * The ID of the HCP organization where the network peering is located. Always matches the HVN's organization.
     */
    organizationId?: pulumi.Input<string>;
    /**
     * The account ID of the peer VPC in AWS.
     */
    peerAccountId?: pulumi.Input<string>;
    /**
     * The ID of the peer VPC in AWS.
     */
    peerVpcId?: pulumi.Input<string>;
    /**
     * The region of the peer VPC in AWS.
     */
    peerVpcRegion?: pulumi.Input<string>;
    /**
     * The ID of the network peering.
     */
    peeringId?: pulumi.Input<string>;
    /**
     * The ID of the HCP project where the network peering is located. Always matches the HVN's project.
     */
    projectId?: pulumi.Input<string>;
    /**
     * The peering connection ID used by AWS.
     */
    providerPeeringId?: pulumi.Input<string>;
    /**
     * A unique URL identifying the network peering.
     */
    selfLink?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a AwsNetworkPeering resource.
 */
export interface AwsNetworkPeeringArgs {
    /**
     * The ID of the HashiCorp Virtual Network (HVN).
     */
    hvnId: pulumi.Input<string>;
    /**
     * The account ID of the peer VPC in AWS.
     */
    peerAccountId: pulumi.Input<string>;
    /**
     * The ID of the peer VPC in AWS.
     */
    peerVpcId: pulumi.Input<string>;
    /**
     * The region of the peer VPC in AWS.
     */
    peerVpcRegion: pulumi.Input<string>;
    /**
     * The ID of the network peering.
     */
    peeringId: pulumi.Input<string>;
}
