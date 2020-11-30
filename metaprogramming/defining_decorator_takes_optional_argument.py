"""
This script shows how to write a decorator that can be used without arguments or with optional arguments.
This adds complexity as there are differences in calling conventions between simple decorators and
those that take arguments.
"""
from functools import wraps, partial
import logging


def logged(func=None, *, level=logging.DEBUG, name=None, message=None):
    if func is None:
        return partial(logged, level=level, name=name, message=message)

    logname = name if name else func.__module__
    log = logging.getLogger(logname)
    logmsg = message if message else func.__name__

    @wraps(func)
    def wrapper(*args, **kwargs):
        log.log(level, logmsg)
        return func(*args, **kwargs)

    return wrapper


# Example usage
@logged
def add(x, y):
    return x + y


@logged(level=logging.CRITICAL, name="example")
def spam():
    print("Spam!")
