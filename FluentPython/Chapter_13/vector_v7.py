from array import array
import reprlib
import math
import numbers
import functools # To use reduce
import operator # To use xor
import itertools # To use chain function in __format__
import numbers # For type checking

class Vector:
    typecode = 'd'

    def __init__(self, components):
        self._components = array(self.typecode, components) # The self._components instance "protected" attribute will hold an array with the Vector components.

    def __iter__(self):
        return iter(self._components) # To allow iteration, we return an iterator over self._components.

    def __repr__(self):
        components = reprlib.repr(self._components) # Use reprlib.repr() to get a limited-length representation of self._components.
        components = components[components.find('['):-1] # Remove the array('d', prefix and the trailing ) before plugging the string into a Vector constructor call.
        return 'Vector({})'.format(components)

    def __str__(self):
        return str(tuple(self))

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) +
                bytes(self._components)) # Build a bytes object directly from self._components.

    def __eq__(self, other):
        '''# return tuple(self) == tuple(other)
        if len(self) != len(other): # If the len of the objects are different, not equal
            return False
        for a, b in zip(self, other): # The len comparison above is needed because zip stops producing values without warning as soon as one of the inputs is exhausted.
            if a!= b: # As soon as two components are different, exit returning False.
                return False
        return True # Otherwise, the objects are equal. '''

        return len(self) == len(other) and all(a==b for a, b in zip(self, other))

    def __hash__(self):
        hashes = (hash(x) for x in self._components) # Create a generator expression to lazily compute the hash of each component.
        #hashes = map(hash, self.components) # Alternate method.
        return functools.reduce(operator.xor, hashes, 0) # Feed hashes to reduce with xor function to compute the aggregate hash value; the third argumet, 0, is the initializer.
    
    def __abs__(self):
        return math.sqrt(sum(x * x for x in self)) # We can't use hypot anymore, so we sum the squares of the components and compute the sqrt of that.

    def __bool__(self):
        return bool(abs(self))

    def __len__(self):
        return len(self._components)

    def __getitem__(self, index):
        cls = type(self) # Get the class of the instance (i.e., Vector) for later use.
        if isinstance(index, slice): # If the index argument is a slice...
            return cls(self._components[index]) # ...invoke the class to build another Vector instance from a slice of the _components array.
        elif isinstance(index, numbers.Integral): # If the index is an int or some other kind of integer...
            return self._components[index] # ...just return the specific item from _components
        else:
            msg = '{cls.__name__} indicies must be integers'
            raise TypeError(msg.format(cls=cls)) # Otherwise, raise an exception.

    shortcut_names = 'xyzt'

    def __getattr__(self, name):
        cls = type(self) # Get the vector class for later use. 
        if len(name) == 1: # If the name is one character, it may be one of the shortcut_names.
            pos = cls.shortcut_names.find(name) # Find position of 1-letter name; str.find would also locate 'yz' and we don't want this.
            if 0 <= pos < len(self._components): # If the position is within range, return the array element. 
                return self._components[pos]
        msg = '{.__name__!r} object has no attribute {!r}' # If either test failed, raise AttributeError with a standard message text. 
        raise AttributeError(msg.format(cls, name))
    
    def __setattr__(self, name, value):
        cls = type(self)
        if len(name) == 1: # Special handling for single character attribute names.
            if name in cls.shortcut_names: # If name is one of xyzt, set specific error message.
                error = 'readonly attribute {attr_name!r}'
            elif name.islower(): # If name is lowercase, set error message about all single-letter names.
                error = "can't set attributes 'a' to 'z' in {cls_name!r}"
            else: # Otherwise, set blank error message.
                error = ''
            if error: # If there is a nonblank error message, raise AttributeError
                msg = error.format(cls_name=cls.__name__, attr_name=name)
                raise AttributeError(msg)
        super().__setattr__(name, value) # Default case: call __setattr__ on superclass for standard behavior.
    
    def angle(self, n): # Compute one of the angular coordinates, using formulas adapted from n-sphere.
        r = math.sqrt(sum(x * x for x in self[n:]))
        a = math.atan2(r, self[n-1])
        if (n == len(self) -1) and (self[-1] < 0):
            return math.pi * 2 - a
        else:
            return a

    def angles(self): # Create generator expression to compute all angular coordinates on demand.
        return (self.angle(n) for n in range(1, len(self)))

    def __format__(self, format_spec=''):
        if format_spec.endswith('h'): # Hyperspherical coordinates
            format_spec = format_spec[:-1]
            coords = itertools.chain([abs(self)], self.angles()) # Use itertools.chain to produce genexp to iterate seamlessly over the magnitude and angular coordinates.
            outer_format = '<{}>' # Configure spherical cordinate display with angular brackets.
        else:
            coords = self
            outer_format = '({})' # Configure Cartesian coordinate display with parentheses.
        components = (format(c, format_spec) for c in coords) # Create generator expression to format each coordinate item on demand.
        return outer_format.format(', '.join(components)) # Plug formatted components separated by commas inside brackets or parentheses.

    def __abs__(self):
        return math.sqrt(sum(x * x for x in self))

    def __neg__(self):
        return Vector(-x for x in self)

    def __pos__(self):
        return Vector(self)

    def __add__(self, other):
        try:
            pairs = itertools.zip_longest(self, other, fillvalue=0.0) # pairs is a generator that will produce tuples (a, b) where a is from self and b is from other. If self and other have different lengths, fillvalue is used to supply the missing values for the shortest iterable.
            return Vector(a + b for a,b in pairs)
        except TypeError:
            return NotImplemented

    def __radd__(self, other): # Just delegates to __add__
        return self + other

    def __mul__(self, scalar):
        if isinstance(scalar, numbers.Real): # If scalar is an instance of a numbers.Real subclass, create new Vector with multiplied component values.
            return Vector(n * scalar for n in self)
        else: # Otherwise, return NotImplemented, to let Python try __rmul__ on the scalar operand.
            return NotImplemented

    def __rmul__(self, scalar):
        return self * scalar # In this example, rmul works fine by just performing self * scalar, delegating to the mul method.

    def __matmul__(self, other):
        try:
            return sum(a * b for a, b in zip(self, other))
        except TypeError:
            return NotImplemented
    
    def __rmatmul__(self, other):
        return self @ other

    @classmethod
    def frombytes(cls, octets):
        typecode = chr(octets[0])
        memv = memoryview(octets[1:]).cast(typecode)
        return cls(memv) # The only change needed from the earlier frombytes is in the last line: we pass the memoryview directly to the constructor, without unpacking with * as we did before.
