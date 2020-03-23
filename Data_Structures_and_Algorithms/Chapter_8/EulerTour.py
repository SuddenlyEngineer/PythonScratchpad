class EulerTour:
    '''Abstract base class for performing Euler tour of a tree. 
    _hook_previsit and _hook_postvisit may be overriden by subclasses.'''

    def __init__(self, tree):
        '''Prepare an Euler tour template for given tree.'''
        self._tree = tree

    def tree(self):
        '''Return reference to the tree being traversed.'''
        return self._tree

    def execute(self):
        '''Perform the tour and return any result from post visit of root.'''
        if len(self._tree) > 0:
            return self._tour(self._tree.root(), 0, []) # Start the recursion

    def _tour(self, p, d, path):
        '''Perform tour of subtree rooted at Position p.
        p = Position of current node being visited.
        d = Depth of p in the tree
        path = List of indicies of children on path from root to p'''
        self._hook_previsit(p, d, path) # pre-visit p
        results = []
        path.append(0) # Add new index to end of path before recursion.
        for c in self._tree.children(p):
            results.append(self._tour(c, d+1, path)) # Recur on child's subtree
            path[-1] += 1 # Increment Index
        path.pop() # Remove extraneous index from end of path.
        answer = self._hook_postvisit(p, d, path, results) # post-visit p
        return answer

    def _hook_previsit(self, p, d, path): # Can be overridden
        pass

    def _hook_postvisit(self, p, d, path, results): # Can be overriden
        pass