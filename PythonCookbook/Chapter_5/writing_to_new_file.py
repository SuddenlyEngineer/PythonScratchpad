import os
# The easy solution, use x mode to open rather than w if you want to write data to a new file.

with open('somefile', 'wt') as f:
    f.write('Hello\n')

with open('somefile', 'xt') as f: # Can also use xb for binary.
    f. write('Hello\n') # Will cause a FileExistsError if a file exists.

# There is an alternative solution. 
if not os.path.exists('somefile'):
    with open('somefile', 'wt') as f:
        f.write('Hello\n')
else:
    print('File already exists!')