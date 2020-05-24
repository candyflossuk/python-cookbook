"""
This script shows how, when using callback functions you can organize
your code so that callback functions look more like a normal sequence of
procedural steps.

Callbacks can be inlined into a function using generators and coroutines.
"""
from queue import Queue
from functools import wraps


def apply_async(func, args, *, callback):
    # Compute the result
    result = func(*args)

    # Invoke the callback with the result
    callback(result)


# The following supporting code - involves an Async class and an inlined_async decorator
class Async:
    def __init__(self, func, args):
        self.func = func
        self.args = args


def inlined_async(func):
    @wraps(func)
    def wrapper(*args):
        f = func(*args)
        result_queue = Queue()
        result_queue.put(None)
        while True:
            result = result_queue.get()
            try:
                a = f.send(result)
                apply_async(a.func, a.args, callback=result_queue.put)
            except StopIteration:
                break
        return wrapper


# The two fragements of code below will allow you to inline the callback steps using yield statements
def add(x, y):
    return x + y


@inlined_async
def test():
    r = yield Async(add, (2, 3))
    print(r)
    r = yield Async(add, ("hello", "world"))
    print(r)
    for n in range(10):
        r = yield Async(add, (n, n))
        print(r)
    print("Goodbye")


# Apart from the special decorator - and yield no callback functions appear anywhere

"""
Code involving callbacks, the whole point is that the current calculation will suspend and resume
at some point later in time.

WHen the calculation resumes, the callback will get executed to continue the processing.
apply_async() function illustrates the essential parts of executing the callback - although
in reality this is more complicated as you will have to deal with threads, processes, event handlers and more!)

A calculation will supend and resume - this maps to the execution model of a generator function. yield makes 
a generator function emit a value and suspend. 
Subsequent calls to __next__() or send() of a generator will make it start again

The core of this recipe is found in the inlined_async() decorator function. The key idea is that the 
decorator will step the generator function through all of its yield statements one at a time. 

To do this a result queue is created and populated with None. A loop is initiated in which a 
result is popped off the queue and sent to the generator.

This then advances to the next yield, an instance of Async is then recieved. The loop
then looks at the function and arguments, and initiates the async calcualtion aaply_async()
Instaed of using a normal callback the callback is set to the queue put() method.

At this point it is open as to what happens next. The main loop goes 
back to the top and simply executes a get() operation on teh queue. If data is present 
it must be the result placed by the put() if there is nothing the operation 
will block waiting for a result in teh future. How that happens depends on the 
implementation of apply_async() function.

If your doubtful that anything like this works - you can try it with the multiprocessing
library and have async operations executed in separate processes
"""

if __name__ == "__main__":
    import multiprocessing

    pool = multiprocessing.Pool()
    apply_async = pool.apply_async

    # Run the test function
    test()

"""
Hiding control flow behind generator functions is found in the standard library and third party 
packages. @contextmanager decorator in the contextlib does something similar - it glues the entry and exit from
a context manager together across a yield statement.
"""
