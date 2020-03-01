import collections

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck2(collections.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                                        for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

    def __setitem__(self, position, value): # Needed to enable shuffling
        self._cards[position] = value

    def __delitem__(self, position): # But subclassing MutableSequence forces us to implement __delitem__. an abstract method of that ABC.
        del self._cards[position]

    def insert(self, position, value): # We are also required to implement insert, the third abstract method of MutableSequence.
        self._cards.insert(position, value)