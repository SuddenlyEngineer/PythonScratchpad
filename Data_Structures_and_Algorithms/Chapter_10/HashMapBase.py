from Data_Structures_and_Algorithms.Chapter_10.MapBase import MapBase
from random import randrange

class HashMapBase(MapBase):
    '''Abstract base class for map using hash-table with MAD compression.'''

    def __init__(self, cap=11, p=109345121):
        '''Create an empty hash-table map'''
        self._table = cap * [None]
        self._n = 0 # Numbers of entries in the map
        self._prime = p # Prime for MAD compression
        self._scale = 1 + randrange(p-1) # Scale from 1 to p-1 for MAD
        self._shift = randrange(p) # Shift from 0 to p-1 for MAD

    def _hash_function(self, k):
        return (hash(k)*self._scale + self._shift) % self._prime % len(self._table)

    def __len__(self):
        return self._n

    def __getitem__(self, k):
        j = self._hash_function(k)
        return self._bucket_getitem(j, k) # May raise KeyError
    
    def __setitem__(self, k, v): 
        j = self._hash_function(k)
        self._bucket_setitem(j, k, v) # Subroutine maintains self._n
        if self._n > len(self._table) // 2: # Keep load factor <= 0.5
            self._resize(2 * len(self._table) - 1) # Number 2^x-1 is often prime

    def __delitem__(self, k):
        j = self._hash_function(k)
        self._bucket_delitem(j,k) # May raise KeyError
        self._n -= 1

    def _resize(self, c): # Resize bucket array to capacity c.
        old = list(self.items()) # Use iteration to record existing items.
        self._table = c * [None] # Then reset table to desired capacity.
        self._n = 0 # N recomputed during subsequent adds.
        for (k,v) in old:
            self[k] = v # Reinsert old key-value pair.