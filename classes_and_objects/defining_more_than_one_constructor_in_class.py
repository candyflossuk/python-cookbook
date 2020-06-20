"""
This script shows how to write a class where you want users to be able to create instances
in more than the one way provided by __init__().

To define a class with more than one constructor, you should use a class method
"""
import time


class Date:
    # Primary constructor
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    # Alternate contructor
    @classmethod
    def today(cls):
        t = time.localtime()
        return cls(t.tm_year, t.tm_mon, t.tm_mday)


# To use this you can use
a = Date(2012, 12, 21)  # Primary
b = Date.today()  # Alternate
