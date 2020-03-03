"""
This script shows how to combine many small strings into
larger strings

Where strings are found in a sequence or iterable - the fastest way
to combine is to use join().
"""

parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts)  # 'Is Chicago Not Chicago?'
','.join(parts)  # 'Is,Chicago,Not,Chicago?'
''.join(parts)  # 'IsChicagoNotChicago?'

"""
This is a method on strings - because you want to join
on different data sequences - it would be redundant to
have join() implemented on every object. Instead the 
separator string is defined and join() is used to glue 
the text together

When only joining a few strings '+' works well enough
"""
a = 'Is Chicago'
b = 'Not Chicago'
a + ' ' + b

"""
+ operator also works fine a substitute for 
complicated string formatting
"""
print('{} {}'.format(a,b))
print(a + ' ' + b)
# both print the same thing

# if your combining string literals in source code just place them next to each other
a = 'Hello' 'World'
a

"""
Using the '+' operator for lots of strings is inefficient as hell due 
to the copies in memory and GC.

NEVER write code like this
"""
s = ''
for p in parts:
    s += p
# This will run slower than join, as += creates a new string object.

"""
A neat trick in conversion of data to strings and concat at the same time
is to use a generator expression
"""
data = ['ACME', 50, 91.1]
','.join(str(d) for d in data)
# 'ACME,50,91.1'

# Be wary of string concatenation you dont need
print(a + ':' + b + ':' + c)  # Ugggggly
print(':'.join([a,b,c]))  # Still ugly
print(a, b, c, sep=':') # Better :)

# Mixing I/O operations and string concatenation is sometimes a use case in apps
# version 1 (string concatenation)
f.write(chunk1 + chunk2)

# version 2 (seperate i/o)
f.write(chunk1)
f.write(chunk2)

"""
if two strings are small, v1 is better. If strings are large
then v2 is better.

If you are writing output from lots of small strings, you might want a generator function
"""

def sample():
    yield 'Is'
    yield 'Chicago'
    yield 'Not'
    yield 'Chicago?'

# No assumption about how to join the fragments
text = ''.join(sample())

# or redirect to I/O
for part in sample():
    f.write(part)

# or hybrid that is smart about combining I/O ops
def combine(source, maxsize):
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)


for part in combine(sample(), 32768):
    f.write(part)

# generator function dosn't need to know details - just yield the parts
