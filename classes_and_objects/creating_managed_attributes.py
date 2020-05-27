"""
This script shows how to carry out extra processing on the getting
or setting of an attribute

A A simple way to customize access is to define it as a property.
The code below adds simple type checking to an attribute
"""
import math


class Person:
    def __init__(self, first_name):
        self.first_name = first_name

    # Getter function
    @property
    def first_name(self):
        return self._first_name

    # Setter function
    @first_name.setter
    def first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._first_name = value

    # Deleter function (optional)
    @first_name.deleter
    def first_name(self):
        raise AttributeError("Cant delete attribute")


"""
All of the methods must have the same name. The setter an deleter decorators
wont be defined unless a @property is defined.

The property looks like a normal attribute but access automatically triggers
the getter setter and deleter methods

The data is stored in the _first_name attribute. Using the setter in the 
__init__ does the type checking for you. Properties can also be defined for 
existing get and set methods as shown below
"""


class Person:
    def __init__(self, first_name):
        self.set_first_name(first_name)

    # Getter function
    def get_first_name(self):
        return self._first_name

    # Setter function
    def set_first_name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")

        self._first_name = value

    def del_first_name(self):
        raise AttributeError("Cant delete attribute")

    fist_name = property(get_first_name, set_first_name, del_first_name)


"""
Dont write properties where extra validation is not required. 
You can also use properties to lazily calculate values on demand 
"""


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def area(self):
        return math.pi * self.radius ** 2

    @property
    def perimeter(self):
        return 2 * math.pi * self.radius
