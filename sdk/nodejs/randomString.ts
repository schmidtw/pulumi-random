// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The resource `random_string` generates a random permutation of alphanumeric
 * characters and optionally special characters.
 * 
 * This resource *does* use a cryptographic random number generator.
 * 
 * ## Example Usage
 * 
 * ```typescript
 * import * as pulumi from "@pulumi/pulumi";
 * import * as aws from "@pulumi/aws";
 * import * as random from "@pulumi/random";
 * 
 * const password = new random.RandomString("password", {
 *     length: 16,
 *     overrideSpecial: "/@\" ",
 *     special: true,
 * });
 * const example = new aws.rds.Instance("example", {
 *     password: password.result,
 * });
 * ```
 *
 * > This content is derived from https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/string.html.markdown.
 */
export class RandomString extends pulumi.CustomResource {
    /**
     * Get an existing RandomString resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RandomStringState, opts?: pulumi.CustomResourceOptions): RandomString {
        return new RandomString(name, <any>state, { ...opts, id: id });
    }

    /** @internal */
    public static readonly __pulumiType = 'random:index/randomString:RandomString';

    /**
     * Returns true if the given object is an instance of RandomString.  This is designed to work even
     * when multiple copies of the Pulumi SDK have been loaded into the same process.
     */
    public static isInstance(obj: any): obj is RandomString {
        if (obj === undefined || obj === null) {
            return false;
        }
        return obj['__pulumiType'] === RandomString.__pulumiType;
    }

    /**
     * Arbitrary map of values that, when changed, will
     * trigger a new id to be generated. See
     * the main provider documentation for more information.
     */
    public readonly keepers!: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The length of the string desired
     */
    public readonly length!: pulumi.Output<number>;
    /**
     * (default true) Include lowercase alphabet characters
     * in random string.
     */
    public readonly lower!: pulumi.Output<boolean | undefined>;
    /**
     * (default 0) Minimum number of lowercase alphabet
     * characters in random string.
     */
    public readonly minLower!: pulumi.Output<number | undefined>;
    /**
     * (default 0) Minimum number of numeric characters
     * in random string.
     */
    public readonly minNumeric!: pulumi.Output<number | undefined>;
    /**
     * (default 0) Minimum number of special characters
     * in random string.
     */
    public readonly minSpecial!: pulumi.Output<number | undefined>;
    /**
     * (default 0) Minimum number of uppercase alphabet
     * characters in random string.
     */
    public readonly minUpper!: pulumi.Output<number | undefined>;
    /**
     * (default true) Include numeric characters in random
     * string.
     */
    public readonly number!: pulumi.Output<boolean | undefined>;
    /**
     * Supply your own list of special characters to
     * use for string generation.  This overrides characters list in the special
     * argument.  The special argument must still be set to true for any overwritten
     * characters to be used in generation.
     */
    public readonly overrideSpecial!: pulumi.Output<string | undefined>;
    /**
     * Random string generated.
     */
    public /*out*/ readonly result!: pulumi.Output<string>;
    /**
     * (default true) Include special characters in random
     * string. These are '!@#$%&*()-_=+[]{}<>:?'
     */
    public readonly special!: pulumi.Output<boolean | undefined>;
    /**
     * (default true) Include uppercase alphabet characters
     * in random string.
     */
    public readonly upper!: pulumi.Output<boolean | undefined>;

    /**
     * Create a RandomString resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args: RandomStringArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RandomStringArgs | RandomStringState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state = argsOrState as RandomStringState | undefined;
            inputs["keepers"] = state ? state.keepers : undefined;
            inputs["length"] = state ? state.length : undefined;
            inputs["lower"] = state ? state.lower : undefined;
            inputs["minLower"] = state ? state.minLower : undefined;
            inputs["minNumeric"] = state ? state.minNumeric : undefined;
            inputs["minSpecial"] = state ? state.minSpecial : undefined;
            inputs["minUpper"] = state ? state.minUpper : undefined;
            inputs["number"] = state ? state.number : undefined;
            inputs["overrideSpecial"] = state ? state.overrideSpecial : undefined;
            inputs["result"] = state ? state.result : undefined;
            inputs["special"] = state ? state.special : undefined;
            inputs["upper"] = state ? state.upper : undefined;
        } else {
            const args = argsOrState as RandomStringArgs | undefined;
            if (!args || args.length === undefined) {
                throw new Error("Missing required property 'length'");
            }
            inputs["keepers"] = args ? args.keepers : undefined;
            inputs["length"] = args ? args.length : undefined;
            inputs["lower"] = args ? args.lower : undefined;
            inputs["minLower"] = args ? args.minLower : undefined;
            inputs["minNumeric"] = args ? args.minNumeric : undefined;
            inputs["minSpecial"] = args ? args.minSpecial : undefined;
            inputs["minUpper"] = args ? args.minUpper : undefined;
            inputs["number"] = args ? args.number : undefined;
            inputs["overrideSpecial"] = args ? args.overrideSpecial : undefined;
            inputs["special"] = args ? args.special : undefined;
            inputs["upper"] = args ? args.upper : undefined;
            inputs["result"] = undefined /*out*/;
        }
        super(RandomString.__pulumiType, name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RandomString resources.
 */
export interface RandomStringState {
    /**
     * Arbitrary map of values that, when changed, will
     * trigger a new id to be generated. See
     * the main provider documentation for more information.
     */
    readonly keepers?: pulumi.Input<{[key: string]: any}>;
    /**
     * The length of the string desired
     */
    readonly length?: pulumi.Input<number>;
    /**
     * (default true) Include lowercase alphabet characters
     * in random string.
     */
    readonly lower?: pulumi.Input<boolean>;
    /**
     * (default 0) Minimum number of lowercase alphabet
     * characters in random string.
     */
    readonly minLower?: pulumi.Input<number>;
    /**
     * (default 0) Minimum number of numeric characters
     * in random string.
     */
    readonly minNumeric?: pulumi.Input<number>;
    /**
     * (default 0) Minimum number of special characters
     * in random string.
     */
    readonly minSpecial?: pulumi.Input<number>;
    /**
     * (default 0) Minimum number of uppercase alphabet
     * characters in random string.
     */
    readonly minUpper?: pulumi.Input<number>;
    /**
     * (default true) Include numeric characters in random
     * string.
     */
    readonly number?: pulumi.Input<boolean>;
    /**
     * Supply your own list of special characters to
     * use for string generation.  This overrides characters list in the special
     * argument.  The special argument must still be set to true for any overwritten
     * characters to be used in generation.
     */
    readonly overrideSpecial?: pulumi.Input<string>;
    /**
     * Random string generated.
     */
    readonly result?: pulumi.Input<string>;
    /**
     * (default true) Include special characters in random
     * string. These are '!@#$%&*()-_=+[]{}<>:?'
     */
    readonly special?: pulumi.Input<boolean>;
    /**
     * (default true) Include uppercase alphabet characters
     * in random string.
     */
    readonly upper?: pulumi.Input<boolean>;
}

/**
 * The set of arguments for constructing a RandomString resource.
 */
export interface RandomStringArgs {
    /**
     * Arbitrary map of values that, when changed, will
     * trigger a new id to be generated. See
     * the main provider documentation for more information.
     */
    readonly keepers?: pulumi.Input<{[key: string]: any}>;
    /**
     * The length of the string desired
     */
    readonly length: pulumi.Input<number>;
    /**
     * (default true) Include lowercase alphabet characters
     * in random string.
     */
    readonly lower?: pulumi.Input<boolean>;
    /**
     * (default 0) Minimum number of lowercase alphabet
     * characters in random string.
     */
    readonly minLower?: pulumi.Input<number>;
    /**
     * (default 0) Minimum number of numeric characters
     * in random string.
     */
    readonly minNumeric?: pulumi.Input<number>;
    /**
     * (default 0) Minimum number of special characters
     * in random string.
     */
    readonly minSpecial?: pulumi.Input<number>;
    /**
     * (default 0) Minimum number of uppercase alphabet
     * characters in random string.
     */
    readonly minUpper?: pulumi.Input<number>;
    /**
     * (default true) Include numeric characters in random
     * string.
     */
    readonly number?: pulumi.Input<boolean>;
    /**
     * Supply your own list of special characters to
     * use for string generation.  This overrides characters list in the special
     * argument.  The special argument must still be set to true for any overwritten
     * characters to be used in generation.
     */
    readonly overrideSpecial?: pulumi.Input<string>;
    /**
     * (default true) Include special characters in random
     * string. These are '!@#$%&*()-_=+[]{}<>:?'
     */
    readonly special?: pulumi.Input<boolean>;
    /**
     * (default true) Include uppercase alphabet characters
     * in random string.
     */
    readonly upper?: pulumi.Input<boolean>;
}
