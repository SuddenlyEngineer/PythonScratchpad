import numpy as np
x = [1, 2, 3, 4] # Python Lists
y = [5, 6, 7, 8]
x * 2 # Returns [1, 2, 3, 4, 1, 2, 3, 4]
x + y # Returns [1, 2, 3, 4, 5,6 , 7, 8]

ax = np.array([1, 2, 3, 4]) # Numpy arrays
ay = np.array([5, 6, 7, 8])
ax * 2 # Returns array([2, 4, 6, 8])
ax + 10 # Returns array([11, 12, 13, 14])
ax + ay # Returns array([ 6,  8, 10, 12])
ax * ay # Returns array([ 5, 12, 21, 32])

# Math operations apply to all elements simultaneously

def f(x):
    return 3*x**2 - 2 * x + 7

f(ax) # Returns array([ 8, 15, 28, 47])

# NumPy has replacements for functions in the math module, but allow for array ops.
np.sqrt(ax) # Returns array([ 1.        ,  1.41421356,  1.73205081,  2.        ])
np.cos(ax) # Returns array([ 0.54030231, -0.41614684, -0.9899925 , -0.65364362])

# NumPy arrays are basically C/Fortran arrays

grid = np.zeros(shape=(10000,10000), dtype=float) # Array of 10k x 10k floats.

# Can do operations like grid += 10 or np.sin(grid)
# NumPy also has great list indexing functionalit with multidimensional arrays.

a = np.array([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

a[1] # Selects row 1
a[:,1] # Selects column 1
a[1:3, 1:3] += 10 # Selects a subregion and changes it
a + [100, 101, 102, 103] # Broadcast a row vector across an operation on all rows
np.where(a < 10, a, 10) # Conditional assignment on an array