import copy

class Bus:

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = []
        else:
            self.passengers = list(passengers) # Make a copy of the passengers list, or convert it to a list if it’s not one.

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name)

class HauntedBus:
    """A bus model haunted by ghost passengers"""

    def __init__(self, passengers=[]): # When the passengers argument is not passed, this parameter is bound to the default list object, which is initially empty.
        self.passengers = passengers # This assignment makes self.passengers an alias for passengers, which is itself an alias for the default list, when no passengers argument is given.

    def pick(self, name):
        self.passengers.append(name) # When the methods .remove() and .append() are used with self.passengers we are actually mutating the default list, which is an attribute of the function object.

    def drop(self, name):
        self.passengers.remove(name)

class TwilightBus:
    """A bus model that makes passengers vanish"""

    def __init__(self, passengers=None):
        if passengers is None:
            self.passengers = [] # Here we are careful to create a new empty list when passengers is None.
        else:
            self.passengers = passengers # However, this assignment makes self.passengers an alias for passengers, which is itself an alias for the actual argument passed to __init__

    def pick(self, name):
        self.passengers.append(name)

    def drop(self, name):
        self.passengers.remove(name) # When the methods .remove() and .append() are used with self.passengers, we are actually mutating the original list received as argument to the constructor.

bus1 = Bus(['Alice', 'Bill', 'Claire', 'David'])
bus2 = copy.copy(bus1)
bus3 = copy.deepcopy(bus1)
id(bus1), id(bus2), id(bus3)
bus1.drop('Bill')
bus2.passengers
id(bus1.passengers), id(bus2.passengers), id(bus3.passengers)
bus3.passengers