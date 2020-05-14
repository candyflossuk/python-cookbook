"""
This script shows how to simplify code where a class has only one function,
this can be done using closures. An example is shown below
"""
from urllib.request import urlopen


class UrlTemplate:
    def __init__(self, template):
        self.template = template

    def open(self, **kwargs):
        return urlopen(self.template.format_map(kwargs))


yahoo = UrlTemplate("http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
# then you have to call .open()


# A simple closure canreplace this
def urltemplate(template):
    def opener(**kwargs):
        return urlopen(template.format_map(kwargs))

    return opener()


yahoo = urltemplate("http://finance.yahoo.com/d/quotes.csv?s={names}&f={fields}")
# here you simpply refer to the variable

"""
The only reason you might have a single method class is to store 
additional state for use in the method.

Using an inner function or closure as shown in the solution 
is more elegant. A closure is just a function, but with 
an extra environment of the variables that used inside the function.

A key feature of a closure is that it remembers the environment in which
it was defined. Thus, the opener() function above remembers the value of the template
argument and uses it in subsequent calls.
"""
