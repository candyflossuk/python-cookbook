"""
Script showing how to format text with alignment applied

ljust(), rjust() and center() methods of strings can be used
"""

text = 'Hello World'
text.ljust(20)  # 'Hello World         '
text.rjust(20)  # '         Hello World'
text.center(20)  # '    Hello World     '

# methods accept optional fill character
text.rjust(20, '=')  # '=========Hello World'
text.center(20, '*')  # '****Hello World*****'

# format() can be used to align as well. Use <  > or ^ along with desired width
format(text, '>20')  # '         Hello World'
format(text, '<20')  # 'Hello World         '
format(text, '^20')  # '    Hello World     '

# if you want to include a fill character other than space, specify before alignment char
format(text, '=>20s')  # '=========Hello World'
format(text, '*^20s')  # '****Hello World*****'

# can also be used to format multiple values
'{:>10s} {:>10s}'.format('Hello', 'World')  # '     Hello      World'

# format isn't string specific
x = 1.2345
format(x, '>10')  # '    1.2345'
format(x, '^10.2f')  # '   1.23   '

# in older code the % operator is used to format text, format() is preferred over
# ljust(), center() and rjust()
