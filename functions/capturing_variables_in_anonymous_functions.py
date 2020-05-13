"""
This script shows how to capture values from anonymous functions (using lambda)
at the time of definition.
"""
x = 10
a = lambda y: x + y
x = 20
b = lambda y: x + y

"""
Looking at the above you may presume a and be when evaluated equal 20 and 30 however they are both
30, this is because x is not bound at definition time - instead it is bound at run time.

If you want an anonymous function to capture a value at the point of definition and keept it,
include the value as a default value as so
"""
x = 10
a = lambda y, x=x: x + y
x = 20
b = lambda y, x=x: x + y
a(10)
# 20
b(10)
# 30

"""
This problem often comes up in code thats trying to be too clever. i.e creating a list
of lambda expressions using list comprehension and expecting the lambda to remember the 
iteration variable at the time of definition.
"""
funcs = [lambda x: x + n for n in range(5)]
for f in funcs:
    print(f(0))
# prints 4 5's

# Instead you want to use
funcs = [lambda x, n=n: x + n for n in range(5)]
for f in funcs:
    print(f(0))
# prints 0,1,2,3,4 sequentially
