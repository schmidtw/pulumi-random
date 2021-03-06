# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['RandomInteger']


class RandomInteger(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 max: Optional[pulumi.Input[int]] = None,
                 min: Optional[pulumi.Input[int]] = None,
                 seed: Optional[pulumi.Input[str]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The resource `RandomInteger` generates random values from a given range, described by the `min` and `max` attributes of a given resource.

        This resource can be used in conjunction with resources that have
        the `create_before_destroy` lifecycle flag set, to avoid conflicts with
        unique names during the brief period where both the old and new resources
        exist concurrently.

        ## Example Usage

        The following example shows how to generate a random priority between 1 and 50000 for
        a `aws_alb_listener_rule` resource:

        ```python
        import pulumi
        import pulumi_aws as aws
        import pulumi_random as random

        priority = random.RandomInteger("priority",
            keepers={
                "listener_arn": var["listener_arn"],
            },
            max=50000,
            min=1)
        main = aws.alb.ListenerRule("main",
            actions=[aws.alb.ListenerRuleActionArgs(
                target_group_arn=var["target_group_arn"],
                type="forward",
            )],
            listener_arn=var["listener_arn"],
            priority=priority.result)
        ```

        The result of the above will set a random priority.

        ## Import

        Random integers can be imported using the `result`, `min`, and `max`, with an optional `seed`. This can be used to replace a config value with a value interpolated from the random provider without experiencing diffs. Example (values are separated by a `,`)

        ```sh
         $ pulumi import random:index/randomInteger:RandomInteger priority 15390,1,50000
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will
               trigger a new id to be generated.
        :param pulumi.Input[int] max: The maximum inclusive value of the range.
        :param pulumi.Input[int] min: The minimum inclusive value of the range.
        :param pulumi.Input[str] seed: A custom seed to always produce the same value.
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
            if max is None and not opts.urn:
                raise TypeError("Missing required property 'max'")
            __props__['max'] = max
            if min is None and not opts.urn:
                raise TypeError("Missing required property 'min'")
            __props__['min'] = min
            __props__['seed'] = seed
            __props__['result'] = None
        super(RandomInteger, __self__).__init__(
            'random:index/randomInteger:RandomInteger',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            max: Optional[pulumi.Input[int]] = None,
            min: Optional[pulumi.Input[int]] = None,
            result: Optional[pulumi.Input[int]] = None,
            seed: Optional[pulumi.Input[str]] = None) -> 'RandomInteger':
        """
        Get an existing RandomInteger resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will
               trigger a new id to be generated.
        :param pulumi.Input[int] max: The maximum inclusive value of the range.
        :param pulumi.Input[int] min: The minimum inclusive value of the range.
        :param pulumi.Input[int] result: (int) The random Integer result.
        :param pulumi.Input[str] seed: A custom seed to always produce the same value.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["keepers"] = keepers
        __props__["max"] = max
        __props__["min"] = min
        __props__["result"] = result
        __props__["seed"] = seed
        return RandomInteger(resource_name, opts=opts, __props__=__props__)

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
    def max(self) -> pulumi.Output[int]:
        """
        The maximum inclusive value of the range.
        """
        return pulumi.get(self, "max")

    @property
    @pulumi.getter
    def min(self) -> pulumi.Output[int]:
        """
        The minimum inclusive value of the range.
        """
        return pulumi.get(self, "min")

    @property
    @pulumi.getter
    def result(self) -> pulumi.Output[int]:
        """
        (int) The random Integer result.
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter
    def seed(self) -> pulumi.Output[Optional[str]]:
        """
        A custom seed to always produce the same value.
        """
        return pulumi.get(self, "seed")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

