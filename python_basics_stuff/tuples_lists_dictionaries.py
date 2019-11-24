"""This code corresponds to Chapter 8 of the Python Basics Book"""

import random

# Section 9.4 - FUNCTIONS

def enrollment_stats(university_list):
    """Takes an input of university names, enrolled students, and annual tuition fees, returning two lists of enrollment 
    values and tuition fees. Simple as."""
    enrollments = [row[1] for row in university_list]
    tuition_rates = [row[2] for row in university_list]
    return [enrollments, tuition_rates]

def mean(list):
    mean = sum(list)/len(list)
    return mean

def median(list):
    list.sort
    if len(list) % 2 == 1: 
        median = list[round(len(list)/2)-1]
        return median 
    else:
        median = (list[len(list)/2]+list[len(list)/2 + 1])/2
        return median

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

[enrollment, tuitions] = enrollment_stats(universities)

enrollment.sort()
tuitions.sort()

total_students = sum(enrollment)
total_tuition = sum(tuitions)
mean_students = mean(enrollment)
median_students = median(enrollment)
mean_tuition = mean(tuitions)
median_tuition = median(tuitions)

print("***************************")
print(f"Total students: {total_students:.0f}")
print(f"Total tuition: {total_tuition:.2f}")
print("")
print(f"Student mean: {mean_students:.0f}")
print(f"Student median: {median_students:.0f}")
print("")
print(f"Tuition mean: ${mean_tuition:.2f}")
print(f"Tuition median: ${median_tuition:.2f}")
print("***************************")

# Section 9.5 - CHALLENGE

nouns = ["fossil", "horse", "aardvark", "judge", "chef", "mango", "extrovert", "gorilla"]
verbs = ["kicks", "jingles", "bounces", "slurps", "meows", "explodes", "curdles"]
adjectives = ["furry", "balding", "incredulous", "fragrant", "exuberant", "glistening"]
prepositions = ["against", "after", "into", "beneath", "upon", "for", "in", "like", "over", "within"]
adverbs = ["curiously", "extravagantly", "tantalizingly", "furiously", "sensuously"]

random_nouns = [random.choice(nouns), random.choice(nouns), random.choice(nouns)]
random_verbs = [random.choice(verbs), random.choice(verbs), random.choice(verbs)]
random_adjectives = [random.choice(adjectives), random.choice(adjectives), random.choice(adjectives)]
random_prepositions = [random.choice(prepositions), random.choice(prepositions), random.choice(prepositions)]
random_adverb = random.choice(adverbs)

poem = f"""A/An {random_adjectives[1]} {random_nouns[1]}

A/An {random_adjectives[0]} {random_nouns[0]} {random_verbs[0]} {random_prepositions[0]} the {random_adjectives[1]} {random_nouns[1]}
{random_adverb}, the {random_nouns[0]} {random_verbs[1]}
the {random_nouns[1]} {random_verbs[2]} {random_prepositions[1]} a {random_adjectives[2]} {random_nouns[2]}"""

print(poem)

# Section 9.6

# Exercise 1
captains = dict()

# Exercise 2
captains = {
    'Enterprise' : 'Picard', 
    'Voyager' : 'Janeway', 
    'Defiant' : 'Sisko'
    }

# Exercise 3
if 'Enterprise' not in captains:
    captains["Enterprise"] = "unknown"
if 'Discovery' not in captains:
    captains['Discovery'] = "unknown"

# Exercise 4
for ships in captains:
    print(f"The {ships} is captained by {captains[ships]}")

# Exercise 5
del captains["Discovery"]

# Exercise 6
captains_list = (
    ('Enterprise', 'Picard'), 
    ('Voyager', 'Janeway'), 
    ('Defiant', 'Sisko')
)
captains2 = dict(captains_list)

# Section 9.7 - CHALLENGE

capitals_dict = {
    "Alabama": "Montgomery",
    "Alaska": "Juneau",
    "Arizona": "Phoenix",
    "Arkansas": "Little Rock",
    "California": "Sacramento",
    "Colorado": "Denver",
    "Connecticut": "Hartford",
    "Delaware": "Dover",
    "Florida": "Tallahassee",
    "Georgia": "Atlanta",
    "Hawaii": "Honolulu",
    "Idaho": "Boise",
    "Illinois": "Springfield",
    "Indiana": "Indianapolis",
    "Iowa": "Des Moines",
    "Kansas": "Topeka",
    "Kentucky": "Frankfort",
    "Louisiana": "Baton Rouge",
    "Maine": "Augusta",
    "Maryland": "Annapolis",
    "Massachusetts": "Boston",
    "Michigan": "Lansing",
    "Minnesota": "Saint Paul",
    "Mississippi": "Jackson",
    "Missouri": "Jefferson City",
    "Montana": "Helena",
    "Nebraska": "Lincoln",
    "Nevada": "Carson City",
    "New Hampshire": "Concord",
    "New Jersey": "Trenton",
    "New Mexico": "Santa Fe",
    "New York": "Albany",
    "North Carolina": "Raleigh",
    "North Dakota": "Bismarck",
    "Ohio": "Columbus",
    "Oklahoma": "Oklahoma City",
    "Oregon": "Salem",
    "Pennsylvania": "Harrisburg",
    "Rhode Island": "Providence",
    "South Carolina": "Columbia",
    "South Dakota": "Pierre",
    "Tennessee": "Nashville",
    "Texas": "Austin",
    "Utah": "Salt Lake City",
    "Vermont": "Montpelier",
    "Virginia": "Richmond",
    "Washington": "Olympia",
    "West Virginia": "Charleston",
    "Wisconsin": "Madison",
    "Wyoming": "Cheyenne",
}

(state, capital) = random.choice(list(capitals_dict.items()))

while True:
    print(f"Your state is {state}. Please enter the capital, or type 'exit' to quit.")
    user_answer = input("Capital: ").lower()
    if user_answer == "exit":
        print(f"I can't believe you are giving up! For the record, the capital of {state} is {capital}.")
        break
    if user_answer == capital.lower():
        print("Correct!")
        break

# Section 9.9 - CHALLENGE

cats = 100 
cats_with_hats = []
laps = 100

for lap in range(1, laps+1):
    for cat in range(1, cats + 1):
        if cat % lap == 0:
            if cat in cats_with_hats:
                cats_with_hats.remove(cat)
            else:
                cats_with_hats.append(cat)

print(cats_with_hats)