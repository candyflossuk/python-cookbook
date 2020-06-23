"""
This script shows how to extend classes with mixins.

Generally - you have a collection of methods that
you would like to make available for extending the
functionality of other class definitions.

The distinction here is that the classes where methods
might be added are not related via inheritence. Thus,
you dont just attach the methods to a common base class

The solution is to use mixins. Sometimes mixin classes
have no value by themselves but once combined with other
classes offer some valuable functionality.

See below for an example...
"""


class LoggedMappingMixin:
    """
    Add logging to get/set/delete operations for debugging
    """

    __slots__ = ()

    def __getitem__(self, item):
        print("Getting " + str(item))
        return super().__getitem__(item)

    def __setitem__(self, key, value):
        print("Setting {} = {!r}".format(key, value))
        return super().__setitem__(key, value)

    def __delitem__(self, key):
        print("Deleting " + str(key))
        return super().__delitem__(key)
