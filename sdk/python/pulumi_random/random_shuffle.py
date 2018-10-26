# coding=utf-8
# *** WARNING: this file was generated by the Pulumi Terraform Bridge (tfgen) Tool. ***
# *** Do not edit by hand unless you're certain you know what you are doing! ***

import pulumi
import pulumi.runtime
from . import utilities

class RandomShuffle(pulumi.CustomResource):
    """
    The resource `random_shuffle` generates a random permutation of a list
    of strings given as an argument.
    """
    def __init__(__self__, __name__, __opts__=None, inputs=None, keepers=None, result_count=None, seed=None):
        """Create a RandomShuffle resource with the given unique name, props, and options."""
        if not __name__:
            raise TypeError('Missing resource name argument (for URN creation)')
        if not isinstance(__name__, basestring):
            raise TypeError('Expected resource name to be a string')
        if __opts__ and not isinstance(__opts__, pulumi.ResourceOptions):
            raise TypeError('Expected resource options to be a ResourceOptions instance')

        __props__ = dict()

        if not inputs:
            raise TypeError('Missing required property inputs')
        elif not isinstance(inputs, list):
            raise TypeError('Expected property inputs to be a list')
        __self__.inputs = inputs
        """
        The list of strings to shuffle.
        """
        __props__['inputs'] = inputs

        if keepers and not isinstance(keepers, dict):
            raise TypeError('Expected property keepers to be a dict')
        __self__.keepers = keepers
        """
        Arbitrary map of values that, when changed, will
        trigger a new id to be generated. See
        the main provider documentation for more information.
        """
        __props__['keepers'] = keepers

        if result_count and not isinstance(result_count, int):
            raise TypeError('Expected property result_count to be a int')
        __self__.result_count = result_count
        """
        The number of results to return. Defaults to
        the number of items in the `input` list. If fewer items are requested,
        some elements will be excluded from the result. If more items are requested,
        items will be repeated in the result but not more frequently than the number
        of items in the input list.
        """
        __props__['resultCount'] = result_count

        if seed and not isinstance(seed, basestring):
            raise TypeError('Expected property seed to be a basestring')
        __self__.seed = seed
        """
        Arbitrary string with which to seed the random number
        generator, in order to produce less-volatile permutations of the list.
        **Important:** Even with an identical seed, it is not guaranteed that the
        same permutation will be produced across different versions of Terraform.
        This argument causes the result to be *less volatile*, but not fixed for
        all time.
        """
        __props__['seed'] = seed

        __self__.results = pulumi.runtime.UNKNOWN
        """
        Random permutation of the list of strings given in `input`.
        """

        super(RandomShuffle, __self__).__init__(
            'random:index/randomShuffle:RandomShuffle',
            __name__,
            __props__,
            __opts__)

    def set_outputs(self, outs):
        if 'inputs' in outs:
            self.inputs = outs['inputs']
        if 'keepers' in outs:
            self.keepers = outs['keepers']
        if 'results' in outs:
            self.results = outs['results']
        if 'resultCount' in outs:
            self.result_count = outs['resultCount']
        if 'seed' in outs:
            self.seed = outs['seed']