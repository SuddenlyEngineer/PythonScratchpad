"""This code corresponds to Chapter 8 of the Python Basics Book"""

# Section 9.4 - FUNCTIONS

def enrollment_stats(university_list):
    """Takes an input of university names, enrolled students, and annual tuition fees, returning two lists of enrollment 
    values and tuition fees. Simple as."""
    enrollments = university_list[:][2]
    tuition_rates = university_list[:][3]
    return [enrollments, tuition_rates]

def mean(list):
    return mean(list)

def median(list):
    list.sort
    return median(list)

# Section 9.1

# Exercise 1

cardinal_numbers = ("first", "second", "third")

# Exercise 2

print(cardinal_numbers[1])

# Exercise 3

position1, position2, position3 = cardinal_numbers

print(position1)
print(position2)
print(position3)

# Exercise 4
my_name = tuple("Thomas")
print(my_name)

# Exercise 5
x_test = "x" in my_name
print(x_test)

# Exercise 6
new_name = my_name[1:len(my_name)] 
print(new_name) 

# Section 9.2

# Exercise 1
food = ["rice", "beans"]

# Exercise 2
food.append("broccoli")

# Exercise 3
food.extend(["bread", "pizza"])

# Exercise 4
print(food[0:1])

# Exercise 5
print(food[len(food)-1])

# Exercise 6
breakfast = "eggs, fruit, orange juice".split(", ")

# Exercise 7
print(len(breakfast))

# Section 9.3

# Exercise 1

data = ((1, 2), (3, 4))

# Exercise 2

for n in range(0,len(data)):
    print(f"Row {n} sum: {sum(data[n])}")

# Exercise 3
numbers = [4, 3, 2, 1]

# Exercise 4
numbers2 = numbers[:]

# Exercise 5
numbers.sort()

# Section 9.4 - CHALLENGE

universities = [
['California Institute of Technology', 2175, 37704],
['Harvard', 19627, 39849],
['Massachusetts Institute of Technology', 10566, 40732],
['Princeton', 7802, 37000],
['Rice', 5879, 35551],
['Stanford', 19535, 40569],
['Yale', 11701, 40500]
]

print(universities[2][:])