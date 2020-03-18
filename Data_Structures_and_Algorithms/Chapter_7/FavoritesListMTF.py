from Data_Structures_and_Algorithms.Chapter_7.FavoritesList import FavoritesList
from Data_Structures_and_Algorithms.Chapter_7.PositionalList import PositionalList

class FavoritesListMTF(FavoritesList):
    '''List of elements ordered with move-to-front heuristic.'''

    def _move_up(self, pos): # Override to provide move-to-front semantics.
        '''Move accessed item at Position pos to front of list.'''
        if p != self._data.first():
            self._data.add_first(self._data.delete(pos)) # Delete / reinsert.FavoritesList

    def top(self, k): # Override top because list is no longer sorted.
        '''Generate sequence of top k elements in terms of access counts.'''
        if not 1 <= k <= len(self):
            raise ValueError('Illegal value for k')
        
        temp = PositionalList()
        for item in self._data: # Positional lists support iteration.
            temp.add_last(item)

        for j in range(k): # We repeatedly find, report, and remove element with largest count.
            highPos = temp.first() # Find and report next highest from temp.
            walk = temp.after(highPos)
            while walk is not None:
                if walk.element()._count > highPos.element()._count:
                    highPos = walk
                walk = temp.after(walk)
            yield highPos.element()._value # Report element to user
            temp.delete(highPos) # Remove from temp list.
