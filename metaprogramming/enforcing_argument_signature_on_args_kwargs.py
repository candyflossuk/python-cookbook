"""
This script shows how to check the passed arguments
to see if they match a specific signature when using
general purpose functions using kwargs and args.

To do this you can use the signature features in the 'inspect'
module. The classes to use are Signature and
Parameter.

Below an example of a function signature is shown
"""
from inspect import Signature, Parameter
import inspect

# Make a signature for a func(x, y=42, *, z=None)
parms = [
    Parameter("x", Parameter.POSITIONAL_OR_KEYWORD),
    Parameter("y", Parameter.POSITIONAL_OR_KEYWORD, default=42),
    Parameter("z", Parameter.KEYWORD_ONLY, default=None),
]

sig = Signature(parms)
print(sig)

# Bind signature to *args and **kwargs using bind()


def func(*args, **kwargs):
    bound_vales = sig.bind(*args, **kwargs)
    for name, value in bound_vales.arguments.items():
        print(name, value)


"""
The binding enforces the usual function calling rules
concerning args, defaults, dupes etc

Shown below is a more concrete example of enforcing
function signatures. The base class has a general
purpose verison of __init__(), but subclasses are 
expected to supply an expected signature
"""


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class Structure:
    ___signature__ = make_sig()

    def __init__(self, *args, **kwargs):
        bound_values = self.___signature__.bind(*args, **kwargs)
        for name, value in bound_values.arguments.items():
            setattr(self, name, value)


# Example use
class Stock(Structure):
    ___signature__ = make_sig("name", "shares", "price")


class Point(Structure):
    ___signature__ = make_sig("x", "y")


print(inspect.signature(Stock))

# This pattern helps build in argument checking into generic functions

"""
An alternative to the above - you can create signature objects
via a custom metaclass. 
"""


def make_sig(*names):
    parms = [Parameter(name, Parameter.POSITIONAL_OR_KEYWORD) for name in names]
    return Signature(parms)


class StructureMeta(type):
    def __new__(cls, clsname, bases, clsdict):
        clsdict["__signature__"] = make_sig(*clsdict.get("_fields", []))
        return super().__new__(cls, clsname, bases, clsdict)

class Structure(metaclass=StructureMeta):
    _fields = []
    def __init__(self, *args, **kwargs):
        bound_values = self.__signature__.bind(*args, **kwargs) for name, value in bound_values.arguments.items():
            setattr(self, name, value)

class Stock(Structure):
    _fields = ['name', 'shares', 'price']
