# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import json
import warnings
import pulumi
import pulumi.runtime
from . import utilities, tables

class RandomPet(pulumi.CustomResource):
    keepers: pulumi.Output[dict]
    """
    Arbitrary map of values that, when changed, will
    trigger a new id to be generated. See
    the main provider documentation for more information.
    """
    length: pulumi.Output[float]
    """
    The length (in words) of the pet name.
    """
    prefix: pulumi.Output[str]
    """
    A string to prefix the name with.
    """
    separator: pulumi.Output[str]
    """
    The character to separate words in the pet name.
    """
    def __init__(__self__, resource_name, opts=None, keepers=None, length=None, prefix=None, separator=None, __name__=None, __opts__=None):
        """
        The resource `random_pet` generates random pet names that are intended to be
        used as unique identifiers for other resources.
        
        This resource can be used in conjunction with resources that have
        the `create_before_destroy` lifecycle flag set, to avoid conflicts with
        unique names during the brief period where both the old and new resources
        exist concurrently.
        
        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[dict] keepers: Arbitrary map of values that, when changed, will
               trigger a new id to be generated. See
               the main provider documentation for more information.
        :param pulumi.Input[float] length: The length (in words) of the pet name.
        :param pulumi.Input[str] prefix: A string to prefix the name with.
        :param pulumi.Input[str] separator: The character to separate words in the pet name.

        > This content is derived from https://github.com/terraform-providers/terraform-provider-random/blob/master/website/docs/r/pet.html.markdown.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if not resource_name:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(resource_name, str):
            raise TypeError('Expected resource name to be a string')
        if opts and not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        __props__['keepers'] = keepers

        __props__['length'] = length

        __props__['prefix'] = prefix

        __props__['separator'] = separator

        super(RandomPet, __self__).__init__(
            'random:index/randomPet:RandomPet',
            resource_name,
            __props__,
            opts)


    def translate_output_property(self, prop):
        return tables._CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return tables._SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

