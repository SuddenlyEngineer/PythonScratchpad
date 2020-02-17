import os
x = 1234
bin(x) # Returns binary, '0b10011010010'
oct(x) # Returns octal, '0o2322'
hex(x) # Returns hexadecimal, '0x4d2'

# Can also use format to omit the 0b, 0o, or 0x prefix
format(x, 'b') # Returns '10011010010'
format(x, 'o') # Returns '2322'
format(x, 'x') # Returns '4d2'

x = -1234 # Note that integers are signed
format(x, 'b') # Returns '-10011010010'
format(x, 'x') # Returns '-4d2'

# Need to produce unsigned values? Add the maximum value to set the bit length.
# Need to show a 32-bit value, use the following:
x = -1234
format(2**32 + x, 'b') # Returns '11111111111111111111101100101110'
format(2**32 + x, 'x') # 'fffffb2e'

# To convert integer strinsg in different bases, use int() with a different base
int('4d2', 16) # Returns 1234
int('10011010010', 2) # Returns 1234

# Python has a weird octal syntax. 
os.chmod('script.py, 0o755') # Octals must be prefixed with 0o.