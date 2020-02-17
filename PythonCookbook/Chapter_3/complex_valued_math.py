import cmath
import math

import numpy as np

a = complex(2, 4) # real, imag
b = 3 - 5j
a # Returns (2+4j)
b # Returns (3-5j)

a.real # Returns 2.0
a.imag # Returns 4.0
a.conjugate() # Returns (2-4j)

a + b # Returns (5-1j)
a * b # Returns (26+2j)
a / b # Returns (-0.4117647058823529+0.6470588235294118j)
abs(a) # Returns 4.47213595499958

cmath.sin(a) # Returns (24.83130584894638-11.356612711218174j)
cmath.cos(a) # Returns (-11.36423470640106-24.814651485634187j)
cmath.exp(a) # Returns (-4.829809383269385-5.5920560936409816j)

a = np.array([2+3j, 4+5j, 6-7j, 8+9j])
a # Returns array([ 2.+3.j,  4.+5.j,  6.-7.j,  8.+9.j])
a + 2 # Returns array([  4.+3.j,   6.+5.j,   8.-7.j,  10.+9.j])
np.sin(a) # array([    9.15449915  -4.16890696j,   -56.16227422 -48.50245524j,
        # -153.20827755-526.47684926j,  4008.42651446-589.49948373j])

# Note that math can't handle sqrt(-1), that needs cmath.
