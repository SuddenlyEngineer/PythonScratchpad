from Data_Structures_and_Algorithms.Chapter_10.SortedTableMap import SortedTableMap

class CostPerformanceDatabase(SortedTableMap):
    '''Maintain a database of maximal (cost, performance) pairs.'''
    def __init__(self):
        '''Create an empty db.'''
        self._M = SortedTableMap() # Or another more efficient sorted map

    def best(self, c):
        '''Return (cost, performance) pair with largest cost not exceeding c. Return None if none exists.'''
        return self._M.find_le(c)

    def add(self, c, p):
        '''Add new entry with cost c and performance p. Start by determining if (c, p) is dominated by an existing pair.'''
        other = self._M.find_le(c) # Other is at least as cheap as c
        if other is not None and other[1] >= p: # If its performance is as good,
            return # (c,p) is dominated, so ignore
        self._M[c] = p  # else, add (c,p) to database
        other = self._M.find_gt(c) # and now remove any pairs that are dominated by (c, p). other more expensive than c.
        while other is not None and other [1] <= p:
            del self._M[other[0]]
            other = self._m.find_gt(c)