import random

money = 100

#Write your game of chance functions here

def coin_flip(call, wager):
  
    flip = random.randint(0, 1)

    if flip == 1 and call == "Heads":
        return wager
    elif flip == 0 and call == "Tails":
        return wager
    else:
        return -1 * wager

def cho_han(prediction, wager):

    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    sum = die1 + die2

    if sum % 2 == 1 and prediction == "Odd":
        return wager
    elif sum % 2 == 0 and prediction == "Even":
        return wager
    else:
        return wager * -1

def two_card_draw(wager):

    cards = ["Ace", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King"]
    suits = ["Clubs", "Diamonds", "Spades", "Hearts"]

    card1 = [random.choice(cards), random.choice(suits)] #Player card
    card2 = [random.choice(cards), random.choice(suits)] #Other card

    while card1[0] == card2[0] and card1[1] == card2[1]:
        card2 = [random.choice(cards), random.choice(suits)]

    if card1[0] > card2[0] and card1[1] != card2[1]:
        return wager
    elif card1[0] < card2[0] and card1[1] != card2[1]:
        return wager
    elif card1[1] == card2[1]:
        return "HOW THE FUCK DID YOU GET HERE?"
    else:
        return 0

def roulette(guess, wager):
    numbers = range(36) + [0] #Extra 0 = 00

    spin = random.choice(numbers)
    if guess == spin:
        return wager
    elif guess == "Even" and spin % 2 == 0 and spin != numbers[-1]:
        return wager
    elif guess == "Odd" and spin % 2 == 1 and spin != numbers[-1]:
        return wager
    else:
        return wager * -1

#Call your game of chance functions here

#Run through every game until broke, you degenerate.
while money > 0:
    money += coin_flip("Heads", 10)
    if money < 0:
        last_game = "Coin Flip"
        break
    money += cho_han("Even", 10)
    if money < 0:
        last_game = "Cho Han"
        break
    money += two_card_draw(10)
    if money < 0:
        last_game = "Two Card Draw"
        break
    money += roulette("Even", 10)
    if money < 0:
        last_game = "Roulette"
        break

print("Bankrupt! Your last game was:")
print(last_game)