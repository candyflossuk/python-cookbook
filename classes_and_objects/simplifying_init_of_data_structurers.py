"""
This script shows how to write a generalized
initialization of data structure of a single __init__()
function defined in a common base class.
"""
import math


class Structure:
    _fields = []

    def __init__(self, *args):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)


# Example class def
if __name__ == "__main__":

    class Stock(Structure):
        _fields = ["name", "shares", "price"]

    class Point(Structure):
        _fields = ["x", "y"]

    class Circle(Structure):
        _fields = ["radius"]

        def area(self):
            return math.pi * self.radius ** 2


"""
Supporting keyword arguments gives you a number of design options.
Choice 1 is to map the keyword arguments so that they only 
correspond to the attribute names specified in _fields
"""


class Structure:
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) > len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        # Set all of the positional arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the remaining keyword arguments
        for name in self._fields[len(args) :]:
            setattr(self, name, kwargs.pop(name))

        # Check for remaining unknown args
        if kwargs:
            raise TypeError("Invalid argument(s):{} ".format(",".join(kwargs)))


# Example use
if __name__ == "__main__":

    class Stock(Structure):
        _fields = ["name", "shares", "price"]


"""
Another possibility is to use keyword arguments as a means 
for adding additional attributes to the structure not specified in _fields
"""


class Structure:
    # Class variable that specifies expected fields
    _fields = []

    def __init__(self, *args, **kwargs):
        if len(args) != len(self._fields):
            raise TypeError("Expected {} arguments".format(len(self._fields)))

        # Set the arguments
        for name, value in zip(self._fields, args):
            setattr(self, name, value)

        # Set the additional arguments (if any)
        extra_args = kwargs.keys() - self._fields
        for name in extra_args:
            setattr(self, name, kwargs.pop(name))
        if kwargs:
            raise TypeError("Duplicate values for {}".format(",".join(kwargs)))


# Example use
if __name__ == "__main__":

    class Stock(Structure):
        _fields = ["name", "shares", "price"]

    s1 = Stock("ACME", 50, 91.1)

"""
If a subclass uses __slots__ or wraps an attribute with 
a property - directly accessing the property will break.

This also impacts docs and help features of IDEs.

You can also automatically initialize instance variables using
a utility function and a 'frame hack'
"""


def init_fromlocals(self):
    import sys

    locs = sys._getframe(1).f_locals
    for k, v in locs.items():
        if k != "self":
            setattr(self, k, v)


class Stock:
    def __init__(self, names, shares, price):
        init_fromlocals(self)
