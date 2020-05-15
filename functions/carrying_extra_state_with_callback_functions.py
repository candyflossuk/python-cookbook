"""
This script shows how to carry extra state for use inside
of a callback function.

Callback functions are used across many libraries and frameworks,
in particular ones related to async processing.

An example of such function is shown below:
"""
from functools import partial

def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # invoke the callback with the result
    callback(result)

"""
In reality this code might do lots of advanced processing involving
threads, processes and timers. We are only focused on the invocation 
of the callback. Here is an example of how this code would be used
"""


def print_result(result):
    print('Got: ', result)


def add(x, y):
    return x + y


apply_async(add, (2,3), callback=print_result)
apply_async(add, ('hello','world'), callback=print_result)

"""
The callback only accepts a single arg - no other info 
is passed in. This can present problems if you want the 
callback to interact with other variables or parts of the 
environment

One way to carry extra information in a callback is to use
a bound-method instead of a simple function. The class below
keeps an internal sequence number that is incremented
"""


class ResultHandler:

    def __init__(self):
        self.sequence = 0

    def handler(self,result):
        self.sequence +=1
        print('[{}] Got: {{}'.format(self.sequence, result))


# To use this - you would create an instance and use the bound method handler as the callback
r = ResultHandler()
apply_async(add, (2,3), callback=r.handler)

# As an alternative to a class you can use a clousre to capture state


def make_handler():
    sequence = 0

    def handler(result):
        nonlocal sequence
        sequence += 1
        print('[{}] Got: {{}'.format(sequence, result))

    return handler


# Here is an example of this variant
handler = make_handler()
apply_async(add, (2,3), callback=handler)
# Sequence = 1
apply_async(add, (2,3), callback=handler)
# Sequence = 2

# You can sometimes use a co routine to accomplish the same thing
def make_hanlder():
    sequence = 0
    while True:
        result = yield
        sequence += 1
        print('[{}] Got: {{}'.format(sequence, result))

# For a co routine you would use its send() method as the callback
handler = make_handler()
next(handler) # Advance to the yield
apply_async(add, (2,3), callback=handler.send)
apply_async(add, (2,3), callback=handler.send)


# And last but not least you can also carry state into a callback using an extra arg and partial function
class SequenceNo:
    def __init__(self):
        self.sequence = 0

    def handler(result, seq):
        seq.sequence += 1
        print('[{}] GOt: {}'.format(seq.sequence, result))


seq = SequenceNo()
apply_async(add, (2,3), callback=partial(handler, seq=seq))

"""
There are two main approaches that are useful for capturing and carrying state.

Carry it aound on an instance, attached to a bound method

OR 

Carry it around in a closure 

Closures are more lightweight and natural. 

When using closures you need to make sure you are careful
about mutable variables. In the solution - the nonlocal
declaration is used to indicate that the sequence variable 
is being modified within the callback - without this 
you will get an error

The use of a co routine as a callback handler is closely related 
to the closure approach. It is cleaner - since its one function 
and you do not have to worry about the non local declaration.

The downside is they arent as well understood as other parts of 
Python. And the need to call next() is tricky. 

The use of the partial() is useful if all you need to do is pass extra values
into a callback. Instead of using partial() youll sometimes see the same 
thing accomplished with a lambda
"""
apply_async(add, (2,3), callback = lambda r: handler(r,seq))
