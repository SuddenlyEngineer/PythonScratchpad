import itertools  # PEP 8 recommends coding imports from the standard library above imports of personal modules.

from tombola import Tombola
from bingo import BingoCage


class AddableBingoCage(BingoCage): # Extends BingoCage

    def __add__(self, other):
        if isinstance(other, Tombola): # Out __add__ will only work with an instance of Tombola as the second operand
            return AddableBingoCage(self.inspect() + other.inspect())
        else:
            return NotImplemented

    def __iadd__(self, other):
        if isinstance(other, Tombola):
            other_iterable = other.inspect() # Retrieve items from other if it is an instance of Tombola.
        else:
            try:
                other_iterable = iter(other) # Otherwise try to iterate over other
            except TypeError: # If that fails, raise an exception explaining what the user should do.
                self_cls = type(self).__name__
                msg = "right operand in += must be {!r} or an iterable"
                raise TypeError(msg.format(self_cls))
        self.load(other_iterable) # If we got this far, we can load the other iterable into self.
        return self # Very important: augmented assignment special methods must return self.