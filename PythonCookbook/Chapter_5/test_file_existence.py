import os
import time
os.path.exists('/etc/passwd') # Should return True
os.path.exists('/tmp/spam') # False
os.path.isfile('/etc/passwd') # Is a regular file
os.path.isdir('/etc/passwd') # Is a directory
os.path.islink('/usr/local/bin/python3') # Is a symbolic link
os.path.realpath('/usr/local/bin/python3') # Get the file linked to.
os.path.getsize('/etc/passwd') # Gets size metadata
os.path.getmtime('/etc/passwd') # Gets modified time.
time.ctime(os.path.getmtime('/etc/passwd')) # Convert from seconds to local time.memoryview

# Watch out for permissions errors!