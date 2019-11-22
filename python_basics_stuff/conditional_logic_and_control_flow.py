"""This code corresponds to Chapter 8 of the Python Basics Book"""

import random


# Section 8.7 - Functions

# Exercise 1

def roll():
    """Randomly return a 6-sided dice roll."""
    integer = random.randint(1, 6)
    return integer


# Section 8.8 - Function

def coin_flip():
    """Randomly return 'heads' or 'tails'."""
    if random.randint(0, 1) == 0:
        return "heads"
    else:
        return "tails"


# Section 8.9 - Function

def election(probability_of_a):
    """Generates election probabilities, given a percentage chance of candidate A winning."""
    if random.random() < probability_of_a:
        return "A"
    else:
        return "B"


# SECTION 8.3

# Exercise 1

actual_thing_to_type = input("Enter a word: ")

if len(actual_thing_to_type) < 5:
    print("C'mon, write more than that.")
elif len(actual_thing_to_type) == 5:
    print("Right on the money.")
else:
    print("Too long; didn't read.")

# SECTION 8.4 - CHALLENGE

factor_me = int(input("Enter a positive integer: "))

for n in range(1, factor_me + 1):
    if factor_me % n == 0:
        print(f"{n} is a factor of {factor_me}")

# Section 8.5

# Exercise 1

qanon = ""
while qanon.lower() != "q":
    qanon = input("Enter a letter: ")

print("You're free!")

# Exercise 2

for n in range(1, 51):
    if n % 3 == 0:
        print(f"{n} is a multiple of 3.")

# Section 8.6

# Exercise 1
while True:
    try:
        capture = input("Enter an integer: ")
        print(int(capture))
        break
    except ValueError:
        print("No, I said an integer: ")

# Exercise 2

while True:
    try:
        user_string = input("Enter a string: ")
        user_int = input("Enter an integer: ")
        print(f"At the index {user_int} in {user_string} if the character {user_string[int(user_int)]}")
        break
    except ValueError:
        print("You didn't enter an integer!")
    except IndexError:
        print("You entered an out of bounds integer!")

# Section 8.7

# Exercise 2

tally_1 = 0
tally_2 = 0
tally_3 = 0
tally_4 = 0
tally_5 = 0
tally_6 = 0

for trial in range(10_000):
    if roll() == 1:
        tally_1 = tally_1 + 1
    elif roll() == 1:
        tally_2 = tally_2 + 1
    elif roll() == 1:
        tally_3 = tally_3 + 1
    elif roll() == 1:
        tally_4 = tally_4 + 1
    elif roll() == 1:
        tally_5 = tally_5 + 1
    else:
        tally_6 = tally_6 + 1

average = (tally_1 + (2 * tally_2) + (3 * tally_3) + (4 * tally_4) + (5 * tally_5) + (6 * tally_6)) / (
        tally_1 + tally_2 + tally_3 + tally_4 + tally_5 + tally_6)
print(average)

# Section 8.8

heads_tally = 0
tails_tally = 0
average_flips = 0

for trial2 in range(10_000):
    while heads_tally <= 1 & tails_tally <= 1:
        if coin_flip() == "heads":
            heads_tally = heads_tally + 1
        else:
            tails_tally = tails_tally + 1
    average_flips = average_flips + heads_tally + tails_tally
    heads_tally = 0
    tails_tally = 0

print(average_flips/10_000)

# Section 8.9

a_wins = 0
b_wins = 0
a_districts = 0

election(.87)
election(.65)
election(.17)

for trial3 in range(10_000):
    if election(.87) == "A":
        a_districts = a_districts + 1
    if election(.65) == "A":
        a_districts = a_districts + 1
    if election(.17) == "A":
        a_districts = a_districts + 1

    if a_districts < 2:
        b_wins = b_wins + 1
        a_districts = 0
    else:
        a_wins = a_wins + 1
        a_districts = 0

print(f"Candidate A won {a_wins / 10_000 * 100}% of the time.")