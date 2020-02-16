import re
line = 'asdf fjdk; afed, fjek,asdf,      foo'
re.split(r'[;,\s]\s*', line) # Returns ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']

# split() is meant for really simple cases, and doesn't allow for multiple delimiters or possible whitespace.
# re.split() lets you; above the separator can be , ; or whitespace, folowed by umlimited whitepace
# Whenever that pattern is matched, a list of fields is generated, just like split()
# Note: if capture groups are used, the matched text is also included

fields = re.split(r'(l|,|\s)\s*', line)
fields #['asdf', ' ', 'fjdk', ';', 'afed', ',', 'fjek', ',', 'asdf', ',', 'foo']

values = fields[::2]
delimiters = fields[1::2] + ['']
values
delimiters

# Reform the line using the same delimiters
''.join(v+d for v,d in zip(values, delimiters))

# Don't want separator characters in the result? Make sure you use a non-capture group
re.split(r'(?:,|;|\s)\s*', line) # Returns ['asdf', 'fjdk', 'afed', 'fjek', 'asdf', 'foo']