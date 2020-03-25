"""
This script shows how a custom container object that internally holds
a list, tuple or other iterable can be made to work with iteration.

To do this defined __iter__() method that delegates iteration to the internally held container
"""

class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, node):
        self._children.append(node)

    def __iter__(self):
        return iter(self._children)

# Usage example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    for ch in root:
        print(ch)

"""
In the above code __iter__() forwards the iteration request to the internally held _children attribute.

Pythons iterator protocol requires __iter__() to return a special iterator object that implements a __next__()
method to carry out the iteration. 
When iterating over the contents of a container - you don't need to worry about how this works, you 
just forward the iteration request along.
The use of iter() is a shortcut. iter(s) returns the underlying iterator by calling s__iter__(), like len
does for __len__() - this is purely a code cleanliness thing.
"""
