import collections


class StrKeyDict(collections.UserDict):  # StrKeyDict extends UserDict.

    def __missing__(self, key):  
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)]

    def __contains__(self, key): # __contains__ is simpler: we can assume all stored keys are str and we can check on self.data instead of invoking self.keys() as we did in StrKeyDict0.
        return str(key) in self.data  

    def __setitem__(self, key, item): # __setitem__ converts any key to a str. This method is easier to overwrite when we can delegate to the self.data attribute.
        self.data[str(key)] = item   

# Because UserDict subclasses MutableMapping, the remaining methods that make StrKeyDict a full-fledged mapping are inherited from UserDict, MutableMapping, or Mapping. 

# https://github.com/fluentpython/example-code Look up TransformDict