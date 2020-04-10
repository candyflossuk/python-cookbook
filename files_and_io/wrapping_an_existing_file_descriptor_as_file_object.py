""""
This script shows how when given an integer file descriptor
that corresponds to an open I/O channel on the os (file, pipe, socket etc)
you want to wrap a higher-level Python file object around it.

What is a file descriptor?
An integer handle assigned by the os to refer to some kind of system I/O
channel.

If you have a file descriptor you can wrap a Python file object around it
using the open() function. However you simply supply the file descriptor as
the first argument instead of the filename.
"""
import os
import sys
from socket import socket, AF_INET, SOCK_STREAM

fd = os.open('somefile.txt', os.O_WRONLY | os.O_CREAT)

# Turn into a proper file
f = open(fd, 'wt')
f.write('hello world\n')
f.close()

"""
When the high level file object is closed or destroyed - the 
underlying file descriptor is also closed. If this is not 
the desired behaviour - supply the optional closefd=False arg to 
open()
"""
f = open(fd, 'wt', closefd=False)

"""
On unix - this technique of wrapping a file descriptor can be 
a means for putting a file-like interface on an existing 
I/O channel that was opened in a different way. Here is an example 
involving sockets.
"""


def echo_client(client_sock, addr):
    print('Got connection from', addr)

    # Make text-mode file wrappers for socket read/write
    client_in = open(client_sock.fileno(), 'rt', encoding='latin-1', closefd=False)
    client_out = open(client_sock.fileno(), 'wt', encoding='latin-1', closefd=False)

    # Echo lines back to the client using file I/O
    for line in client_in:
        client_out.write(line)
        client_out.flush()
    client_sock.close()


def echo_server(address):
    sock = socket(AF_INET, SOCK_STREAM)
    sock.bind(address)
    sock.listen(1)
    while True:
        client, addr = sock.accept()
        echo_client(client, addr)

# Above only works on unix - for cross platform use makefile - otherwise this is better for performance

"""
You can use this to make an alias that allows an already open file to be used 
in a different way than how it was first opened. Example below shows how to 
create a file object that allows you to emit binary data on stdout (opened in text mode typically)
"""
bstdout = open(sys.stdout.fileno(), 'wb', closefd=False)
bstdout.write(b'Hello World\n')
bstdout.flush()

"""
Although it is possible to wrap an existing file descriptor as a proper file
be aware that not all file modes may be supported and that certain kinds of file descriptors
may have side effects - in particular error handling, end of file conditions etc).
"""
