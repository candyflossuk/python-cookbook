"""
This script shows how to define a class that serves as
an interface or abstract class from which you can perform
type checking and ensure that certain methods are implemented
in subclasses.
"""
from abc import ABCMeta, abstractmethod
import collections


class IStream(metaclass=ABCMeta):
    @abstractmethod
    def read(self, maxbytes=-1):
        pass

    @abstractmethod
    def write(self, data):
        pass


"""
A central feature of an abstract base class it that 
it cannot be instantiated directly. The following errors
"""
a = IStream()  # TypeError


# Instead it should be used as a base class for other classes
class SocketStream(IStream):
    def read(self, maxbytes=-1):
        ...

    def write(self, data):
        ...


"""
A major use of abstract classes is in code that 
wants to enforce an expected interface.

@abstractmethod can also be applied to static methods, class methods 
and properties. You just need to make sure you apply it in the 
proper sequence where @abstractmethod appears immediately before the function
definition.
"""


class A(metaclass=ABCMeta):
    @property
    @abstractmethod
    def name(self):
        pass

    @name.setter
    @abstractmethod
    def name(self, value):
        pass

    @classmethod
    @abstractmethod
    def method(cls):
        pass

    @staticmethod
    @abstractmethod
    def method2():
        pass


# You can use predefined ABCs to perform more generalized kinds of type checking

# Check if x is a sequence
if isinstance(x, collections.Sequence):
    ...

# Check x is iterable
if isinstance(x, collections.Iterable):
    ...
