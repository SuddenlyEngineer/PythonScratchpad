import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    def __init__(self):
        allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        allowed_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
        self.cards = [Card(suits, value) for suits in allowed_suits for value in allowed_values]
    
    def __repr__(self):
        return "Deck of {} cards".format(len(self.cards))
        
    def count(self):
        return len(self.cards)
                
    def _deal(self, num):
        to_remove = min([int(num), self.count()])
        if self.count() == 0:
            raise ValueError("No more cards left in the deck!")
        removed_cards = self.cards[-to_remove:]
        self.cards = self.cards[:-to_remove]
        return removed_cards
        
    def shuffle(self):
        if self.count() == 52:
            random.shuffle(self.cards)
        else:
            raise ValueError("Only full decks can be shuffled")
            print(self.count())
        
    def deal_card(self):
        cards = self._deal(1)
        return cards[0]
    def deal_hand(self, num):
        cards = self._deal(num)
        return cards
