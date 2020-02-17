from functools import partial
# Wanna iterate over a collection of fixed-size records or chunks? Use iter() and functools.partial()
RECORD_SIZE = 32

with open('somefile.data', 'rb') as f:
    records = iter(partial(f.read, RECORD_SIZE), b'')
    for r in records:
        print('blah')

# The records object is an iterable that will producce chunks until file end.
# Last item may have fewer bytes than expected if the file size is not an exact multiple of the record size

# iter() can create an iterator if you pass it a callable and sentinal value.
# The iterator calls the callable over and over again until it returns the sentinal.

# functools.partial() creates a callable that reads a fixed number of bytes
# b'' is the sentinal that gets returned when a file is read but file end is reached.