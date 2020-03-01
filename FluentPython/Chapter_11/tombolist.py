from random import randrange

from tombola import Tombola

@Tombola.register # Tombolist is registered as a virtual subclass of Tombola
class TomboList(list): # Tombolist extends list

    def pick(self):
        if self: # Tombolist inherits __bool__ from list and that returns True if the list is not empty.
            position = randrange(len(self))
            return self.pop(position) # Out pick calls self.pop inherited from list, passing a random item index.
        else:
            raise LookupError('pop from empty TomboList')

    load = list.extend # Tombolist.load is the same as list.extend

    def loaded(self):
        return bool(self) # loaded delegates to bool.

    def inspect(self):
        return tuple(sorted(self))