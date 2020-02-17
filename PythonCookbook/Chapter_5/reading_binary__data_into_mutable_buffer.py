import os.path

# To read data into a mutable array without intermediate copying, use readinto()

def read_into_buffer(filename):
    buf = bytearray(os.path.getsize(filename))
    with open(filename, 'rb') as f:
        f.readinto(buf)
    return buf

with open('sample.bin', 'wb') as f: # Write a sample file
    f.write(b'Hello World')

buf = read_into_buffer('sample.bin') # Returns bytearray(b'Hello World')
buf[0:5] = b'Hallo' # Modifies into bytearray(b'Hallo World')

with open('newsample.bin', 'wb') as f:
    f.write(buf) # Returns 11

# Readinto() can fill any preallocated array (array module, numpy, etc.) with data
# Unlike read(), readinto() fills the contents of existing buffers rather than creating + returning new objects.
# See the example below of reading a binary file with equally sized records

record_size = 32           # Size of each record (adjust value)

buf = bytearray(record_size)
with open('somefile', 'rb') as f:
    while True:
        n = f.readinto(buf)
        if n < record_size:
            break
        # Use the contents of buf

# Can also use memoryview() to make zero-copy slices of an existing buffer and modify it.

buf # Returns bytearray(b'Hello World')
m1 = memoryview(buf)
m2 = m1[-5:]
m2 # Returns <memory>
m2[:] = b'WORLD' # Modifies to bytearray(b'Hello WORLD')

# Always remember to check the return code of readinto(), the number of bytes read.
# If smaller than supplied, could suggest truncated or corrupted data.

# Look into recv_into(), pack_into(), etc.