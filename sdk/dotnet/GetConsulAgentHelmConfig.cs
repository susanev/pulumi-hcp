// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

using System;
using System.Collections.Generic;
using System.Collections.Immutable;
using System.Threading.Tasks;
using Pulumi.Serialization;

namespace Pulumi.Hcp
{
    public static class GetConsulAgentHelmConfig
    {
        /// <summary>
        /// The Consul agent Helm config data source provides Helm values for a Consul agent running in Kubernetes.
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
        ///         var example = Output.Create(Hcp.GetConsulAgentHelmConfig.InvokeAsync(new Hcp.GetConsulAgentHelmConfigArgs
        ///         {
        ///             ClusterId = @var.Cluster_id,
        ///             KubernetesEndpoint = @var.Kubernetes_endpoint,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Task<GetConsulAgentHelmConfigResult> InvokeAsync(GetConsulAgentHelmConfigArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.InvokeAsync<GetConsulAgentHelmConfigResult>("hcp:index/getConsulAgentHelmConfig:getConsulAgentHelmConfig", args ?? new GetConsulAgentHelmConfigArgs(), options.WithDefaults());

        /// <summary>
        /// The Consul agent Helm config data source provides Helm values for a Consul agent running in Kubernetes.
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
        ///         var example = Output.Create(Hcp.GetConsulAgentHelmConfig.InvokeAsync(new Hcp.GetConsulAgentHelmConfigArgs
        ///         {
        ///             ClusterId = @var.Cluster_id,
        ///             KubernetesEndpoint = @var.Kubernetes_endpoint,
        ///         }));
        ///     }
        /// 
        /// }
        /// ```
        /// {{% /example %}}
        /// {{% /examples %}}
        /// </summary>
        public static Output<GetConsulAgentHelmConfigResult> Invoke(GetConsulAgentHelmConfigInvokeArgs args, InvokeOptions? options = null)
            => Pulumi.Deployment.Instance.Invoke<GetConsulAgentHelmConfigResult>("hcp:index/getConsulAgentHelmConfig:getConsulAgentHelmConfig", args ?? new GetConsulAgentHelmConfigInvokeArgs(), options.WithDefaults());
    }


    public sealed class GetConsulAgentHelmConfigArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the HCP Consul cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public string ClusterId { get; set; } = null!;

        /// <summary>
        /// Denotes that the gossip ports should be exposed.
        /// </summary>
        [Input("exposeGossipPorts")]
        public bool? ExposeGossipPorts { get; set; }

        /// <summary>
        /// The FQDN for the Kubernetes API.
        /// </summary>
        [Input("kubernetesEndpoint", required: true)]
        public string KubernetesEndpoint { get; set; } = null!;

        public GetConsulAgentHelmConfigArgs()
        {
        }
    }

    public sealed class GetConsulAgentHelmConfigInvokeArgs : Pulumi.InvokeArgs
    {
        /// <summary>
        /// The ID of the HCP Consul cluster.
        /// </summary>
        [Input("clusterId", required: true)]
        public Input<string> ClusterId { get; set; } = null!;

        /// <summary>
        /// Denotes that the gossip ports should be exposed.
        /// </summary>
        [Input("exposeGossipPorts")]
        public Input<bool>? ExposeGossipPorts { get; set; }

        /// <summary>
        /// The FQDN for the Kubernetes API.
        /// </summary>
        [Input("kubernetesEndpoint", required: true)]
        public Input<string> KubernetesEndpoint { get; set; } = null!;

        public GetConsulAgentHelmConfigInvokeArgs()
        {
        }
    }


    [OutputType]
    public sealed class GetConsulAgentHelmConfigResult
    {
        /// <summary>
        /// The ID of the HCP Consul cluster.
        /// </summary>
        public readonly string ClusterId;
        /// <summary>
        /// The agent Helm config.
        /// </summary>
        public readonly string Config;
        /// <summary>
        /// Denotes that the gossip ports should be exposed.
        /// </summary>
        public readonly bool? ExposeGossipPorts;
        /// <summary>
        /// The provider-assigned unique ID for this managed resource.
        /// </summary>
        public readonly string Id;
        /// <summary>
        /// The FQDN for the Kubernetes API.
        /// </summary>
        public readonly string KubernetesEndpoint;

        [OutputConstructor]
        private GetConsulAgentHelmConfigResult(
            string clusterId,

            string config,

            bool? exposeGossipPorts,

            string id,

            string kubernetesEndpoint)
        {
            ClusterId = clusterId;
            Config = config;
            ExposeGossipPorts = exposeGossipPorts;
            Id = id;
            KubernetesEndpoint = kubernetesEndpoint;
        }
    }
}
