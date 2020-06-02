"""
This script shows how to extend the functionality of a property
defined in a parent class.
"""


class Person:
    def __init__(self, name):
        self.name = name

    # Getter function
    @property
    def name(self):
        return self._name

    # Setter function
    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise TypeError("Expected a string")
        self._name = name

    # Deleter function
    @name.deleter
    def name(self):
        raise AttributeError("Can't delete attribute")


# Example of a class inheriting from this class
class SubPerson(Person):
    @property
    def name(self):
        print("Getting name")
        return super().name

    @name.setter
    def name(self, value):
        print("Setting name to ", value)
        super(SubPerson, SubPerson).name.__set__(self, value)


# If you want to extend one of the methods of a property, use code as so
class SubPersonOneProp(Person):
    @Person.name.getter
    def name(self):
        print("Getting name")
        return super().name
