"""
This script shows how to create or test values for infinity,
negative infinity or NaN

These can be created using float()
"""
import math

a = float('inf')
b = float('-inf')
c = float('nan')

# To test for the presence of these values use math.isinf()/isnan() functions
math.isinf(a)  # True
math.isnan(c)  # True

# Some details on comparisons and operators
a + 45  # inf
a * 10  # inf
10 / a  # 0.0

# Some operations are undefined and will result in NaN
a = float('inf')
a/a  # nan
b = float('-inf')
a + b  # nan

# NaN propogate through all operations without raising an exception
c = float('nan')
c + 23  # nan
c / 2  # nan
c * 2  # nan
math.sqrt(c)  # nan

# Subtle NaN values is that they never compare as equal
c = float('nan')
d = float('nan')
c == d  # False
c is d  # False

# The only way to test for NaN is to use math.isnan()

# To change pythons behaviour to raise exceptions when infinite or NaN - use fpectl,
# This is expert level and not part of the standard python build.

