from Data_Structures_and_Algorithms.Chapter_10.HashMapBase import HashMapBase
from Data_Structures_and_Algorithms.Chapter_10.UnsortedTableMap import UnsortedTableMap

class ChainHashMap(HashMapBase):
    def _bucket_getitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(f'Key Error: {repr(k)}') # No match found
        return bucket[k] # May raise KeyError
    
    def _bucket_setitem(self, j, k, v):
        if self._table[j] is None:
            self._table[j] = UnsortedTableMap() # Bucket is new to the table
        oldsize = len(self._table[j])
        self._table[j][k] = v
        if len(self._table[j]) > oldsize: # Key was new to the table
            self._n += 1 # Increase overall map size

    def _bucket_delitem(self, j, k):
        bucket = self._table[j]
        if bucket is None:
            raise KeyError(f'Key Error: {repr(k)}') # No match found
        del bucket[k] # May raise KeyError

    def __iter__(self):
        for bucket in self._table:
            if bucket is not None: # A nonempty slot
                for key in bucket:
                    yield key