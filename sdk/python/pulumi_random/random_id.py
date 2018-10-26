# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities

class RandomId(pulumi.CustomResource):
    """
    The resource `random_id` generates random numbers that are intended to be
    used as unique identifiers for other resources.
    
    This resource *does* use a cryptographic random number generator in order
    to minimize the chance of collisions, making the results of this resource
    when a 16-byte identifier is requested of equivalent uniqueness to a
    type-4 UUID.
    
    This resource can be used in conjunction with resources that have
    the `create_before_destroy` lifecycle flag set to avoid conflicts with
    unique names during the brief period where both the old and new resources
    exist concurrently.
    """
    def __init__(__self__, __name__, __opts__=None, byte_length=None, keepers=None, prefix=None):
        """Create a RandomId resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not byte_length:
            raise TypeError('Missing required property byte_length')
        elif not isinstance(byte_length, int):
            raise TypeError('Expected property byte_length to be a int')
        __self__.byte_length = byte_length
        """
        The number of random bytes to produce. The
        minimum value is 1, which produces eight bits of randomness.
        """
        __props__['byteLength'] = byte_length

        if keepers and not isinstance(keepers, dict):
            raise TypeError('Expected property keepers to be a dict')
        __self__.keepers = keepers
        """
        Arbitrary map of values that, when changed, will
        trigger a new id to be generated. See
        the main provider documentation for more information.
        """
        __props__['keepers'] = keepers

        if prefix and not isinstance(prefix, basestring):
            raise TypeError('Expected property prefix to be a basestring')
        __self__.prefix = prefix
        """
        Arbitrary string to prefix the output value with. This
        string is supplied as-is, meaning it is not guaranteed to be URL-safe or
        base64 encoded.
        """
        __props__['prefix'] = prefix

        __self__.b64 = pulumi.runtime.UNKNOWN
        __self__.b64_std = pulumi.runtime.UNKNOWN
        """
        The generated id presented in base64 without additional transformations.
        """
        __self__.b64_url = pulumi.runtime.UNKNOWN
        """
        The generated id presented in base64, using the URL-friendly character set: case-sensitive letters, digits and the characters `_` and `-`.
        """
        __self__.dec = pulumi.runtime.UNKNOWN
        """
        The generated id presented in non-padded decimal digits.
        """
        __self__.hex = pulumi.runtime.UNKNOWN
        """
        The generated id presented in padded hexadecimal digits. This result will always be twice as long as the requested byte length.
        """

        super(RandomId, __self__).__init__(
            'random:index/randomId:RandomId',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'b64' in outs:
            self.b64 = outs['b64']
        if 'b64Std' in outs:
            self.b64_std = outs['b64Std']
        if 'b64Url' in outs:
            self.b64_url = outs['b64Url']
        if 'byteLength' in outs:
            self.byte_length = outs['byteLength']
        if 'dec' in outs:
            self.dec = outs['dec']
        if 'hex' in outs:
            self.hex = outs['hex']
        if 'keepers' in outs:
            self.keepers = outs['keepers']
        if 'prefix' in outs:
            self.prefix = outs['prefix']