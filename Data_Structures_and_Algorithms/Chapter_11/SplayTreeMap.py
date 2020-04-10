from Data_Structures_and_Algorithms.Chapter_11.TreeMap import TreeMap

class SplayTreeMap(TreeMap):
    '''Sorted map implementation using a splay tree.'''

    def _splay(self, p):
        while p != self.root():
            parent = self.parent(p)
            grand = self.parent(parent)
            if grand is None:
                # Zig case
                self._rotate(p)
            elif (parent == self.left(grand)) == (p == self.left(parent)):
                # Zig-zig case
                self._rotate(parent) # Move PARENT up
                self._rotate(p) # Then move p up
            else:
                #Zig-zag case
                self._rotate(p) # Move p up
                self._rotate(p) # Move p up again
    
    def _rebalance_insert(self, p):
        self._splay(p)
    
    def _rebalance_delete(self, p):
        if p is not None:
            self._splay(p)

    def _rebalance_access(self, p):
        self._splay(p)