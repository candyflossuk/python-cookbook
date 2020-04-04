"""
This script shows how to write data in a file with gzip
or bz2 compression

To do this the gzip and bz2 modules can be used. Both provide
an alternative implementation of open() that can be used for
this purpose.
"""
import gzip
import bz2

# gzip compression - read
with gzip.open('somefile.gz', 'rt') as f:
    text = f.read()

# bz2 compression
with bz2.open('somefile.bz2', 'rt') as f:
    text = f.read()

# gzip compression - write
with gzip.open('somefile.gz', 'wt') as f:
    f.write(text)

# bz2 compression - write
with bz2.open('somefile.bz2', 'wt') as f:
    f.write(text)

"""
For the most part writing compressed data is straight forward. Be aware
you choose the correct file mode. If you do not specify a mode - the 
default mode is binary - which will break applications that expect text

Both gzip.open() and bz2.open() expect the same parameters as the built in open()
function, including encoding, errors, newline etc

When writing compressed data, the compression level can be optionally 
specified using the compress level keyword argument
"""
with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

# default level is 9 - highes level of compression (less performant)

"""
gzip.open() and bz2.open() can be layered on top of an existing file opened
in binary mode, this allows them to work with various file like objects
such as sockets, pipes and in memory files.
"""
f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
    text = g.read()
