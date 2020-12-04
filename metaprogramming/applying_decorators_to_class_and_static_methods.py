"""
This script shows how to apply a decorator to a class or static method

Applying decorators at class and static method level is easy, you
just need to make sure that decorators are applied prior to
@classmethod or @staticmethod
"""
import time
from functools import wraps
from abc import ABCMeta, abstractmethod


# A simple decorator
def timethis(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        r = func(*args, **kwargs)
        end = time.time()
        print(end - start)
        return r

    return wrapper


# Class illustrating application of decorator to different kinds of methods
class Spam:
    @timethis
    def instance_method(self, n):
        print(self, n)
        while n > 0:
            n -= 1

    @classmethod
    @timethis
    def class_method(cls, n):
        print(cls, n)
        while n > 0:
            n -= 1

    @staticmethod
    @timethis
    def static_method(n):
        print(n)
        while n > 0:
            n -= 1


"""
The order of the decorators is important if @timethis then @staticmethod is defined the 
static method will crash

In abstract base classes its important - the order of @classmethod and @abstractmethod matters
see example below
"""


class A(metaclass=ABCMeta):
    @classmethod
    @abstractmethod
    def method(cls):
        pass
