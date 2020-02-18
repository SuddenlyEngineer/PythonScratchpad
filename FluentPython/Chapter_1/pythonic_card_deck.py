import collections
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suit'])

class FrenchDeck:
    ranks = [str(n) for n in range(2,11)] + list('JQKA')
    suits = 'spades diamonds clubs hearts'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits for rank in self.ranks]
    
    def __len__(self):
        return len(self._cards)
    
    def __getitem__(self, position): # Delegates to the [] operator of self._cards, so FrenchDeck supports slicing
        return self._cards[position] # Also makes the deck iterable.

beer_card = Card('7', 'diamonds') # Returns Card(rank='7', suit='diamonds')
deck = FrenchDeck()
len(deck) # Returns 52
deck[0] # Returns Card(rank='2', suit='spades'), thanks to the __getitem__ method
deck[-1] # Returns Card(rank='A', suit='hearts')
choice(deck) # Gets a random card from the sequence

deck[:3] # Returns [Card(rank='2', suit='spades'), Card(rank='3', suit='spades', Card(rank='4', suit='spades')
deck[12::13] # Returns [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]

for card in deck: # doctest: +ELLIPSIS
    print(card)

for card in reversed(deck):  # doctest: +ELLIPSIS
    print(card) # Iterate in reverse

Card('Q', 'hearts') in deck # Returns True because the deck is iterable
Card('7', 'beasts') in deck # Returns False

# Can we do sorting? Let's sort by rank (aces at the highest), then by suit.
suit_values = dict(spades=3, hearts=2, diamonds=1, clubs=0)
def spades_high(card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]

for card in sorted(deck, key=spades_high): # doctest: +ELLIPSIS
    print(card) # Sort with a key of the spades_high function. for i in x invokes iter() and __iter__()

# FrenchDeck implicitly inherits from object, but leverages the data model and composition.
# Through implementing __len__ and __getitem__, FrenchDeck behaves like a standard Python sequence. 
# This lets it benefit from iteration and slicing, and from the standard library like random.choice, reversed, and sorted.
# Thanks to composition, the __len__ and __getitem__ implementations can hand off all the work to a list object, self._cards.
# Currently, this is immmutable and so cannot be shuffled. Needs __setitem__
# Avoid creating arbitrary dunders, and always use built-ins if available.