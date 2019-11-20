"""This code corresponds to Chapter 4 of the Python Basics Book"""

# SECTION 4.1

test = "Find your dreams come true"
num_letters = len(test)
print(num_letters)

longstring_is_long = "Testing multi-line \
let's go"

longstring_is_long = """I like this approach better anyway because it's a lot more easy to read; I mean, backslashes 
are really weird and obnoxious anyway, plus they have a weird syntax highlighting inside of PyCharm, so I'm immediately
discouraged from using them. """

print(longstring_is_long)

# Exercises follow here

# Exercise 1:
print('"Sneed"')
# Exercise 2:
print("Sneed's Feed and Seed")
# Exercise 3:
print("""Sneed's Feed and Seed
         Formerly Chuck's""")
# Exercise 4:
print("Chuck's Fuck and Suck \
Formerly Sneed's")

# SECTION 4.2
first_name = "Arthur"
last_name = "Fleck"
joker = first_name + " " + last_name

joker_initials = first_name[0] + "." + last_name[0] + "."
joker_domain_name = first_name[:3] + last_name[:3]

print(joker)
print(joker_initials)
print(joker_domain_name)

not_immutable = "Batman"
not_immutable = "F" + not_immutable[1:]
print(not_immutable)

# Exercises follow here

# Exercise 1:
ex1_string = "Haha, I'm using the internet!"
print(len(ex1_string))

# Exercise 2/3 (There's really no need for 2):
ex3_string1 = "Do you believe"
ex3_string2 = "in life after love?"
print(ex3_string1 + " " + ex3_string2)

# Exercise 4
cursed_string = "Bazinga"
print(cursed_string[2:-1])

# SECTION 4.3
dio = "Holy Diver, you've been down too long in the midnight sea."
print(dio.lower)
print(dio.upper)
dio = dio.upper()

whitespace_string = "   You can hide in the sun 'till you see the light         "
print(whitespace_string.lstrip())
print(whitespace_string.rstrip())
print(whitespace_string.strip())

checkstring = "Sunlight can never been seen!"
print(checkstring.startswith("Su"))
print(checkstring.endswith("!"))

# Exercises follow here

# Exercise 1:
print("Animals".lower())
print("Badger".lower())
print("Honey Bee".lower())
print("Honeybadger".lower())

# Exercise 2:
print("Animals".upper())
print("Badger".upper())
print("Honey Bee".upper())
print("Honeybadger".upper())

# Exercise 3:
string1 = " Filet Mignon"
string2 = "Brisket "
string3 = " Cheeseburger "
print(string1.lstrip())
print(string2.rstrip())
print(string3.strip())

# Exercise 4:
string1 = "Becomes"
string2 = "becomes"
string3 = "BEAR"
string4 = "   bEautiful"

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

# Exercise 5:
string1 = string1.lower()
string3 = string3.lower()
string4 = string4.lstrip().lower()

print(string1.startswith("be"))
print(string2.startswith("be"))
print(string3.startswith("be"))
print(string4.startswith("be"))

# SECTION 4.4

prompt = "Hey, what's up? "
user_input = input(prompt)
print("You said:", user_input)

response = input("What did you say? ")
response = response.upper()
print("Oh, I get it!", response)

# Exercises follow here

# Exercise 1:
third_grade_insult = input("I know you are but what am I? ")
print(third_grade_insult)

# Exercise 2:
print(third_grade_insult.lower())

# Exercise 3:
print(len(third_grade_insult))

# SECTION 4.5 - CHALLENGE
im_a_dolphin = input("Tell me your password: ")
print("The first letter you entered was:", im_a_dolphin[0].upper())

# SECTION 4.6
num = input("Check these dubs: ")
dubs = float(num) * 2
print(dubs)

# Exercises follow here

# Exercise 1:
running_out_of_ideas_here = "23"
test = int(running_out_of_ideas_here) * 17
print(test)

# Exercise 2:
running_out_of_ideas_here = "23"
test = float(running_out_of_ideas_here) * 17
print(test)

# Exercise 3: 
hours_of_sleep = 8
recommendation = "You should get this many hours of sleep:"
print(recommendation, str(hours_of_sleep))

# Exercise 4:
number1 = input("Gimme a number: ")
number2 = input("How about another: ")
print("The product of ",str(number1), "and ",str(number2), "is ", str(float(number1)*float(number2)))

# SECTION 4.7

# Exercises follow here

# Exercise 1:
weight = float(0.2)
animal = "newt"
print(str(weight),"kg is the weight of the",animal,".")

# Exercise 2:
print("{} kg is the weight of the {}.".format(weight, animal))

# Exercise 3
print(f"{weight} kg is the wieght of the {animal}.")

# SECTION 4.8

# Exercises follow here

# Exercise 1:
print("AAA".find("a"))

# Exercise 2:
print("Somebody said something to Samantha.".replace("s","x"))

# Exercise 3:
parsing = input("Gimme some text, one last time? ")
letter = "e"
print(parsing.find(letter))

# SECTION 4.9 - CHALLENGE
translation = input("Okay, I lied. Gimme some more text. ")
translation = translation.replace("a","4")
translation = translation.replace("b","8")
translation = translation.replace("e","3")
translation = translation.replace("l","1")
translation = translation.replace("o","0")
translation = translation.replace("s","5")
translation = translation.replace("t","7")
print(translation)