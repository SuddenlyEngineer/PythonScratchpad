from Data_Structures_and_Algorithms.Chapter_7.PositionalList import PositionalList

class FavoritesList(PositionalList):
    '''List of elements ordered from most frequently accessed to least.'''

    class _Item:
        __slots__ = '_value', '_count' # For memory usage
        def __init__(self, e):
                self._value = e # The user's element
                self._count = 0 # Access count
            
    def _find_position(self, e):
        '''Search for element and return its Pisition (or None if not found).'''
        walk = self._data.first()
        while walk is not None and walk.element()._value != e:
            walk = self._data.after(walk)
        return walk

    def _move_up(self, pos):
        '''Move item at Position pos earlier in the list based on access count.'''
        if pos != self._data.first(): # Consider moving
            cnt = pos.element()._count
            walk = self._data.before(pos)
            if cnt > walk.element()._count: # Must shift forward
                while (walk != self._data.first() and cnt > self._data.before(walk).element()._count):
                    walk = self._data.before(walk)
                self._data.add_before(walk, self._data.delete(pos)) # Delete / reinsert

    def __init__(self):
        self._data = PositionalList() # Will be list of _Item instances

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def access(self, e): 
        '''Access element e, thereby increasing its access count.'''
        pos = self._find_position(e) # Try to locate existing element
        if pos is None:
            pos = self._data.add_last(self._Item(e)) # Place at end if new
        p.element()._count += 1
        self._move_up(pos) # Consider moving forward.

    def remove(self, e):
        '''Remove element e from the list of favorites.'''
        pos = self._find_position(e) # Try to locate element
        if pos is not None:
            self._data.delete(pos) # Delete if found

    def top(self, k):
        '''Generate sequence of top k elements in terms of access count.'''
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        walk = self._data.first()
        for j in range(k):
            item = walk.element() # Element of list is _Item
            yield item._value # Report user's element
            walk = self._data.after(walk)