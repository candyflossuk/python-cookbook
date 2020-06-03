"""
This script shows how to create a new kind of instance attribute type with extra
functionallity such as type checking

To do this - define the functionality in the form of a descriptor class
"""

# Descriptor attribute for an integer type checked attribute
class Integer:
    def __init__(self, name):
        self.name = name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, int):
            raise TypeError("Expected an int")
        instance.__dict__[self.name] = value

    def __delete__(self, instance):
        del instance.__dict__[self.name]


"""
A descriptor is class that implements get,set and delete.
These methods work by receiving an instance as input.
The underlying dictionary of the instance is then manipulated.

To use a descriptor, instances of the descriptor are placed into
a class definition as class variables.
"""


class Point:
    x = Integer("x")
    y = Integer("y")

    def __init__(self, x, y):
        self.x = x
        self.y = y


# Doing this, all access to the descriptor attributes (e.g x / y) are captured by __get__,__set__ and __delete__
p = Point(2, 3)
p.x  # Calls Point.x__get__(p, Point)
p.y = 5  # Calls Point.y.__set__(p, 5)

"""
Descriptors provide the underlying magic for most of Pythons class features, including
@classmethod, @staticmethod, @property and __slots__

By defining a descriptor - you capture core instance operations at a low level
and can customize what they do. Descriptors can ONLY be defined at the class level
not at an instance level.

Descriptors are one component of a larger programming framework using decorators
and metaclasses. Their use may be hidden out of sight. Descriptors should not 
be used for just one attribute (properties are better for this). Descriptors are more useful
where there will be a lot of code reuse - for example you want to use the functionality
provided by the descriptor in 100s of places in your code - or as a library.
"""


# Here is another example of advanced descriptor-based code
class Typed:
    def __init__(self, name, expected_type):
        self.name = name
        self.expected_type = expected_type

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return instance.__dict__[self.name]

    def __set__(self, instance, value):
        if not isinstance(value, self.expected_type):
            raise TypeError("Expected " + str(self.expected_type))

    def __delete__(self, instance):
        del instance.__dict__[self.name]


# Class decorator that applies it to selected attributes
def typeassert(**kwargs):
    def decorate(cls):
        for name, expected_type in kwargs.items():
            # Attached a Typed descriptor to the class
            setattr(cls, name, Typed(name, expected_type))
            return cls

    return decorate


# Example use
@typeassert(name=str, shares=int, price=float)
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price
