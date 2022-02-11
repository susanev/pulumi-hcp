// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The cluster data source provides information about an existing HCP Consul cluster.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/pulumi/pulumi-hcp/sdk/go/hcp"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := hcp.LookupConsulCluster(ctx, &GetConsulClusterArgs{
// 			ClusterId: _var.Cluster_id,
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func LookupConsulCluster(ctx *pulumi.Context, args *LookupConsulClusterArgs, opts ...pulumi.InvokeOption) (*LookupConsulClusterResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv LookupConsulClusterResult
	err := ctx.Invoke("hcp:index/getConsulCluster:getConsulCluster", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getConsulCluster.
type LookupConsulClusterArgs struct {
	// The ID of the HCP Consul cluster.
	ClusterId string `pulumi:"clusterId"`
}

// A collection of values returned by getConsulCluster.
type LookupConsulClusterResult struct {
	// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation.
	AutoHvnToHvnPeering bool `pulumi:"autoHvnToHvnPeering"`
	// The provider where the HCP Consul cluster is located. Only 'aws' is available at this time.
	CloudProvider string `pulumi:"cloudProvider"`
	// The ID of the HCP Consul cluster.
	ClusterId string `pulumi:"clusterId"`
	// Denotes the Consul connect feature should be enabled for this cluster.  Default to true.
	ConnectEnabled bool `pulumi:"connectEnabled"`
	// Denotes that automatic Consul upgrades are enabled.
	ConsulAutomaticUpgrades bool `pulumi:"consulAutomaticUpgrades"`
	// The cluster CA file encoded as a Base64 string.
	ConsulCaFile string `pulumi:"consulCaFile"`
	// The cluster config encoded as a Base64 string.
	ConsulConfigFile string `pulumi:"consulConfigFile"`
	// The private URL for the Consul UI.
	ConsulPrivateEndpointUrl string `pulumi:"consulPrivateEndpointUrl"`
	// The public URL for the Consul UI. This will be empty if `publicEndpoint` is `false`.
	ConsulPublicEndpointUrl string `pulumi:"consulPublicEndpointUrl"`
	// The Consul snapshot interval.
	ConsulSnapshotInterval string `pulumi:"consulSnapshotInterval"`
	// The retention policy for Consul snapshots.
	ConsulSnapshotRetention string `pulumi:"consulSnapshotRetention"`
	// The Consul version of the cluster.
	ConsulVersion string `pulumi:"consulVersion"`
	// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `clusterId`.
	Datacenter string `pulumi:"datacenter"`
	// The ID of the HVN this HCP Consul cluster is associated to.
	HvnId string `pulumi:"hvnId"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// The ID of the organization the project for this HCP Consul cluster is located.
	OrganizationId string `pulumi:"organizationId"`
	// The `selfLink` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If not specified, it is a standalone cluster.
	PrimaryLink string `pulumi:"primaryLink"`
	// The ID of the project this HCP Consul cluster is located.
	ProjectId string `pulumi:"projectId"`
	// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
	PublicEndpoint bool `pulumi:"publicEndpoint"`
	// The region where the HCP Consul cluster is located.
	Region string `pulumi:"region"`
	// The the number of Consul server nodes in the cluster.
	Scale int `pulumi:"scale"`
	// A unique URL identifying the HCP Consul cluster.
	SelfLink string `pulumi:"selfLink"`
	// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for development tier - `xSmall`. Valid options for other tiers - `small`, `medium`, `large`. For more details - https://cloud.hashicorp.com/pricing/consul
	Size string `pulumi:"size"`
	// The tier that the HCP Consul cluster will be provisioned as.  Only `development`, `standard` and `plus` are available at this time.
	Tier string `pulumi:"tier"`
}

func LookupConsulClusterOutput(ctx *pulumi.Context, args LookupConsulClusterOutputArgs, opts ...pulumi.InvokeOption) LookupConsulClusterResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupConsulClusterResult, error) {
			args := v.(LookupConsulClusterArgs)
			r, err := LookupConsulCluster(ctx, &args, opts...)
			return *r, err
		}).(LookupConsulClusterResultOutput)
}

// A collection of arguments for invoking getConsulCluster.
type LookupConsulClusterOutputArgs struct {
	// The ID of the HCP Consul cluster.
	ClusterId pulumi.StringInput `pulumi:"clusterId"`
}

func (LookupConsulClusterOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConsulClusterArgs)(nil)).Elem()
}

// A collection of values returned by getConsulCluster.
type LookupConsulClusterResultOutput struct{ *pulumi.OutputState }

func (LookupConsulClusterResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupConsulClusterResult)(nil)).Elem()
}

func (o LookupConsulClusterResultOutput) ToLookupConsulClusterResultOutput() LookupConsulClusterResultOutput {
	return o
}

func (o LookupConsulClusterResultOutput) ToLookupConsulClusterResultOutputWithContext(ctx context.Context) LookupConsulClusterResultOutput {
	return o
}

// Enables automatic HVN to HVN peering when creating a secondary cluster in a federation.
func (o LookupConsulClusterResultOutput) AutoHvnToHvnPeering() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) bool { return v.AutoHvnToHvnPeering }).(pulumi.BoolOutput)
}

// The provider where the HCP Consul cluster is located. Only 'aws' is available at this time.
func (o LookupConsulClusterResultOutput) CloudProvider() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.CloudProvider }).(pulumi.StringOutput)
}

// The ID of the HCP Consul cluster.
func (o LookupConsulClusterResultOutput) ClusterId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ClusterId }).(pulumi.StringOutput)
}

// Denotes the Consul connect feature should be enabled for this cluster.  Default to true.
func (o LookupConsulClusterResultOutput) ConnectEnabled() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) bool { return v.ConnectEnabled }).(pulumi.BoolOutput)
}

// Denotes that automatic Consul upgrades are enabled.
func (o LookupConsulClusterResultOutput) ConsulAutomaticUpgrades() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) bool { return v.ConsulAutomaticUpgrades }).(pulumi.BoolOutput)
}

// The cluster CA file encoded as a Base64 string.
func (o LookupConsulClusterResultOutput) ConsulCaFile() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ConsulCaFile }).(pulumi.StringOutput)
}

// The cluster config encoded as a Base64 string.
func (o LookupConsulClusterResultOutput) ConsulConfigFile() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ConsulConfigFile }).(pulumi.StringOutput)
}

// The private URL for the Consul UI.
func (o LookupConsulClusterResultOutput) ConsulPrivateEndpointUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ConsulPrivateEndpointUrl }).(pulumi.StringOutput)
}

// The public URL for the Consul UI. This will be empty if `publicEndpoint` is `false`.
func (o LookupConsulClusterResultOutput) ConsulPublicEndpointUrl() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ConsulPublicEndpointUrl }).(pulumi.StringOutput)
}

// The Consul snapshot interval.
func (o LookupConsulClusterResultOutput) ConsulSnapshotInterval() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ConsulSnapshotInterval }).(pulumi.StringOutput)
}

// The retention policy for Consul snapshots.
func (o LookupConsulClusterResultOutput) ConsulSnapshotRetention() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ConsulSnapshotRetention }).(pulumi.StringOutput)
}

// The Consul version of the cluster.
func (o LookupConsulClusterResultOutput) ConsulVersion() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ConsulVersion }).(pulumi.StringOutput)
}

// The Consul data center name of the cluster. If not specified, it is defaulted to the value of `clusterId`.
func (o LookupConsulClusterResultOutput) Datacenter() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.Datacenter }).(pulumi.StringOutput)
}

// The ID of the HVN this HCP Consul cluster is associated to.
func (o LookupConsulClusterResultOutput) HvnId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.HvnId }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o LookupConsulClusterResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.Id }).(pulumi.StringOutput)
}

// The ID of the organization the project for this HCP Consul cluster is located.
func (o LookupConsulClusterResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

// The `selfLink` of the HCP Consul cluster which is the primary in the federation setup with this HCP Consul cluster. If not specified, it is a standalone cluster.
func (o LookupConsulClusterResultOutput) PrimaryLink() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.PrimaryLink }).(pulumi.StringOutput)
}

// The ID of the project this HCP Consul cluster is located.
func (o LookupConsulClusterResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

// Denotes that the cluster has a public endpoint for the Consul UI. Defaults to false.
func (o LookupConsulClusterResultOutput) PublicEndpoint() pulumi.BoolOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) bool { return v.PublicEndpoint }).(pulumi.BoolOutput)
}

// The region where the HCP Consul cluster is located.
func (o LookupConsulClusterResultOutput) Region() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.Region }).(pulumi.StringOutput)
}

// The the number of Consul server nodes in the cluster.
func (o LookupConsulClusterResultOutput) Scale() pulumi.IntOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) int { return v.Scale }).(pulumi.IntOutput)
}

// A unique URL identifying the HCP Consul cluster.
func (o LookupConsulClusterResultOutput) SelfLink() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.SelfLink }).(pulumi.StringOutput)
}

// The t-shirt size representation of each server VM that this Consul cluster is provisioned with. Valid option for development tier - `xSmall`. Valid options for other tiers - `small`, `medium`, `large`. For more details - https://cloud.hashicorp.com/pricing/consul
func (o LookupConsulClusterResultOutput) Size() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.Size }).(pulumi.StringOutput)
}

// The tier that the HCP Consul cluster will be provisioned as.  Only `development`, `standard` and `plus` are available at this time.
func (o LookupConsulClusterResultOutput) Tier() pulumi.StringOutput {
	return o.ApplyT(func(v LookupConsulClusterResult) string { return v.Tier }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupConsulClusterResultOutput{})
}
