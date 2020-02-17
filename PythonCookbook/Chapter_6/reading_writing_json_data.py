import json
from pprint import pprint
from urllib.request import urlopen
from collections import OrderedDict

data = {
   'name' : 'ACME',
   'shares' : 100,
   'price' : 542.23
}

json_str = json.dumps(data) # Mirrors other serialization libraries, like pickle.

data = json.loads(json_str) # And back into a Python data structure.

# Use dump and load if working with files instead of strings.

with open('data.json', 'w') as f: # Writing JSON data.
     json.dump(data, f)

with open('data.json', 'r') as f: # Reading JSON data.
     data = json.load(f)

# JSON supports None, bool, int, float, str, lists, tuples, and dictionaries.
# Dict keys assumed to be strings (and non strings converted when encoded)
# Spec calls for lists and dictionaries only for encoding. 
# Web app standard practice has the top-level ovject as a dictionary.
# Note True is true, False is false, and None is null. 

json.dumps(False) # Returns 'false'
d = {'a': True,
      'b': 'Hello',
      'c': None}

json.dumps(d) # Returns '{"b": "Hello", "c": null, "a": true}'

# An exmaple of dumping JSON and alphabetizing keys and output a dictionary. 
u = urlopen('http://search.twitter.com/search.json?q=python&rpp=5')
resp = json.loads(u.read().decode('utf-8'))
pprint(resp)

# Normally JSON will create dicts or lists from the supplied data. Use object_pairs_hook or object-hook to json.loads()
# Here's how to encode JSON data, preserving order in OrderedDict.

s = '{"name": "ACME", "shares": 50, "price": 490.1}'
data = json.loads(s, object_pairs_hook=OrderedDict) # Returns OrderedDict([('name', 'ACME'), ('shares', 50), ('price', 490.1)])

# Or to turn a JSON dictionary into a Python object:
class JSONObject:
    def __init__(self, d):
        self.__dict__ = d # Dictionary passed to the object; free to use as the object's instance dict.

data = json.loads(s, object_hook=JSONObject)
data.name # Returns 'ACME'
data.shares # Returns 50
data.price # Returns 490.1

# For encoding, use the indent argument to json.dumps() for similar output to pprint()
print(json.dumps(data)) # {"price": 542.23, "name": "ACME", "shares": 100}, versus
print(json.dumps(data, indent=4)) 

# Wanna sort keys on output? Use sort_keys
print(json.dumps(data, sort_keys=True)) #{"name": "ACME", "price": 542.23, "shares": 100}

# Can't normally serialize instances as JSON
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

def serialize_instance(obj): # Takes instance as input, returns serializable dictionary. 
    d = { '__classname__' : type(obj).__name__ }
    d.update(vars(obj))
    return d

classes = { # Dictionary mapping names to known classes
    'Point' : Point
}

def unserialize_object(d): # Returns an instance from a dictionary.
    clsname = d.pop('__classname__', None)
    if clsname:
        cls = classes[clsname]
        obj = cls.__new__(cls)   # Make instance without calling __init__
        for key, value in d.items():
            setattr(obj, key, value)
            return obj
    else:
        return d

p = Point(2,3)
s = json.dumps(p, default=serialize_instance) # Returns '{"__classname__": "Point", "y": 3, "x": 2}'
a = json.loads(s, object_hook=unserialize_object) # Returns <__main__.Point object>
a.x # Returns 2
a.y # Returns 3