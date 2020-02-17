import numpy as np
import numpy.linalg
# Wanna do matrix algebra? NumPy has a matrix object.
m = np.matrix([[1,-2,3],[0,4,5],[7,8,-9]])
m.T # Returns a transpose of the matrix
m.I # Returns an inverse of the matrix
v = np.matrix([[2],[3],[4]])
m * v # Matrix multiplication, returns matrix([[8],[32],[2]])

numpy.linalg.det(m) # Determinant
numpy.linalg.eigvals(m) # Eigenvalues
x = numpy.linalg.solve(m, v) # Solve for x in mx = v
m * x