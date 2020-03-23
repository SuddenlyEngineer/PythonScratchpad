from collections.abc import MutableMapping

class MapBase(MutableMapping):
    '''Our own abstract base class that includes a nonpublic _Item class.'''
    __slots__ = '_key', '_value'

    class _Item:

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __eq__(self, other):
            return self._key == other._key # Compare items based on their keys

        def __ne__(self, other):
            return not (self == other) # Opposite of __eq__

        def __lt__(self, other):
            return self._key < other._key # Compare items based on their keys