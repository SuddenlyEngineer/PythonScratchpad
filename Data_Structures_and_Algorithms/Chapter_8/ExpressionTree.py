from Data_Structures_and_Algorithms.Chapter_8.LinkedBinaryTree import LinkedBinaryTree

class ExpressionTree(LinkedBinaryTree):
    '''An arithmetic expression tree.'''

    def __init__(self, token, left=None, right=None):
        '''Create an expression tree.
        In a single parameter form, token should be a leaf value (e.g., '42'), and the expression tree will have that value at an isolated node.
        In a three-parameter version, token should be an operator, and left and right should be existing ExpressionTree instances that become operands for the binary operator.'''
        super().__init__() # LinkedBinaryTree initialization
        if not isinstance(token, str):
            raise TypeError('Token must be a string')
        self._add_root(token) # Use inherited, nonpublic method
        if left is not None: # Presumably three-parameter form
            if token not in '+-*x/':
                raise ValueError('Token must be valid operator.')
            self._attach(self.root(), left, right) # Use inherited, nonpublic method.
    
    def __str__(self):
        '''Return string representation of the expression.'''
        pieces = [] # Sequence of piecewise strings to compose
        self._parenthesize_recur(self.root(), pieces)
        return ''.join(pieces)

    def _parenthesize_recur(self, p, result):
        '''Append piecewise representation of p's subtree to resulting list.'''
        if self.is_leaf(p):
            result.append(str(p.element())) # Leaf value as a string
        else:
            result.append('(') # Opening parenthesis
            self._parenthesize_recur(self.left(p), result) # Left subtree
            result.append(p.element()) # Operator
            self._parenthesize_recur(self.right(p), result) # Right subtree
            result.append(')') # Closing parenthesis

    def evaluate(self):
        '''Return the numeric result of the expression.'''
        return self._evaluate_recir(self.root())

    def _evaluate_recur(self, p):
        '''Return the numeric result of subtree rooted at p.'''
        if self.is_leaf(p):
            return float(p.element()) # Assume element is numeric
        else:
            op = p.element()
            left_val = self._evaluate_recur(self.left(p))
            right_val = self._evaluate_recur(self.right(p))
            if op == '+':
                return left_val + right_val
            elif op == '-':
                return left_val - right_val
            elif op == '/':
                return left_val / right_val
            else: # Treat 'x' or '*' as multiplication
                return left_val * right_val

    def build_expression_tree(tokens):
        '''Returns an Expression Tree based upon a tokenized expression.'''
        S = [] # We use Python list as a stack.
        for t in tokens:
            if t in '+-x*/': # t is an operator symbol
                S.append(t) # Push the operator symbol
            elif t not in '()': # Consider t to be a literal
                S.append(ExpressionTree(t)) # Push trivial tree storing value
            elif t == ')': # Compose a new tree from three constituent parts
                right = S.pop() # Right subtree as per LIFO
                op = S.pop() # Operator symbol
                left = S.pop() # Left subtree
                S.append(ExpressionTree(op, left, right)) # Repush tree.
        return S.pop() # Ultimately we ignore the left parenthesis