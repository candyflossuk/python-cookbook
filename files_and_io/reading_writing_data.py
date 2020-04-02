"""
This script shows how to read or write text data, in different text encodings

use the open() function with mode rt to read a text file
"""

# Read the entire file as a single string
with open('somefile.txt', 'rt') as f:
    data = f.read()

# Iterate over the lines of a file
with open('somefile.txt', 'rt') as f:
    for line in f:
        # Process
        print(line)

# To write use mode 'wt' - overriding any previous content
# Write chunks of text data

with open('somefile.txt', 'wt') as f:
    f.write(text1)
    f.write(text2)

# Redirected print statement
with open('somefile.txt', 'wt') as f:
    print(line1, file=f)
    print(line2, file=f)

"""
To append to the end of an existing file, use open() with mode 'at'.
By default files are read/writen using the system default text encoding,
as can be found in sys.getdefaultencoding(). On most machines this is 'utf-8'.
If you are using different encoding this should be provided
"""
with open('somefile.txt', 'rt', encoding='latin-1') as f:
    data = f.read()

"""
Some subtleties exist when reading and writing to files - that should be kept in mind 

using 'with' establishes a context in which the file will be used. When control
leaves the 'with' block the file will be closed automatically. You do not need 
to use the with statement but if you dont you must close the file as follows
"""
f = open('somefile.txt', 'rt')
data = f.read()
f.close()

"""
Another consideration to make is the recognition of new lines, which are 
different in unix and windows. By default Python operates in 
universal newline mode. In which all common newline conventions are recogniszed,
and new line chars are converted to \n while reading, and also as the output.
If you don't want this translation use newline='' argument as follows:
"""
with open('somefile.txt', 'rt', newline='') as f:
    data = f.read()

"""
The final issue is encoding in text files. When reading or writing a text file, you might 
encounter an encoding or decoding error. As follows:
"""
f = open('sample.txt', 'rt', encoding='ascii')
f.read()

# This could produce an UnicodeDecode error

"""
If you get a UnicodeDecode error it means you are not reading the file in the correct
encoding. You should carefully read the spec of whatever you are reading and 
check you are doing it right. If encoding errors are still a possibility you
can supply an optional errors argument to open() to deal with the errors - here are 
some examples of said schemes
"""
# Replace bad chars with Unicode U+fffd replacement char
f = open('sample.txt', 'rt', encoding='ascii', errors='replace')
f.read()
# Ignore bad chars entirely
f = open('sample.txt', 'rt', encoding='ascii', errors='ignore')
f.read()

# If you are fiddling - life may be more difficult than required. Always make sure you are using the right encoding.

# WHEN IN DOUBT USE UTF-8
