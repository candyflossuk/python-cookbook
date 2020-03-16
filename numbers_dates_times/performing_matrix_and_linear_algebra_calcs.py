"""
This script shows how to perform linear and matrix algebra operations
such as matrix multiplication, determinants, and linear equations.

To do this you can use the numpy library matrix object
"""
import numpy as np
import numpy.linalg

m = np.matrix([[1,-2,3], [0,4,5],[7,8,-9]])
m
"""
matrix([[ 1, -2,  3],
        [ 0,  4,  5],
        [ 7,  8, -9]])
"""

# Return transposed matrix
m.T
"""
matrix([[ 1,  0,  7],
        [-2,  4,  8],
        [ 3,  5, -9]])
"""

# Return Inverse
m.I
"""
matrix([[ 0.33043478, -0.02608696,  0.09565217],
        [-0.15217391,  0.13043478,  0.02173913],
        [ 0.12173913,  0.09565217, -0.0173913 ]])
"""

# Create a vector and multiply
v = np.matrix([[2],[3],[4]])
v
"""
matrix([[2],
        [3],
        [4]])
"""

m * v
"""
matrix([[ 8],
        [32],
        [ 2]])
"""

# More operations can be found in the numpy.linalg subpackage

# Determinant
numpy.linalg.det(m)  # -229.99999999999983

# Eigenvalues
numpy.linalg.eigvals(m)  # array([-13.11474312,   2.75956154,   6.35518158])

# Solve for x in mx = v
x = numpy.linalg.solve(m, v)
"""
matrix([[0.96521739],
        [0.17391304],
        [0.46086957]])
"""

m * x
"""
matrix([[2.],
        [3.],
        [4.]])
"""

v
"""
matrix([[2],
        [3],
        [4]])
"""
