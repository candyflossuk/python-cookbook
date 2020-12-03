"""
This script shows how to wrap functions with a decorator - where
the result is a callable instance. This requires a decorator to work
both inside and outside of class definitions

This requires you to define a decorator with the __call__() and __get__()
methods.
"""
import types
from functools import wraps


class Profiled:
    def __init__(self, func):
        wraps(func)(self)
        self.ncalls = 0

    def __call__(self, *args, **kwargs):
        self.ncalls += 1
        return self.__wrapped__(*args, **kwargs)

    def __get__(self, instance, owner):
        if instance is None:
            return self
        else:
            return types.MethodType(self, instance)


# Usage is like a normal decorator both in and out of class
@Profiled
def add(x, y):
    return x + y


class Spam:
    @Profiled
    def bar(self, x):
        print(self, x)


"""
functools.wraps() is used to copy important metadata from the wrapped
function to the callable instance

__get__() is invoked as part of the descriptor protocol. It creates
a bound method object which supplies the self argument to the method.
It ensures that bound method objects get created properly. type.MethodType()
creates a bound method manually for use  if an instance is being used.
If the method is on the class the instance argument to __get__() is set to
None and the Profiled instance itself is returned.
"""
