"""
This script shows how to compare instances of a class using the standard
comparison operators - without writing special methods.

By using functools.total_ordering as a decorator you can simplify writing out every
single comparator method. You just need to define __eq__() and ONE other comparison
method such as __lt__,__le__,__gt__ etc. The decorator then fills in the rest
of the methods for you
"""
from functools import total_ordering


class Room:
    def __init__(self, name, length, width):
        self.name = name
        self.length = length
        self.width = width
        self.square_feet = self.length * self.width


@total_ordering
class House:
    def __init__(self, name, style):
        self.name = name
        self.style = style
        self.rooms = list()

    @property
    def living_space_footage(self):
        return sum(r.square_feet for r in self.rooms)

    def add_room(self, room):
        self.rooms.append(room)

    def __str__(self):
        return "{}: {} square foot {}".format(
            self.name, self.living_space_footage, self.style
        )

    def __eq__(self, other):
        return self.living_space_footage == other.living_space_footage

    def __lt__(self, other):
        return self.living_space_footage < other.living_space_footage


"""
In this example only __eq__ and __lt__ are provided to compare houses based 
on square footage.This is all that is required to make all of the comparisons work
"""
