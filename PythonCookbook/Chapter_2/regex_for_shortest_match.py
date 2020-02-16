import re
# Regexes ID the longest possible matches. What about the shortest?

str_pat = re.compile(r'\"(.*)\"')
text1 = 'Computer says "no."'
str_pat.findall(text1) # Returns ['no.']
text2 = 'Computer says "no." Phone says "yes."'
str_pat.findall(text2) # Returns ['no." Phone says "yes.']

# What went wrong? It's trying to match text enclosed inside quotes. 
# The * operator is greedy, so it grabs the longest possible match. Fix with the ? modifier.
# This makes matching non-greedy and returns the shortest match.

str_pat = re.compile(r'\"(.*?)\"')
str_pat.findall(text2) # Returns ['no.', 'yes.']

# . matches any character except a new line. Bracket it with a quote and it will try to find the 
# longest possible match. Adding the ? right after * or + forces the algorithm to look for the
# shortest match possible.