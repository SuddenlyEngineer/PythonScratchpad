from Data_Structures_and_Algorithms.Chapter_9.PriorityQueueBase import PriorityQueueBase
from Data_Structures_and_Algorithms.Chapter_7.PositionalList import PositionalList

class SortedPriorityQueue(PriorityQueueBase): # Base class defines _Item
    '''A min-oriented priority queue implemented with a sorted list.'''

    def __init__(self):
        '''Create a new empty Priority Queue.'''
        self._data = PositionalList()
    
    def __len__(self):
        '''Return the number of items in the priority queue.'''
        return len(self._data)

    def add(self, key, value):
        '''Add a key-value pair.'''
        newest = self._Item(key, value) # Make new item instance
        walk = self._data.last() # Walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest) # New key is smallest
        else:
            self._data.add_after(walk, newest) # Newest goes after walk

    def min(self):
        '''Return but do not remove (k,v) tuple with minimum key.'''
        if self.is_empty():
            raise ValueError('Priority queue is empty.')
        p = self._data.first()
        item = p.element()
        return (item._key, item._value)

    def remove_min(self):
        '''Remove and return (k,v) tuple with minimum key.'''
        if self.is_empty():
            raise ValueError('Priority queue is empty.')
        item = self._data.delete(self._data.first())
        return (item._key, item._value)