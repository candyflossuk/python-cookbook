"""
This script shows how to deal with a large number of instances taking up a large amount of 
memory.

For classes that serve as simple data structures you can
often greatly reduce the memory footprint of instances by
adding the __slots__ attribute to the class definition
"""


class Date:
    __slots__ = ["year", "month", "day"]

    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


"""
Defining __slots__ uses a more compact internal representation for instances.
Instead of a dictionary, instances are built around a small fixed sized array,
like a tuple or list.

Attribute names listed in __slots__ are internally mapped to specific indices
within this array. A side effect of using __slots__ is that you no longer
have a way of adding new attributes to instances - you are restricted by those
in the __slots__specifier.

You should resist the use of slots - as lots of python relies on the normal
dictionary implementation. 

__slots__ was not created for encapsulation purposes (although this is a side effect)
instead they were created as an optimization tool.

"""
