"""
This script shows how to read and write encoded data as binary array of uniform structures into Python tuples

To work with binary - use the struct module. Below an example is shown that writes a list of Python
tuples out to binary file - encoding each as a structure using struct.
"""
from struct import Struct
from collections import namedtuple
import numpy as np

def write_records(records, format, f):
    """
    Write a sequence of tuples to a binary file of structures.
    """
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))


# Usage example
if __name__ == '__main__':
    records = [(1, 2.3, 4.5),
               (6, 7.8, 9.0),
               (12, 13.4, 56.7)]

    with open('data.b', 'wb') as f:
        write_records(records, '<idd', f)


# You can read the data back in using chunks
def read_records(format, f):
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)


# Usage
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        for rec in read_records('<idd', f):
            # process rec
            print(rec)


# To read the file entirely into a byte string with a single read and convert it piece by piece - use the following


def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset)
            for offset in range(0, len(data), record_struct.size))


# Usage
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()

    for rec in unpack_records('<idd', data):
        # Process rec
        print(rec)

"""
Common to use the struct module when dealing with binary data. 
<idd = Little endian 32 bit integer
< specifies the byte ordering
i,d,f are structure codes

An example of the pack and unpack method are shown below
"""
record_struct = Struct('<idd')
record_struct.size
record_struct.pack(1, 2.0, 3.0)
record_struct.unpack_from(_)
# (1, 2.0, 3.0)

"""
Code for reading binary structures involves some nice programming idioms.
read_records() function - iter() is used to make an iterator that returns 
fixed size chunks - this calls a user supplied callable 
until it returns a specified value - then it stops.
"""
f = open('data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')

for chk in chunks:
    print(chk)


# Iterables are nice because they allow you create records using a generator comprehension
def read_records(format, f):
    record_struct = Struct(format)
    while True:
        chk = f.read(record_struct.size)
        if chk == b'':
            break
        yield record_struct.unpack(chk)


# unpack_from extracts binary data from a larger binary array - without making any temp objects or memory copies.
# unpack() requires that you modify code to make lots of small slices and offset calculations as follows
def unpack_records(format, data):
    record_struct = Struct(format)
    return (record_struct.unpack(data[offset:offset + record_struct.size])
            for offset in range(0, len(data), record_struct.size))

# You can use namedtuple to unpack records and set attribute names
Record = namedtuple('Record', ['kind','x','y'])

with open('data.p', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))

for r in records:
    print(r.kind, r.x, r.y)

# When working with lots of data use numpy
f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')
records[0]
records[1]
