import re
import os

# Byte strings already support common text operations, like stripping/searching/replacement

data = b'Hello World'
data[0:5] # Returns b'Hello'
data.startswith(b'Hello') # Returns True
data.split() # Returns [b'Hello', b'World']
data.replace(b'Hello', b'Hello Cruel') # Returns b'Hello Cruel World'

# Also works with byte arrays
data = bytearray(b'Hello World')
data[0:5] # Returns bytearray(b'Hello')
data.startswith(b'Hello') # Returns True
data.split() # Returns [bytearray(b'Hello'), bytearray(b'World')]
data.replace(b'Hello', b'Hello Cruel') # Returns bytearray(b'Hello Cruel World')

# Can apply regex, but the patterns need to be bytes, too.
data = b'FOO:BAR,SPAM'
re.split(b'[:,]',data) # Returns [b'FOO', b'BAR', b'SPAM']

# Note that indexing byte strings produces integers, not individual characters
a = 'Hello World'
a[0] # H
a[1] # E
b = b'Hello World'
b[0] # 72
b[1] # 101

# Byte strings don't provide a string representations and don't print cleanly unless decoded into a text string.
s = b'Hello World'
print(s) # Returns b'Hello World'
print(s.decode('ascii')) # Returns Hello World

# No string formatting operations exist. Should be done with normal text strings + encoding.
'{:10s} {:10d} {:10.2f}'.format('ACME', 100, 490.1).encode('ascii') # Returns b'ACME              100     490.10'

# Supplying a filename encoded as bytes rather than a text string usually disables filename encoding / decoding.

with open('jalape\xf1o.txt', 'w') as f: # Write a UTF-8 filename
    f.write('spicy')

os.listdir('.') # Get a directory listing, returns Text string (names are decoded) ['jalapeño.txt']
os.listdir(b'.') # Returns Byte string (names left as bytes) b'jalapen\xcc\x83o.txt']

# There may be performance improvements to using bytes over text, but makes the code very messy.
# Just use text lmao.