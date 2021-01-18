"""
This script shows how to split a module into multiple files, without breaking existing code by keeping
separate files unified as a single logical module.

This can be done by splitting a module into separate files - turning it into a package
"""


class A:
    def spam(self):
        print("A.spam")


class B:
    def bar(self):
        print("B.bar")


# The above can be split into two files (see mymodule) and gluing them together using __init__.py

"""
An extension of this is to use lazy imports - this involves a variation to __init__.py as demonstrated in
the 'lazy_mymodule'

One of the disadvantages here is that your inheritance and type checking might break
"""
