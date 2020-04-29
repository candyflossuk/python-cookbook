"""
This script discusses the use and benefit of slots.

By default Python uses a dict to store an object's instance attributes. This helps
as it allows for arbitary new attributes at runtime.

For small classes with known attributes this can be a bottleneck. The dict
wastes RAM. Creating lots of objects therefore uses lots of RAM. Using
__slots__ tells Python not to use the dict and only allocate space for a fixed
set of attributes.
"""


# Example without slots
class MyClassNoSlots(object):
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.setup()
        # .....


class MyClassSlots(object):
    __slots__ = ['name', 'identifier']
    def __init__(self, name, identifier):
        self.name = name
        self.identifier = identifier
        self.setup()
        # ...

"""
The second example with slots will reduce Ram by anywhere between 40-50% - PyPy does these optimizations by default
"""
