"""
This script shows how to create an instance that delegates attribute access to an internally
held instance possibly as an alternative to inheritence or to implement a proxy object

Delegation is the programming pattern where the responsibility for implementing
a particular operation is handed off to different objects. In its simplest form it can be
represented as:
"""


class A:
    def spam(self, x):
        pass

    def foo(self):
        pass


class B:
    def __init__(self):
        self._a = A()

    def spam(self, x):
        # Delegate
        return self._a.spam(x)

    def foo(self):
        # Delegate to the internal self._a
        return self._a.foo()

    def bar(self):
        pass


# Where you have lots of methods to delegate you can use __getattr__()
class B:
    def __init__(self):
        self._a = A()

    def bar(self):
        pass

    def __getattr__(self, item):
        return getattr(self._a, item)


#  Another example of delegation is the implementation of proxies
#  that wrap around another object exposing its public attributes
class Proxy:
    def __init__(self, obj):
        self._obj = obj

    # Delegate attribute lookup to internal obj
    def __getattr__(self, item):
        print("getattr:", item)
        return getattr(self._obj, item)

    # Delegate attribute assignment
    def __setattr__(self, key, value):
        if key.startswith("_"):
            super().__setattr__(name, value)
        else:
            print("setattr:", name, value)
            setattr(self._obj, name, value)

    # Delegate attribute deletion
    def __delattr__(self, item):
        if item.startswith("_"):
            super().__delattr__(item)
        else:
            print("delattr:", item)
            delattr(self._obj, item)


# Usage example
class Spam:
    def __init__(self, x):
        self.x = x

    def bar(self, y):
        print("Spam.bar:", self.x, y)
