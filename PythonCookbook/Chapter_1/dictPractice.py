from collections import defaultdict
from collections import OrderedDict
import json

"""Recipies 1.6 through 1.9"""

d = defaultdict(list)
d['a'].append(1)
d['a'].append(2)
d['b'].append(4)

e = defaultdict(set)
e['a'].add(1)
e['a'].add(2)
e['a'].add(4)

# f = defaultdict(list)
# for key, value in pairs:
#     d[key].append(value)

f = OrderedDict()
f['foo'] = 1
f['bar'] = 2
f['spam'] = 3
f['grok'] = 4

for key in f:
    print(key, f[key])

json.dumps(f)

prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

min_price = min(zip(prices.values(), prices.keys()))
max_price = max(min(zip(prices.values(), prices.keys())))
prices_sorted = sorted(zip(prices.values(), prices.keys()))
prices_and_names = zip(prices.values(), prices.keys())

min_price_2 = prices(min(prices, key=lambda k: prices[k]))

a = {
   'x' : 1,
   'y' : 2,
   'z' : 3
}

b = {
   'w' : 10,
   'x' : 11,
   'y' : 2
}

a.keys() & b.keys() # Keys in common
a.keys() - b.keys() # Keys in a not in b
a.items() & b.items() # Common key, value pairs
c = {key:a[key] for key in a.keys() - {'z', 'w'}} # Makes a new dictionary with certain keys removed