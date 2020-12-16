"""
This script shows how to enforce coding conventions within your codebase.
One way in which this can be achieved is by using a metaclass.
"""
from inspect import signature
import logging


class MyMeta(type):
    def __new__(self, clsname, bases, clsdict):
        """
        :param clsname: name of class being defined
        :param bases: is tuple of base classes
        :param clsdict: is a class dictionary
        """
        return super().__new__(cls, clsname, bases, clsdict)


"""
To use a metaclass you incorporate it into a top level
base class and other objects inherit it
"""


class Root(metaclass=MyMeta):
    pass


class A(Root):
    pass


class B(Root):
    pass


"""
The following example shows a metaclass that checks
the definition of redefined methods to ensure they match 
the calling signature of the original method in the superclass
"""


class MatchSignatureMeta(type):
    def __init__(self, clsname, bases, clsdict):
        super().__init__(clsname, bases, clsdict)
        sup = super(self, self)
        for name, value in clsdict.items():
            if name.startswith("_") or not callable(value):
                continue

            # Get previous def and compare signature
            prev_dfn = getattr(sup, name, None)
            if prev_dfn:
                prev_sig = signature(prev_dfn)
                val_sig = signature(value)
                if prev_sig != val_sig:
                    logging.warning(
                        "Signature mismatch in %s. %s != %s",
                        value.__qualname__,
                        prev_sig,
                        val_sig,
                    )


class RootTwo(metaclass=MatchSignatureMeta):
    pass


class ATwo(RootTwo):
    def foo(self, x, y):
        pass

    def spam(self, x, *, z):
        pass


# Running the below will get you a warning
class BTwo(ATwo):
    def foo(self, a, b):
        pass

    def spam(self, x, z):
        pass
