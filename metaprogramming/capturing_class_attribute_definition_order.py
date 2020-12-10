"""
This script shows how to automatically record the order
in which attributes and methods are defined in a class
body so that you can use it in various operations

This is easily accomplished through the use of a metaclass.
"""
from collections import OrderedDict

# A set of descriptors for various types
class Typed:
    _expected_type = type(None)

    def __init__(self, name=None):
        self._name = name

    def __set__(self, instance, value):
        if not isinstance(value, self._expected_type):
            raise TypeError("Expected " + str(self._expected_type))
        instance.__dict__[self._name] = value


class Integer(Typed):
    _expected_type = int


class Float(Typed):
    _expected_type = float


# Metaclass that uses an OrderedDict for class body
class OrderedMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        d = dict(clsdict)
        order = []

        for name, value in clsdict.items():
            if isinstance(value, Typed):
                value._name = name
                order.append(name)
        d["_order"] = order
        return type.__new__(cls, clsname, bases, d)

    """
    This is the part of the code that is important,
    the __prepare__ method is invoked immediately at the 
    start of a class definition. It must return 
    a mapping object to use when processing the class body.
    By returning an OrderedDict instead of a normal one
    the order is captured.
    """

    @classmethod
    def __prepare__(cls, clsname, bases):
        return OrderedDict()
