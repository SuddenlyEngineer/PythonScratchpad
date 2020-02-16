from fnmatch import fnmatch, fnmatchcase # Only two functions, but good practice. 
# This lets you use Unix shell wildcards.

fnmatch('foo.txt', '*.txt') # True
fnmatch('foo.txt', '?oo.txt') # True
fnmatch('Dat45.csv', 'Dat[0-9]*') # True

# Note that fnmatch() matches patterns using the same case-sensitivity rules as the system's underlying file system/

fnmatch('foo.txt', '*.TXT') # False on OS X, True on Windows

# If the distinction matters, use fnmatchcase()

fnmatchcase('foo.txt', '*.TXT') # False on everything

# You can use this to process nonfilename strings as well.

addresses = [
    '5412 N CLARK ST',
    '1060 W ADDISON ST',
    '1039 W GRANVILLE AVE',
    '2122 N CLARK ST',
    '4802 N BROADWAY',
]

[addr for addr in addresses if fnmatchcase(addr, '* ST')] # ['5412 N CLARK ST', '1060 W ADDISON ST', '2122 N CLARK ST']
[addr for addr in addresses if fnmatchcase(addr, '54[0-9][0-9]')] # ['5412 N CLARK ST']

# This is a good middle point between simple string methods and full regex for allowing wildcards.