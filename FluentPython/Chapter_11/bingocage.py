import random
from tombola import tombola


class BingoCage(tombola): # This BingoCage class explicitly extends Tombola.

    def __init__(self):
        self._randomizer = random.SystemRandom() # Pretend we'll use this for online gaming. random.SystemRandom implements the random API on top of the os.urandom() function.
        self._items = []
        self.load(items) # Delegate initial loading to the .load() method

    def load(self, items):
        self._items.extend(items)
        self._randomizer.shuffle(self._items) # Instead of the plain random.shuffle()

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError('pick from empty BingoCage')

    def __call__(self): # No harm in adding extra methods!
        self.pick()