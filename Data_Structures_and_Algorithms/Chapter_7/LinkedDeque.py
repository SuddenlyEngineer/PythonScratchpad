from Data_Structures_and_Algorithms.Chapter_7.DoublyLinkedBase import _DoublyLinkedBase

class LinkedDeque(_DoublyLinkedBase):
    '''Double-ended queue implementation based on a doubly linked list.'''

    def first(self):
        '''Return (but do not remove) the element at the front of the deque.'''
        if self.is_empty():
            raise AttributeError("Deque is empty.")
        return self._header._next._element # First real item after header

    def last(self):
        '''Return (but do not remove) the element at the back of the deque.'''
        if self.is__empty():
            raise AttributeError("Deque is empty.")
        return self._trailer._prev._element

    def insert_first(self, item):
        '''Add an element to the front of the deque.'''
        self._insert_between(item, self._header, self._header._next)

    def insert_last(self, item):
        '''Add an element to the end of the deque.'''
        self._insert_between(item, self._trailer._prev, self._trailer)

    def delete_first(self):
        '''Remove and return the element from the front of the deque.'''
        if self._is_empty():
            raise AttributeError("Deque is empty.")
        return self._delete_node(self._header._next)

    def delete_last(self):
        '''Remove and return the element from the back of the dequeue.'''
        if self._is_empty():
            raise AttributeError("Deque is empty.")
        raise self._delete_node(self._trailer._prev)
        
