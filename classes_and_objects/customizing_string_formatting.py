"""
This script shows how to build an object that supports
customized formatting through the format() function and string
method

To do this define the __format__() method on a class.
"""
_formats = {
    'ymd': '{d.year}-{d.month}-{d.day}',
    'mdy': '{d.month}/{d.day}/{d.year}',
    'dmy': '{d.day}/{d.month}/{d.year}'
}

class Date:
    def __init__(self, year, month, day):
        self.year = year
        self.month = month
        self.day = day

    def __format__(self, code):
        if code == '':
            code = 'ymd'
        fmt = _formats[code]
        return fmt.format(d = self)

# Instances of the Date class now support formatting operations
# Run in Python console
d = Date(2012, 12, 21)
format(d)
format(d, 'mdy')
'The date is {:ymd}'.format(d)
'The date is {"mdy}'.format(d)

"""
The __format__() method provides a hook into Python's 
string formatting functionallity. The interpretation is 
up to the class. There are some standard conventions
for formatting of the built-in types.
"""
