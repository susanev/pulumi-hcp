// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hcp
{
    /// <summary>
    /// ## Import
    /// 
    /// # The import ID is {hvn_id}:{transit_gateway_attachment_id}
    /// 
    /// ```sh
    ///  $ pulumi import hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment example main-hvn:example-tgw-attachment
    /// ```
    /// </summary>
    [HcpResourceType("hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment")]
    public partial class AwsTransitGatewayAttachment : Pulumi.CustomResource
    {
        /// <summary>
        /// The time that the transit gateway attachment was created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The time after which the transit gateway attachment will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        /// </summary>
        [Output("expiresAt")]
        public Output<string> ExpiresAt { get; private set; } = null!;

        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Output("hvnId")]
        public Output<string> HvnId { get; private set; } = null!;

        /// <summary>
        /// The ID of the HCP organization where the transit gateway attachment is located. Always matches the HVN's organization.
        /// </summary>
        [Output("organizationId")]
        public Output<string> OrganizationId { get; private set; } = null!;

        /// <summary>
        /// The ID of the HCP project where the transit gateway attachment is located. Always matches the HVN's project.
        /// </summary>
        [Output("projectId")]
        public Output<string> ProjectId { get; private set; } = null!;

        /// <summary>
        /// The transit gateway attachment ID used by AWS.
        /// </summary>
        [Output("providerTransitGatewayAttachmentId")]
        public Output<string> ProviderTransitGatewayAttachmentId { get; private set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
        /// The Resource Share should be associated with the HCP AWS account principal (see
        /// [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
        /// and the transit gateway resource (see
        /// [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        /// </summary>
        [Output("resourceShareArn")]
        public Output<string> ResourceShareArn { get; private set; } = null!;

        /// <summary>
        /// A unique URL identifying the transit gateway attachment.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// The state of the transit gateway attachment.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// The user-settable name of the transit gateway attachment in HCP.
        /// </summary>
        [Output("transitGatewayAttachmentId")]
        public Output<string> TransitGatewayAttachmentId { get; private set; } = null!;

        /// <summary>
        /// The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        /// </summary>
        [Output("transitGatewayId")]
        public Output<string> TransitGatewayId { get; private set; } = null!;


        /// <summary>
        /// Create a AwsTransitGatewayAttachment resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public AwsTransitGatewayAttachment(string name, AwsTransitGatewayAttachmentArgs args, CustomResourceOptions? options = null)
            : base("hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment", name, args ?? new AwsTransitGatewayAttachmentArgs(), MakeResourceOptions(options, ""))
        {
        }

        private AwsTransitGatewayAttachment(string name, Input<string> id, AwsTransitGatewayAttachmentState? state = null, CustomResourceOptions? options = null)
            : base("hcp:index/awsTransitGatewayAttachment:AwsTransitGatewayAttachment", name, state, MakeResourceOptions(options, id))
        {
        }

        private static CustomResourceOptions MakeResourceOptions(CustomResourceOptions? options, Input<string>? id)
        {
            var defaultOptions = new CustomResourceOptions
            {
                Version = Utilities.Version,
            };
            var merged = CustomResourceOptions.Merge(defaultOptions, options);
            // Override the ID if one was specified for consistency with other language SDKs.
            merged.Id = id ?? merged.Id;
            return merged;
        }
        /// <summary>
        /// Get an existing AwsTransitGatewayAttachment resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static AwsTransitGatewayAttachment Get(string name, Input<string> id, AwsTransitGatewayAttachmentState? state = null, CustomResourceOptions? options = null)
        {
            return new AwsTransitGatewayAttachment(name, id, state, options);
        }
    }

    public sealed class AwsTransitGatewayAttachmentArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnId", required: true)]
        public Input<string> HvnId { get; set; } = null!;

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
        /// The Resource Share should be associated with the HCP AWS account principal (see
        /// [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
        /// and the transit gateway resource (see
        /// [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        /// </summary>
        [Input("resourceShareArn", required: true)]
        public Input<string> ResourceShareArn { get; set; } = null!;

        /// <summary>
        /// The user-settable name of the transit gateway attachment in HCP.
        /// </summary>
        [Input("transitGatewayAttachmentId", required: true)]
        public Input<string> TransitGatewayAttachmentId { get; set; } = null!;

        /// <summary>
        /// The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        /// </summary>
        [Input("transitGatewayId", required: true)]
        public Input<string> TransitGatewayId { get; set; } = null!;

        public AwsTransitGatewayAttachmentArgs()
        {
        }
    }

    public sealed class AwsTransitGatewayAttachmentState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The time that the transit gateway attachment was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The time after which the transit gateway attachment will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
        /// </summary>
        [Input("expiresAt")]
        public Input<string>? ExpiresAt { get; set; }

        /// <summary>
        /// The ID of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnId")]
        public Input<string>? HvnId { get; set; }

        /// <summary>
        /// The ID of the HCP organization where the transit gateway attachment is located. Always matches the HVN's organization.
        /// </summary>
        [Input("organizationId")]
        public Input<string>? OrganizationId { get; set; }

        /// <summary>
        /// The ID of the HCP project where the transit gateway attachment is located. Always matches the HVN's project.
        /// </summary>
        [Input("projectId")]
        public Input<string>? ProjectId { get; set; }

        /// <summary>
        /// The transit gateway attachment ID used by AWS.
        /// </summary>
        [Input("providerTransitGatewayAttachmentId")]
        public Input<string>? ProviderTransitGatewayAttachmentId { get; set; }

        /// <summary>
        /// The Amazon Resource Name (ARN) of the Resource Share that is needed to grant HCP access to the transit gateway in AWS.
        /// The Resource Share should be associated with the HCP AWS account principal (see
        /// [aws_ram_principal_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_principal_association))
        /// and the transit gateway resource (see
        /// [aws_ram_resource_association](https://registry.terraform.io/providers/hashicorp/aws/latest/docs/resources/ram_resource_association))
        /// </summary>
        [Input("resourceShareArn")]
        public Input<string>? ResourceShareArn { get; set; }

        /// <summary>
        /// A unique URL identifying the transit gateway attachment.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// The state of the transit gateway attachment.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// The user-settable name of the transit gateway attachment in HCP.
        /// </summary>
        [Input("transitGatewayAttachmentId")]
        public Input<string>? TransitGatewayAttachmentId { get; set; }

        /// <summary>
        /// The ID of the user-owned transit gateway in AWS. The AWS region of the transit gateway must match the HVN.
        /// </summary>
        [Input("transitGatewayId")]
        public Input<string>? TransitGatewayId { get; set; }

        public AwsTransitGatewayAttachmentState()
        {
        }
    }
}
