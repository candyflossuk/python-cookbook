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


"""
Using __new__() would work, however __init__ is always called regardless of whether 
its cached or not.

The solution above also relies on global variables and a factory function the is decouple from the 
class definition - one way to solve this is to put the caching code into a separate manager class and 
glue it together like this
"""


class CachedSpamManager:
    def __int__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s

    def clear(self):
        self._cache.clear()


class Spam:
    manager = CachedSpamManager

    def __init__(self, name):
        self.name = name

    @staticmethod
    def get_spam(name):
        return Spam.manager.get_spam(name)


"""
This approach gives you greater flexibility. You can for example have different management schemes and attach 
these as replacements of the default caching mechanism. No code would need to be changed otherwise.

Another design consideration to think about is whether you want to leave the class definition exposed to the user.
If preventing this is important then you can take steps to avoid this - You can start the class name with an
underscore such as _Spam - OR you can give an even stronger hint - you can make __init__ raise an exception as so...
"""


class Spam:
    def __init__(self, *args, **kwargs):
        raise RuntimeError("Cannot instantiate directly")

    # Alternative Constructor
    @classmethod
    def _new(cls, name):
        self = cls.__new__(cls)
        self.name = name


# To use this modify the caching code to use Spam._new()
class CachedSpamManager:
    def __init__(self):
        self._cache = weakref.WeakValueDictionary()

    def get_spam(self, name):
        if name not in self._cache:
            s = Spam._new(name)
            self._cache[name] = s
        else:
            s = self._cache[name]
        return s
