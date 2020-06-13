"""
This script shows how to implement a custom class
that mimics the behaviour of a common built-in
container type such as list or dict.

The collections library defines abstract base classes that
are useful when implementing custom container classes.

You need to implement all of the required methods -
or you get an error upon instantiation

Below is a simple example of a class that implements the
preceding methods to create a sequence where items are
always stored in a sorted order.
"""
import collections
import bisect


class SortedItems(collections.Sequence):
    def __init__(self, initial=None):
        self._items = sorted(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, item):
        return self._items[item]

    def __len__(self):
        return len(self._items)

    # Method for adding an item in the right location
    def add(self, item):
        bisect.insort(self._items, item)


"""
Inheriting from one of the abstract base classes in collections
ensures that your custom container implements all of the required 
methods expected of the container. However, this inheritance also
facilitates type checking.

Many of the abstract base classes in collections also provide
default implementations of common container methods. 
"""


class Items(collections.MutableSequence):
    def __init__(self, initial=None):
        self._items = list(initial) if initial is not None else []

    # Required sequence methods
    def __getitem__(self, item):
        print("Getting:", index)
        return self._items[index]

    def __setitem__(self, key, value):
        print("Setting:", key, value)
        self._items[key] = value

    def __delitem__(self, key):
        print("Deleting:", index)
        del self._items[index]

    def insert(self, index, value):
        print("Inserting", index, value)
        self._items.insert(index, value)

    def __len__(self):
        print("Len")
        return self._items
