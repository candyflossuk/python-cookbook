"""
This script shows how to write functions that ONLY accept
certain arguments by keyword.

This is easy to implement, by placing keyword arguments
after a * argument or single unnamed *
"""


def recv(maxsize, *, block):
    "Receives a message"
    pass


recv(1024, True)  # TypeError
recv(1024, block=True)  # OK

"""
This technique can also be used to specify kewyword arguments for functions that 
accept a varying number of positional arguments
"""


def minimum(*values, clip=None):
    m = min(values)
    if clip is not None:
        m = clip if clip > m else m
    return m


minimum(1, 5, 2, -5, 10)  # Returns -5
minimum(1, 5, 2, -5, 10, clip=0)  # Returns 0

"""
Keyword only arguments are often a good way to enforce greater
code clarity when specifying optional functional arguments
"""
msg = recv(1024, False)

"""
If you are rerading this - and are not faimilar with how recv works - 
it is not clear what the False argument means. Something like the following
makes far more sense
"""
msg = recv(1024, block=False)

"""
The use of keyword only arguments is often preferrable to tricks
involving ***kwargs - as they show up properly when a user
asks for help using help(recv) for example. 

Keyword only arguments also have utility in more advanced contexts. i.e
to inject arguments into functions that make use of *args and **kwargs convention
for accepting all inputs
"""
