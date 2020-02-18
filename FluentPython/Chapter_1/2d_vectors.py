'''v1 = Vector(2, 4)
v2 = Vector(2, 1)
v1 + v2 # Returns Vector(4, 5)
v = Vector(3, 4)
abs(v) # Returns 5.0
v * 3 # Returns Vector(9, 12)
abs(v * 3) # Returns 15.0'''

from math import hypot

class Vector:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    
    def __repr__(self):
        return 'Vector(%r, %r)' % (self.x, self.y)
    
    def __abs__(self):
        return hypot(self.x, self.y)
    
    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)
    
    def __mul__(self, scalar):
        return Vector(self.x * scalar, self.y * scalar)

# The repr method gets the string representation of the object. Without the dunder, we would get <Vector object>

# The interactive console calls repr on the results of evaluated expressions, as does $r and !r in str.format()
# repr shows the difference between Vector(1,2) which would work and Vector('1','2') which wouldn't because strings.
# The string returned by repr should be unambiguous and match the source code necessary to recreate the object.
# __str__ is implicitly used by print and should return an end-user string. Choose __repr__ if using one, because
# that is the fallback if no __str__ method.

# __add__ and __mul__ are infix operators. They create new objects and do not touch their operands.
# __rmul__ is to be covered later.

# By default, instances of user defined classes are considered truthy, unless __bool__ or __len__ are implemented. 
# __bool__ is called first, if not implemented, __len__, otherwise just returns True if __len__ not implemented or returns 0.
# Here, __bool__ returns False if magnitude is zero, True otherwise. Bool must return a boolean. 