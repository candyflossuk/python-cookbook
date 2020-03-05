"""
This script shows how to perform common text operations such as
stripping, searching and replacement on byte strings
"""
import re
import os

# Byte strings support most of the same built in operations as text strings
data = b'Hello World'
data[0:5]  # b'Hello'
data.startswith(b'Hello')  # True
data.split()  # [b'Hello', b'World']
data.replace(b'Hello', b'Hello Cruel')  # b'Hello Cruel World'

# Similar operations work with byte arrays
data = bytearray(b'Hello World')
data[0:5]  # bytearray(b'Hello')
data.startswith(b'Hello')  # True
data.split()  # [bytearray(b'Hello'), bytearray(b'World')]
data.replace(b'Hello', b'Hello World')

# You can apply regex pattern matching to byte strings.
data = b'FOO:BAR,SPAM'
re.split('[:,]', data)  # error as not string like object
re.split(b'[:,]', data)  # [b'FOO', b'BAR', b'SPAM']

# There are notable difference between string and bytes

# Indexing - byte strings produce ints not characters
a = 'Hello World'
a[0]  # 'H'
a[1]  # 'e'

b = b'Hello World'
b[0]  # 72
b[1]  # 101

# This can have an affect on apps that process byte-orientated data on char by char basis

# Byte strings don't provide a nice string representation unless first decoded
s = b'Hello World'
print(s)  # b'Hello World'
print(s.decode('ascii'))  # Hello World

# There are not string formatting operations available to byte strings
# To do formatting - use normal text strings and encoding

'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii')
# b'ACME              100     490.10'

# Using a byte string changes semantics of operations - especially the file system.
# If you supply a file name encoded as bytes it disables filename encoding/decoding

# Write a UTF-8 filename
with open('jalape\xf1o.txt', 'w') as f:
    f.write('spicy')

# Get a directory listing
os.listdir('.')  # Text string (names are decoded)
os.listdir(b'.')  # Byte string (names left as bytes)

"""
When using byte strings over normal strings (for performance improvement) 
take into account that the code may be messier. Byte strings don't play
well with the rest of python and all the manual encoding and decoding 
to get things correct may be cumbersome. PREFER STRINGS OVER BYTES
"""
