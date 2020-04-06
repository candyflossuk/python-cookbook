"""
This script shows how to map a binary files into a mutable byte array - for random access
to its contents or to make in place modifications.

Use mmap module to memory map files. As shown below
"""
import os
import mmap


def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR)
    return mmap.mmap(fd, size, access=access)


# To use - you need a file with data, here is how this could be done
size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

# Now - here is how to use memory_map() to map the contents of this file
m = memory_map('data')
len(m)
m[0:10]
# Reassign a slice
m[0:11] = b'Hello World'
m.close()

# Verify the changes
with open(data, 'rb') as f:
    print(f.read(11))

# b'Hello World'

# mmap object returned by mmap() can also be used a context manager
# - in which the underlying file is closed automatically
with memory_map('data') as m:
    print(len(m))
    print(m[0:10])

m.closed  # True

"""
By default memory_map() opens a file for both reading and writing. Any modifications made to the 
data are copied back to the original file. 

If you need read_only access use mmap.ACCESS_READ for the access argument. Shown below
"""

filename = 'Sample.bin'
m = memory_map(filename, mmap.ACCESS_READ)

# To modify the data locally - when you don't want to write back to the original file use mmpa.ACCESS_COPY

m = memory_map(filename, mmap.ACCESS_COPY)

"""
Using mmap to map files into memory is efficient and elegant for randomly acessing the contents of the file.
Instead of using seek(), read() and write you can map to memory and use slicing operations.

The object exposed by mmap() looks like a byte array object - however you can interpret the data 
differently using a memoryview - as shown below.
"""

m = memory_map('data')
# Memoryview of unsigned integers
v = memoryview(m).cast('I')
v[0] = 7
m[0:4]
m[0:4] = b'\x07\x01\x00\x00'
v[0]

"""
Memory mapping a file does not cause the entire file to be mapped into memory - i.e it is not
copied into a memory buffer or array. Instead the OS reserves a section of virtual memory
for the files contents. As you access different regions of the file - they are read and mapped into
the virtual memory as needed. Parts not accessed are kept on disk! 

If more than one Python interpreter memory maps the same file - the resulting mmap object can be used 
to exchange data between interpreters. This is sometimes used as an alternative to pipes
and sockets.

There are differences between OS's when it comes to memory mapping that should be considered.
"""
