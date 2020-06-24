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
from collections import defaultdict
from collections import OrderedDict


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


class SetOnceMappingMixin:
    """
    Only allow a key to be set once
    """

    __slots__ = ()

    def __setitem__(self, key, value):
        if key in self:
            raise KeyError(str(key) + " already set")
        return super().__setitem__(key, value)


class StringKeysMappingMixin:
    """
    Restrict keys to strings only
    """

    __slots__ = ()

    def __setitem__(self, key, value):
        if not isinstance(key, str):
            raise TypeError("keys must be strings")
        return super().__setitem__(key, value)


"""
By themselves these classes are useless. They are supposed 
to be mixed with other mapping classes through multiple inheritance.
"""


class LoggedDict(LoggedMappingMixin, dict):
    pass


d = LoggedDict()
d["x"] = 23
d["x"]


class SetOnceDefaultDict(SetOnceMappingMixin, defaultdict):
    pass


d = SetOnceDefaultDict(list)
d["x"].append(2)


class StringOrderedDict(StringKeysMappingMixin, SetOnceMappingMixin, OrderedDict):
    pass


"""
Some details:

Mixin classes are never meant to be instantiated directly

Mixin classes typically have no state of their own

USe of super() is essential to writing mixin classes. Using
super() delegates to the next class on the method resolution order.
The order in the mixin definition is important - and the order the 
mixins are called to check for implementations 
"""
