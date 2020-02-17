# For simple rounding, use the built in round(value, ndigits) function
round(1.23, 1) # Returns 1.2
round(1.27, 1) # Returns 1.3
round(-1.27, 1) # Returns -1.3
round(1.25361, 3) # Returns 1.254

# Round rounds to the nearest even digit. 1.5 and 2.5 both get rounded to 2.
# Round can also have negative ndigits, so rounding takes place for tens, hundreds, thousands, etc.
a = 1627731
round(a, -1) # Returns 1627730
round(a, -2) # Returns 1627700
round(a, -3) # Returns 1628000

# Note that rounding != formatting for output
x = 1.23456
format(x, '0.2f') # Returns '1.23'
format(x, '0.3f') # Returns '1.235'
'value is {:0.3f}'.format(x) # Returns 'value is 1.235', could also be f'value is {x:0.3f}'

# Do not round floats to fix accuracy problems
a = 2.1
b = 4.2
c = a + b # Returns 6.300000000000001
c = round(c, 2) # Just use the decimal module.