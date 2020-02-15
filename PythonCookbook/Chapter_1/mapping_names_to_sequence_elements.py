from collections import namedtuple #Tuple where elements accessible by name

Subscriber = namedtuple('Subscriber', ['addr', 'joined'])
sub = Subscriber(addr='jonesy@example.com', joined='2012-10-19')
sub
sub.addr
sub.joined

len(sub) # Namedtuple looks like a class, is a tuple subclass.
addr, joined = sub #Hence indexing and unpacking work.
addr
joined

# This decouples code from the position of elements it manipulates.
# This way, you can add columns to data sets but still have old code work.

""" def compute_cost(records):
    total = 0.0
    for rec in records:
        total += rec[1] * rec[2]
    return total """

Stock = namedtuple('Stock', ['name', 'shares', 'price'])

def compute_cost(records):
    total = 0.0
    for rec in records:
        s  = Stock(*rec) 
        total += s.shares * s.price
    return total

# If the records sequence already contained such instances, you could avoid the explicit conversion to the Stock namedtuple.

# Namedtuples can replace dictionaries and save memory. However, unlike dictionaries, these are immutable.
# If an attribute must be changed, can use _replace(), which makes an entirely new namedtuple with values replaced.

s = Stock('ACME', 100, 123.45)
s
# s.shares = 75 # NOT POSSIBLE
s = s._replace(shares=75)
s

# _replace() can also populate namedtuples with optional/missing fields
# Create a prototype tuple with default values, then use _replace to create new instances

Stock = namedtuple('Stock', ['name', 'shares', 'price', 'date', 'time'])

# Create the prototype
stock_prototype = Stock('', 0, 0.0, None, None)

# Function to convert dictionary to stock
def dict_to_stock(s):
    return stock_prototype._replace(**s) # ** unpacks a dictionary

a = {'name': 'ACME', 'shares': 100, 'price': 123.45}
dict_to_stock(a)
b = {'name': 'ACME', 'shares': 100, 'price': 123.45, 'date': '12/17/2012'}
dict_to_stock(b)

# If your goal is to define an efficient data structure where you will be changing various 
# instance attributes, define a class using __slots__ instead.

