"""
This script shows how to write a function that accepts any number of input arguments.

To write a function that accepts any number of positional arguments use * argument for example
"""
import html


def avg(first, *rest):
    return (first + sum(rest)) / (1 + len(rest))


# Usage
avg(1, 2)
avg(1, 2, 3, 4)

"""
In the example - rest is a tuple of all the extra positional arguments passed.
The code treats it as a sequence in performing subsequent calculations.

To accept any number of keyword arguments use ** argument
"""


def make_element(name, value, **attrs):
    keyvals = [' s="%s"' % item for item in attrs.items()]
    attr_str = "".join(keyvals)
    element = "<{name}{attrs}>{value}</{name}>".format(
        name=name, attrs=attr_str, value=html.escape(value)
    )
    return element


# Example
make_element("item", "Albatross", size="large", quantity=6)
make_element("p", "<spam>")

"""
attrs is a dictionary that holds the passed keyword arguments (if any)
If you want a function that can accept both any number of positional
and keyword arguments use * and ** together
"""


def anyargs(*args, **kwargs):
    print(args)
    print(kwargs)


"""
All positional arguments are place into a tuple args
all keyword arguments into a dictionary called kwargs

A * argument can only appear as the last positional argument in
a function definition

A ** argument can only appear as the last argument

Arguments can still appear after a * argument
"""


def a(x, *args, y):
    pass


def b(x, *args, y, **kwargs):
    pass
