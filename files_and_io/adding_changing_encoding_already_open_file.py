"""
This script shows how to add or change the unicode encoding of an already open file without closing
the file.

To add - Unicode encoding/decoding to an already existing file object that is opened
in binary mode - wrap it in a io.TextIOWrapper() object
"""
import urllib.request
import io
import sys

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u, encoding='utf-8')
text = f.read()

# To change the encoding of an already open text-mode file use detach() before replacing it
sys.stdout.encoding  # UTF-8
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
sys.stdout.encoding  # latin-1

# I/O is built a series of layers. See below
f = open('sample.txt', 'w')
f.buffer
f.buffer.new

"""
In this example - the io.TextIOWrapper is a text-handling layer that encodes
and decodes Unicode

BufferedWriter is a buffered IO layer that handles bianry

io.FileIO is a raw file representing the low level descriptor in the OS

Adding or changing the text encoding involves adding or changing the topmost io.TextIOWrapper layer

General rule of thumb is that it is not safe to manipulate the layers by accessing the attributes shown

detach() disconnects the topmost layer of a file and returns the next lower layer, after which
the top layer will no longer be usable
"""
f = open('sample.txt', 'w')
b = f.detach()
f.write('hello') # throws ValueError: underlying buffer has been detached

# Once detached, you can add new top layer to returned result as follows:
f = io.TextIOWrapper(b, encoding='latin-1')

# You can use the same technique to change the line handling, error policy or other aspects of file handling as follows:
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='ascii', errors='xmlcharrefreplace')
print('Jalape\u00f1o')  # non ascii n has been replaced by &#241; in the output
