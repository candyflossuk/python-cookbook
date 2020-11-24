"""
This script shows how to pull the function metadata thru
a decorator. To do this you must always apply the @wraps
decorator from functools to the underlying wrapper
"""
import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports execution time
    :param func:
    :return:
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(func.__name__, end - start)
        return result

    return wrapper


"""
Copying decorator metadata is an important part of 
writing decorators. If you don't use @wraps the 
decorated function loses all sorts of useful info. 
Some examples include __name__, __doc__, __annotations__

An important feature of @wraps is that it makes the 
wrapped function available to you via the __wrapped__
attribute

This allows the decorated functions properly expose
the underlying signature of the wrapped function.
"""
