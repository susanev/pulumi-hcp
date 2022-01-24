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
    /// # The import ID is {hvn_id}:{hvn_route_id}
    /// 
    /// ```sh
    ///  $ pulumi import hcp:index/hvnRoute:HvnRoute example main-hvn:example-hvn-route
    /// ```
    /// </summary>
    [HcpResourceType("hcp:index/hvnRoute:HvnRoute")]
    public partial class HvnRoute : Pulumi.CustomResource
    {
        /// <summary>
        /// The time that the HVN route was created.
        /// </summary>
        [Output("createdAt")]
        public Output<string> CreatedAt { get; private set; } = null!;

        /// <summary>
        /// The destination CIDR of the HVN route.
        /// </summary>
        [Output("destinationCidr")]
        public Output<string> DestinationCidr { get; private set; } = null!;

        /// <summary>
        /// The `self_link` of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Output("hvnLink")]
        public Output<string> HvnLink { get; private set; } = null!;

        /// <summary>
        /// The ID of the HVN route.
        /// </summary>
        [Output("hvnRouteId")]
        public Output<string> HvnRouteId { get; private set; } = null!;

        /// <summary>
        /// A unique URL identifying the HVN route.
        /// </summary>
        [Output("selfLink")]
        public Output<string> SelfLink { get; private set; } = null!;

        /// <summary>
        /// The state of the HVN route.
        /// </summary>
        [Output("state")]
        public Output<string> State { get; private set; } = null!;

        /// <summary>
        /// A unique URL identifying the target of the HVN route. Examples of the target: `aws_network_peering`, `aws_transit_gateway_attachment`
        /// </summary>
        [Output("targetLink")]
        public Output<string> TargetLink { get; private set; } = null!;


        /// <summary>
        /// Create a HvnRoute resource with the given unique name, arguments, and options.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resource</param>
        /// <param name="args">The arguments used to populate this resource's properties</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public HvnRoute(string name, HvnRouteArgs args, CustomResourceOptions? options = null)
            : base("hcp:index/hvnRoute:HvnRoute", name, args ?? new HvnRouteArgs(), MakeResourceOptions(options, ""))
        {
        }

        private HvnRoute(string name, Input<string> id, HvnRouteState? state = null, CustomResourceOptions? options = null)
            : base("hcp:index/hvnRoute:HvnRoute", name, state, MakeResourceOptions(options, id))
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
        /// Get an existing HvnRoute resource's state with the given name, ID, and optional extra
        /// properties used to qualify the lookup.
        /// </summary>
        ///
        /// <param name="name">The unique name of the resulting resource.</param>
        /// <param name="id">The unique provider ID of the resource to lookup.</param>
        /// <param name="state">Any extra arguments used during the lookup.</param>
        /// <param name="options">A bag of options that control this resource's behavior</param>
        public static HvnRoute Get(string name, Input<string> id, HvnRouteState? state = null, CustomResourceOptions? options = null)
        {
            return new HvnRoute(name, id, state, options);
        }
    }

    public sealed class HvnRouteArgs : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The destination CIDR of the HVN route.
        /// </summary>
        [Input("destinationCidr", required: true)]
        public Input<string> DestinationCidr { get; set; } = null!;

        /// <summary>
        /// The `self_link` of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnLink", required: true)]
        public Input<string> HvnLink { get; set; } = null!;

        /// <summary>
        /// The ID of the HVN route.
        /// </summary>
        [Input("hvnRouteId", required: true)]
        public Input<string> HvnRouteId { get; set; } = null!;

        /// <summary>
        /// A unique URL identifying the target of the HVN route. Examples of the target: `aws_network_peering`, `aws_transit_gateway_attachment`
        /// </summary>
        [Input("targetLink", required: true)]
        public Input<string> TargetLink { get; set; } = null!;

        public HvnRouteArgs()
        {
        }
    }

    public sealed class HvnRouteState : Pulumi.ResourceArgs
    {
        /// <summary>
        /// The time that the HVN route was created.
        /// </summary>
        [Input("createdAt")]
        public Input<string>? CreatedAt { get; set; }

        /// <summary>
        /// The destination CIDR of the HVN route.
        /// </summary>
        [Input("destinationCidr")]
        public Input<string>? DestinationCidr { get; set; }

        /// <summary>
        /// The `self_link` of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnLink")]
        public Input<string>? HvnLink { get; set; }

        /// <summary>
        /// The ID of the HVN route.
        /// </summary>
        [Input("hvnRouteId")]
        public Input<string>? HvnRouteId { get; set; }

        /// <summary>
        /// A unique URL identifying the HVN route.
        /// </summary>
        [Input("selfLink")]
        public Input<string>? SelfLink { get; set; }

        /// <summary>
        /// The state of the HVN route.
        /// </summary>
        [Input("state")]
        public Input<string>? State { get; set; }

        /// <summary>
        /// A unique URL identifying the target of the HVN route. Examples of the target: `aws_network_peering`, `aws_transit_gateway_attachment`
        /// </summary>
        [Input("targetLink")]
        public Input<string>? TargetLink { get; set; }

        public HvnRouteState()
        {
        }
    }
}
