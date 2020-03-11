"""
This script shows how to do calculations and use complex numbers in python

Complex numbers can be specified using the complex(real, imag) function or
by floating-point numbers using a j suffix
"""
import cmath
import math
import numpy as np

a = complex(2, 4)  # (2+4j)
b = 3 - 5j  # (3-5j)

# The real, imaginary and conjugate values are easy to obtain
a.real  # 2.0
a.imag  # 4.0
a.conjugate()  # (2-4j)

# The usual mathematical operators work
a + b  # (5-1j)
a * b  # (26+2j)
a / b  # (-0.4117647058823529+0.6470588235294118j)
abs(a)  # 4.47213595499958

# To perform additional complex-valued functions such as sines, cosines, sq roots use cmath module
cmath.sin(a)  # (24.83130584894638-11.356612711218174j)
cmath.cos(a)  # (-11.36423470640106-24.814651485634187j)
cmath.exp(a)  # (-4.829809383269385-5.5920560936409816j)


# Most of pythons math modules are aware of complex values
a = np.array([2+3j, 4+5j, 6-7j, 8+9j])  # array([2.+3.j, 4.+5.j, 6.-7.j, 8.+9.j])
a + 2  # array([ 4.+3.j,  6.+5.j,  8.-7.j, 10.+9.j])
np.sin(a)
# array([   9.15449915  -4.16890696j,  -56.16227422 -48.50245524j,
#        -153.20827755-526.47684926j, 4008.42651446-589.49948373j])

"""
Python's standard math functions do not produce complex values by default
"""
math.sqrt(-1)  # ValueError: math domain error
# If you want complex numbers you have to use cmath or declare the use of a complex type
cmath.sqrt(-1)  # 1j
