"""
This script shows how to perform I/O operations using raw filenmaes that have
not been decoded or encoded according to the default file name encoding.

By default filenames are encoded and decoded according to the text encoding
returned by sys.getfilesystemencoding()
"""
import os

sys.getfilesystemencoding()  # utf-8

# To bypass this specify a filename using a raw byte string instead

# Write a file using a unicode filename
with open('jalap\xf1o.txt', 'w') as f:
    f.write('Spicy!')

# Directory listing (decoded)
os.listdir('.') # [jalapeño.txt']

# Directory list ing (raw)
os.listdir(b'.')  # [b'jalapen\xcc\x83o.txt']

# Open file with raw filename
with open(b'jalapen\xcc\x83o.txt') as f:
    print(f.read())

# Spicy!

"""
In the last two operations - filename handling changes.

In normal circumstances you should not need to worry about the above. Some OS allow
a user to create files that dont conform to encoding rules. These may 
break applications that on the whole work.
"""
