def dedupe(items):
    seen = set()
    for item in items:
        if item not in seen:
            yield item
            seen.add(item)

def dedupe_unhashable(items, key=None):
    seen = set()
    for item in items:
        val = item if key is None else key(item)
        if val not in seen:
            yield item
            seen.add(val)

a = [1, 5, 2, 1, 9, 1, 5, 10]
list(dedupe(a))

a = [ {'x':1, 'y':2}, {'x':1, 'y':3}, {'x':1, 'y':2}, {'x':2, 'y':4}]

list(dedupe_unhashable(a, key=lambda d: (d['x'],d['y'])))
list(dedupe_unhashable(a, key=lambda d: d['x']))

"""Using a set will eliminate duplicates, if order doesn't matter. 
The above solution fixes the ordering issue"""

# with open(somefile,'r') as f:
#   for line in dedupe(f):