class Tree:
    '''Tree ABC'''

    class Position:
        '''An abstraction representing the location of a single element.'''

        def element(self):
            '''Return the element stored at this Position.'''
            raise NotImplementedError('Must be implemented by subclass.')

        def __eq__(self, other):
            '''Return True if other Position represents the same location.'''
            raise NotImplementedError('Must be implemented by subclass.')

        def __ne__(self, other):
            '''Return True if other does not represent the same location.'''
            return not (self == other) # Opposite of __eq__

    def root(self):
        '''Return Position representing the tree's root (or None if empty).'''
        raise NotImplementedError('Must be implemented by subclass')

    def parent(self, p):
        '''Return Position representing p's parent (or None if p is root).'''
        raise NotImplementedError('Must be implemented by subclass')

    def num_children(self, p):
        '''Return the number of children that Position p has.'''
        raise NotImplementedError('Must be implemented by subclass')

    def children(self, p):
        '''Generate an iteration of Positions representing p's children.'''
        raise NotImplementedError('Must be implemented by subclass')

    def __len__(self):
        '''Return the total number of elements in the tree.'''
        raise NotImplementedError('Must be implemented by subclass')

    def is_root(self, p):
        '''Return True is Position p represents the root of the tree.'''
        return self.root() == p

    def is_leaf(self, p):
        '''Return True if Position p does not have any children.'''
        return self.num_children(p) == 0

    def is_empty(self):
        '''Return True if the tree is empty.'''
        return len(self) == 0

    def depth(self, p):
        '''Return the number of levels separating Position p from the root.'''
        if self.is_root(p):
            return 0
        else:
            return 1 + self.depth(self.parent(p))

    def _height2(self, p): # time is linear in size of subtree
        '''Return the height of the subtree rooted at Position p.'''
        if self.is_leaf(p):
            return 0
        else:
            return 1 + max(self._height2(c) for c in self.chilren(p))

    def height(self, p=None):
        '''Return the height of the subtree rooted as Position p. If p is None, return the height of the entire tree.'''
        if p is None:
            p = self.root()
        return self._height2(p)

    def preorder(self):
        '''Generate a preorder iteration of position in the tree.'''
        if not self.is_empty():
            for p in self._subtree_preorder(self.root()): # Start recursion
                yield p

    def _subtree_preorder(self, p):
        '''Generate a preorder iteration of positions in subtree rooted at p.'''
        yield p # Visit p before its subtrees
        for c in self.children(p): # For each child c
            for other in self._subtree_preorder(c): # Do preorder of c's subtree
                yield other # yielding each to our caller

    def position(self):
        '''Generate an iteration of tree's positions.'''
        return self.preorder() # Return entire preorder iteration.

    def postorder(self):
        '''Generate a postorder iteration of positions in the tree.'''
        if not self.is_empty():
            for p in self._subtree_postorder(self.root()):
                yield p

    def _subtree_postorder(self, p):
        '''Generate a postorder iteration of positions in subtree rooted at p.'''
        for c in self.children(p): # For each child c
            for other in self._subtree_postorder(c): # Do postorder of c's subtree
                yield other # Yielding each to our caller
            yield p # Visit p after its subtrees

    def breadthfirst(self):
        '''Generate a breadth-first iteration of the positions of the tree.'''
        if not self.is_empty():
            fringe = LinkedQueue() # Known positions not yet yielded
            fringe.enqueue(self.root()) # Starting with the root
            while not fringe.is_empty():
                p = fringe.dequeue() # Remove from front of the queue
                yield p # Report this position
                for c in self.children(p):
                    fringe.enqueue(c) # Add children to the back of the queue.

    def inorder(self):
        '''Generate an inorder iteration of positions in the tree.'''
        if not self.is_empty():
            for p in self._subtree_inorder(self.root()):
                yield p

    def _subtree_inorder(self, p):
        '''Generate an inorder iteration of positions in subtree rooted at p.'''
        if self.left(p) is not None: # If left child exists, traverse its subtree
            for other in self._subtree_inorder(self.left(p)):
                yield other
        yield p # Visit p between its subtrees
        if self.right(p) is not None: # if right child exists, traverse its subtree.
            for other in self._subtree_postorder(self.right(p)):
                yield other

        