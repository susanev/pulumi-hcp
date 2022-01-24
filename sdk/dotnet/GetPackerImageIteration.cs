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
    public static class GetPackerImageIteration
    {
        /// <summary>
        /// &gt; **Note:** This feature is currently in beta.
        /// 
        /// The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.
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
        ///         var alpine = Output.Create(Hcp.GetPackerImageIteration.InvokeAsync(new Hcp.GetPackerImageIterationArgs
        ///         {
        ///             BucketName = "alpine",
        ///             Channel = "production",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetPackerImageIterationResult> InvokeAsync(GetPackerImageIterationArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetPackerImageIterationResult>("hcp:index/getPackerImageIteration:getPackerImageIteration", args ?? new GetPackerImageIterationArgs(), options.WithVersion());

        /// <summary>
        /// &gt; **Note:** This feature is currently in beta.
        /// 
        /// The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.
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
        ///         var alpine = Output.Create(Hcp.GetPackerImageIteration.InvokeAsync(new Hcp.GetPackerImageIterationArgs
        ///         {
        ///             BucketName = "alpine",
        ///             Channel = "production",
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetPackerImageIterationResult> Invoke(GetPackerImageIterationInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetPackerImageIterationResult>("hcp:index/getPackerImageIteration:getPackerImageIteration", args ?? new GetPackerImageIterationInvokeArgs(), options.WithVersion());
    }


    public sealed class GetPackerImageIterationArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The slug of the HCP Packer Registry image bucket to pull from.
        /// </summary>
        [Input("bucketName", required: true)]
        public string BucketName { get; set; } = null!;

        /// <summary>
        /// The channel that points to the version of the image you want.
        /// </summary>
        [Input("channel", required: true)]
        public string Channel { get; set; } = null!;

        public GetPackerImageIterationArgs()
        {
        }
    }

    public sealed class GetPackerImageIterationInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The slug of the HCP Packer Registry image bucket to pull from.
        /// </summary>
        [Input("bucketName", required: true)]
        public Input<string> BucketName { get; set; } = null!;

        /// <summary>
        /// The channel that points to the version of the image you want.
        /// </summary>
        [Input("channel", required: true)]
        public Input<string> Channel { get; set; } = null!;

        public GetPackerImageIterationInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetPackerImageIterationResult
    {
        /// <summary>
        /// The slug of the HCP Packer Registry image bucket to pull from.
        /// </summary>
        public readonly string BucketName;
        /// <summary>
        /// Builds for this iteration. An iteration can have more than one build if it took more than one go to build all images.
        /// </summary>
        public readonly ImmutableArray<Outputs.GetPackerImageIterationBuildResult> Builds;
        /// <summary>
        /// The channel that points to the version of the image you want.
        /// </summary>
        public readonly string Channel;
        /// <summary>
        /// Creation time of this iteration
        /// </summary>
        public readonly string CreatedAt;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// Incremental version of this iteration
        /// </summary>
        public readonly int IncrementalVersion;
        /// <summary>
        /// The ID of the organization this HCP Packer registry is located in.
        /// </summary>
        public readonly string OrganizationId;
        /// <summary>
        /// The ID of the project this HCP Packer registry is located in.
        /// </summary>
        public readonly string ProjectId;

        [OutputConstructor]
        private GetPackerImageIterationResult(
            string bucketName,

            ImmutableArray<Outputs.GetPackerImageIterationBuildResult> builds,

            string channel,

            string createdAt,

            string id,

            int incrementalVersion,

            string organizationId,

            string projectId)
        {
            BucketName = bucketName;
            Builds = builds;
            Channel = channel;
            CreatedAt = createdAt;
            Id = id;
            IncrementalVersion = incrementalVersion;
            OrganizationId = organizationId;
            ProjectId = projectId;
        }
    }
}
