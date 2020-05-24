"""
This script shows how to extend a closure with functions that allow the
inner variables to be accessed and modified.

Normally these are hidden to the outside world. However you can provide
access by writing accessor functions and attaching them to the closure
as function attributes as follows
"""
import sys


def sample():
    n = 0

    # closure function
    def func():
        print("n=", n)

    # Accessor methods for n
    def get_n():
        return n

    def set_n(value):
        nonlocal n
        n = value

    # Attach as function attributes
    func.get_n = get_n
    func.set_n = set_n
    return func


# Usage example
f = sample()
f()
f.set_n(10)
f()
f.get_n()

"""
There are two things that make this work:
nonlocal declaration - makes it possible to write functions that change inner variables
function attributes allow accessor methods to be attached to the closure function in a straightforward way- 
in that they look like instance methods.

An extension to this can be made to have closures emulate instances of a class. 
All you do is copy the inner functions over to the dictionary of an instance and return it
"""


class ClosureInstance:
    def __init__(self, locals=None):
        if locals is None:
            locals = sys._getframe(1).f_locals

        # Update instance dictionary with callables
        self.__dict__.update(
            (key, value) for key, value in locals.items() if callable(value)
        )

        # Redirect special methods
        def __len__(self):
            return self.__dict__["__len__"]()


# Example use
def Stack():
    items = []

    def push(item):
        items.append(item)

    def pop(item):
        items.pop()

    def __len__():
        return len(items)

    return ClosureInstance()


# This runs faster than a normal class definition (around 8% faster)

"""
This runs faster as access is streamlined to the instance variables. Closures are faster because there is no
self variable involved.

Although this can be used to replace classes in some instances - it is confusing to those who aren't aware 
of this pattern - so best to use it in special circumstances or where the pattern is well understood across
a team / explained in code as to why it is being used.
"""
