import os

nums = [1, 2, 3, 4, 5]
s = sum(x * x for x in nums) #The elegant way to calculate the sum of squares

# Determine if any .py files exist in a directory
files = os.listdir('dirname')
if any(name.endswith('py') for name in files):
    print('There be python!')
else:
    print('Sorry, no python.')

# Output a tuple as CSV
s = ('ACME', 50, 123.45)
print(','.join(str(x) for x in s))

# Data reduction across fields of a data structure 
portfolio = [
   {'name':'GOOG', 'shares': 50},
   {'name':'YHOO', 'shares': 75},
   {'name':'AOL', 'shares': 20},
   {'name':'SCOX', 'shares': 65}
]
min_shares = min(s['shares'] for s in portfolio) # Returns 20

s = sum((x*x for x in nums)) # Pass generator-expr as argument
s = sum(x*x for x in nums) # More elegant, no?

s = sum([x * x for x in nums]) # Introduces an extra step and creates an extra list
# The generator transforms the data iteratively, much more memory efficient

# min() and max() accept a key, useful when considering using a generator

min_shares = min(portfolio, key=lambda s: s['shares']) # Returns {'name': 'AOL', 'shares': 20}