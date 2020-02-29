"""
This script shows how to split long strings into a user-specified
number of columns.

To do this the textwrap module can be used
"""
import textwrap
import os

s = "Look into my eyes, look into my eyes, the eyes, the eyes," \
    "the eyes, not around the eyes, don't look around the eyes," \
    "look into my eyes, you're under"

print(textwrap.fill(s, 70))
"""
Look into my eyes, look into my eyes, the eyes, the eyes,the eyes, not
around the eyes, don't look around the eyes,look into my eyes, you're
under

"""

print(textwrap.fill(s, 40))
"""
Look into my eyes, look into my eyes,
the eyes, the eyes,the eyes, not around
the eyes, don't look around the
eyes,look into my eyes, you're under
"""

print(textwrap.fill(s, 40, initial_indent='    '))
"""
    Look into my eyes, look into my
eyes, the eyes, the eyes,the eyes, not
around the eyes, don't look around the
eyes,look into my eyes, you're under
"""

print(textwrap.fill(s, 40, subsequent_indent='    '))
"""
Look into my eyes, look into my eyes,
    the eyes, the eyes,the eyes, not
    around the eyes, don't look around
    the eyes,look into my eyes, you're
    under
"""

"""
textwrap module is a pretty straightforward way to clean up text 
for printing - especially for fitting to terminal. You
can obtain terminal size using the following...
"""

os.get_terminal_size().columns

# fill() has a few additional options to control tabs, endings etc
