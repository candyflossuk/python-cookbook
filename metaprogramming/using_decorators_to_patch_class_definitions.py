"""
This script shows how to inspect or rewrite portions of a
class definition without using inheritance or metaclasses.

A class decorator can be used to do this.
"""


def log_getattribute(cls):
    # Gets the original implementation
    orig_getattribute = cls.__geattribute__

    # Make a new definition
    def new_get_attribute(self, name):
        print("getting:", name)
        return orig_getattribute(self, name)

    # Attach to the class and return
    cls.__getattribute__ = new_get_attribute
    return cls


# Example use
@log_getattribute
class A:
    def __init__(self, x):
        self.x = x

    def spam(self):
        pass
