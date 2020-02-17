import sys
import os
sys.getfilesystemencoding() # Always start with the OS encoding.

# To bypass this encoding, specify a filename using a raw byte string instead.
with open('jalape\xf1o.txt', 'w') as f: # Write a file with a unicode filename
    f.write('Spicy!')

os.listdir # Directory listing (decoded), ['jalapeño.txt']
os.listdir(b'.') # Directory listing (raw), here a byte string, [b'jalapen\xcc\x83o.txt']

with open(b'jalapen\xcc\x83o.txt') as f: # Open file with raw filename
    print(f.read())