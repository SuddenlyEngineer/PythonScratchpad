from array import array
import math


class Vector2d:
    typecode = 'd' # typecode is a class attribute we’ll use when converting Vector2d instances to/from bytes.

    def __init__(self, x, y):
        self.x = float(x) # Converting x and y to float in __init__ catches errors early, which is helpful in case Vector2d is called with unsuitable arguments.
        self.y = float(y)

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