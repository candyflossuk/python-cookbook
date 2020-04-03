"""
This script shows how to read and write binary data such images,
sound files etc

To do this you can use the open() function with mode rb or wb
to read binary or write binary data.
"""
import array

# Read the entire file as a single byte string
with open('somefile.bin', 'rb') as f:
    data = f.read()

# Write binary data to a file
with open('somefile.bin', 'wb') as f:
    data = f.write(b'Hello World')

"""
When reading binary remember all data returned will be byte strings, not text strings.
When writing data must be exposed as bytes (byte string, bytearray objects etc)

When reading binary data, the subtle semantic difference between byte strings and text
strings pose a potential gotcha - beware indexing and iteration return integer byte
values instead of byte strings. Example shown below:
"""
# Text string
t = 'Hello World'
t[0] # 'H'

for c in t:
    print(c)
"""
H
e
l
l
o
 
W
o
r
l
d
"""

# Byte String
b = b'Hello World'
b[0]
for c in b:
    print(c)
"""
72
101
108
108
111
32
87
111
114
108
100
"""

# To read or write text from binary=model file - remember to encode or decode it
with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

# I/O objects such as arrays and C structures can be used for writing without any conversion to a bytes object
nums = array.array('i', [1, 2, 3, 4])
with open('data.bin', 'wb') as f:
    f.write(nums)

"""
This applies to any object that implements the 'buffer' interface, which directly exposes and underlying memory 
buffer to operations that can work with it. Writing binary is one of these operations.

Objects allow binary data to be directly read into their underlying memory using readinto() method of files
"""
a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a)

# NOTE: use care with this technique as its platform specific and may depend on word size and ordering
# i.e big endian and little endian
