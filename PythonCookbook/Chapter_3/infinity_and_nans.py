import math

# No special syntax for infinity or NaNs. Can use float(). NaNs don't raise exceptions.
a = float('inf')
b = float('-inf')
c = float('nan')

math.isinf(a) # Returns True
math.isnan(c) # Returns True

a + 45 # Returns inf
a * 10 # Returns inf
10 / a # Returns 0.0

a = float('inf')
a/a # Returns nan
b = float('-inf')
a + b # Returns nan

c = float('nan')
d = float('nan')
c + 23 # Returns nan
c / 2 # Returns nan
c * 2 # Returns nan
math.sqrt(c) # Returns nan

c == d # False, NaNs never compare as equal
c is d # False, only way to test for NaN is math.isnan()

# To raise exceptions, use fpectl. Not enabled in standard Python builds.
