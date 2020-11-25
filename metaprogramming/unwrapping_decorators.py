"""
This script shows how to 'undo' a decorator - gaining access to the original function

The following assumes that the decorator has been implemented using @wraps
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


@timethis
def add(x, y):
    return x + y


# To unwrap this decorator
orig_add = add.__wrapped__  # Pulls the original method from the wrapper
orig_add(3, 4)

"""
In the event that multiple decorators have been added - this behaviour is undocumented, as of Python 3.3 it 
will bypass all layers - but this may change
"""
