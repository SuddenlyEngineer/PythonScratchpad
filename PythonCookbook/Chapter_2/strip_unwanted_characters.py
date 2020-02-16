import re

# Use the strip() method to strip from the beginning or the end, or lstrip() / rstrip() for left/right sides.
# By default, they strip whitespace. But you can give other characters as well.

s = '   hello world  \n' # Whitespace stripping
s.strip() # Returns 'hello world'
s.lstrip() # Returns 'hello world  \n'
s.rstrip() # Returns '   hello world'

t = '-----hello=====' # Character stripping
t.lstrip('-') # Returns 'hello====='
t.rstrip('-=') # Returns 'hello'

# These methods are used for reading/cleaning up data for further processing.
# Note: does not apply to text in the middle of a string. For that, use replace() or regex.

s = '  hello       world   \n'
s = s.strip()
s # Returns 'hello       world'
s.replace(' ', '') # Returns 'helloworld'
re.sub('\s+', ' ', s) # Returns 'hello world'

# Can also use generators.
'''with open(filename) as f:
    lines = (line.strip() for line in f)
    for line in lines:
        print('blah')'''
 # For better stripping, use translate()