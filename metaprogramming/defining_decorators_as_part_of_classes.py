"""
This script shows how to define decorator classes inside a class definition
and apply these to other functions and methods.

The application of the decorator is important. Whether that be as an instance or
a class method.
"""
from functools import wraps


class A:
    # Decorator as an instance method
    def decorator1(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 1")
            return func(*args, **kwargs)

        return wrapper

    # Decorator as class method
    @classmethod
    def decorator2(cls, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            print("Decorator 2")
            return func(*args, **kwargs)

        return wrapper
