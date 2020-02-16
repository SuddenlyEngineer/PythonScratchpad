import re

# Trying for a simple literal? Just use basic string methods
text = 'yeah, but no, but yeah, but no, but yeah'

text == 'yeah' # False, Exact Match
text.startswith('yeah') # True, Match at start
text.endswith('no') # False, Match at end
text.find('no') # 10, Searches for the location of the first occurrence 

# More complicated matching? Use regex and the re module.
text1 = '11/27/2012'
text2 = 'Nov 27, 2012'

if re.match(r'\d+/\d+/\d+', text1): # Simple matching: \d+ means match one or more digits. Should return yes
    print('yes')
else:
    print('no')

if re.match(r'\d+/\d+/\d+', text2): # Should return no
    print('yes')
else:
    print('no')

# Performing a lot of matches using the same pattern? Precompile the regex into a pattern object.

datepat = re.compile(r'\d+/\d+/\d+') # Remember, use double backslashes to interpret the \ character.
if datepat.match(text1):
    print('yes')
else:
    print('no')

# match() always tries to find a match at the start. Need to search for all occurrences? Use findall()

text = 'Today is 11/27/2012. PyCon starts 3/13/2013.'
datepat.findall(text) # Returns ['11/27/2012', '3/13/2013']

datepat = re.compile(r'(\d+)/(\d+)/(\d+)') # Rewriting with capture groups, (), so the contents can be extracted individiually

m = datepat.match('11/27/2012')
m # <_sre.SRE_Match object>
m.group(0) # '11/27/2012', this extracts the contents of each group
m.group(1) # '11'
m.group(2) # '27'
m.group(3) # '2012'
m.groups() # ('11', '27', '2012')
month, day, year = m.groups() # Unpack it

datepat.findall(text) # Now it will split into tuples, [('11', '27', '2012'), ('3', '13', '2013')]

for month, day, year in datepat.findall(text):
    print('{}-{}-{}'.format(year, month, day)) # 2012-11-27, 2013-3-13

# Want to find matches iteratively? Use finditer()

for m in datepat.finditer(text): #('11', '27', '2012'), ('3', '13', '2013')
    print(m.groups())

# Be aware that match() only checks the beginning of the string.

m = datepat.match('11/27/2012abcdef')
m # <_sre.SRE_Match object>
m.group() # '11/27/2012'

# To get an exact match, make sure to include $
datepat = re.compile(r'(\d+)/(\d+)/(\d+)$')
datepat.match('11/27/2012abcdef') # Returns nothing
datepat.match('11/27/2012') # Hey, an <_sre.SRE_Match object>

# If you're just doing a simple text match/search, you can skip compilation and just use re module-level functions.
re.findall(r'(\d+)/(\d+)/(\d+)', text) # [('11', '27', '2012'), ('3', '13', '2013')]

# Note that module level functions do keep a cache of recently compiled patterns, but if you're using it repeatedly, you'll save a bit of processing.