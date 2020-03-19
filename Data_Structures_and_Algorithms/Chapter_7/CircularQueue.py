class CircularQueue:
    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._tail = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise AttributeError('Queue is empty.')
        head = self._tail._next
        return head._element

    def dequeue(self): # FIFO
        if self.is_empty():
            raise AttributeError('Queue is empty.')
        old_head = self._tail._next
        if self._size == 1:
            self._tail = None # Makes queue empty.
        else:
            self._tail._next = old_head._next
        self._size -= 1
        return old_head._element

    def enqueue(self, item): # Add to the back of the queue
        new = self._Node(item, None)
        old_head = self._tail._next
        if self.is_empty():
            new._next = new # Initialize the circular relationship
        else:
            new._next = self._tail._next # New node points to head
            self._tail._next = new # Old tail points to new node
        self._tail = new
        self._size += 1

    def rotate(self): # Rotate front element to the back of the queue:
        if self._size > 0:
            self._tail = self._tail._next # Old head becomes new tail