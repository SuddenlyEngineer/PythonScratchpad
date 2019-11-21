"""This code corresponds to Chapter 8 of the Python Basics Book"""

# SECTION 8.3

# Exercise 1

actual_thing_to_type = input("Enter a word: ")

if len(actual_thing_to_type) < 5:
    print("C'mon, write more than that.")
elif len(actual_thing_to_type) == 5:
    print("Right on the money.")
else:
    print("Too long; didn't read.")