class SortedTableMap(MapBase):
    '''Map implementation using a sorted table.'''
    def _find_index(self, k, low, high):
        '''Return index of the leftmost item with key greater than or equal to k. Return high + 1 if no such item qualifies.
        That is, j will be returned such that all items of slice table[low:j] have key < k and all items of slice table[j:high+1] have key >= k.'''
        if high < low:
            return high + 1 # no item qualifies
        else:
            mid = (low + high) // 2
            if k == self._table[mid]._key:
                return mid # found exact match
            elif k < self._table[mid]._key:
                return self._find_index(k, low, mid - 1) # may return mid
            else:
                return self._find_index(k, mid + 1, high) # answer is right of mid
    
    def __init__(self):
        self._table = [] # Create an empty map.
    
    def __len__(self):
        return len(self._table) # Return number of items in the map.
    
    def __getitem__(self, k):
        '''Return value associated with key k, else raise KeyError.'''
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        return self._table[j]._value

    def __setitem__(self, k, v):
        '''Assign value v to key k, overwriting existing value if present.'''
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            self._table[j]._value = v # Reassign value
        else:
            self._table[j].insert(j, self._Item(k,v)) # Adds new item

    def __delitem(self, k):
        '''Remove item associated with key k (raise KeyError if not found).'''
        j = self._find_index(k, 0, len(self._table) - 1)
        if j == len(self._table) or self._table[j]._key != k:
            raise KeyError('Key Error: ' + repr(k))
        self._table.pop(j) # Delete item

    def __iter__(self):
        '''Generate keys of the map ordered from minimum to maximum.'''
        for item in self._table:
            yield item._key

    def __reversed__(self):
        '''Generate keys of the map ordered from maximum to minumum.'''
        for item in reversed(self._table):
            yield item._key

    def find_min(self):
        '''Return (key, value) pair with minimum key (or None if empty).'''
        if len(self._table) > 0:
            return (self._table[0]._key, self._table[0]._value)
        else:
            return None

    def find_max(self):
        '''Return (key, value) pair with maximum key (or None if empty.)'''
        if len(self._table) > 0:
            return (self._table[-1]._key, self._table[-1]._value)
        else:
            return None
    
    def find_ge(self, k):
        '''Return (key, value) pair with least key greater than or equal to k.'''
        j = self._find_index(k, 0, len(self._table) - 1) # j's key >= k
        if j < len(self._table):
            return (self._table[j]._key, self.table[j]._value)
        else:
            return None

    def find_le(self, k):
        '''Return (key, value) pair with least key less than or equal to k.'''
        j = self._find_index(k, 0, len(self._table) - 1) # j's key >= k
        if j > 0:
            return (self._table[j]._key, self.table[j]._value)
        else:
            return None
    
    def find_lt(self, k):
        '''Return (key, value) pair with greatest key strictly less than k.'''
        j = self._find_index(k, 0, len(self._table) - 1) # j's key >= k
        if j > 0:
            return (self._table[j-1]._key, self.table[j-1]._value) # Note use of j-1
        else:
            return None

    def find_gt(self, k):
        '''Return (key, value) pair with greatest key strictly greater than k.'''
        j = self._find_index(k, 0, len(self._table) - 1) # j's key >= k
        if j < len(self._table) and self._table[j]._key == k:
            j+= 1 # Advanced past match
        if j < len(self._table):
            return (self._table[j]._key, self.table[1]._value)
        else:
            return None

    def find_range(self, start, stop):
        '''Iterate all (key, value) pairs such that start <= key < stop.
        If start is None, iteration begins with minimum key of map.
        If stop is None, iteration continues through the maxmimum key of map.'''
        if start is None:
            j = 0
        else:
            j = self._find_index(start, 0, len(self._table) - 1) # Find first result
        while j < len(self._table) and (stop is None or self._table[j]._key < stop):
            yield (self._table[j]._key, self._table[j]._value)
            j += 1