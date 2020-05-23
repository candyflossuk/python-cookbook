"""
This script shows how to make objects support the context management protocol
(the with statement)

In order to make an object compatible with the with statement you need to implement
__enter__() and __exit__() methods.
"""
from socket import socket, AF_INET, SOCK_STREAM
from functools import partial


class LazyConnection:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.sock = None

    def __enter__(self):
        if self.sock is not None:
            raise RuntimeError("Already connected")
        self.sock = socket(self.family, self.type)
        self.sock.connect(self.address)
        return self.sock

    def __exit__(self, exc_ty, exc_val, tb):
        self.sock.close()
        self.sock = None


"""
The key feature of the class is that it represents a network connection - it 
does not however do anything up front - instead the connection is establish 
and closed using a with statement
"""
conn = LazyConnection(("www.python.org", 80))
# connection closed
with conn as s:
    # conn.__enter__() excutes connection open
    s.send(b"GET /index.html HTTP/1.0\r\n")
    # conn.__exit__() connection closed

"""
The principle behind writing a context manager is that your writing code thats meant 
to surround a block of statements as defined by the use of the with statement.

When the with statement is first encountered __enter_() is triggered. The return value 
is placed into the variable indicated with the as qualifier. Afterward the statements
in the body of the with statement execute. Finally __exit__() is triggered to clean up.

The control flow happens regardless of what happens in the body of the with statement,
including exceptions.

The three arguments to the __exit__() method contain the exception type value and traceback
for pending exceptions (if any). The __exit__() method can choose to use the exception 
information in some way or to ignore it by doing nothing and returning None as a result.

If __exit__() returns True, the exception is cleared as if nothing has happened and the 
application will continue executing after the with block

One subtle aspect of the above is LazyConnection class - and that it allows nested use 
of the connection with multiple with statements. Our current implementation only allows 
a single socket connection at a time - a slightly different implementation can be carried out
to get round this.

In this version the LazyConnection class acts as a factory for connections. It creates
the connection, adds it to the stack. __exit__() pops the last connection off the stack and closes it.
Using __enter__ and __exit__ helps avoid deadlocking since the celanup code in __exit__ guarantees 
to run no matter what.  
"""


class LazyConnectionMulti:
    def __init__(self, address, family=AF_INET, type=SOCK_STREAM):
        self.address = address
        self.family = family
        self.type = type
        self.connections = []

    def __enter__(self):
        sock = socket(self.family, self.type)
        sock.connect(self.address)
        self.connections.append(sock)
        return sock

    def __exit(self, exc_ty, exc_val, tb):
        self.connections.pop().close()


# Example usage
conn = LazyConnectionMulti(("www.python.org", 80))
with conn as sl:
    print("1")
    with conn as s2:
        # etc etc
        print("2")
