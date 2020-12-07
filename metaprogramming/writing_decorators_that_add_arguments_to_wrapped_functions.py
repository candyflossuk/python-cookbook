"""
This script shows how to write a decorator that adds an
extra argument to the calling signature of a wrapped
function.

The added argument however does not interfere with the
existing calling conventions of the function.

Extra arguments are injected into the calling signature
using keyword only arguments
"""
from functools import wraps
import inspect


def optional_debug(func):
    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)

    return wrapper


# Usage example
@optional_debug
def spam(a, b, c):
    print(a, b, c)


spam(1, 2, 3)
# 1 2 3

spam(1, 2, 3, debug=True)
# Calling spam

# This pattern is useful when you have replication patterns

"""
This implementation is predicated on the fact that keyword
only args are easy to add to functions that also accept
*args and and **kwargs. 

The special case keyword param when removed - leaves only the 
positional and keyword arguments defined.

If the name of the keyword clashes with that of the 
wrapped function it will break - to combat this an 
additional check can be inserted
"""


def optional_debug_two(func):
    if "debug" in inspect.getargspec(func).args:
        raise TypeError("debug argument already defined")

    @wraps(func)
    def wrapper(*args, debug=False, **kwargs):
        if debug:
            print("Calling", func.__name__)
        return func(*args, **kwargs)

    sig = inspect.signature(func)

    parms = list(sig.parameters.values())
    parms.append(
        inspect.Parameter("debug", inspect.Parameter.KEYWORD_ONLY, default=False)
    )
    wrapper.__signature__ = sig.replace(parameters=parms)
    return wrapper
