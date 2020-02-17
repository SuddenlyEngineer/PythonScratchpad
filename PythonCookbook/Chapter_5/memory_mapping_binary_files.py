import os
import mmap

# This memory maps a binary file into a mutable byte array for random access or in place modifications.

def memory_map(filename, access=mmap.ACCESS_WRITE):
    size = os.path.getsize(filename)
    fd = os.open(filename, os.O_RDWR) # Open for reading and writing
    return mmap.mmap(fd, size, access=access)

# Use this to create an initial file and expand it to a desired size.
size = 1000000
with open('data', 'wb') as f:
    f.seek(size-1)
    f.write(b'\x00')

m = memory_map('data')
len(m) # Returns 1000000
m[0:10] # Returns b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
m[0] # Returns 0
m[0:11] = b'Hello World' # Reassign a slice
m.close()

with open('data', 'rb') as f:
    print(f.read(11)) # b'Hello World'

# Can also use the mmap object as a context manager, which closes the underlying file automatically.

with memory_map('data') as m:
    print(len(m)) # 1000000
    print(m[0:10]) # b'Hello World'

m.closed # Returns True

# m = memory_map(filename, mmap.ACCESS_READ) # Default opens a file for reading and writing, this is read only
# m = memory_map(filename, nmap.ACCESS_COPY) # Modifies data locally, but doesn't write changes back to the original file.

m = memory_map('data') # Instead of opening a file and using seek/read/write, use this
v = memoryview(m).cast('I') # Memoryview of unsigned integers.
v[0] = 7
m[0:4]  # Returns b'\x07\x00\x00\x00'
m[0:4] = b'\x07\x01\x00\x00'
v[0] # 263