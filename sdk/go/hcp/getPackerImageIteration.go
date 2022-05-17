// Code generated by the Pulumi Terraform Bridge (tfgen) Tool DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The Packer Image data source iteration gets the most recent iteration (or build) of an image, given a channel.
//
// ## Example Usage
//
// ```go
// package main
//
// import (
// 	"github.com/grapl-security/pulumi-hcp/sdk/go/hcp"
// 	"github.com/pulumi/pulumi-hcp/sdk/go/hcp"
// 	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
// )
//
// func main() {
// 	pulumi.Run(func(ctx *pulumi.Context) error {
// 		_, err := hcp.GetPackerImageIteration(ctx, &GetPackerImageIterationArgs{
// 			BucketName: "alpine",
// 			Channel:    "production",
// 		}, nil)
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
func GetPackerImageIteration(ctx *pulumi.Context, args *GetPackerImageIterationArgs, opts ...pulumi.InvokeOption) (*GetPackerImageIterationResult, error) {
	opts = pkgInvokeDefaultOpts(opts)
	var rv GetPackerImageIterationResult
	err := ctx.Invoke("hcp:index/getPackerImageIteration:getPackerImageIteration", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

// A collection of arguments for invoking getPackerImageIteration.
type GetPackerImageIterationArgs struct {
	// The slug of the HCP Packer Registry image bucket to pull from.
	BucketName string `pulumi:"bucketName"`
	// The channel that points to the version of the image you want.
	Channel string `pulumi:"channel"`
}

// A collection of values returned by getPackerImageIteration.
type GetPackerImageIterationResult struct {
	// The slug of the HCP Packer Registry image bucket to pull from.
	BucketName string `pulumi:"bucketName"`
	// Builds for this iteration. An iteration can have more than one build if it took more than one go to build all images.
	Builds []GetPackerImageIterationBuild `pulumi:"builds"`
	// The channel that points to the version of the image you want.
	Channel string `pulumi:"channel"`
	// Creation time of this iteration
	CreatedAt string `pulumi:"createdAt"`
	// The provider-assigned unique ID for this managed resource.
	Id string `pulumi:"id"`
	// Incremental version of this iteration
	IncrementalVersion int `pulumi:"incrementalVersion"`
	// The ID of the organization this HCP Packer registry is located in.
	OrganizationId string `pulumi:"organizationId"`
	// The ID of the project this HCP Packer registry is located in.
	ProjectId string `pulumi:"projectId"`
}

func GetPackerImageIterationOutput(ctx *pulumi.Context, args GetPackerImageIterationOutputArgs, opts ...pulumi.InvokeOption) GetPackerImageIterationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (GetPackerImageIterationResult, error) {
			args := v.(GetPackerImageIterationArgs)
			r, err := GetPackerImageIteration(ctx, &args, opts...)
			var s GetPackerImageIterationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(GetPackerImageIterationResultOutput)
}

// A collection of arguments for invoking getPackerImageIteration.
type GetPackerImageIterationOutputArgs struct {
	// The slug of the HCP Packer Registry image bucket to pull from.
	BucketName pulumi.StringInput `pulumi:"bucketName"`
	// The channel that points to the version of the image you want.
	Channel pulumi.StringInput `pulumi:"channel"`
}

func (GetPackerImageIterationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPackerImageIterationArgs)(nil)).Elem()
}

// A collection of values returned by getPackerImageIteration.
type GetPackerImageIterationResultOutput struct{ *pulumi.OutputState }

func (GetPackerImageIterationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*GetPackerImageIterationResult)(nil)).Elem()
}

func (o GetPackerImageIterationResultOutput) ToGetPackerImageIterationResultOutput() GetPackerImageIterationResultOutput {
	return o
}

func (o GetPackerImageIterationResultOutput) ToGetPackerImageIterationResultOutputWithContext(ctx context.Context) GetPackerImageIterationResultOutput {
	return o
}

// The slug of the HCP Packer Registry image bucket to pull from.
func (o GetPackerImageIterationResultOutput) BucketName() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerImageIterationResult) string { return v.BucketName }).(pulumi.StringOutput)
}

// Builds for this iteration. An iteration can have more than one build if it took more than one go to build all images.
func (o GetPackerImageIterationResultOutput) Builds() GetPackerImageIterationBuildArrayOutput {
	return o.ApplyT(func(v GetPackerImageIterationResult) []GetPackerImageIterationBuild { return v.Builds }).(GetPackerImageIterationBuildArrayOutput)
}

// The channel that points to the version of the image you want.
func (o GetPackerImageIterationResultOutput) Channel() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerImageIterationResult) string { return v.Channel }).(pulumi.StringOutput)
}

// Creation time of this iteration
func (o GetPackerImageIterationResultOutput) CreatedAt() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerImageIterationResult) string { return v.CreatedAt }).(pulumi.StringOutput)
}

// The provider-assigned unique ID for this managed resource.
func (o GetPackerImageIterationResultOutput) Id() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerImageIterationResult) string { return v.Id }).(pulumi.StringOutput)
}

// Incremental version of this iteration
func (o GetPackerImageIterationResultOutput) IncrementalVersion() pulumi.IntOutput {
	return o.ApplyT(func(v GetPackerImageIterationResult) int { return v.IncrementalVersion }).(pulumi.IntOutput)
}

// The ID of the organization this HCP Packer registry is located in.
func (o GetPackerImageIterationResultOutput) OrganizationId() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerImageIterationResult) string { return v.OrganizationId }).(pulumi.StringOutput)
}

// The ID of the project this HCP Packer registry is located in.
func (o GetPackerImageIterationResultOutput) ProjectId() pulumi.StringOutput {
	return o.ApplyT(func(v GetPackerImageIterationResult) string { return v.ProjectId }).(pulumi.StringOutput)
}

func init() {
	pulumi.RegisterOutputType(GetPackerImageIterationResultOutput{})
}
