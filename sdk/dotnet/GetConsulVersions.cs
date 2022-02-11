// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hcp
{
    public static class GetConsulVersions
    {
        /// <summary>
        /// The Consul versions data source provides the Consul versions supported by HCP.
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
        ///         var @default = Output.Create(Hcp.GetConsulVersions.InvokeAsync());
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetConsulVersionsResult> InvokeAsync(InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetConsulVersionsResult>("hcp:index/getConsulVersions:getConsulVersions", InvokeArgs.Empty, options.WithDefaults());
    }


    [OutputType]
    public sealed class GetConsulVersionsResult
    {
        /// <summary>
        /// The Consul versions available on HCP.
        /// </summary>
        public readonly ImmutableArray<string> Availables;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The preview versions of Consul available on HCP.
        /// </summary>
        public readonly ImmutableArray<string> Previews;
        /// <summary>
        /// The recommended Consul version for HCP clusters.
        /// </summary>
        public readonly string Recommended;

        [OutputConstructor]
        private GetConsulVersionsResult(
            ImmutableArray<string> availables,

            string id,

            ImmutableArray<string> previews,

            string recommended)
        {
            Availables = availables;
            Id = id;
            Previews = previews;
            Recommended = recommended;
        }
    }
}
