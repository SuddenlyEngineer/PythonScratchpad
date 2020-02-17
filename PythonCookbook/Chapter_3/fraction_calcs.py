from fractions import Fraction
a = Fraction(5, 4) # 5/4
b = Fraction(7, 16) # 7/16
print(a+b) # 27/16
print(a*b) # 35/64

c = a * b
c.numerator # 35
c.denominator # 64

float(c) # Returns .546875

print(c.limit_denominator(8)) # Limits a value's denominator, 4/7

x = 3.75
y = Fraction(*x.as_integer_ratio()) # Returns Fraction(15, 4)