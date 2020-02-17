import os
path = '/Users/beazley/Data/data.csv'

os.path.basename(path) # Get the last component of the path, 'data.csv'
os.path.dirname(path) # Get the directory name, '/Users/beazley/Data'
os.path.join('tmp', 'data', os.path.basename(path)) # Joins path components together, 'tmp/data/data.csv'

path = '~/Data/data.csv'
os.path.expanduser(path) # Expand the user's home directory, '/Users/beazley/Data/data.csv'
os.path.splitext(path) # Split the file extension, ('~/Data/data', '.csv')