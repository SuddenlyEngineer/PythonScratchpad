import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def __repr__(self):
        return "{} of {}".format(self.value, self.suit)

class Deck:
    count = 0
    allowed_suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
    allowed_values = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]
    deck_list = []
    def __init__(self):
        Deck.count = 52
        for suits in Deck.allowed_suits:
            for values in Deck.allowed_values:
                Card(suits, values)
                Deck.count += 1
                deck_list.append(Card) #Note: this list will appear in order. 
    
    def __repr__(self):
        return Deck.count
                
    def _deal(self, number):
        removed_cards = []
        if Deck.count == 0:
            raise ValueError("No more cards left in the deck!")
        if number > Deck.count:
            number = Deck.count
        for num in range(number):
            removed_card = Deck.deck_list.pop()
            removed_cards.append(removed_card)
        Deck.count -= number
        return removed_cards
        
    def shuffle(self):
        if Deck.count != 52:
            raise TypeError("Only full decks can be shuffled")
        random.shuffle(Deck.deck_list)
        
    def deal_card(self):
        cards = Deck._deal(1)
        return cards[0]
    def deal_hand(self, number):
        cards = Deck._deal(number)
        return cards
