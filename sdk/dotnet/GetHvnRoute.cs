// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;
using Pulumi.Utilities;

namespace Pulumi.Hcp
{
    public static class GetHvnRoute
    {
        /// <summary>
        /// The HVN route data source provides information about an existing HVN route.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Hcp = Pulumi.Hcp;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Hcp.GetHvnRoute.InvokeAsync(new Hcp.GetHvnRouteArgs
        ///         {
        ///             HvnLink = @var.Hvn_link,
        ///             DestinationCidr = @var.Hvn_route_id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetHvnRouteResult> InvokeAsync(GetHvnRouteArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetHvnRouteResult>("hcp:index/getHvnRoute:getHvnRoute", args ?? new GetHvnRouteArgs(), options.WithVersion());

        /// <summary>
        /// The HVN route data source provides information about an existing HVN route.
        /// 
        /// {{% examples %}}
        /// ## Example Usage
        /// {{% example %}}
        /// 
        /// ```csharp
        /// using Pulumi;
        /// using Hcp = Pulumi.Hcp;
        /// 
        /// class MyStack : Stack
        /// {
        ///     public MyStack()
        ///     {
        ///         var example = Output.Create(Hcp.GetHvnRoute.InvokeAsync(new Hcp.GetHvnRouteArgs
        ///         {
        ///             HvnLink = @var.Hvn_link,
        ///             DestinationCidr = @var.Hvn_route_id,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetHvnRouteResult> Invoke(GetHvnRouteInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetHvnRouteResult>("hcp:index/getHvnRoute:getHvnRoute", args ?? new GetHvnRouteInvokeArgs(), options.WithVersion());
    }


    public sealed class GetHvnRouteArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The `self_link` of the HashiCorp Virtual Network (HVN).
        /// </summary>
        [Input("hvnLink", required: true)]
        public string HvnLink { get; set; } = null!;

        /// <summary>
        /// The ID of the HVN route.
        /// </summary>
        [Input("hvnRouteId", required: true)]
        public string HvnRouteId { get; set; } = null!;

        public GetHvnRouteArgs()
        {
        }
    }

    public sealed class GetHvnRouteInvokeArgs : Pulumi.InvokeArgs
    {
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

        public GetHvnRouteInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetHvnRouteResult
    {
        /// <summary>
        /// The time that the HVN route was created.
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// The destination CIDR of the HVN route.
        /// </summary>
        public readonly string DestinationCidr;
        /// <summary>
        /// The `self_link` of the HashiCorp Virtual Network (HVN).
        /// </summary>
        public readonly string HvnLink;
        /// <summary>
        /// The ID of the HVN route.
        /// </summary>
        public readonly string HvnRouteId;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// A unique URL identifying the HVN route.
        /// </summary>
        public readonly string SelfLink;
        /// <summary>
        /// The state of the HVN route.
        /// </summary>
        public readonly string State;
        /// <summary>
        /// A unique URL identifying the target of the HVN route.
        /// </summary>
        public readonly string TargetLink;

        [OutputConstructor]
        private GetHvnRouteResult(
            string createdAt,

            string destinationCidr,

            string hvnLink,

            string hvnRouteId,

            string id,

            string selfLink,

            string state,

            string targetLink)
        {
            CreatedAt = createdAt;
            DestinationCidr = destinationCidr;
            HvnLink = hvnLink;
            HvnRouteId = hvnRouteId;
            Id = id;
            SelfLink = selfLink;
            State = state;
            TargetLink = targetLink;
        }
    }
}
