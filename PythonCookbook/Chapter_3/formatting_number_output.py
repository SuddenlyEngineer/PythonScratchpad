# Need to format a number for output? Use the format() function.

x = 1234.56789
format(x, '0.2f') # Two decimal places of accuracy, '1234.57'
format(x, '>10.1f') # Right justified in 10 chars, one-digit accuracy, '    1234.6'
format(x, '<10.1f') # Above but left justified, '1234.6    '
format(x, '^10.1f') # Above, but centered, '  1234.6  '
format(x, ',') #Includes the thousands separator, '1,234.56789'
format(x, '0,.1f') # Returns '1, 234.6'

# Change the f to an e or E, depending on desired case, for exponential notation.
format(x, 'e') # Returns '1.234568e+03'
format(x, '0.2E') # Returns '1.23E+03'

# Can also use .format or f strings, floats or decimals.
# Note the formatting of values with a thousands separator is not locale aware.
# Check the locale module, or use the translate() method.
swap_separators = { ord('.'):',', ord(','):'.' }
format(x, ',').translate(swap_separators) # Returns '1.234,56789'

# Can also format with %, but outdated.