# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['RandomPet']


class RandomPet(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 length: Optional[pulumi.Input[int]] = None,
                 prefix: Optional[pulumi.Input[str]] = None,
                 separator: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The resource `RandomPet` generates random pet names that are intended to be
        used as unique identifiers for other resources.

        This resource can be used in conjunction with resources that have
        the `create_before_destroy` lifecycle flag set, to avoid conflicts with
        unique names during the brief period where both the old and new resources
        exist concurrently.

        ## Example Usage

        The following example shows how to generate a unique pet name for an AWS EC2
        instance that changes each time a new AMI id is selected.

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_random as random

        server_random_pet = random.RandomPet("serverRandomPet", keepers={
            "ami_id": var["ami_id"],
        })
        server_instance = aws.ec2.Instance("serverInstance",
            ami=server_random_pet.keepers["amiId"],
            tags={
                "Name": server_random_pet.id.apply(lambda id: f"web-server-{id}"),
            })
        ```

        The result of the above will set the Name of the AWS Instance to
        `web-server-simple-snake`.

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will
               trigger a new id to be generated.
        :param pulumi.Input[int] length: The length (in words) of the pet name.
        :param pulumi.Input[str] prefix: A string to prefix the name with.
        :param pulumi.Input[str] separator: The character to separate words in the pet name.
        """
        if __name__ is not None:
            warnings.warn("explicit use of __name__ is deprecated", DeprecationWarning)
            resource_name = __name__
        if __opts__ is not None:
            warnings.warn("explicit use of __opts__ is deprecated, use 'opts' instead", DeprecationWarning)
            opts = __opts__
        if opts is None:
            opts = pulumi.ResourceOptions()
        if not isinstance(opts, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')
        if opts.version is None:
            opts.version = _utilities.get_version()
        if opts.id is None:
            if __props__ is not None:
                raise TypeError('__props__ is only valid when passed in combination with a valid opts.id to get an existing resource')
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

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            length: Optional[pulumi.Input[int]] = None,
            prefix: Optional[pulumi.Input[str]] = None,
            separator: Optional[pulumi.Input[str]] = None) -> 'RandomPet':
        """
        Get an existing RandomPet resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will
               trigger a new id to be generated.
        :param pulumi.Input[int] length: The length (in words) of the pet name.
        :param pulumi.Input[str] prefix: A string to prefix the name with.
        :param pulumi.Input[str] separator: The character to separate words in the pet name.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["keepers"] = keepers
        __props__["length"] = length
        __props__["prefix"] = prefix
        __props__["separator"] = separator
        return RandomPet(resource_name, opts=opts, __props__=__props__)

    @property
    @pulumi.getter
    def keepers(self) -> pulumi.Output[Optional[Mapping[str, Any]]]:
        """
        Arbitrary map of values that, when changed, will
        trigger a new id to be generated.
        """
        return pulumi.get(self, "keepers")

    @property
    @pulumi.getter
    def length(self) -> pulumi.Output[Optional[int]]:
        """
        The length (in words) of the pet name.
        """
        return pulumi.get(self, "length")

    @property
    @pulumi.getter
    def prefix(self) -> pulumi.Output[Optional[str]]:
        """
        A string to prefix the name with.
        """
        return pulumi.get(self, "prefix")

    @property
    @pulumi.getter
    def separator(self) -> pulumi.Output[Optional[str]]:
        """
        The character to separate words in the pet name.
        """
        return pulumi.get(self, "separator")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

