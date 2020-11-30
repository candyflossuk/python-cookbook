"""
This script shows how to write a decorator function that wraps a function
with user adjustable arguments that can be used to control the behaviour
of the decorator at runtime

It introduces accessor functions that change the internal variables through the use of
nonlocal variables. The functions are then attached to the wrapper function as function
attributes.
"""
from functools import wraps, partial
import logging


# Utility decorator to attach a function as an attribute of obj
def attach_wrapper(obj, func=None):
    if func is None:
        return partial(attach_wrapper, obj)
    setattr(obj, func.__name__, func)
    return func


def logged(level, name=None, message=None):
    """
    Add logging to a function.
    :param level: logging level
    :param name: logger name
    :param message: log message
    :return:
    """

    def decorate(func):
        logname = name if name else func.__module__
        log = logging.getLogger(logname)
        logmsg = message if message else func.__name__

        @wraps(func)
        def wrapper(*args, **kwargs):
            log.log(level, logmsg)
            return func(*args, **kwargs)

        # Attach setter functions
        @attach_wrapper(wrapper)
        def set_level(newlevel):
            nonlocal level
            level = newlevel

        @attach_wrapper(wrapper)
        def set_message(newmsg):
            nonlocal logmsg
            logmsg = newmsg

        return wrapper

    return decorate


# Example use
@logged(logging.DEBUG)
def add(x, y):
    return x + y


@logged(logging.CRITICAL, "example")
def spam():
    print("Spam!")


"""
The key to this recipe lies in the accessor functions (set_message and set_level)
that gets attached to the wrapper attributes. 

Each accessor allows internal params to be adjusted through the use of nonlocal
assignments

A nice feature is that accessor functions will propogate through multiple levels
of decoration (if they use @functools.wraps).
"""
