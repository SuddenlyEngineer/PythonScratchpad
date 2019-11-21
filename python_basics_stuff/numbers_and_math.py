"""This code corresponds to Chapter 5 of the Python Basics Book"""

# SECTION 5.1

# Exercises follow here

# Exercise 1:

num1 = 25000000
num2 = 25_000_000
print(num1)
print(num2)

# Exercise 2:
num = 1.75e5
print(num)

# Exercise 3:
print(2e1000)

# SECTION 5.3 (5.2 had no exercises)

base = input("Enter a base: ")
exponential = input("Enter an exponent: ")
result53 = float(base) ** float(exponential)
print(f"{base} to the power of {exponential} = {result53}")

# SECTION 5.5 (5.4 had no exercise)

# Exercise 1
num1 = input("Enter a number: ")
num1round = round(float(num1), 2)
print(f"{num1} rounded to 2 decimal places is {num1round}")

# Exercise 2
num2 = input("Enter a number: ")
num2abs = abs(float((num2)))
print(f"The absolute value of {num2} is {num2abs}")

# Exercise 3
num3 = input ("Enter a number: ")
num32 = input("Enter another number: ")
difference = (float(num3)-float(num32)).is_integer()
print(f"The difference between {num3} and {num32} is an integer? {difference}!")

