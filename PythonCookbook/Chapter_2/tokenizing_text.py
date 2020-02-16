import re
from collections import namedtuple

# Let's tokenize text below into a sequence of pairs. How? Regex
text = 'foo = 23 + 42 + 10'
#tokens = [('NAME', 'foo'), ('EQ','='), ('NUM', '23'), ('PLUS','+'),
          #('NUM', '42'), ('TIMES', '*'), ('NUM', '10')]

NAME = r'(?P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'
NUM  = r'(?P<NUM>\d+)'
PLUS = r'(?P<PLUS>\+)'
TIMES = r'(?P<TIMES>\*)'
EQ    = r'(?P<EQ>=)'
WS    = r'(?P<WS>\s+)'

master_pat = re.compile('|'.join([NAME, NUM, PLUS, TIMES, EQ, WS]))

# In these regex patterns, the ?P<TOKENNAME> convension assigns a name to the pattern
# Next, use the scanner() method of pattern objects. This creates a scanner object in which
# repeated calls to match() step through the supplied text one match at a time. 

scanner = master_pat.scanner('foo = 42')
scanner.match() # Returns <_sre.SRE_Match object>

# Now to package this as a generator

Token = namedtuple('Token', ['type', 'value'])

def generate_tokens(pat, text):
    scanner = pat.scanner(text)
    for m in iter(scanner.match, None):
        yield Token(m.lastgroup, m.group())

for tok in generate_tokens(master_pat, 'foo = 42'): 
    print(tok)

# Produces output
# Token(type='NAME', value='foo')
# Token(type='WS', value=' ')
# Token(type='EQ', value='=')
# Token(type='WS', value=' ')
# Token(type='NUM', value='42')

# Can filter the token stream with more generator functions or a generator expression. 

tokens = (tok for tok in generate_tokens(master_pat, text) if tok.type != 'WS')
for tok in tokens:
    print(tok)

# For scanning above, must make sure that every possible sequence has a corresponding regex pattern.
# If a nonmatchinng text pattern is found, scanning stops. Hence why a WS (whitespace) token was created.
# Order of tokens in the regex matters. When matching, re tries to match patterns in the order specified.
# If one pattern is a substring of a longer one, longer goes first.

LT = r'(?P<LT><)'
LE = r'(?P<LE><=)'
EQ = r'(?P<EQ>=)'

master_pat = re.compile('|'.join([LE, LT, EQ]))    # Correct
# master_pat = re.compile('|'.join([LT, LE, EQ]))  # Incorrect, because it would match the text <= as the token LT followed by EQ

# Also need to watch out for patterns which form substrings. 

PRINT = r'(P<PRINT>print)'
NAME  = r'(P<NAME>[a-zA-Z_][a-zA-Z_0-9]*)'

master_pat = re.compile('|'.join([PRINT, NAME])) 
for tok in generate_tokens(master_pat, 'printer'):
    print(tok)

# Outputs :
#  Token(type='PRINT', value='print')
#  Token(type='NAME', value='er')

# May also want to examine the PyParsing or PLY packages.