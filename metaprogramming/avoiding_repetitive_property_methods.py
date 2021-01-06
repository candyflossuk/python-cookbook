"""
This script shows how to avoid having to repeatedly define
methods that perform common tasks.
"""
from functools import partial


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("name must be a string")
        self._name = value

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if not isinstance(value, int):
            raise TypeError("age must be an int")
        self._age = value


"""
A lot of code is written to enforce type assertions. One approach 
to solve this repetition is to make a function that defines the property 
and returns it.
"""


def typed_property(name, expected_type):
    storage_name = "_" + name

    @property
    def prop(self):
        return getattr(self, storage_name)

    @prop.setter
    def prop(self, value):
        if not isinstance(value, expected_type):
            raise TypeError("{} must be a {}".format(name, expected_type))
        setattr(self, storage_name, value)
        return prop


# Usage
class Person:
    name = typed_property("name", str)
    age = typed_property("age", int)

    def __init__(self, name, age):
        self.name = name
        self.age = age


"""
The above recipe illustrates how inner functions / closures 
work like a macro. The typed_property() function is generating
the property code for you and returning the property object. 
The example can be tweaked in an interesting way using functools.partial()
"""

String = partial(typed_property, expected_type=str)
Integer = partial(typed_property, expected_type=int)


class Person:
    name = String("name")
    age = Integer("age")

    def __init__(self, name, age):
        self.name = name
        self.age = age
