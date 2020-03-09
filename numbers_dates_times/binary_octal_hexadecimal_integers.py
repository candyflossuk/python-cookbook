"""
This script shows how to convert or output integers represented
by binary, octal or hexadecimal.

use bin(), oct() or hex() to do this
"""
import os

x = 1234
bin(x)  # '0b10011010010'
oct(x)  # '0o2322'
hex(x)  # '0x4d2'

# Alternatively you can use format() function if you don't want 0b, 0o or 0x
format(x, 'b')  # '10011010010'
format(x, 'o')  # '2322'
format(x, 'x')  # '4d2'

# Integers are signed - so if using negative numbers use the sign
x = -1234
format(x, 'b')  # '-10011010010'
format(x, 'x')  # '-4d2'

# If you want to produce an unsigned value instead youll need to add in the
# maximum value to set the bit length.
x = -1234
format(2**32 + x, 'b')  # '11111111111111111111101100101110'
format(2**32 + x, 'x')  # 'fffffb2e'

# To convert integer strings in different bases use int() function with an appropiate base
int('4d2', 16)  # 1234
int('10011010010', 2)  # 1234

# Under the covers there is just one integer type - this is just a textual representation
"""
One caution using octal - Python for specifying octal is different than other languages
The following will give you a syntax error
"""

os.chmod('script.py', 0755)
# to get this working you need to prefix the octal with 0o
os.chmod('script.py', 0o755)



