from array import array
import math

class Vector2d:
    #__slots__ = ('__x', '__y')
    
    typecode = 'd' # typecode is a class attribute we’ll use when converting Vector2d instances to/from bytes.

    def __init__(self, x, y):
        self.__x = float(x) # Converting x and y to float in __init__ catches errors early, which is helpful in case Vector2d is called with unsuitable arguments.
        self.__y = float(y) # Two leading underscores (with zero or one trailing underscore) make an attribute private.

    @property # The @property decorator marks the getter method of a property.
    def x(self): # The getter method is named after the public property it exposes. 
        return self.__x # Just return self.__x

    @property # Repeat the same formula for the y property.
    def y(self):
        return self.__y
    
    def __iter__(self):
        return (i for i in (self.x, self.y)) # __iter__ makes a Vector2d iterable; this is what makes unpacking work (e.g, x, y = my_vector). We implement it simply by using a generator expression to yield the components one after the other.

    def __repr__(self):
        class_name = type(self).__name__
        return '{}({!r}, {!r})'.format(class_name, *self) # __repr__ builds a string by interpolating the components with {!r} to get their repr; because Vector2d is iterable, *self feeds the x and y components to format.

    def __str__(self):
        return str(tuple(self)) # From an iterable Vector2d, it’s easy to build a tuple for display as an ordered pair.

    def __bytes__(self):
        return (bytes([ord(self.typecode)]) + # To generate bytes, we convert the typecode to bytes and concatenate…
                bytes(array(self.typecode, self))) # …bytes converted from an array built by iterating over the instance.

    def __eq__(self, other):
        return tuple(self) == tuple(other) # To quickly compare all components, build tuples out of the operands. This works for operands that are instances of Vector2d, but has issues. See the following warning. Tl;dr will return true when comparing instances to other iterables with the same numeric values (e.g., Vector(3, 4) == [3, 4]). Will be fixed later.

    def __abs__(self):
        return math.hypot(self.x, self.y) # The magnitude is the length of the hypotenuse of the triangle formed by the x and y components.

    def __bool__(self):
        return bool(abs(self)) # __bool__ uses abs(self) to compute the magnitude, then converts it to bool, so 0.0 becomes False, nonzero is True.

    def __format__(self, format_spec=''):
        if format_spec.endswith('p'): # Format ends with 'p', use polar coords
            format_spec = format_spec[:-1] # Remove 'p' suffix from format_spec
            coords = (abs(self), self.angle()) # Build tuple of polar coords: (magnitude, angle)
            outer_format = '<{}, {}>' # Configure outer format with angle brackets.
        else:
            coords = self # Otherwise, use x, y components of self for rectangular coordiantes.
            outer_format = '({}, {})' # Configure outer format with parentheses.
        components = (format(c, format_spec) for c in coords) # Use the format built-in to apply the format_spec to each vector component, building an iterable of formatted strings. 
        return outer_format.format(*components) # Plug the formatted strings into the outer format.

    def __hash__(self):
        return hash(self.x) ^ hash(self.y)

    def __int__(self):
        return tuple(int(self.x, self.y))

    def __float__(self):
        return tuple(float(self.x, self.y))
    
    def angle(self):
        return math.atan2(self.y, self.x)

@classmethod # Class method is modified by the classmethod decorator
def frombytes(cls, octets):  # No self argument; instead the class itself is passed as cls.
    typecode = chr(octets[0])  # Read the typecode from the first byte.
    memv = memoryview(octets[1:]).cast(typecode) # Create a memoryview from the octets binary sequence and use the typecode to cast it.
    return cls(*memv) # Unpack the memoryview resulting from the cast into the pair of arguemnts needed for the constructor. 