import re
from calendar import month_abbr
# Simple literal patterns? Use str.replace()
text = 'yeah, but no, but yeah, but no, but yeah'
text.replace('yeah', 'yep')

# More complicated patterns? Use the sub() function in the re module.
text = 'Today is 11/27/2012. PyCon starts 3/13/2013.' #Here, rewrite dates as YYYY-MM-DD
re.sub(r'(\d+)/(\d+)/(\d+)', r'\3-\1-\2', text) # Returns 'Today is 2012-11-27. PyCon starts 2013-3-13.'

# The first argument is the pattern to match, second is replacement pattern. Backslashed digits refer to capture groups.

# Using it multiple times? Compile it.
datepat = re.compile(r'(\d+)/(\d+)/(\d+)')
datepat.sub(r'\3-\1-\2', text) #Does the same as above.

# Yet more complicated? Specify a substitution callback function.
def change_date(m):
    mon_name = month_abbr[int(m.group(1))]
    return '{} {} {}'.format(m.group(2), mon_name, m.group(3))

datepat.sub(change_date, text) #Returns 'Today is 27 Nov 2012. PyCon starts 13 Mar 2013.'

# As input, the argument to the substituion callback is a match object, returned by match() or find().
# Use the .group() method to extract specific parts. The function returns replacement text.

# Want to know how many substitutions were made, besides getting the text back? Use re.subn()

newtext, n = datepat.subn(r'\3-\1-\2', text)
newtext # Returns 'Today is 2012-11-27. PyCon starts 2013-3-13.'
n # Returns 2