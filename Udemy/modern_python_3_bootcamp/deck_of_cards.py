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
        self.deck_list = [Card(suits, value) for suits in allowed_suits for value in allowed_values]
    
    def __repr__(self):
        return len(Deck.deck_list)
                
    def _deal(self, number):
        removed_cards = []
        if len(Deck.deck_list) == 0:
            raise ValueError("No more cards left in the deck!")
        if number > len(Deck.deck_list):
            number = len(Deck.deck_list)
        for num in range(number):
            removed_card = Deck.deck_list.pop()
            removed_cards.append(removed_card)
        return removed_cards
        
    def shuffle(self):
        if len(Deck.deck_list) != 52:
            raise TypeError("Only full decks can be shuffled")
        random.shuffle(Deck.deck_list)
        
    def deal_card(self):
        cards = Deck._deal(1)
        return cards[0]
    def deal_hand(self, number):
        cards = Deck._deal(number)
        return cards
