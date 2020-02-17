import array

# Reading/Writing binary data is simple, just use 'rb' and 'wb'

with open('somefile.bin', 'rb') as f: # Read the entire file as a single byte string
    data = f.read()

with open('somefile.bin', 'wb') as f: # Write binary data to a file
    f.write(b'Hello World')

# All data returned is byte strings, not text strings. When writing, supply data with
# byte strings, bytearray objects, etc. Also remember indexing and iteration return
# integer byte values instead of bute strings.

# Remember to decode/encode text when reading/writing to/from a binary file.

with open('somefile.bin', 'rb') as f:
    data = f.read(16)
    text = data.decode('utf-8')

with open('somefile.bin', 'wb') as f:
    text = 'Hello World'
    f.write(text.encode('utf-8'))

nums = array.array('i', [1, 2, 3, 4]) # Arrays and C structures can be used for writing without intermediate conversion to a bytes object.
with open('data.bin','wb') as f: # Does this by exposing the buffer interface, which binary data supports.
    f.write(nums)

a = array.array('i', [0, 0, 0, 0, 0, 0, 0, 0])
with open('data.bin', 'rb') as f:
    f.readinto(a) # Reads data directly into underlying memory, returns array('i', [1, 2, 3, 4, 0, 0, 0, 0])

