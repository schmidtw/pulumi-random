# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import warnings
import pulumi
import pulumi.runtime
from typing import Any, Mapping, Optional, Sequence, Union
from . import _utilities, _tables

__all__ = ['RandomString']


class RandomString(pulumi.CustomResource):
    def __init__(__self__,
                 resource_name: str,
                 opts: Optional[pulumi.ResourceOptions] = None,
                 keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
                 length: Optional[pulumi.Input[int]] = None,
                 lower: Optional[pulumi.Input[bool]] = None,
                 min_lower: Optional[pulumi.Input[int]] = None,
                 min_numeric: Optional[pulumi.Input[int]] = None,
                 min_special: Optional[pulumi.Input[int]] = None,
                 min_upper: Optional[pulumi.Input[int]] = None,
                 number: Optional[pulumi.Input[bool]] = None,
                 override_special: Optional[pulumi.Input[str]] = None,
                 special: Optional[pulumi.Input[bool]] = None,
                 upper: Optional[pulumi.Input[bool]] = None,
                 __props__=None,
                 __name__=None,
                 __opts__=None):
        """
        The resource `RandomString` generates a random permutation of alphanumeric
        characters and optionally special characters.

        This resource *does* use a cryptographic random number generator.

        Historically this resource's intended usage has been ambiguous as the original example
        used it in a password. For backwards compatibility it will
        continue to exist. For unique ids please use the `RandomId` resource, for sensitive
        random values please use the `RandomPassword` resource.

        ## Example Usage

        ```python
        import pulumi
        import pulumi_random as random

        random = random.RandomString("random",
            length=16,
            override_special="/@£$",
            special=True)
        ```

        ## Import

        Strings can be imported by just specifying the value of the string

        ```sh
         $ pulumi import random:index/randomString:RandomString test test
        ```

        :param str resource_name: The name of the resource.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will
               trigger a new id to be generated.
        :param pulumi.Input[int] length: The length of the string desired
        :param pulumi.Input[bool] lower: (default true) Include lowercase alphabet characters
               in random string.
        :param pulumi.Input[int] min_lower: (default 0) Minimum number of lowercase alphabet
               characters in random string.
        :param pulumi.Input[int] min_numeric: (default 0) Minimum number of numeric characters
               in random string.
        :param pulumi.Input[int] min_special: (default 0) Minimum number of special characters
               in random string.
        :param pulumi.Input[int] min_upper: (default 0) Minimum number of uppercase alphabet
               characters in random string.
        :param pulumi.Input[bool] number: (default true) Include numeric characters in random
               string.
        :param pulumi.Input[str] override_special: Supply your own list of special characters to
               use for string generation.  This overrides the default character list in the special
               argument.  The special argument must still be set to true for any overwritten
               characters to be used in generation.
        :param pulumi.Input[bool] special: (default true) Include special characters in random
               string. These are `!@#$%&*()-_=+[]{}<>:?`
        :param pulumi.Input[bool] upper: (default true) Include uppercase alphabet characters
               in random string.
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
            if length is None and not opts.urn:
                raise TypeError("Missing required property 'length'")
            __props__['length'] = length
            __props__['lower'] = lower
            __props__['min_lower'] = min_lower
            __props__['min_numeric'] = min_numeric
            __props__['min_special'] = min_special
            __props__['min_upper'] = min_upper
            __props__['number'] = number
            __props__['override_special'] = override_special
            __props__['special'] = special
            __props__['upper'] = upper
            __props__['result'] = None
        super(RandomString, __self__).__init__(
            'random:index/randomString:RandomString',
            resource_name,
            __props__,
            opts)

    @staticmethod
    def get(resource_name: str,
            id: pulumi.Input[str],
            opts: Optional[pulumi.ResourceOptions] = None,
            keepers: Optional[pulumi.Input[Mapping[str, Any]]] = None,
            length: Optional[pulumi.Input[int]] = None,
            lower: Optional[pulumi.Input[bool]] = None,
            min_lower: Optional[pulumi.Input[int]] = None,
            min_numeric: Optional[pulumi.Input[int]] = None,
            min_special: Optional[pulumi.Input[int]] = None,
            min_upper: Optional[pulumi.Input[int]] = None,
            number: Optional[pulumi.Input[bool]] = None,
            override_special: Optional[pulumi.Input[str]] = None,
            result: Optional[pulumi.Input[str]] = None,
            special: Optional[pulumi.Input[bool]] = None,
            upper: Optional[pulumi.Input[bool]] = None) -> 'RandomString':
        """
        Get an existing RandomString resource's state with the given name, id, and optional extra
        properties used to qualify the lookup.

        :param str resource_name: The unique name of the resulting resource.
        :param pulumi.Input[str] id: The unique provider ID of the resource to lookup.
        :param pulumi.ResourceOptions opts: Options for the resource.
        :param pulumi.Input[Mapping[str, Any]] keepers: Arbitrary map of values that, when changed, will
               trigger a new id to be generated.
        :param pulumi.Input[int] length: The length of the string desired
        :param pulumi.Input[bool] lower: (default true) Include lowercase alphabet characters
               in random string.
        :param pulumi.Input[int] min_lower: (default 0) Minimum number of lowercase alphabet
               characters in random string.
        :param pulumi.Input[int] min_numeric: (default 0) Minimum number of numeric characters
               in random string.
        :param pulumi.Input[int] min_special: (default 0) Minimum number of special characters
               in random string.
        :param pulumi.Input[int] min_upper: (default 0) Minimum number of uppercase alphabet
               characters in random string.
        :param pulumi.Input[bool] number: (default true) Include numeric characters in random
               string.
        :param pulumi.Input[str] override_special: Supply your own list of special characters to
               use for string generation.  This overrides the default character list in the special
               argument.  The special argument must still be set to true for any overwritten
               characters to be used in generation.
        :param pulumi.Input[str] result: Random string generated.
        :param pulumi.Input[bool] special: (default true) Include special characters in random
               string. These are `!@#$%&*()-_=+[]{}<>:?`
        :param pulumi.Input[bool] upper: (default true) Include uppercase alphabet characters
               in random string.
        """
        opts = pulumi.ResourceOptions.merge(opts, pulumi.ResourceOptions(id=id))

        __props__ = dict()

        __props__["keepers"] = keepers
        __props__["length"] = length
        __props__["lower"] = lower
        __props__["min_lower"] = min_lower
        __props__["min_numeric"] = min_numeric
        __props__["min_special"] = min_special
        __props__["min_upper"] = min_upper
        __props__["number"] = number
        __props__["override_special"] = override_special
        __props__["result"] = result
        __props__["special"] = special
        __props__["upper"] = upper
        return RandomString(resource_name, opts=opts, __props__=__props__)

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
    def length(self) -> pulumi.Output[int]:
        """
        The length of the string desired
        """
        return pulumi.get(self, "length")

    @property
    @pulumi.getter
    def lower(self) -> pulumi.Output[Optional[bool]]:
        """
        (default true) Include lowercase alphabet characters
        in random string.
        """
        return pulumi.get(self, "lower")

    @property
    @pulumi.getter(name="minLower")
    def min_lower(self) -> pulumi.Output[Optional[int]]:
        """
        (default 0) Minimum number of lowercase alphabet
        characters in random string.
        """
        return pulumi.get(self, "min_lower")

    @property
    @pulumi.getter(name="minNumeric")
    def min_numeric(self) -> pulumi.Output[Optional[int]]:
        """
        (default 0) Minimum number of numeric characters
        in random string.
        """
        return pulumi.get(self, "min_numeric")

    @property
    @pulumi.getter(name="minSpecial")
    def min_special(self) -> pulumi.Output[Optional[int]]:
        """
        (default 0) Minimum number of special characters
        in random string.
        """
        return pulumi.get(self, "min_special")

    @property
    @pulumi.getter(name="minUpper")
    def min_upper(self) -> pulumi.Output[Optional[int]]:
        """
        (default 0) Minimum number of uppercase alphabet
        characters in random string.
        """
        return pulumi.get(self, "min_upper")

    @property
    @pulumi.getter
    def number(self) -> pulumi.Output[Optional[bool]]:
        """
        (default true) Include numeric characters in random
        string.
        """
        return pulumi.get(self, "number")

    @property
    @pulumi.getter(name="overrideSpecial")
    def override_special(self) -> pulumi.Output[Optional[str]]:
        """
        Supply your own list of special characters to
        use for string generation.  This overrides the default character list in the special
        argument.  The special argument must still be set to true for any overwritten
        characters to be used in generation.
        """
        return pulumi.get(self, "override_special")

    @property
    @pulumi.getter
    def result(self) -> pulumi.Output[str]:
        """
        Random string generated.
        """
        return pulumi.get(self, "result")

    @property
    @pulumi.getter
    def special(self) -> pulumi.Output[Optional[bool]]:
        """
        (default true) Include special characters in random
        string. These are `!@#$%&*()-_=+[]{}<>:?`
        """
        return pulumi.get(self, "special")

    @property
    @pulumi.getter
    def upper(self) -> pulumi.Output[Optional[bool]]:
        """
        (default true) Include uppercase alphabet characters
        in random string.
        """
        return pulumi.get(self, "upper")

    def translate_output_property(self, prop):
        return _tables.CAMEL_TO_SNAKE_CASE_TABLE.get(prop) or prop

    def translate_input_property(self, prop):
        return _tables.SNAKE_TO_CAMEL_CASE_TABLE.get(prop) or prop

