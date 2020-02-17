from struct import Struct # Use this to work with binary data structures
import struct
from collections import namedtuple
import numpy as np

def write_records(records, format, f):
    '''
    Write a sequence of tuples to a binary file of structures.
    '''
    record_struct = Struct(format)
    for r in records:
        f.write(record_struct.pack(*r))

def read_records(format, f): # Reads the file back into a list of tuples using chunks.
    record_struct = Struct(format)
    chunks = iter(lambda: f.read(record_struct.size), b'')
    return (record_struct.unpack(chunk) for chunk in chunks)

if __name__ == '__main__': # Encoding example.
    records = [ (1, 2.3, 4.5),
                (6, 7.8, 9.0),
                (12, 13.4, 56.7) ]

    with open('data.b', 'wb') as f:
         write_records(records, '<idd', f)

if __name__ == '__main__': # Decoding example
    with open('data.b','rb') as f:
        for rec in read_records('<idd', f):
            print(rec)

def unpack_records(format, data): # Read the file entirely into a byte string with a single read and convert it piece by piece.
    record_struct = Struct(format)
    return (record_struct.unpack_from(data, offset) for offset in range(0, len(data), record_struct.size))

# Example
if __name__ == '__main__':
    with open('data.b', 'rb') as f:
        data = f.read()

    for rec in unpack_records('<idd', data):
        # Process rec
        print(rec)

# Either way, generates an interable that produces the original tuples.
# Struct is common in programs that encode/decode binary data.

# Little endian 32-bit integer, two double precision floats.
record_struct = Struct('<idd')
record_struct.size # Returns size of the structure in bytes, here 20
record_struct.pack(1, 2.0, 3.0) # Packs data, like b'\x01\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00@\x00\x00\x00\x00\x00\x00\x08@'
record_struct.unpack() # Unpacks data, here (1, 2.0, 3.0)

# Can also use pack and unpack as module-level functions
struct.pack('<idd', 1, 2.0, 3.0)
struct.unpack('<idd') # These work, but far less elegant.

# The code for reading binary structures uses iter() to return fixed-size chunks.
# The iterator repeatedly calls a user-supplied callable (the lambda) until it returns the b'' sentinal, then iteration stops.

f = open('data.b', 'rb')
chunks = iter(lambda: f.read(20), b'')
for chk in chunks:
    print(chk)

# The iterable also nicely allows records to be created using a generator comprehension.
# When unpacking, unpack_from() extracts binary data without making temp objects or memcopies.
# This also avoids slices and offset calculations.

# When unpacking, also consider using namedtuples.

Record = namedtuple('Record', ['kind','x','y'])
with open('data.p', 'rb') as f:
    records = (Record(*r) for r in read_records('<idd', f))

for r in records:
    print(r.kind, r.x, r.y)

# With a large amount of binary data, use numpy and read into a structured array
f = open('data.b', 'rb')
records = np.fromfile(f, dtype='<i,<d,<d')