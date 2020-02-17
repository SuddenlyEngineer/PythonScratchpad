# Just use the file keyword argument to print()
with open('somefile.txt', 'wt') as f:
    print('hello world', file=f)

# Only works if file open in text, not binary, mode.