"""
This script shows how to perform accurate calculations with decimal numbers where you don't
want the small errors that occur within floats.
"""
from decimal import Decimal
from decimal import localcontext
import math

# The following produces small errors
a = 4.2
b = 2.1
a + b  # 6.300000000000001
(a + b) == 6.3  # False

# The errors are a feature of the underlying CPU & IEEE 754 arithmetic performed by floating point unit.
# There is nothing you can do to avoid such errors - to get more accurate (but less performance) use decimal module.
a = Decimal('4.2')
b = Decimal('2.1')
a + b  # Decimal('6.3')
(a + b) == Decimal('6.3')  # True

# Looks weird (as strings) but all arithemtic works as expected

"""
Decimal allows you to control aspects of the calculations, including number of digits and rounding,
this is done using local contexts and changing its settings
"""
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)  # 0.7647058823529411764705882353

with localcontext() as ctx:
    ctx.prec = 3
    print(a / b)  # 0.765

with localcontext() as ctx:
    ctx.prec = 50
    print(a / b)  # 0.76470588235294117647058823529411764705882352941176

# In science, engineering, computer graphics its more common to use floating point
# Very few things in the real world are measured to floats accuracy, therefore errors don't matter
# You can't ignore the errors completely - some algorithms handle it better than others - so you have to be careful

nums = [1.23e+18, 1, -1.23e+18]
sum(nums)  # 0.0 - 1 has disappeared
# This can be addressed using math.fsum()
math.fsum(nums)  # 1.0

# For other algorithms - you must understand the error propagation properties
# Main use of decimal is finance

