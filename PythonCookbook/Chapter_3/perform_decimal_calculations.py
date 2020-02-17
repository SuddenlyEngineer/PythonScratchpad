from decimal import Decimal, localcontext
import math

a = 4.2
b = 2.1
a + b # Returns 6.300000000000001
(a+b) == 6.3 # Returns False

# Want to trade more accuracy for performance? Use Decimal

a = Decimal(4.2)
b = Decimal(2.1)
a + b # Returns Decimal('6.3')
print(a+b) # Returns 6.3
(a + b) == Decimal('6.3') # Returns True

# Decimal objects support all normal math operations and string formatting functions.
# Local Contexts and their settings let you set number of digits and rounding

a = Decimal('1.3')
b = Decimal('1.7')
print(a / b) #0.7647058823529411764705882353
with localcontext() as ctx:
    ctx.prec = 3
    print(a / b) # Returns 0.765
with localcontext() as ctx:
    ctx.prec = 50
    print(a/b) # Returns 0.76470588235294117647058823529411764705882352941176

# Use floats for highly accurate / large nunmbers of calculations
nums = [1.23e+18, 1, -1.23e+18]
sum(nums) # Returns 0, 1 just disappears.

math.fsum(nums) # Returns 1.0, as expected