import sys

# Your program received a directory listing, but when it tried to print the filenames, it crashed with a UnicodeEncodeError exception and a cryptic message about “surrogates not allowed.”

# Easy enough to fix, use this convention:
def bad_filename(filename):
    return repr(filename)[1:-1]

'''try:
    print(filename)
except UnicodeEncodeError:
    print(bad_filename(filename))'''

# This works around files not encoded with the filesystem encoding.

def bad_filename(filename): # Could also re-encode the bad filename.
    temp = filename.encode(sys.getfilesystemencoding(), errors='surrogateescape')
    return temp.decode('latin-1')