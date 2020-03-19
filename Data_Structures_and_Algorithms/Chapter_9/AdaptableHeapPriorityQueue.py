from Data_Structures_and_Algorithms.Chapter_9.HeapPriorityQueue import HeapPriorityQueue

class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    '''A locator-based priority queue implemented with a binary heap.'''

    class Locator(HeapPriorityQueue._Item):
        '''Token for locating an entry of the priority queue.'''
        __slots__ = '_index' # Add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k,v)
            self._index = j

    def _swap(self, i, j): # Override swap to record new indices
        super()._swap(i,j) # Perform the swap
        self._data[i]._index = i # Reset locator index (post-swap)
        self._data[j]._index = j # Reset locator index (post-swap)

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        '''Add a key-value pair.'''
        token = self.Locator(key, value, len(self._data)) # Initialize locator index
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc, newkey, newval):
        '''Update the key and value for the entry identified by Locator loc.'''
        j = loc._index
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError('Invalid Locator')
        if j == len(self) - 1: # item at last position
            self.data.pop() # just remove it
        else:
            self.swap(j, len(self) - 1) # swap item to the last position
            self._data.pop() # remove it from the list
            self._bubble(j) # fix item displaced by the swap
        return (loc._key, loc._value)