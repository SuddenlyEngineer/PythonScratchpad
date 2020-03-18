from Data_Structures_and_Algorithms.Chapter_7.DoublyLinkedBase import _DoublyLinkedBase

class PositionalList(_DoublyLinkedBase):
    '''A sequential container of elements allowing positional access.'''

    class Position:
        '''An abstraction representing the location of a single element.'''

        def __init__(self, container, node):
            '''Should not be invoked by the user.'''
            self._container = container
            self._node = node

        def element(self): 
            '''Return the element stored at this position.'''
            return self._node._element

        def __eq__(self, other):
            '''Return true if other is a Position representing the same location.'''
            return type(other) is type(self) and other._node is self._node

        def __ne__(self, other):
            '''Return True if other does not represent the same location.'''
            return not (self == other) # Opposite of eq dunder

    def _validate(self, pos):
        '''Return position's node, or raise appropriate error if invalid.'''
        if not isinstance(pos, self.Position):
            raise TypeError('pos must be proper Position type.')
        if pos._container is not self:
            raise ValueError('pos does not belong to this container.')
        if pos._node._next is None: # Convention for deprecated nodes.
            raise ValueError('pos is no longer valid.')
        return pos._node

    def _make_position(self, node):
        '''Return position instance for given node, or None if sentinal.'''
        if node is self._header or node is self._trailer:
            return None
        else:
            return self.Position(self, node)

    def first(self):
        '''Return the last Position in the list, or None if list is empty.'''
        return self._make_position(self._header._next)
    
    def last(self):
        '''Return the last Position int the list, or None if list is empty.'''
        return self._make_position(self._trailer._prev)
    
    def before(self, pos):
        '''Return the position just before Position pos, or None if pos is first.'''
        node = self._validate(pos)
        return self._make_position(node._prev)

    def after(self, pos):
        '''Return the position just after Position pos, or None if pos is last.'''
        node = self._validate(pos)
        return self._make_position(node._next)

    def __iter__(self):
        '''Generate a forward iteration of the elements in the list.'''
        cursor = self.first()
        while cursor is not None:
            yield cursor.element()
            cursor = self.after(cursor)

    def _insert_between(self, item, predecessor, successor):
        '''Add element between existing nodes and return new Position.'''
        node = super()._insert_between(item, predecessor, successor)
        return self._make_position(node)

    def add_first(self, item):
        '''Insert element item at the front of the list and return new Position.'''
        return self._insert_between(item, self._header, self._header._next)

    def add_last(self, item):
        '''Insert element item at the back of the list and return new Position.'''
        return self._insert_between(item, self._trailer._prev, self._trailer)
        
    def add_before(self, pos, item):
        '''Insert element item into list before Position pos and return new Position.'''
        original = self._validate(pos)
        return self._insert_between(item, original._prev, original)

    def add_after(self, pos, item):
        '''Insert element item into list after Position pos and return new Position.'''
        original = self.validate(pos)
        return self._insert_between(item, original, original._next)

    def delete(self, pos):
        '''Remove and return the element at Position p.'''
        original = self._validate(pos)
        return self._delete._node(original)

    def replace(self, pos, element):
        '''Replace the element at Position pos with element. Return the element formerly at position pos.'''
        original = self.validate(pos)
        old_value = original._element # Temporarily store old element
        original._element = element # Replace with new element
        return old_value

    def insertion_sort(self):
        '''Sort PositionalList of comparable elements into nondecreasing order.'''
        if len(self) > 1: # Otherwise, no need to sort!
            marker = self.first()
            while marker != self.last():
                pivot = self.after(marker) # Next item to place
                value = pivot.element()
                if value > marker.element(): # Pivot is already sorted
                    marker = pivot # Pivot becomes new marker
                else: # Must relocate pivot
                    walk = marker # Find leftmost item greater than value
                    while walk != self.first() and self.before(walk).element() > value:
                        walk = self.before(walk)
                self.delete(pivot)
                self.add_before(walk, value) # Reinsert value before walk