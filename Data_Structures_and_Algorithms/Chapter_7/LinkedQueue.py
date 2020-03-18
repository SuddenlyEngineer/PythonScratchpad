class LinkedQueue:
    '''Fifo queue implementation using a singly linked list'''

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise AttributeError('Queue is empty.')
        return self._head._element

    def dequeue(self): # Note FIFO, so dequeue head
        if self.is_empty():
            raise AttributeError('Queue is empty,')
        top = self._head._element
        self._head = self._head._next
        self._size -= 1
        if self.is_empty(): # Special case as queue is empty 
            self._tail = None # If the removed head was also the tail.
        return top

    def enqueue(self, item): # Add item to back of the queue
        new = self._Node(item, None)
        if self.is_empty(): # Special case for empty queue.
            self._head = new
        else:
            self._tail._next = new
        self._tail = new
        self._size += 1

    