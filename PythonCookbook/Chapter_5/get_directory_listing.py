import os
import os.path
import glob
from fnmatch import fnmatch

names = os.listdir('somedir') # Gets all files in the directory, including subdirs, symbolic links, etc.

names = [name for name in os.listdir('somedir') # Get all regular files
         if os.path.isfile(os.path.join('somedir', name))]

dirnames = [name for name in os.listdir('somedir') # Get all directories
            if os.path.isdir(os.path.join('somedir', name))]

pyfiles = [name for name in os.listdir('somedir') # A filtering example
           if name.endswith('.py')]

pyfiles = glob.glob('somedir/*.py') # Using the glob module
pyfiles = [name for name in os.listdir('somedir') # Using the fnmatch module
           if fnmatch(name, '*.py')]

pyfiles = glob.glob('*.py')

name_sz_date = [(name, os.path.getsize(name), os.path.getmtime(name)) # Get file sizes and modification dates
                for name in pyfiles]

for name, size, mtime in name_sz_date:
    print(name, size, mtime)

file_metadata = [(name, os.stat(name)) for name in pyfiles] # Alternative: Get file metadata
for name, meta in file_metadata:
    print(name, meta.st_size, meta.st_mtime)