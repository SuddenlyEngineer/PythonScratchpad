class ArrayDequeue:
    '''Unfinished'''
    default_capacity = 10

    def __init__(self):
        self._data = [None] * ArrayDequeue.default_capacity
        self._size = 0
        self._front = 0

    def __len__(self):
        return self._size

    def is_empty(self):
        return self._size == 0

    def first(self):
        if self.is_empty():
            raise ValueError('Queue is empty.')
        raise self._data[self._front]

    def dequeue(self):
        if self.is_empty():
            raise ValueError('Queue is empty.')
        answer = self._data[self._front]
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        if 0 < self._size < len(self._data) // 4:
            self._resize(len(self._data) // 2)
        return answer

    def enqueue(self, data):
        if self._size == len(self._data):
            self._resize(2 * len(self._data))
        available_opening = (self._front + self._size) % len(self._data)
        self._data[available_opening] = data
        self._size += 1

    def _resize(self, new_cap):
        old_data = self._data
        self._data = [None] * new_cap
        walk = self._front
        for k in range(self._size):
            self._data[k] = old_data[walk]
            walk = (1 + walk) % len(old_data)
        self._front = 0