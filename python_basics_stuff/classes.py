"""This code corresponds to Chapter 10 of the Python Basics Book"""

# Section 10.2

#class Dog:
#    # Class Attribute
#    species = "Canis familiaris"
#    
#    def __init__(self, name, age, coat_color, breed):
#        self.name = name
#        self.age = age
#        self.coat_color = coat_color
#        self.breed = breed
#    
#    def description(self):
#        return f"{self.name} is {self.age} years old"
#    
#    def __str__(self):
#        return f"{self.name} is {self.age} years old"
#    
#    def speak(self, sound):
#        return f"{self.name} says {sound}"

class Dog:
    species = "Canis familiaris"

    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self):
        return f"{self.name} is {self.age} years old"
    def speak(self, sound):
        return f"{self.name} says {sound}"

class Car:
    def __init__(self, color, mileage):
        self.color = color
        self.mileage = mileage

    def drive(self, added_miles):
        self.mileage = self.mileage + added_miles
    
class GoldenRetriever(Dog):
    def speak(self, sound="Bark"):
        return f"{self.name} says {sound}"

class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width
    
    def area(self):
        return self.length * self.width

class Square(Rectangle):
    def __init__(self, side_length):
        self.length = side_length
        self.width = side_length

class Animal: #Section 10.4 - CHALLENGE
    def __init__(self, name, age, behavior):
        self.name = name
        self.age = age
        self.behavior = behavior
    
    def running(self):
        self.behavior = "running"
    
    def sleeping(self):
        self.behavior = "sleeping"
    
    def eating(self):
        self.behavior = "eating"
    
class Horse(Animal):
    def graze(self):
        self.behavior = "grazing"

class Cow(Animal):
    def moo(self):
        self.behavior = "mooing"

class Chicken(Animal):
    def peck(self):
        self.behavior = "pecking"
   
# Exercise 1
#philo = Dog("Philo", 5)
#print(f"{philo.name}'s coat is {philo.coat_color}.")

# Exercise 2
blue_car = Car("blue",20_000)
red_car = Car("red",30_000)

print(f"The {blue_car.color} has {blue_car.mileage} miles.")
print(f"The {red_car.color} has {red_car.mileage} miles.")

# Exercise 3
green_car = Car("green",0)
green_car.drive(100)
print(green_car.mileage)

# Section 10.3

# Exercise 1

test = GoldenRetriever("Tester", 4)
print(test.speak())

# Exercise 2

print(Square(4).area())