# Need to format text with an alignment? Use ljust(), rjust(), and center().
text = 'Hello World'
text.ljust(20) # Returns  'Hello World         ', default it is padded out with spaces
text.rjust(20) # Returns '         Hello World'
text.center(20) # Returns '    Hello World     '

text.rjust(20,'=') # Returns '=========Hello World'
text.center(20,'*') # Returns '****Hello World*****'

format(text, '>20') # Alternate syntax for rjust
format(text, '<20') # Alternate syntax for ljust
format(text, '^20') # Alternate syntax for center

format(text, '=>20s') # text.rjust(20,'=')
format(text, '*^20s') # text.center(20,'*') 
# Can also use the format method with multiple values
'{:>10s} {:>10s}'.format('Hello', 'World') # Returns '     Hello      World'

x = 1.2345 # format() works with any value
format(x, '>10') # Returns '    1.2345'
format(x, '^10.2f') # Returns '   1.23   '

# Older code uses the % to format text, but format is nwer and more powerful.