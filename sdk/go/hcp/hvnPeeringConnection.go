// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The HVN peering connection resource allows you to manage a peering connection between HVNs.
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
// 		hvn1, err := hcp.NewHvn(ctx, "hvn1", &hcp.HvnArgs{
// 			HvnId:         pulumi.String("hvn-1"),
// 			CloudProvider: pulumi.String("aws"),
// 			Region:        pulumi.String("us-west-2"),
// 			CidrBlock:     pulumi.String("172.25.16.0/20"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		hvn2, err := hcp.NewHvn(ctx, "hvn2", &hcp.HvnArgs{
// 			HvnId:         pulumi.String("hvn-2"),
// 			CloudProvider: pulumi.String("aws"),
// 			Region:        pulumi.String("us-west-2"),
// 			CidrBlock:     pulumi.String("172.18.16.0/20"),
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		_, err = hcp.NewHvnPeeringConnection(ctx, "peer1", &hcp.HvnPeeringConnectionArgs{
// 			Hvn1: hvn1.SelfLink,
// 			Hvn2: hvn2.SelfLink,
// 		})
// 		if err != nil {
// 			return err
// 		}
// 		return nil
// 	})
// }
// ```
//
// ## Import
//
// # The import ID requires the first HVN ID in the format {hvn_1_id}:{peering_id}
//
// ```sh
//  $ pulumi import hcp:index/hvnPeeringConnection:HvnPeeringConnection peer_1 hvn-1:peer-1
// ```
type HvnPeeringConnection struct {
	pulumi.CustomResourceState

	// The time that the peering connection was created.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
	ExpiresAt pulumi.StringOutput `pulumi:"expiresAt"`
	// The unique URL of one of the HVNs being peered.
	Hvn1 pulumi.StringOutput `pulumi:"hvn1"`
	// The unique URL of one of the HVNs being peered.
	Hvn2 pulumi.StringOutput `pulumi:"hvn2"`
	// The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The ID of the peering connection.
	PeeringId pulumi.StringOutput `pulumi:"peeringId"`
	// The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// A unique URL identifying the peering connection
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
}

// NewHvnPeeringConnection registers a new resource with the given unique name, arguments, and options.
func NewHvnPeeringConnection(ctx *pulumi.Context,
	name string, args *HvnPeeringConnectionArgs, opts ...pulumi.ResourceOption) (*HvnPeeringConnection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Hvn1 == nil {
		return nil, errors.New("invalid value for required argument 'Hvn1'")
	}
	if args.Hvn2 == nil {
		return nil, errors.New("invalid value for required argument 'Hvn2'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource HvnPeeringConnection
	err := ctx.RegisterResource("hcp:index/hvnPeeringConnection:HvnPeeringConnection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetHvnPeeringConnection gets an existing HvnPeeringConnection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetHvnPeeringConnection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *HvnPeeringConnectionState, opts ...pulumi.ResourceOption) (*HvnPeeringConnection, error) {
	var resource HvnPeeringConnection
	err := ctx.ReadResource("hcp:index/hvnPeeringConnection:HvnPeeringConnection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering HvnPeeringConnection resources.
type hvnPeeringConnectionState struct {
	// The time that the peering connection was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
	ExpiresAt *string `pulumi:"expiresAt"`
	// The unique URL of one of the HVNs being peered.
	Hvn1 *string `pulumi:"hvn1"`
	// The unique URL of one of the HVNs being peered.
	Hvn2 *string `pulumi:"hvn2"`
	// The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
	OrganizationId *string `pulumi:"organizationId"`
	// The ID of the peering connection.
	PeeringId *string `pulumi:"peeringId"`
	// The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
	ProjectId *string `pulumi:"projectId"`
	// A unique URL identifying the peering connection
	SelfLink *string `pulumi:"selfLink"`
}

type HvnPeeringConnectionState struct {
	// The time that the peering connection was created.
	CreatedAt pulumi.StringPtrInput
	// The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
	ExpiresAt pulumi.StringPtrInput
	// The unique URL of one of the HVNs being peered.
	Hvn1 pulumi.StringPtrInput
	// The unique URL of one of the HVNs being peered.
	Hvn2 pulumi.StringPtrInput
	// The ID of the HCP organization where the peering connection is located. Always matches the HVNs' organization.
	OrganizationId pulumi.StringPtrInput
	// The ID of the peering connection.
	PeeringId pulumi.StringPtrInput
	// The ID of the HCP project where the peering connection is located. Always matches the HVNs' project.
	ProjectId pulumi.StringPtrInput
	// A unique URL identifying the peering connection
	SelfLink pulumi.StringPtrInput
}

func (HvnPeeringConnectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*hvnPeeringConnectionState)(nil)).Elem()
}

type hvnPeeringConnectionArgs struct {
	// The unique URL of one of the HVNs being peered.
	Hvn1 string `pulumi:"hvn1"`
	// The unique URL of one of the HVNs being peered.
	Hvn2 string `pulumi:"hvn2"`
}

// The set of arguments for constructing a HvnPeeringConnection resource.
type HvnPeeringConnectionArgs struct {
	// The unique URL of one of the HVNs being peered.
	Hvn1 pulumi.StringInput
	// The unique URL of one of the HVNs being peered.
	Hvn2 pulumi.StringInput
}

func (HvnPeeringConnectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*hvnPeeringConnectionArgs)(nil)).Elem()
}

type HvnPeeringConnectionInput interface {
	pulumi.Input

	ToHvnPeeringConnectionOutput() HvnPeeringConnectionOutput
	ToHvnPeeringConnectionOutputWithContext(ctx context.Context) HvnPeeringConnectionOutput
}

func (*HvnPeeringConnection) ElementType() reflect.Type {
	return reflect.TypeOf((**HvnPeeringConnection)(nil)).Elem()
}

func (i *HvnPeeringConnection) ToHvnPeeringConnectionOutput() HvnPeeringConnectionOutput {
	return i.ToHvnPeeringConnectionOutputWithContext(context.Background())
}

func (i *HvnPeeringConnection) ToHvnPeeringConnectionOutputWithContext(ctx context.Context) HvnPeeringConnectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnPeeringConnectionOutput)
}

// HvnPeeringConnectionArrayInput is an input type that accepts HvnPeeringConnectionArray and HvnPeeringConnectionArrayOutput values.
// You can construct a concrete instance of `HvnPeeringConnectionArrayInput` via:
//
//          HvnPeeringConnectionArray{ HvnPeeringConnectionArgs{...} }
type HvnPeeringConnectionArrayInput interface {
	pulumi.Input

	ToHvnPeeringConnectionArrayOutput() HvnPeeringConnectionArrayOutput
	ToHvnPeeringConnectionArrayOutputWithContext(context.Context) HvnPeeringConnectionArrayOutput
}

type HvnPeeringConnectionArray []HvnPeeringConnectionInput

func (HvnPeeringConnectionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*HvnPeeringConnection)(nil)).Elem()
}

func (i HvnPeeringConnectionArray) ToHvnPeeringConnectionArrayOutput() HvnPeeringConnectionArrayOutput {
	return i.ToHvnPeeringConnectionArrayOutputWithContext(context.Background())
}

func (i HvnPeeringConnectionArray) ToHvnPeeringConnectionArrayOutputWithContext(ctx context.Context) HvnPeeringConnectionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnPeeringConnectionArrayOutput)
}

// HvnPeeringConnectionMapInput is an input type that accepts HvnPeeringConnectionMap and HvnPeeringConnectionMapOutput values.
// You can construct a concrete instance of `HvnPeeringConnectionMapInput` via:
//
//          HvnPeeringConnectionMap{ "key": HvnPeeringConnectionArgs{...} }
type HvnPeeringConnectionMapInput interface {
	pulumi.Input

	ToHvnPeeringConnectionMapOutput() HvnPeeringConnectionMapOutput
	ToHvnPeeringConnectionMapOutputWithContext(context.Context) HvnPeeringConnectionMapOutput
}

type HvnPeeringConnectionMap map[string]HvnPeeringConnectionInput

func (HvnPeeringConnectionMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*HvnPeeringConnection)(nil)).Elem()
}

func (i HvnPeeringConnectionMap) ToHvnPeeringConnectionMapOutput() HvnPeeringConnectionMapOutput {
	return i.ToHvnPeeringConnectionMapOutputWithContext(context.Background())
}

func (i HvnPeeringConnectionMap) ToHvnPeeringConnectionMapOutputWithContext(ctx context.Context) HvnPeeringConnectionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(HvnPeeringConnectionMapOutput)
}

type HvnPeeringConnectionOutput struct{ *pulumi.OutputState }

func (HvnPeeringConnectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**HvnPeeringConnection)(nil)).Elem()
}

func (o HvnPeeringConnectionOutput) ToHvnPeeringConnectionOutput() HvnPeeringConnectionOutput {
	return o
}

func (o HvnPeeringConnectionOutput) ToHvnPeeringConnectionOutputWithContext(ctx context.Context) HvnPeeringConnectionOutput {
	return o
}

type HvnPeeringConnectionArrayOutput struct{ *pulumi.OutputState }

func (HvnPeeringConnectionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*HvnPeeringConnection)(nil)).Elem()
}

func (o HvnPeeringConnectionArrayOutput) ToHvnPeeringConnectionArrayOutput() HvnPeeringConnectionArrayOutput {
	return o
}

func (o HvnPeeringConnectionArrayOutput) ToHvnPeeringConnectionArrayOutputWithContext(ctx context.Context) HvnPeeringConnectionArrayOutput {
	return o
}

func (o HvnPeeringConnectionArrayOutput) Index(i pulumi.IntInput) HvnPeeringConnectionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *HvnPeeringConnection {
		return vs[0].([]*HvnPeeringConnection)[vs[1].(int)]
	}).(HvnPeeringConnectionOutput)
}

type HvnPeeringConnectionMapOutput struct{ *pulumi.OutputState }

func (HvnPeeringConnectionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*HvnPeeringConnection)(nil)).Elem()
}

func (o HvnPeeringConnectionMapOutput) ToHvnPeeringConnectionMapOutput() HvnPeeringConnectionMapOutput {
	return o
}

func (o HvnPeeringConnectionMapOutput) ToHvnPeeringConnectionMapOutputWithContext(ctx context.Context) HvnPeeringConnectionMapOutput {
	return o
}

func (o HvnPeeringConnectionMapOutput) MapIndex(k pulumi.StringInput) HvnPeeringConnectionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *HvnPeeringConnection {
		return vs[0].(map[string]*HvnPeeringConnection)[vs[1].(string)]
	}).(HvnPeeringConnectionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*HvnPeeringConnectionInput)(nil)).Elem(), &HvnPeeringConnection{})
	pulumi.RegisterInputType(reflect.TypeOf((*HvnPeeringConnectionArrayInput)(nil)).Elem(), HvnPeeringConnectionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*HvnPeeringConnectionMapInput)(nil)).Elem(), HvnPeeringConnectionMap{})
	pulumi.RegisterOutputType(HvnPeeringConnectionOutput{})
	pulumi.RegisterOutputType(HvnPeeringConnectionArrayOutput{})
	pulumi.RegisterOutputType(HvnPeeringConnectionMapOutput{})
}
