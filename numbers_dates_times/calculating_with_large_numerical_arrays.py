"""
This script shows how to perform calculations on large numerical datasets,
such as arrays, grids or arrays.

For any heavy computation using arrays use NumPy

Below is a short example illustrating important behavioural differences between lists and NumPy arrays
"""
import numpy as np
# Python Lists
x = [1, 2, 3, 4]
y = [5, 6, 7, 8]
x * 2  # [1, 2, 3, 4, 1, 2, 3, 4]
x + 10  # TypeError: can only concatenate list (not "int") to list
x + y  # [1, 2, 3, 4, 5, 6, 7, 8]


# NumPy arrays
ax = np.array([1, 2, 3, 4])
ay = np.array([5, 6, 7, 8])
ax * 2  # array([2, 4, 6, 8])
ax + 10  # array([11, 12, 13, 14])
ax + ay  # array([ 6,  8, 10, 12])
ax * ay  # array([ 5, 12, 21, 32])

# The way mathematical operations perform is different.

# To compute the value of a polynomial use:
def f(x):
    return 3*x**2 - 2*x + 7

f(ax)  # array([ 8, 15, 28, 47])

# NumPy provides 'universal functions' that allow for array operations, most of which are in the math module.
np.sqrt(ax)  # array([1.        , 1.41421356, 1.73205081, 2.        ])
np.cos(ax)  # array([ 0.54030231, -0.41614684, -0.9899925 , -0.65364362])

# You should prefer NumPy where possible

# To build a grid of 10,000 by 10,000 floats
grid = np.zeros(shape=(10000,10000), dtype=float)

# All usual operations apply simultaneously
grid += 10
np.sin(grid)

# NumPy extends Pythons list indexing functionallity - see examples below
a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# Select Row 1
a[1]

# Select Column 1
a[:,1]

# Select a subregion and change it
a[1:3, 1:3]
a[1:3, 1:3] += 10

# Broadcast a row vector across an operation on all rows
a + [100, 101, 102, 103]

# Conditional assignment on an array
np.where(a < 10, a, 10)
# array(Fraction(5, 4), dtype=object)

# It is standard to use import numpy as np


