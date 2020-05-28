"""
This script shows how to invoke a method in a parent class in place
of a method that has been overridden in a subclass

To do this use super()
"""


class A:
    def __init(self):
        self.x = 0

    def spam(self):
        print("A.spam")


class B:
    def __init__(self):
        super().__init__()
        self.y = 1

    def spam(self):
        print("B.spam")
        super().spam()


# Another common use is in code that overrides any of Python's special methods
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, item):
        return getattr(self._obj, name)

    # Delegate attribute assignment
    def __setattr__(self, key, value):
        if name.startswith("_"):
            super().__setattr__(key, value)
        else:
            setattr(self._obj, key, value)


"""
In this code - the implementation of __setattr__() includes a name check. 
super will work even though no explicit base class is listed.

When using inheritance be careful not to directly name the super class i.e Base.method instead 
use super() - this will ensure that methods called on the base class when using multiple 
inheritance only get called once. (see below)
"""


class Base:
    def __init__(self):
        print("Base.__init__")


class A(Base):
    def __init__(self):
        super().__init__()
        print("A.__init__")


class B(Base):
    def __init__(self):
        super().__init__()
        print("B.__init__")


class C(B, A):
    def __init__(self):
        super().__init__()
        print("C.__init__")


"""
Some rules of thumb -

Make sure all methods with the same name in an inheritence hierarchy have compatible calling signature.
(ie - same number of args, arg names)

This ensures that super() wont get tripped up if it tries to invoke a method on a class thats not a direct parent.

The topmost class should provide an implementation - so that the chain of lookups is terminated by an actual method
"""
