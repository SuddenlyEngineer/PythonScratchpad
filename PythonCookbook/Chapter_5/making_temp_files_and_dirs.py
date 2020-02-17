from tempfile import TemporaryFile
from tempfile import TemporaryDirectory
import tempfile

with TemporaryFile('w+t') as f: # Make an unnamed temporary file. +t is text, +b is binary
    f.write('Hello World\n') # Read/Write to the file.
    f.write('Testing')

    f.seek(0) # Seek back to the beginning and read the data.
    data = f.read()

# Temp file is destroyed now.
f = TemporaryFile('w+t') # Use the temporary file.
f.close() # Manually destroy it. 

with TemporaryFile('w+t', encoding='utf-8', errors='ignore') as f: # Same arguments as open()
    print('blah')

# UNIX: the temp file won't have a name or directory entry. Fix with NamedTemporaryFile()

from tempfile import NamedTemporaryFile

with NamedTemporaryFile('w+t') as f:
    print('filename is:', f.name)

# File now destroyed. The f.name attribute contains the filename. 
# Try the delete=False kwarg to prevent the temp file from being auto deleted.

with NamedTemporaryFile('w+t', delete=False) as f:
    print('filename is:', f.name)

with TemporaryDirectory() as dirname: # Similar syntax for directories.
     print('dirname is:', dirname) # Use the directory here

# Directory and contents destroyed

# For lower-level ops, use mkstemp and mkdtemp. These don't take care of proper managament (cleanup, only returns raw OS file descriptors, etc.)
tempfile.mkstemp()
tempfile.mkdtemp()

# Use gettempdir() to find the location of where these files are being created.
tempfile.gettempdir()

# Have some more kwargs
f = NamedTemporaryFile(prefix='mytemp', suffix='.txt', dir='/tmp')
f.name # Might return '/tmp/mytemp8ee899.txt'