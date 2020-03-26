"""
This script shows how to build custom objects that support iteration. The script shows
an easy way to implement the iterator protocol.

The easiest way to do this is to use a generator function. This iterator traverses nodes in
a depth first pattern
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

    def depth_first(self):
        yield self
        for c in self:
            yield from c.depth_first()


# Example
if __name__ == '__main__':
    root = Node(0)
    child1 = Node(1)
    child2 = Node(2)
    root.add_child(child1)
    root.add_child(child2)
    child1.add_child(Node(3))
    child1.add_child(Node(4))
    child2.add_child(Node(4))

    for ch in root.depth_first():
        print(ch)

"""
Node(0)
Node(1)
Node(3)
Node(4)
Node(2)
Node(4)
"""

"""
This code is simple - it first yields itself and then iterates over each child yielding the items produced by the 
depth_first() method (using yield from)

Python's iterator protocol requires __iter__() to return a special iterator object that implements a __next__()
operation and uses a StopIteration exception to signal completion. This often messy - the implementation below
shows an alternative to depth_first() using an associated iterator class 
"""


class Node:
    def __init__(self, value):
        self._value = value
        self._children = []

    def __repr__(self):
        return 'Node({!r})'.format(self._value)

    def add_child(self, other_node):
        self._children.append(other_node)

    def __iter__(self):
        return iter(self._children)

    def depth_first(self):
        return DepthFirstIterator(self)


class DepthFirstIterator(object):
    """
    Depth first traversal
    """
    def __init__(self, start_node):
        self._node = start_node
        self._children_iter = None
        self._child_iter = None

    def __iter__(self):
        return self

    def __next__(self):
        # Return myself if just started, create iterator for children
        if self._children_iter is None:
            self._children_iter = iter(self._node)
            return self._node

        # If processing a child, return its next item
        elif self._child_iter:
            try:
                nextchild = next(self._child_iter)
                return nextchild
            except StopIteration:
                self._child_iter = None
                return next(self)

        # Advance to the next child and start iteration
        else:
            self._child_iter = next(self._children_iter).depth_first()
            return next(self)


"""
The DepthFirstIterator class works in the same way as the previous generator version, but its way more messy 
because the iterator has to maintain a lot of state about where it is in the iteration. 

INSTEAD - ALWAYS define your iterator as a generator!
"""
