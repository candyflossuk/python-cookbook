"""
This script shows how to create an instance - but you want to bypass the execution
of __init__() - for some reason?

To do this you can use a bare uninitialized instance calling __new__()
"""
from time import localtime


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day


# How to create a Date instance without invoking __init__
d = Date.__new__(Date)
# The result is uninitialized - you then need to set the instance variables
data = {"year": 2012, "month": 8, "day": 29}

for key, value in data.items():
    setattr(d, key, value)

"""
The problem with bypassing __init__() is that when instances are being created 
in a non standard way - such as deserializing data or in the implementation
of a class method. The example below shows using an alternate constructor today()
"""


class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    @classmethod
    def today(cls):
        d = cls.__new__(cls)
        t = localtime()
        d.year = t.tm_year
        d.month = t.tm_mon
        d.day = t.tm_mday
        return d


"""
When creating instances in a non standard way - its best not to make assumptions about their 
implementation. Don't write code that manipulates the underlying instance __dict__.
Otherwise the code will break if the class uses __slots__, properties, or descriptors 
or other advanced techniques for that matter. Using setattr() the code is pretty general purpose
"""
