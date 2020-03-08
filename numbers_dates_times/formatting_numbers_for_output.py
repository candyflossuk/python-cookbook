"""
This script shows how to format a number for output, controlling the number of digits, alignment,
inclusion of a thousands separator and other details
"""

# Formatting a single number for output - use built in format()
x = 1234.56789

# Right justified in 10 chars, on-digit accuracy
format(x, '>10.1f')  # '    1234.6'

# Left justified
format(x, '<10.1f')  # '1234.6    '

# Centered
format(x, '^10.1f')

# Inclusion of thousands separator
format(x, ',')  # '1,234.56789'

# to change to exponential notation change f to an E or e
format(x, 'e')  # '1.234568e+03'
format(x, '0.2E')  # '1.23E+03'

"""
General form of the width and precision in both cases is
'[<>^]?width[,]?(.digits)?' where width and digits are integers
and ? signifies optional parts. Same format codes are used in 
.format() method of strings. 
"""
'The value is {:0,.2f}'.format(x)  # 'The value is 1,234.57'

# Technique shown works for floats and decimals

# When number of digits is restricted, values are rounded away according to rules of round
format(x, '0.1f')  # '1234.6'
format(-x, '0.1f')  # '-1234.6'

# Foramtting of values with thousands separator is not locale aware
# To take locale into account you might use locale module
# You can also swap seperator characters using the translate() method

swap_separators = {ord('.'):',',ord(','):'.'}
format(x, ',').translate(swap_separators)  # '1.234,56789'

# In python numbers are formatted using the % operator
'%0.2f' % x  # '1234.57'
'%10.1f' % x  # '    1234.6'
'%-10.1f' % x  # '1234.6    '

# This formatting is acceptable but less powerful than format()
