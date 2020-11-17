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

# The usual rules of garbage collection often don't apply in Python

# Class to illustrate when deletion occurs


class Data:
    def __del__(self):
        print("Data.__del__")


# Node class involving a cycle
class Node:
    def __init__(self):
        self.data = Data()
        self.parent = None
        self.children = []

    # DO NOT DO THIS - this will leak memory as the cycle is defining its own __del__ method
    def __del__(self):
        del self.data
        del self.parent
        del self.children

    def add_child(self, child):
        self.children.append(child)
        child.parent = self


a = Data()
del a  # immediate delete

a = Node()
del a  # immediate delete

a = Node()
a.add_child(Node())
del a  # Not deleted

"""
From the above you can see the objects are deleted apart from where a cycle is involved.
A cycle in this case is where the parent references the child and vice versa.

The reason that the object is not simply deleted is that Python's garbage collection
is done using simple reference counting. When the reference count is 0 it is deleted.
For cyclic structures this does not occur.

To deal with cycles - there is a separate garbage collector that runs. A good rule here 
is that you cnanot guarantee when it is run, and therefore you never know when the 
cyclic data structures are collected. You can force GC 
"""
import gc

gc.collect()  # Force collection

# weak references eliminate ref cycles. This is a pointer that does not increase the ref count
a = Node()
a_ref = weakref.ref(a)

# To deref a weak reference you call it like a function
print(a_ref())

# By using weak reference you will find you don't get reference cycles and that gc occurs immediately
