"""
When creating instances of a class - you want to return a cached reference to a
previous instance created wth the same arguments (if any).

This ensures that for one set of inputs there is only one instance of the class.
logging for example is a good example of this (see below for example)
"""
import logging
import weakref

a = logging.getLogger("foo")
b = logging.getLogger("bar")

c = logging.getLogger("foo")

# Given the above a != b but a = c

# To implement this - use a factory function separate than the class


class Spam:
    def __init__(self, name):
        self.name = name


# Caching support
_spam_cache = weakref.WeakValueDictionary()


def get_spam(name):
    if name not in _spam_cache:
        s = Spam(name)
        _spam_cache[name] = s
    else:
        s = _spam_cache[name]
    return s


"""å
Using __new__() would work, however __init__ is always called regardless of whether 
its cached or not.
"""
