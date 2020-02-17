# Need to read/write text data in different encodings? Start with open()

with open('somefile.txt', 'rt') as f: # Read the entire file as a single string
    data = f.read()

with open('somefile.txt', 'rt') as f: # Iterate over the lines of the file
    for line in f:
        # Process lines here
        print('blah')

text1 = ' '
text2 = ' '
line1 = ' '
line2 = ' '

with open('somefile.txt', 'wt') as f: # Write chunks of text data, can append with 'at'
    f.write(text1)
    f.write(text2)

with open('somefile.txt', 'wt') as f: # Redirected print statement
    print(line1, file=f)
    print(line2, file=f)

# By default, files are read/written using sys.getdefaultencoding(), usually utf-8

with open('somefile.txt', 'rt', encoding='latin-1') as f:
    print('blah')

# If you don't use the with statement to establish a context for the file use, the file must be manually closed.

f = open('somefile.txt', 'rt')
data = f.read()
f.close()

# Python default to universal newline mode, where all common newline conventions are recognized and converted into a single \n while reading. 
# Disable this with the newline='' argument to open()

f = open('hello.txt', 'rt') #  Newline translation enabled (the default)
f.read() # Returns 'hello world!\n'

g = open('hello.txt', 'rt', newline='') # Newline translation disabled
g.read() # Returns 'hello world!\r\n' # Note this assumes a Windows-encoded file.

# A UnicodeDecodeError is raised usually when the file isn't read with the correct encoding.
# Can also supply an optional errors argument to open() to deal with the errors.
f = open('sample.txt', 'rt', encoding='ascii', errors='replace') # Replace bad chars with Unicode U+fffd replacement char
f.read() # Returns 'Spicy Jalape?o!'
g = open('sample.txt', 'rt', encoding='ascii', errors='ignore') # Ignore bad chars entirely
g.read() # Returns 'Spicy Jalapeo!'