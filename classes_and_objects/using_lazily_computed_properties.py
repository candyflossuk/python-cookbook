"""
This script shows how to define a read-nly attribute as a property
that is only computed on access.

Once accessed, you'd like the value cached and not recomputed on
each access

This can be done via a descriptor class
"""
import math


class lazyproperty:
    def __init__(self, func):
        self.func = func

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            value = self.func(instance)
            setattr(instance, self.func.__name__, value)
            return value


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @lazyproperty
    def area(self):
        print("Computing area")
        return math.pi * self.radius ** 2

    @lazyproperty
    def perimeter(self):
        print("Computing perimiter")
        return 2 * math.pi * self.radius


c = Cirlce(4.0)
c.area
# Computing area - i.e the value needs to be calculated the first time
# 50.2653....
c.area
# 50.2653....
# Notice how no 'Computing area' is printed

"""
The downside is the computed value is mutable after its created - to combat this a slightly 
less efficient (as shown below) can be put in place.
"""


def lazyproperty(fund):
    name = "_lazy_" + func.__name__

    @property
    def lazy(self):
        if hasattr(self, name):
            return getattr(self, name)
        else:
            value = func(self)
            setattr(self, name, value)
            return value

    return lazy


""" 
The disadvantage to this is that all get operations have to be routed
through the property's getter function. This is less efficient than
the original solution.
"""
