import gzip
import bz2

# The above imports provide alternatives to open()

with gzip.open('somefile.gz', 'rt') as f: # Reads gzip files as text.
    text = f.read()

with bz2.open('somefile.bz2', 'rt') as f: # Reads bz2 files as text.
    text = f.read()

with gzip.open('somefile.gz', 'wt') as f: # Writes gzip files as text.
    f.write(text)

with bz2.open('somefile.bz2', 'wt') as f: # Writes bz2 files as text.
    f.write(text) # Can also use rb or wb to write binary.

# These functions accept encoding, errors, newine, and other open() parameters.
# Can specify compression level with the compresslevel argument. Default is 9 - max compression.
# Lower levels lower compression but higher performance.

with gzip.open('somefile.gz', 'wt', compresslevel=5) as f:
    f.write(text)

# Can also layer gzip.open() and bz2.open() ontop of an existing open binary file.

f = open('somefile.gz', 'rb')
with gzip.open(f, 'rt') as g:
     text = g.read()