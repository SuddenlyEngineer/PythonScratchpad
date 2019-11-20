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
