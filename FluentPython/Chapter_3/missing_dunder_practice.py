class StrKeyDict0(dict): # StrKeyDict0 inherits from dict.

    def __missing__(self, key): # Check whether key is already a str. If it is, and it’s missing, raise KeyError.
        if isinstance(key, str):
            raise KeyError(key)
        return self[str(key)] # Build str from key and look it up.

    def get(self, key, default=None):
        try:
            return self[key] # The get method delegates to __getitem__ by using the self[key] notation; that gives the opportunity for our __missing__ to act.
        except KeyError:
            return default # If a KeyError was raised, __missing__ already failed, so we return the default.

    def __contains__(self, key): # Search for unmodified key (the instance may contain non-str keys), then for a str built from the key.
        return key in self.keys() or str(key) in self.keys()

d = StrKeyDict0([('2', 'two'), ('4', 'four')])

'''Without the test isinstance(key, str), our __missing__ method would work OK for any key k —str or not str— whenever str(k) produced an existing key. 
But if str(k) is not an existing key, we’d have an infinite recursion. The last line, self[str(key)] would call __getitem__ passing that str key, 
which in turn would call __missing__ again.

The __contains__ method is also needed for consistent behavior in this example, because the operation k in d calls it, but the method inherited 
from dict does not fall back to invoking __missing__. There is a subtle detail in our implementation of __contains__: we do not check for the key 
in the usual Pythonic way—k in my_dict—because str(key) in self would recursively call __contains__. We avoid this by explicitly looking up 
the key in self.keys().
'''