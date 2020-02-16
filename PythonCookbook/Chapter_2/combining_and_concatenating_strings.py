# Are the strings in a sequence or iterable? Use join()
parts = ['Is', 'Chicago', 'Not', 'Chicago?']
' '.join(parts) # Returns 'Is Chicago Not Chicago?'
','.join(parts) # Returns 'Is,Chicago,Not,Chicago?'
''.join(parts) # Returns 'IsChicagoNotChicago?'

# Just a few strings, use + 
a = 'Is Chicago'
b = 'Not Chicago?'
a + ' ' + b # Returns 'Is Chicago Not Chicago?'

print('{} {}'.format(a,b)) # Alternate syntax
print(a + ' ' + b) 

# Trying to combine string literals together in source code? Place them adjacent to each other.

a = 'Hello' 'World' # Returns 'HelloWorld'

# The + operator is really inefficient due to memcopies and garbage collection.
# Don't ever do the below:
'''s = '' #This is infinitely slower than join()
for p in parts:
    s += p'''

# You can convert data to strings and concatenate with a generator
data = ['ACME', 50, 91.1]
','.join(str(d) for d in data) # Returns 'ACME,50,91.1'

# Be careful of ugliness:
# print(a + ':' + b + ':' + c) # NOPE
# print(':'.join([a, b, c])) # NOPE
# print(a, b, c, sep=':') # MUCH BETTER

# Weigh the balance of I/O system calls and memory copies.
# f.write(chunk1 + chunk2) with string concatenation may be more efficient for small strings
# f.write(chunk1)
# f.write(chunk2) may be more efficient for large strings due to moving large memory blocks around

# Writing code that builds output from small strings? Make a generator to yield fragements.

def sample(): # Makes no assumption about how framenets are assembled
    yield "Is"
    yield "Chicago"
    yield "Not"
    yield "Chicago?"

text = ''.join(sample()) # Join fragments

f = ''

for part in sample(): # Redirect fragments to I/O
    f.write(part)

def combine(source, maxsize): # How about a hybrid approach?
    parts = []
    size = 0
    for part in source:
        parts.append(part)
        size += len(part)
        if size > maxsize:
            yield ''.join(parts)
            parts = []
            size = 0
    yield ''.join(parts)

for part in combine(sample(), 32768):
    f.write(part)

# The generator doesn't have to know details, just yield parts.