""""
This script shows how to replace infinite while loops (i.e whiles with a test condition)

An example of this involving I/O is as follows
"""
import sys

CHUNKSIZE = 8192


def reader(s):
    while True:
        data = s.recv(CHUNKSIZE)
        if data == b'':
            break
        process_data(data)


# This can be replaced using an iter() as follows
def reader(s):
    for chunk in iter(lambda: s.recv(CHUNKSIZE), b''):
        process_data(chunk)


# Below is an example using files:
f = open('/etc/passwd')
for chunk in iter(lambda: f.read(10), ''):
    n = sys.stdout.write(chunk)

"""
built-in iter() function optionally accepts a zero-argument callable
and sentinel(terminating) value as inputs. When this is used, it creates 
an iterator that repeatedly calls the supplied callable over and over
until it returns the value given as sentinel (terminator)

This works well with repeatedly called functions such as those involving I/O
for example - read data in chunks from sockets or files where you have to 
keep executing read() or recv() calls followed by end-of-file test.

This recipe takes those two features and combines them into a single iter() call.
The use of lambda is needed to create a callable that takes no
arguments, yet supplies the desired size argument to recv() or read()
"""
