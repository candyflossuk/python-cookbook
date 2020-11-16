"""
Data structures that have cycles such as trees, graphs, observer patterns etc can sometimes experience
problems with regards to memory management.

When creating a tree structure where a parent points to its children and the children point back
to the parent - one of the links should be a weak reference using the weakref library.

So what is a weak reference? A weak reference allows an object to be referenced however if the
references to said object are ONLY weak references there is nothing stopping garbage collection
coming along and tidying them up.

An example usage of using weakref can be found below
"""
import weakref


class Node:
    def __init__(self, value):
        self.value = value
        self._parent = None
        self.children = []

    def __repr__(self):
        return "Node({!r:})".format(self.value)

    # property that manages the parent as a weak reference
    @property
    def parent(self):
        return self._parent if self._parent is None else self.parent()

    @parent.setter
    def parent(self, node):
        self._parent = weakref.ref(node)

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


# The parent can then quietly die - e.g
root = Node("parent")
cl = Node("child")
root.add_child(cl)
print(cl.parent)  # Node('parent')
del root
print(cl.parent)  # None  -  Rather than throwing
