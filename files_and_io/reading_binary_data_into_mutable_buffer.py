"""
This script shows how to read binary data directly into a mutable buffer without
any intermediate copying.

One use case for this could be you want to mutate the data in-place and write
it back out to a file

To read data into a mutable array use the readinto() method of files.
"""
import os.path


def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf


# Usage example - write a sample file
with open('sample.bin', 'wb') as f:
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin')
buf[0:5] = b'Hallo'  # Changes 'Hello' to 'Hallo'

with open('newsample.bin', 'wb') as f:
    f.write(buf)

"""
The readinto() method of files can be used to fill any preallocated array with data.
Including arrays created from array module or libraries like numpy.

readinto() fills the content of an existing buffer whereas read() allocates new objects and returns them.
You can use it to avoid making extra memory allocations.
If you are reading a binary file consisting of equally sized records you can write code as follows:
"""
record_size = 32  # Size of each record

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # Use the contents of buf

# memoryview is interesting - lets you make zero-copy slices of an existing buffer and change the contents.
m1 = memoryview(buf)
m2 = m1[-5:]
m2[:] = b'WORLD' # Will change the word 'World' to 'WORLD"

"""
You must always check the return code when using readinto() this will give you the number of bytes actually read.
If number of bytes is smaller than size of supplied buffer - it indicates missing or truncated data.

Be on the lookout for other 'into functions. Many modules in python have direct I/O or data access
that can be used to fill or alter the contents of arrays and buffers.
"""
