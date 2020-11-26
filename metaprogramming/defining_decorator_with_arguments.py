"""
This script shows how to define a decorator function that takes arguments.

The following example shows how to build a logging decorator that accepts and argument to
specify the level of logging.
"""
from functools import wraps
import logging


def logged(level, name=None, message=None):
    """
    Add logging to a function.
    :param level: logging level
    :param name: name of the logger
    :param message: log message
    :return:
    """

    def decorator(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        return wrapper

    return decorator


# usage
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, "example")
def spam():
    print("Spam!")
