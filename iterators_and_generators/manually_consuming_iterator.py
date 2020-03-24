"""
This script shows how to process items in an iterable, without using a for loop.

To do this - use next() function and catch the StopIteration exception,
for example the following manually reads lines from a file.
"""

with open('/etc/passwd') as f:
    try:
        while True:
            line = next(f)
            print(line, end='')
    except StopIteration:
        pass

"""
Typically - StopIteration is used to signal the end of iteration.
If using next() manually, you can also instruct it to return a terminating value,
such as None
"""
with open('/etc/passwd') as f:
    while True:
        line = next(f, None)
        if line is None:
            break
        print(line, end='')

"""
In most cases - for is used to consume an iterable. When you require precise control
over the underlying iteration mecahnism - use the pattern above. Below is an example 
from the interactive window that illustrates the mechanisms of what happens during 
iteration.
"""
items = [1, 2, 3]
# Get the iterator
it = iter(items)  # <list_iterator object at 0x10c69d978>

# Run the iterator
next(it)  # 1
next(it)  # 2
next(it)  # 3
next(it)
"""
Traceback (most recent call last):
  File "<input>", line 1, in <module>
StopIteration
"""
