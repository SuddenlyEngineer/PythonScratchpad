import random

from tombola import Tombola


class LotteryBlower(Tombola):

    def __init__(self, iterable):
        self._balls = list(iterable) # The initializer accepts any iterable: the argument is used to build a list.

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            position = random.randrange(len(self._balls)) # The random.randrange() function raises ValueError if the range is empty, so we catch that and throw LookupError instead, to be compatible with Tombola.
        except ValueError:
            raise LookupError('pick from empty BingoCage')
        return self._balls.pop(position) # Otherwise the randomly selected item is popped from self._balls

    def loaded(self): # Override loaded to avoid calling inspect (as Tombola.loaded does). We can make it faster by working with self._balls directly - no need to build a whole sorted tuple.
        return bool(self._balls)

    def inspect(self): # Override inspect with a one-liner.
        return tuple(sorted(self._balls))