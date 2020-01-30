// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

// nolint: lll
package random

import (
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/go/pulumi"
)

// > **Note:** Requires random provider version >= 2.2.0
// 
// Identical to .RandomString with the exception that the
// result is treated as sensitive and, thus, _not_ displayed in console output.
// 
// > **Note:** All attributes including the generated password will be stored in
// the raw state as plain-text. [Read more about sensitive data in
// state](https://www.terraform.io/docs/state/sensitive-data.html).
// 
// This resource *does* use a cryptographic random number generator.
// 
// > This content is derived from https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/password.html.markdown.
type RandomPassword struct {
	pulumi.CustomResourceState

	Keepers pulumi.MapOutput `pulumi:"keepers"`
	Length pulumi.IntOutput `pulumi:"length"`
	Lower pulumi.BoolPtrOutput `pulumi:"lower"`
	MinLower pulumi.IntPtrOutput `pulumi:"minLower"`
	MinNumeric pulumi.IntPtrOutput `pulumi:"minNumeric"`
	MinSpecial pulumi.IntPtrOutput `pulumi:"minSpecial"`
	MinUpper pulumi.IntPtrOutput `pulumi:"minUpper"`
	Number pulumi.BoolPtrOutput `pulumi:"number"`
	OverrideSpecial pulumi.StringPtrOutput `pulumi:"overrideSpecial"`
	Result pulumi.StringOutput `pulumi:"result"`
	Special pulumi.BoolPtrOutput `pulumi:"special"`
	Upper pulumi.BoolPtrOutput `pulumi:"upper"`
}

// NewRandomPassword registers a new resource with the given unique name, arguments, and options.
func NewRandomPassword(ctx *pulumi.Context,
	name string, args *RandomPasswordArgs, opts ...pulumi.ResourceOption) (*RandomPassword, error) {
	if args == nil || args.Length == nil {
		return nil, errors.New("missing required argument 'Length'")
	}
	if args == nil {
		args = &RandomPasswordArgs{}
	}
	var resource RandomPassword
	err := ctx.RegisterResource("random:index/randomPassword:RandomPassword", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRandomPassword gets an existing RandomPassword resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRandomPassword(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RandomPasswordState, opts ...pulumi.ResourceOption) (*RandomPassword, error) {
	var resource RandomPassword
	err := ctx.ReadResource("random:index/randomPassword:RandomPassword", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RandomPassword resources.
type randomPasswordState struct {
	Keepers map[string]interface{} `pulumi:"keepers"`
	Length *int `pulumi:"length"`
	Lower *bool `pulumi:"lower"`
	MinLower *int `pulumi:"minLower"`
	MinNumeric *int `pulumi:"minNumeric"`
	MinSpecial *int `pulumi:"minSpecial"`
	MinUpper *int `pulumi:"minUpper"`
	Number *bool `pulumi:"number"`
	OverrideSpecial *string `pulumi:"overrideSpecial"`
	Result *string `pulumi:"result"`
	Special *bool `pulumi:"special"`
	Upper *bool `pulumi:"upper"`
}

type RandomPasswordState struct {
	Keepers pulumi.MapInput
	Length pulumi.IntPtrInput
	Lower pulumi.BoolPtrInput
	MinLower pulumi.IntPtrInput
	MinNumeric pulumi.IntPtrInput
	MinSpecial pulumi.IntPtrInput
	MinUpper pulumi.IntPtrInput
	Number pulumi.BoolPtrInput
	OverrideSpecial pulumi.StringPtrInput
	Result pulumi.StringPtrInput
	Special pulumi.BoolPtrInput
	Upper pulumi.BoolPtrInput
}

func (RandomPasswordState) ElementType() reflect.Type {
	return reflect.TypeOf((*randomPasswordState)(nil)).Elem()
}

type randomPasswordArgs struct {
	Keepers map[string]interface{} `pulumi:"keepers"`
	Length int `pulumi:"length"`
	Lower *bool `pulumi:"lower"`
	MinLower *int `pulumi:"minLower"`
	MinNumeric *int `pulumi:"minNumeric"`
	MinSpecial *int `pulumi:"minSpecial"`
	MinUpper *int `pulumi:"minUpper"`
	Number *bool `pulumi:"number"`
	OverrideSpecial *string `pulumi:"overrideSpecial"`
	Special *bool `pulumi:"special"`
	Upper *bool `pulumi:"upper"`
}

// The set of arguments for constructing a RandomPassword resource.
type RandomPasswordArgs struct {
	Keepers pulumi.MapInput
	Length pulumi.IntInput
	Lower pulumi.BoolPtrInput
	MinLower pulumi.IntPtrInput
	MinNumeric pulumi.IntPtrInput
	MinSpecial pulumi.IntPtrInput
	MinUpper pulumi.IntPtrInput
	Number pulumi.BoolPtrInput
	OverrideSpecial pulumi.StringPtrInput
	Special pulumi.BoolPtrInput
	Upper pulumi.BoolPtrInput
}

func (RandomPasswordArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*randomPasswordArgs)(nil)).Elem()
}

