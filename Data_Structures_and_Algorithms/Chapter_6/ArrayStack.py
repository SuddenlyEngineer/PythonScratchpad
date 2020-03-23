class ArrayStack:
    """LIFT STack implementation using a Python list as underlying storage."""

    def __init__(self):
        self._data = []

    def __len__(self):
        return len(self._data)

    def is_empty(self):
        return len(self._data) == 0

    def push(self, item):
        self._data.append(item)

    def top(self):
        if self.is_empty:
            raise ValueError('Stack is empty.')
        return self._data[-1]

    def pop(self):
        if self.is_empty:
            raise ValueError('Stack is empty.')
        return self._data.pop()