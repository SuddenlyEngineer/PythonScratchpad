"""This code corresponds to Chapter 11 of the Python Basics Book"""

# Section 11.1

# Exercise 1

input_file = open("poem.txt", "r")
for line in input_file.readlines():
    print(line, end="")
input_file.close()

# Exercise 2
with open("poem.txt", "r") as input_file:
    for line in input_file.readlines():
        print(line, end="")

# Exercise 3

with open("poem.txt", "r") as source_file, open("output.txt", "w") as dest:
    for line in source_file.readlines():
        dest.write(line)

# Exercise 4

input_file = open("output.txt", "a")
input_file.writelines("\nSneed's Feed and Seed: Formerly Chuck's")
input_file.close()

