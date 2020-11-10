"""
This script shows how to call a method on an object
where the name is given as a string
"""
import math
import operator

# For simple cases - you can use getattr()
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return "Point({!r:},{!r:})".format(self.x, self.y)

    def distance(self, x, y):
        return math.hypot(self.x - x, self.y - y)


p = Point(2, 3)
d = getattr(p, "distance")(0, 0)

# An alternative is to use operator.methodcaller()
operator.methodcaller("distance", 0, 0)(p)

"""
operator.methodcaller is useful if you want to look up a 
method by name and supply the same args multiple times

Calling a method is two steps: 
> Attribute lookup 
> Function call

getattr() does the lookup and you just call the result as a
funciton

operator.methodcaller() creates a callable object,
fixes the arguments that are to be supplied.

This pattern is useful when emulating case statements
or the visitor pattern.
"""
