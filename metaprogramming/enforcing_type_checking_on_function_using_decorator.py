"""
This script shows how to optionally enforce type checking of function arguments
as a kind of assertion or contract.

A short example below shows how to enforce type contracts on the input arguments of a function
"""
from inspect import signature
from functools import wraps


def typeassert(*ty_args, **ty_kwargs):
    def decorate(func):
        # If in optimized mode, disable type checking
        if not __debug__:
            return func

        # Map function argument names to supplied types
        sig = signature(func)
        bound_types = sig.bind_partial(*ty_args, **ty_kwargs).arguments

        @wraps(func)
        def wrapper(*args, **kwargs):
            bound_values = sig.bind(*args, **kwargs)
            # Enforce type assertions across supplied arguments
            for name, value in bound_values.arguments.items():
                if name in bound_types and not isinstance(value, bound_types[name]):
                    raise TypeError(
                        "Argument {} must be {}".format(name, bound_types[name])
                    )
                return func(*args, **kwargs)
            return wrapper

        return decorate


@typeassert(int, int)
def add(x, y):
    return x + y


"""
This script shows a number of useful concepts:
> __debug__ variable set to False results in the unmodified function being returned,
this is also the case when python executes in optimized mode with -o or -oo options

> inspect.signature() function allows you to extract a signature information from a callable

> bind_partial() is used to perform a partial binding of the supplied types to argument names

> Assertions do not get applied to unsupplied arguments with default values

> Decorator arguments can be used instead of function annotations. The decorator is 
very general purpose and can be used with any function - even ones with further annotations
"""
