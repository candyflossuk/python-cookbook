"""
Metaprogramming is about creating functions and classes whose goal is to manipulate code (modifying, generating
or wrapping existing code.

This script file shows how to put a wrapper around a function to add extra processing to said function (e.g
logging, timing, etc)

This is done be defining a decorator function
"""
import time
from functools import wraps


def timethis(func):
    """
    Decorator that reports the execution time
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


# Example usage
@timethis
def countdown(n):
    """
    Counts down
    :param n:
    :return:
    """
    while n > 0:
        n -= 1


countdown(100000)  # prints time taken inline

"""
A decorator is a function that accepts a function as input and returns a new function as output. Build in 
decorators such as @staticmethod, @classmethod and @property work in the same way

The code inside a decorator normally follows this design:
> new function that accepts and arguments using *args and **kwargs
> Inside you place a call to the original input function and return the result
> Along side you add your own code

Generally they dont alter the calling signature or return value of the function being wrapped.
"""
