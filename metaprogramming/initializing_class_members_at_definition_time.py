"""
This script shows how to initialize parts of a class definition at time
of definition - rather than when the class instance is created.

Setup at time of definition is a use case for metaclasses. A metaclass
is triggered at point of definition - at which point you can
perform some steps.

The example below uses this idea to create classes similar to named
tuples from the collection modules
"""
import operator


class StructTupleMeta(type):
    def __init__(cls, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for n, name in enumerate(
            cls._fields
        ):  # This is valid - as it pulls _fields from the class
            setattr(cls, name, property(operator.itemgetter(n)))


class StructTuple(tuple, metaclass=StructTupleMeta):
    _fields = []

    def __new__(cls, *args):
        if len(args) != len(cls._fields):
            raise ValueError("{} arguments required".format(len(cls._fields)))
        return super().__new__(cls, args)


class Stock(StructTuple):
    _fields = ["name", "shares", "price"]


class Point(StructTuple):
    _fields = ["x", "y"]


# Example usage
s = Stock("ACME", 50, 91.1)
# This maps the values above to the fields in the meta class
s.name  # 'ACME'
s[0]  # 'ACME'
