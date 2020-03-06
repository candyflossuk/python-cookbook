"""
This script shows how to round a floating-point number to a fixed
number of decimal places
"""

# Simple rounding
round(1.23, 1)
# 1.2
round(1.27, 1)
# 1.3
round(-1.27, 1)
# -1.3
round(1.25361, 3)
# 1.254

"""
When a value is exactly halfway between two choices the 
behaviour of 'round' is to round to the nearest even digit.
1.5 = 2 , 2.5 = 2

The number of digits given to round() can be negative,
rounding takes place for tens, hundreds, thousands.
"""
a = 1627731
round(a, -1)  # 1627730
round(a, -2)  # 1627700
round(a, -3)  # 1628000

# Formatting and rounding should not be confused
# To simply output a numerical value with a certain number of decimals, use format

x = 1.23456
format(x, '0.2f')  # '1.23'
format(x, '0.3f')  # '1.235'
'value is {:0.3f}'.format(x)  # 'value is 1.235'

# Resist the urge to round floating-point numbers to fix accuracy problems
a = 2.1
b = 4.2
c = a+b
c = round(c,2) # feels like a fix - but is it?
c

# Not needed - and is usually tolerated - if important consider the decimal module.

