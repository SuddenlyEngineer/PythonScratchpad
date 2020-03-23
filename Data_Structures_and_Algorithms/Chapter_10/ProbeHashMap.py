from Data_Structures_and_Algorithms.Chapter_10.HashMapBase import HashMapBase

class ProbeHashMap(HashMapBase):
    '''Hash map implemented with linear probing for collision resolution.'''
    _AVAIL = object() # Sentinal marks locations of previous deletions

    def _is_available(self, j):
        '''Return True if index j is available in table.'''
        return self._table[j] is None or self._table[j] is ProbeHashMap._AVAIL
    
    def _find_slot(self, j, k):
        '''Search for key k in bucket at index j/
        Return (success, index) tuple, described as follows:
        If match was found, success is True and index denotes its location.
        If no match found, success is False and index denotes first available slot.'''
        firstAvail = None
        while True:
            if self._is_available(j):
                if firstAvail is None:
                    firstAvail = j # Mark this as first avail
                if self._table[j] is None:
                    return (False, firstAvail) # Search has failed
            elif k == self._table[j]._key:
                return (True, j) # Found a match
            j = (j + 1) % len(self._table) # Keep looking (cyclically)

    def _bucket_getitem(self, j, k):
        found, s = self._find_slot(j, k)
        if not found:
            raise KeyError(f'Key Error: {repr(k)}') # No match found
        self._table[s] = ProbeHashMap._AVAIL # Mark as vacated

    def __iter__(self):
        for j in range(len(self._table)): # Scan entire table
            if not self._is_available(j):
                yield self._table[j]._key