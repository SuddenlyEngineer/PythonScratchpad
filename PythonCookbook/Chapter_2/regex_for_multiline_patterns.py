import re

# Need a regex match to span multiple lines?
comment = re.compile(r'/\*(.*?)\*/')
text1 = '/* this is a comment */'
text2 = '''/* this is a 
multiline comment */
'''
comment.findall(text1) # Returns [' this is a comment ']
comment.findall(text2) # Returns []

# Can fix with a new regex
comment = re.compile(r'/\*((?:.|\n)*?)\*/')
comment.findall(text2) # Returns [' this is a\n              multiline comment ']

# (?:.|\n) specifies a non-capture group, a group for the purposes of matching, but a group not captured separately or numbered.

# re.compile() accepts re.DOTALL, which makes . match all characters including newlines

comment = re.compile(r'/\*(.*?)\*/', re.DOTALL)
comment.findall(text2) # Returns [' this is a\n              multiline comment ']

# Note that re.DOTALL may have issues when working with complicated patterns
# Or a mix of separate regexes combined for tokenizations.