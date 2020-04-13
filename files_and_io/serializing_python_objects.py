"""
This script shows how to serialize a Python object into a byte stream - so that
you save it to a file, store it in a database, or transmit over the network.

The most common approach is to use the pickle module.
"""
import pickle
import math
import time
import threading


data = ...  # Some python object
f = open('somefile', 'wb')
pickle.dump(data, f)

# To dump an object to string use pickle.dumps()
s = pickle.dumps(data)

# To re-recreate an object from a byte stream use pickle.load or pickle.loads functions
f = open('somefile', 'rb')
data = pickle.loads(f)

# Restore from a string
data = pickle.loads(s)

"""
For most programs dump() and load() will be all you need to use pickle.

pickle - is a Python specific self describing data encoding. 
By self describing the serialized data contains info related to 
the start and end of each object as well as info about type.

For example...
"""
f = open('somedata', 'wb')
pickle.dump([1, 2, 3, 4], f)
pickle.dump('hello', f)
pickle.dump({'Apple', 'Pear', 'Banana'}, f)
f.close()
f = open('somedata', 'rb')
pickle.load(f)  # [1, 2, 3, 4]
pickle.load(f)  # 'hello'
pickle.load(f)  # {'Apple', 'Pear', 'Banana'}

"""
You can pickle functions, classes, instances but the resulting data only encodes
name references to the associated code objects. e.g...
"""
pickle.dumps(math.cos)  # b'\x80\x03cmath\ncos\nq\x00.'

"""
When the data is unpickled - it is assumed that all required source is available.
Modules, classes and functions will be imported as needed.
For apps where Python data is shared between interpreters this is a potential
maintainence issue.

WARNING: pickled.load() should not be used on untrusted data. Evil people
can write python that writes system commands - therefore only use it when 
interpreters can authenticate one another.

Some types of objects cannot be pickled - ones that have external system state.
You can get round this by providing:
> __getstate__()
> __setstate__()
Here is an example showing this:
"""


class Countdown:
    def __init__(self, n):
        self.n = n
        self.thr = threading.Thread(target=self.run)
        self.thr.daemon = True
        self.thr.start()

    def run(self):
        while self.n > 0:
            print('T-minus', self.n)
            self.n -= 1
            time.sleep(5)

    def __getstate__(self):
        return self.n

    def __setstate__(self, state):
        self.__init__(m)


# The following experiment involves some pickling
c = Countdown(30)
T-minus  # 30

# After a few moments
f = open('cstate.p', 'wb')
pickle.dump(c, f) # dumps countdown object to file
f.close()

# Restart python do the following
f = open('cstate.p', 'rb')
pickle.load(f)

# The thread will spring to life again

"""
pickle is not efficient for large data structures.
Your better saving bulk array data in file or more standard encoding if large.
Don't use pickle for long term storage - due to compatability issues.
"""
