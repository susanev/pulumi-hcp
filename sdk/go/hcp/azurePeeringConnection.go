// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package hcp

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// > **Note:** Azure support coming soon. This resource is currently in internal preview only.
//
// The Azure peering connection resource allows you to manage a peering connection between an HVN and a peer Azure VNet.
//
// ## Import
//
// # The import ID is {hvn_id}:{peering_id}
//
// ```sh
//  $ pulumi import hcp:index/azurePeeringConnection:AzurePeeringConnection peer main-hvn:199e7e96-4d5f-4456-91f3-b6cc71f1e561
// ```
type AzurePeeringConnection struct {
	pulumi.CustomResourceState

	// The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
	ApplicationId pulumi.StringOutput `pulumi:"applicationId"`
	// The peering connection ID used by Azure.
	AzurePeeringId pulumi.StringOutput `pulumi:"azurePeeringId"`
	// The time that the peering connection was created.
	CreatedAt pulumi.StringOutput `pulumi:"createdAt"`
	// The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
	ExpiresAt pulumi.StringOutput `pulumi:"expiresAt"`
	// The `selfLink` of the HashiCorp Virtual Network (HVN).
	HvnLink pulumi.StringOutput `pulumi:"hvnLink"`
	// The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
	OrganizationId pulumi.StringOutput `pulumi:"organizationId"`
	// The resource group name of the peer VNet in Azure.
	PeerResourceGroupName pulumi.StringOutput `pulumi:"peerResourceGroupName"`
	// The subscription ID of the peer VNet in Azure.
	PeerSubscriptionId pulumi.StringOutput `pulumi:"peerSubscriptionId"`
	// The tenant ID of the peer VNet in Azure.
	PeerTenantId pulumi.StringOutput `pulumi:"peerTenantId"`
	// The name of the peer VNet in Azure.
	PeerVnetName pulumi.StringOutput `pulumi:"peerVnetName"`
	// The region of the peer VNet in Azure.
	PeerVnetRegion pulumi.StringOutput `pulumi:"peerVnetRegion"`
	// The ID of the peering connection.
	PeeringId pulumi.StringOutput `pulumi:"peeringId"`
	// The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
	ProjectId pulumi.StringOutput `pulumi:"projectId"`
	// A unique URL identifying the peering connection.
	SelfLink pulumi.StringOutput `pulumi:"selfLink"`
}

// NewAzurePeeringConnection registers a new resource with the given unique name, arguments, and options.
func NewAzurePeeringConnection(ctx *pulumi.Context,
	name string, args *AzurePeeringConnectionArgs, opts ...pulumi.ResourceOption) (*AzurePeeringConnection, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.HvnLink == nil {
		return nil, errors.New("invalid value for required argument 'HvnLink'")
	}
	if args.PeerResourceGroupName == nil {
		return nil, errors.New("invalid value for required argument 'PeerResourceGroupName'")
	}
	if args.PeerSubscriptionId == nil {
		return nil, errors.New("invalid value for required argument 'PeerSubscriptionId'")
	}
	if args.PeerTenantId == nil {
		return nil, errors.New("invalid value for required argument 'PeerTenantId'")
	}
	if args.PeerVnetName == nil {
		return nil, errors.New("invalid value for required argument 'PeerVnetName'")
	}
	if args.PeerVnetRegion == nil {
		return nil, errors.New("invalid value for required argument 'PeerVnetRegion'")
	}
	if args.PeeringId == nil {
		return nil, errors.New("invalid value for required argument 'PeeringId'")
	}
	opts = pkgResourceDefaultOpts(opts)
	var resource AzurePeeringConnection
	err := ctx.RegisterResource("hcp:index/azurePeeringConnection:AzurePeeringConnection", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetAzurePeeringConnection gets an existing AzurePeeringConnection resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetAzurePeeringConnection(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *AzurePeeringConnectionState, opts ...pulumi.ResourceOption) (*AzurePeeringConnection, error) {
	var resource AzurePeeringConnection
	err := ctx.ReadResource("hcp:index/azurePeeringConnection:AzurePeeringConnection", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering AzurePeeringConnection resources.
type azurePeeringConnectionState struct {
	// The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
	ApplicationId *string `pulumi:"applicationId"`
	// The peering connection ID used by Azure.
	AzurePeeringId *string `pulumi:"azurePeeringId"`
	// The time that the peering connection was created.
	CreatedAt *string `pulumi:"createdAt"`
	// The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
	ExpiresAt *string `pulumi:"expiresAt"`
	// The `selfLink` of the HashiCorp Virtual Network (HVN).
	HvnLink *string `pulumi:"hvnLink"`
	// The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
	OrganizationId *string `pulumi:"organizationId"`
	// The resource group name of the peer VNet in Azure.
	PeerResourceGroupName *string `pulumi:"peerResourceGroupName"`
	// The subscription ID of the peer VNet in Azure.
	PeerSubscriptionId *string `pulumi:"peerSubscriptionId"`
	// The tenant ID of the peer VNet in Azure.
	PeerTenantId *string `pulumi:"peerTenantId"`
	// The name of the peer VNet in Azure.
	PeerVnetName *string `pulumi:"peerVnetName"`
	// The region of the peer VNet in Azure.
	PeerVnetRegion *string `pulumi:"peerVnetRegion"`
	// The ID of the peering connection.
	PeeringId *string `pulumi:"peeringId"`
	// The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
	ProjectId *string `pulumi:"projectId"`
	// A unique URL identifying the peering connection.
	SelfLink *string `pulumi:"selfLink"`
}

type AzurePeeringConnectionState struct {
	// The ID of the Azure application whose credentials are used to peer the HCP HVN's underlying VNet with the customer VNet.
	ApplicationId pulumi.StringPtrInput
	// The peering connection ID used by Azure.
	AzurePeeringId pulumi.StringPtrInput
	// The time that the peering connection was created.
	CreatedAt pulumi.StringPtrInput
	// The time after which the peering connection will be considered expired if it hasn't transitioned into `ACCEPTED` or `ACTIVE` state.
	ExpiresAt pulumi.StringPtrInput
	// The `selfLink` of the HashiCorp Virtual Network (HVN).
	HvnLink pulumi.StringPtrInput
	// The ID of the HCP organization where the peering connection is located. Always matches the HVN's organization.
	OrganizationId pulumi.StringPtrInput
	// The resource group name of the peer VNet in Azure.
	PeerResourceGroupName pulumi.StringPtrInput
	// The subscription ID of the peer VNet in Azure.
	PeerSubscriptionId pulumi.StringPtrInput
	// The tenant ID of the peer VNet in Azure.
	PeerTenantId pulumi.StringPtrInput
	// The name of the peer VNet in Azure.
	PeerVnetName pulumi.StringPtrInput
	// The region of the peer VNet in Azure.
	PeerVnetRegion pulumi.StringPtrInput
	// The ID of the peering connection.
	PeeringId pulumi.StringPtrInput
	// The ID of the HCP project where the peering connection is located. Always matches the HVN's project.
	ProjectId pulumi.StringPtrInput
	// A unique URL identifying the peering connection.
	SelfLink pulumi.StringPtrInput
}

func (AzurePeeringConnectionState) ElementType() reflect.Type {
	return reflect.TypeOf((*azurePeeringConnectionState)(nil)).Elem()
}

type azurePeeringConnectionArgs struct {
	// The `selfLink` of the HashiCorp Virtual Network (HVN).
	HvnLink string `pulumi:"hvnLink"`
	// The resource group name of the peer VNet in Azure.
	PeerResourceGroupName string `pulumi:"peerResourceGroupName"`
	// The subscription ID of the peer VNet in Azure.
	PeerSubscriptionId string `pulumi:"peerSubscriptionId"`
	// The tenant ID of the peer VNet in Azure.
	PeerTenantId string `pulumi:"peerTenantId"`
	// The name of the peer VNet in Azure.
	PeerVnetName string `pulumi:"peerVnetName"`
	// The region of the peer VNet in Azure.
	PeerVnetRegion string `pulumi:"peerVnetRegion"`
	// The ID of the peering connection.
	PeeringId string `pulumi:"peeringId"`
}

// The set of arguments for constructing a AzurePeeringConnection resource.
type AzurePeeringConnectionArgs struct {
	// The `selfLink` of the HashiCorp Virtual Network (HVN).
	HvnLink pulumi.StringInput
	// The resource group name of the peer VNet in Azure.
	PeerResourceGroupName pulumi.StringInput
	// The subscription ID of the peer VNet in Azure.
	PeerSubscriptionId pulumi.StringInput
	// The tenant ID of the peer VNet in Azure.
	PeerTenantId pulumi.StringInput
	// The name of the peer VNet in Azure.
	PeerVnetName pulumi.StringInput
	// The region of the peer VNet in Azure.
	PeerVnetRegion pulumi.StringInput
	// The ID of the peering connection.
	PeeringId pulumi.StringInput
}

func (AzurePeeringConnectionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*azurePeeringConnectionArgs)(nil)).Elem()
}

type AzurePeeringConnectionInput interface {
	pulumi.Input

	ToAzurePeeringConnectionOutput() AzurePeeringConnectionOutput
	ToAzurePeeringConnectionOutputWithContext(ctx context.Context) AzurePeeringConnectionOutput
}

func (*AzurePeeringConnection) ElementType() reflect.Type {
	return reflect.TypeOf((**AzurePeeringConnection)(nil)).Elem()
}

func (i *AzurePeeringConnection) ToAzurePeeringConnectionOutput() AzurePeeringConnectionOutput {
	return i.ToAzurePeeringConnectionOutputWithContext(context.Background())
}

func (i *AzurePeeringConnection) ToAzurePeeringConnectionOutputWithContext(ctx context.Context) AzurePeeringConnectionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AzurePeeringConnectionOutput)
}

// AzurePeeringConnectionArrayInput is an input type that accepts AzurePeeringConnectionArray and AzurePeeringConnectionArrayOutput values.
// You can construct a concrete instance of `AzurePeeringConnectionArrayInput` via:
//
//          AzurePeeringConnectionArray{ AzurePeeringConnectionArgs{...} }
type AzurePeeringConnectionArrayInput interface {
	pulumi.Input

	ToAzurePeeringConnectionArrayOutput() AzurePeeringConnectionArrayOutput
	ToAzurePeeringConnectionArrayOutputWithContext(context.Context) AzurePeeringConnectionArrayOutput
}

type AzurePeeringConnectionArray []AzurePeeringConnectionInput

func (AzurePeeringConnectionArray) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AzurePeeringConnection)(nil)).Elem()
}

func (i AzurePeeringConnectionArray) ToAzurePeeringConnectionArrayOutput() AzurePeeringConnectionArrayOutput {
	return i.ToAzurePeeringConnectionArrayOutputWithContext(context.Background())
}

func (i AzurePeeringConnectionArray) ToAzurePeeringConnectionArrayOutputWithContext(ctx context.Context) AzurePeeringConnectionArrayOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AzurePeeringConnectionArrayOutput)
}

// AzurePeeringConnectionMapInput is an input type that accepts AzurePeeringConnectionMap and AzurePeeringConnectionMapOutput values.
// You can construct a concrete instance of `AzurePeeringConnectionMapInput` via:
//
//          AzurePeeringConnectionMap{ "key": AzurePeeringConnectionArgs{...} }
type AzurePeeringConnectionMapInput interface {
	pulumi.Input

	ToAzurePeeringConnectionMapOutput() AzurePeeringConnectionMapOutput
	ToAzurePeeringConnectionMapOutputWithContext(context.Context) AzurePeeringConnectionMapOutput
}

type AzurePeeringConnectionMap map[string]AzurePeeringConnectionInput

func (AzurePeeringConnectionMap) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AzurePeeringConnection)(nil)).Elem()
}

func (i AzurePeeringConnectionMap) ToAzurePeeringConnectionMapOutput() AzurePeeringConnectionMapOutput {
	return i.ToAzurePeeringConnectionMapOutputWithContext(context.Background())
}

func (i AzurePeeringConnectionMap) ToAzurePeeringConnectionMapOutputWithContext(ctx context.Context) AzurePeeringConnectionMapOutput {
	return pulumi.ToOutputWithContext(ctx, i).(AzurePeeringConnectionMapOutput)
}

type AzurePeeringConnectionOutput struct{ *pulumi.OutputState }

func (AzurePeeringConnectionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**AzurePeeringConnection)(nil)).Elem()
}

func (o AzurePeeringConnectionOutput) ToAzurePeeringConnectionOutput() AzurePeeringConnectionOutput {
	return o
}

func (o AzurePeeringConnectionOutput) ToAzurePeeringConnectionOutputWithContext(ctx context.Context) AzurePeeringConnectionOutput {
	return o
}

type AzurePeeringConnectionArrayOutput struct{ *pulumi.OutputState }

func (AzurePeeringConnectionArrayOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*[]*AzurePeeringConnection)(nil)).Elem()
}

func (o AzurePeeringConnectionArrayOutput) ToAzurePeeringConnectionArrayOutput() AzurePeeringConnectionArrayOutput {
	return o
}

func (o AzurePeeringConnectionArrayOutput) ToAzurePeeringConnectionArrayOutputWithContext(ctx context.Context) AzurePeeringConnectionArrayOutput {
	return o
}

func (o AzurePeeringConnectionArrayOutput) Index(i pulumi.IntInput) AzurePeeringConnectionOutput {
	return pulumi.All(o, i).ApplyT(func(vs []interface{}) *AzurePeeringConnection {
		return vs[0].([]*AzurePeeringConnection)[vs[1].(int)]
	}).(AzurePeeringConnectionOutput)
}

type AzurePeeringConnectionMapOutput struct{ *pulumi.OutputState }

func (AzurePeeringConnectionMapOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*map[string]*AzurePeeringConnection)(nil)).Elem()
}

func (o AzurePeeringConnectionMapOutput) ToAzurePeeringConnectionMapOutput() AzurePeeringConnectionMapOutput {
	return o
}

func (o AzurePeeringConnectionMapOutput) ToAzurePeeringConnectionMapOutputWithContext(ctx context.Context) AzurePeeringConnectionMapOutput {
	return o
}

func (o AzurePeeringConnectionMapOutput) MapIndex(k pulumi.StringInput) AzurePeeringConnectionOutput {
	return pulumi.All(o, k).ApplyT(func(vs []interface{}) *AzurePeeringConnection {
		return vs[0].(map[string]*AzurePeeringConnection)[vs[1].(string)]
	}).(AzurePeeringConnectionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*AzurePeeringConnectionInput)(nil)).Elem(), &AzurePeeringConnection{})
	pulumi.RegisterInputType(reflect.TypeOf((*AzurePeeringConnectionArrayInput)(nil)).Elem(), AzurePeeringConnectionArray{})
	pulumi.RegisterInputType(reflect.TypeOf((*AzurePeeringConnectionMapInput)(nil)).Elem(), AzurePeeringConnectionMap{})
	pulumi.RegisterOutputType(AzurePeeringConnectionOutput{})
	pulumi.RegisterOutputType(AzurePeeringConnectionArrayOutput{})
	pulumi.RegisterOutputType(AzurePeeringConnectionMapOutput{})
}
