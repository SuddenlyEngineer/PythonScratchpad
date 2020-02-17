import urllib.request
import io
import sys

u = urllib.request.urlopen('http://www.python.org')
f = io.TextIOWrapper(u,encoding='utf-8') # Adds Unicode encoding/decoding to an existing object.
text = f.read()

# To change the encoding of an already open text-mode file, use its detach() method to remove existing encoding before replacing it.
sys.stdout.encoding # Should give 'UTF-8'
sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='latin-1')
sys.stdout.encoding # Now gives 'latin-1'

f = open('sample.txt','w') # The I/O system is built as a series of layers. 
f # <_io.TextIOWrapper name='sample.txt' mode='w' encoding='UTF-8'>
f.buffer # <_io.BufferedWriter name='sample.txt'>
f.buffer.raw # <_io.FileIO name='sample.txt' mode='wb'>

