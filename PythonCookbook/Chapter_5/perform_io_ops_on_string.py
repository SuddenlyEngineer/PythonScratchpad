import io

# Need to feed text / binary strings to code that wants file-like objects? 
# Use io.StringIO() or io.BytesIO() to create objects that operate on string data

s = io.stringIO()
s.write('Hello World\n') # Returns 12
print('This is a test', file=s) # Returns 15
s.getvalue() # Gets all of the data written so far, returns 'Hello World\nThis is a test\n'

s = io.StringIO('Hello\nWorld\n') # Wraps a file interface around an existing string.
s.read(4) # Returns Hell
s.read() # Returns 'o\nWorld\n'

# Using binary data? Time for BytesIO
s = io.BytesIO()
s.write(b'binary data')
s.getvalue() # Returns b'binary data'

# In unit tests, these functions are valuable. But without a proper integer file-descriptor,
# They do not work with code that requires a real file like file, pipes, or sockets.