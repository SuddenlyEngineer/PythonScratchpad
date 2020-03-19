class LinkedStack:
    '''LIFO Stack implementation with singly linked list for storage.'''

    class _Node:
        __slots__ = '_element', '_next'

        def __init__(self, element, next):
            self._element = element
            self._next = next

    def __init__(self):
        self._head = None
        self._size = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def push(self, item):
        self._head = self._Node(item, self._head)
        self._size += 1

    def top(self):
        if self.is_empty():
            raise AttributeError('Stack is empty')
        return self._head._element

    def pop(self):
        if self.is_empty():
            raise AttributeError('Stack is empty.')
        top = self._head._element
        self._head = self._head._next
        self._size -= 1
        return top