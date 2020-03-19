from Data_Structures_and_Algorithms.Chapter_8.Tree import Tree

class BinaryTree(Tree):
    '''Abstract base class representing a binary tree structure.'''

    def left(self, p):
        '''Return a Position representing p's left child. Return None if p does not have a left child.'''
        raise NotImplementedError('Must be implemented by subclass.')

    def right(self, p):
        '''Return a Position representing p's right child. Return None if p does not have a right child.'''
        raise NotImplementedError('Must be implemented by subclass')

    def sibling(self, p):
        '''Return a Position representing p's sibling (or None if no sibling).'''
        parent = self.parent(p)
        if parent is None: # p must be the root
            return None # root has no sibling
        else:
            if p == self.left(parent):
                return self.right(parent) # possibly None
            else:
                return self.left(parent) # possibly None

    def children(self, p):
        '''Generate an iteration of Positions representing p's children.'''
        if self.left(p) is not None:
            yield self.left(p)
        if self.right(p) is not None:
            yield self.right(p)

    def positions(self): # Override inherited version to make inorder the default.
        '''Generate an iteration of the tree's positions.'''
        return self.inorder() # Make inorder the default.