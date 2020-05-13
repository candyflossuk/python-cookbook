"""
This script shows how to write small one line functions. For example
you want to supply a short callback function for use with an operation
such as sort(), but you don't want to write a separate one-line
function using the def statement - instead you want an in-line function

These simple functions do nothing more than evaluate an expression.
And they can be replaced by a lambda expression
"""
add = lambda x, y: x + y
add(2, 3)  # 5

add("hello", "world")
# helloworld

# The use of lambda is the same as the following function definition
def add(x, y):
    return x + y


# Typically lambda is used in the context of another operation such as sorting or data reduction
names = ["Ross Humphrey", "David David", "Ray Ray"]
sorted(names, key=lambda name: name.split()[-1].lowert())

"""
Usage of lambda is highly restricted.
For example: only one expression can be specified, the result of which is the return value.
This means - no other language features can be included such as multiple statements, conditionals, iteration,
exception handling.
"""
