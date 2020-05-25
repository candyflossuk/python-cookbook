"""
This script shows how to encapsulate 'private' data on instances of a class
where pythons lack of control access makes this difficult.

Python programmers are relied on to observe certain naming conventions concerning
the intended usage of data and methods.

The first is that any name starting with an '_' is assumed to be internal to the
implementation
"""


class A:
    def __init__(self):
        self._internal = 0
        self.public = 1

    def public_method(self):
        print("public")

    def _internal_method(self):
        print("internal")


"""
Underscores are also used for naming module names and module-level functions.
If you see a module name starting with a leading _ its internal implementation.
Likewise module-level functions like sys._getframe() should be used with caution.

Double underscores are used to mangle the name to something else. Specifically the private
attributes in the following class get renamed to _B__private and _B__private_method. This
is so methods cannot be overriden via inheritance.
"""


class B:
    def __init__(self):
        self.__private = 0

    def __private_method(self):
        print("private")

    def public_method(self):
        self.__private_method()


class C(B):
    def __init__(self):
        super().__init__()
        self.__private = 1  # Does not override B.__private

    def __private_method(self):
        # Also does not override __private_method
        print("No overriding here")


"""
Use trailing underscores to avoid name clashes with internal variable names
"""
