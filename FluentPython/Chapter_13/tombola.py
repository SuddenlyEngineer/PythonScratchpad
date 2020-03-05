import abc

class Tombola(abc.ABC): # To define an ABC, subclass abc.ABC

    @abc.abstractmethod
    def load(self, iterable): # An abstract method is marked with the @abstractmethod decorator, and often its body is empty except for a docstring.
        """Add items from an iterable."""

    @abc.abstractmethod
    def pick(self): # The docstring instructs implementers to raise LookupError if there are no items to pick. 
        """Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self): # An ABC may include concrete methods.
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect()) # Concrete methods in an ABC must rely only on the interface defined by the ABC (i.e., other concrete or abstract methods or properties of the ABC.)


    def inspect(self):
        """Return a sorted tuple with the items currently inside."""
        items = []
        while True: # We can't know how concrete subclasses will store the items, but we can build the inspect result by emptying the Tombola with successive calls to .pick()...
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items) # ...then use .load() to put everything back. 
        return tuple(sorted(items))