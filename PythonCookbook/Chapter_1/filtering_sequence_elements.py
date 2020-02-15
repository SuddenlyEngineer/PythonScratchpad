import math
from itertools import compress

mylist = [1, 4, -5, 10, -7, 2, 3, -1]
[n for n in mylist if n > 0]
[n for n in mylist if n < 0]

# List comprehensions may produce large results given a large original input

pos = (n for n in mylist if n > 0) # Based generator object

for x in pos:
    print(x)

# But what about when the filter criteria can't be easily expressed in either?

values = ['1', '2', '-3', '-', 'N/A', '5']
def is_int(val): # Put the filter code into its own function
    try:
        x = int(val)
        return True
    except ValueError:
        return False

ivals = list(filter(is_int, values)) #Call with the filter() function.
print(ivals) #Outputs ['1', '2', '-3', '4', '5']

# Note that filter creates an iterator, so list() is required to make a list

[math.sqrt(n) for n in mylist if n > 0]

clip_neg = [n if n > 0 else 0 for n in mylist]
clip_pos = [n if n < 0 else 0 for n in mylist]

addresses = [
    '5412 N CLARK',
    '5148 N CLARK',
    '5800 E 58TH',
    '2122 N CLARK',
    '5645 N RAVENSWOOD',
    '1060 W ADDISON',
    '4801 N BROADWAY',
    '1039 W GRANVILLE',
]

counts = [ 0, 3, 10, 4, 1, 7, 6, 1]

#Make a list of all addresses where the corresponding count value was > 5
more5 = [n > 5 for n in counts]
more5
list(compress(addresses, more5))

# Creates a sequence of booleans that indicate which elements satisfy the condition
# Compress() then picks out the True items
# Returns an interator, so list() was needed
