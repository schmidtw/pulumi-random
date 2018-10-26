// *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "./utilities";

/**
 * The resource `random_pet` generates random pet names that are intended to be
 * used as unique identifiers for other resources.
 * 
 * This resource can be used in conjunction with resources that have
 * the `create_before_destroy` lifecycle flag set, to avoid conflicts with
 * unique names during the brief period where both the old and new resources
 * exist concurrently.
 */
export class RandomPet extends pulumi.CustomResource {
    /**
     * Get an existing RandomPet resource's state with the given name, ID, and optional extra
     * properties used to qualify the lookup.
     *
     * @param name The _unique_ name of the resulting resource.
     * @param id The _unique_ provider ID of the resource to lookup.
     * @param state Any extra arguments used during the lookup.
     */
    public static get(name: string, id: pulumi.Input<pulumi.ID>, state?: RandomPetState): RandomPet {
        return new RandomPet(name, <any>state, { id });
    }

    /**
     * Arbitrary map of values that, when changed, will
     * trigger a new id to be generated. See
     * the main provider documentation for more information.
     */
    public readonly keepers: pulumi.Output<{[key: string]: any} | undefined>;
    /**
     * The length (in words) of the pet name.
     */
    public readonly length: pulumi.Output<number | undefined>;
    /**
     * A string to prefix the name with.
     */
    public readonly prefix: pulumi.Output<string | undefined>;
    /**
     * The character to separate words in the pet name.
     */
    public readonly separator: pulumi.Output<string | undefined>;

    /**
     * Create a RandomPet resource with the given unique name, arguments, and options.
     *
     * @param name The _unique_ name of the resource.
     * @param args The arguments to use to populate this resource's properties.
     * @param opts A bag of options that control this resource's behavior.
     */
    constructor(name: string, args?: RandomPetArgs, opts?: pulumi.CustomResourceOptions)
    constructor(name: string, argsOrState?: RandomPetArgs | RandomPetState, opts?: pulumi.CustomResourceOptions) {
        let inputs: pulumi.Inputs = {};
        if (opts && opts.id) {
            const state: RandomPetState = argsOrState as RandomPetState | undefined;
            inputs["keepers"] = state ? state.keepers : undefined;
            inputs["length"] = state ? state.length : undefined;
            inputs["prefix"] = state ? state.prefix : undefined;
            inputs["separator"] = state ? state.separator : undefined;
        } else {
            const args = argsOrState as RandomPetArgs | undefined;
            inputs["keepers"] = args ? args.keepers : undefined;
            inputs["length"] = args ? args.length : undefined;
            inputs["prefix"] = args ? args.prefix : undefined;
            inputs["separator"] = args ? args.separator : undefined;
        }
        super("random:index/randomPet:RandomPet", name, inputs, opts);
    }
}

/**
 * Input properties used for looking up and filtering RandomPet resources.
 */
export interface RandomPetState {
    /**
     * Arbitrary map of values that, when changed, will
     * trigger a new id to be generated. See
     * the main provider documentation for more information.
     */
    readonly keepers?: pulumi.Input<{[key: string]: any}>;
    /**
     * The length (in words) of the pet name.
     */
    readonly length?: pulumi.Input<number>;
    /**
     * A string to prefix the name with.
     */
    readonly prefix?: pulumi.Input<string>;
    /**
     * The character to separate words in the pet name.
     */
    readonly separator?: pulumi.Input<string>;
}

/**
 * The set of arguments for constructing a RandomPet resource.
 */
export interface RandomPetArgs {
    /**
     * Arbitrary map of values that, when changed, will
     * trigger a new id to be generated. See
     * the main provider documentation for more information.
     */
    readonly keepers?: pulumi.Input<{[key: string]: any}>;
    /**
     * The length (in words) of the pet name.
     */
    readonly length?: pulumi.Input<number>;
    /**
     * A string to prefix the name with.
     */
    readonly prefix?: pulumi.Input<string>;
    /**
     * The character to separate words in the pet name.
     */
    readonly separator?: pulumi.Input<string>;
}