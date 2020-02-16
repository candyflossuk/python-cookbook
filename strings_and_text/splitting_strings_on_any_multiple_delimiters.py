"""
Script showing how to split a string into fields,
but the delimiters are not consistent

split() method is meant for simple cases. Instead use re.split()
"""
import re

line = 'asdf fjdk; afed, fjek,asdf,      foo'
re.split(r'[;,\s]\s*', line)

# ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

"""
This pattern is useful because you can specify multiple 
patterns for the serpartor. 

In this solution it shows ; , and whitespace followed by any amount of extra
whitespace.

When using re.split(), be careful that if the regular expression pattern
involves a capture group enclosed in parens then the matched text is 
also included in the result.
"""
fields = re.split(r'(;|,|\s)\s*', line)
# ['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

"""
Getting the split characters is sometimes useful - as in needing them to reform 
the string later on.
"""
values = fields[::2]
delimiters = fields[1::2] + ['']
values  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
delimiters  # [' ', ';', ',', ',', ',', '']

# Reform
''.join(v+d for v,d in zip(values, delimiters))
# 'asdf fjdk;afed,fjek,asdf,foo'

# No seperators in result = use noncapture group (?:...)
re.split(r'(?:,|;|\s)\s*', line)  # ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']
