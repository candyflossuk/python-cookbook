"""
This script shows how to take a callable that has too many arguments and
causes an exception when called.

To reduce the number of arguments you should use functools.partial().
The partial() function allows you to assign fixed values to one or more of the
arguments , reducing the number of arguments that need to be supplied
in subsequent calls.

An example is shown below
"""
from functools import partial
import math
from socketserver import StreamRequestHandler, TCPServer


def spam(a, b, c, d):
    print(a, b, c, d)


# You can then use a partial() for fix certain argument values
s1 = partial(spam, 1)
s1(2, 3, 4)
# 1, 2, 3,4
s(4, 5, 6)
# 1, 4, 5, 6

s2 = partial(spam, d=42)
s2(1, 2, 3)
# 1, 2, ,3, 42

# you get the idea...

"""
Note - partial() fixes the values for certain arguments and returns a new 
callable as the result - this new callable still accepts the unassigned
arguments - combines them with the arguments given to partial() and passes
everything to the original function.

This recipe is related to the problem of making incompatible bits
of code work together

Here are some examples...

Example 1: list of points represented as tuples (x,y) you
could use the following function to compute the distance between
said points
"""
points = [(1, 2), (3, 4), (5, 6), (7, 8)]


def distance(p1, p2):
    x1, y1 = p1
    x2, y2 = p2
    return math.hypot(x2 - x1, y2 - y1)


"""
Now suppose you want to sort all of the points according to their
distance from some other point. The sort() method of list
accepts a key argument that can be used to customize how to sort
but it only works with functions that take 1 argument - i.e
distance() above is not suitable - but you could fix it with a partial
"""
pt = (4, 3)
points.sort(key=partial(distance, pt))

"""
As an extension of this idea - partial() can be used to tweak the argument
signatures of callback functions used in other libraries.

For example here is some code that uses multiprocessing to asynchronously 
compute a result which is handed to a callback function that accepts 
both the result and an optional logging argument
"""


def output_result(result, log=None):
    if log is not None:
        log.debug("Got: %r", result)


# A sample function
def add(x, y):
    return x + y


if __name__ == "__main__":
    import logging
    from multiprocessing import Pool
    from functools import partial

    logging.basicConfig(level=logging.DEBUG)
    log = logging.getLogger("test")
    p = Pool()
    p.apply_async(add, (3, 4), callback=partial(output_result, log=log))
    p.close()
    p.join()


# Consider this example of writing network servers
class EchoHandler(StreamRequestHandler):
    def handle(self):
        for line in self.rfile:
            self.wfile.write(b"GOT:" + line)


serv = TCPServer(("", 15000), EchoHandler)
serv.serve_forever()


# Now suppose you want to giveEchoHandler class __init__() method that accepts additional config arguments as so
class EchoHandler(StreamRequestHandler):
    # ack is added keyword-only arg. * args, ** kwargs are any normal params supplied
    def __init__(self, *args, ack, **kwargs):
        self.ack = ack
        super().__init__(*args, **kwargs)

    def handle(self) -> None:
        for line in self.rfile:
            self.wfile.write(self.ack + line)


# This can no longer be plugged into the TCPServer class- but you can use a partialto supple the value of ack
serv = TCPServer(("", 15000), partial(EchoHandler, ack=b"RECEIVED:"))
serv.serve_forever()

# Sometimes partials are replaced by lambdas e.g
points.sort(key=lambda p: distance(pt, p))
p.apply_async(add, (3, 4), callback=lambda result: output_result(result, log))
output_result(result, log)
serv = TCPServer(
    ("", 15000), lambda *args, **kwargs: EchoHandler(*args, ack=b"RECEIVED", **kwargs)
)
# Of course the above works - its just confusing as hell!
# partials are more explicit about what you arewanting to achieve
