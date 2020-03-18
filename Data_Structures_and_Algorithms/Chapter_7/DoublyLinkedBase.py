class _DoublyLinkedBase:

    class _Node:

        def __init__(self, element, prev, next):
            self._element = element
            self._prev = prev
            self._next = next

    def __init__(self):
        self._header = self._Node(None, None, None)
        self._trailer = self._Node(None, None, None)
        self._header._next = self._trailer
        self._trailer._prev = self._header
        self._size = 0
    
    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def _insert_between(self, item, predecessor, successor):
        '''Add element item between two existing nodes and return new node.'''
        new = self._Node(item, predecessor, successor)
        predecessor._next = new
        successor._prev = new
        self._size += 1
        return new

    def _delete_node(self, node):
        '''Delete nonsentinal node from the list and return its element.'''
        predecessor = node._prev
        successor = node._next
        predecessor._next = successor
        successor._prev = predecessor
        self._size -= 1
        element = node._element # Record deleted element
        node._prev = node._next = node._element = None # Deprecate node
        return element # Return deleted element