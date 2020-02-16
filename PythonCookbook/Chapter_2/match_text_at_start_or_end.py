import os
import re
from urllib.request import urlopen

filename = 'spam.txt'
filename.endswith('.txt') # True
filename.startswith('file:') # False
url = 'http://www.python.org'
url.startswith('http:') # True

# Need to check against multiple choices? Provide a tuple

filenames = os.listdir('.')
filenames # Assume [ 'Makefile', 'foo.c', 'bar.py', 'spam.c', 'spam.h' ]
[name for name in filenames if name.endswith(('.c', '.h'))] # ['foo.c', 'spam.c', 'spam.h' ]
any(name.endswith('.py') for name in filenames) # True

def read_data(name):
    if name.startswith(('http:', 'https:', 'ftp:')):
        return urlopen(name).read()
    else:
        with open(name) as f:
            return f.read()

choices = ['http:', 'ftp:']
# url.startswith(choices) # Gives TypeError
url.startswith(tuple(choices)) # startswith requires an input tuple

# You could use slices instead of startswith() and endswith(), but it's gross

fileame = 'spam.txt'
filename[-4:] == '.txt' # Returns True
url[:5] == 'http:' or url[:6] == 'https:' or url[:4] == 'ftp:' # Returns True

# You could also use regex, but that's overkill and less performant
re.match('http:|https:|ftp:', url)

# The startswith() / endswith() methods can be combined with other operations, too.
# For example, checking a dictionary for the presence of certain kinds of files
# if any(name.endswith(('.c', '.h')) for name in listdir(dirname)):