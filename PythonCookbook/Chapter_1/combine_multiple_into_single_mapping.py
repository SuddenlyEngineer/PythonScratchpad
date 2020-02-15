from collections import ChainMap

a = {'x': 1, 'z': 3 }
b = {'y': 2, 'z': 4 }

# Suppose you want to perform lookups that check both dictionaries
# Check a, then b if not found.

c = ChainMap(a,b)
print(c['x']) # Outputs 1 (from a)
print(c['y']) # Outputs 2 (from b)
print(c['z']) # Outputs 3 (from a)

# A ChainMap takes multiple mappings and makes them logically appear as one.
# They are not merged; a list of the underlying mappings is kept and common dictionary ops are redefined to scan the list.

len(c) # Outputs 3
list(c.keys()) # Outputs ['x', 'y', 'z']
list(c.values()) # Outputs [1, 2, 3]

# If keys are duplicated, first mapping values get used
# Hence, c['z'] will always hit dict a, not b

# Operations that mutate the mapping always affect the first mapping listed.

c['z'] = 10
c['w'] = 40
del c['x']
a # Outputs {'w': 40, 'z', 10}
# del c['y'] # Outputs KeyError: "Key not found in teh first mapping: 'y'"

# ChainMaps are also useful when working with scoped variables
values = ChainMap()
values['x'] = 1 
# Add a new mapping
values = values.new_child()
values['x'] = 2
# Add a new mapping
values = values.new_child()
values['x'] = 3
values # Outputs ChainMap({'x': 3}, {'x': 2}, {'x': 1})
values['x'] # Outputs 3
# Discard last mapping
values = values.parents
values['x'] # Outputs 2
# Discard last mapping
values = values.parents
values['x'] # Outputs 1
values # Outputs ChainMap({'x': 1})

# Could also consider merging dictionaries together with update()
a = {'x': 1, 'z': 3}
b = {'y': 3, 'z': 4}
merged = dict(b)
merged.update(a)
merged['x'] # 1
merged['y'] # 2
merged['z'] # 3

# Works, but requires creation of a separate dict object or destructively altering the existing.
# If any original dictionaries mutate, changes not reflected in merged.

a['x'] = 13
merged['x'] # Still 1

# ChainMaps use the original dictionaries, so they don't have this behavior.
a = {'x': 1, 'z': 3}
b = {'y': 3, 'z': 4}
merged = ChainMap(a, b)
merged['x'] # 1
a['x'] = 42
merged['x'] # Notice the change, returns 42.