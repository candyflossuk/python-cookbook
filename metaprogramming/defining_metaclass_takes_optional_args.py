"""
This script shows how to define a metaclass that allows
class definitions to supply optional arguments,
to control or configure aspects of processing during
type creation
"""

from abc import ABCMeta, abstractmethod


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxsize=None):
        pass

    @abstractmethod
    def write(self, data):
        pass


# In custom metaclasses , additional keyword args can be supplied

"""
To support additional keyword args define them on
__prepare__
__new__
__init__

As follows:
"""


class MyMeta(type):
    # Optional
    @classmethod
    def __prepare__(cls, name, bases, *, debug=False, synchronize=False):
        return super().__prepare__(name, bases)

    # Required
    def __new__(cls, name, bases, ns, *, debug=False, synchronize=False):
        return super().__new__(cls, name, bases, ns)

    # Required
    def __init__(self, name, bases, ns, *, debug=False, synchronize=False):
        super().__init__(name, bases, ns)


"""
The extra arguments are passed to every method involvd. __prepare__ 
is called first and used to create the class namespace prior to the body
of any class definition being processed.

__new__ is used to instantiate the resulting type object. It is called after the 
class body has been fully executed.

__init__ is called last and used to perform any additional initialization steps.
"""
