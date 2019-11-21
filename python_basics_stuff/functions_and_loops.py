"""This code corresponds to Chapter 6 of the Python Basics Book"""
# Section 6.2 - Functions
def cube(x):
    """This function simply returns the cube of an entered number."""
    thirdpower = float(x) ** 3
    return thirdpower

def greet(name):
    """This function returns a simple greeting as a string."""
    print(f"Hello, {name}!")

# Section 6.3 CHALLENGE

def convert_cel_to_far(cel):
    """This function convers celsius to fahrenheit."""
    far = (float(cel) * 1.8) + 32
    return far

def convert_far_to_cel(far):
    """This function converts fahrenheit to celsius."""
    cel = (float(far) - 32) * 5 / 9
    return cel

# Section 6.4 - Functions

def doubles(x):
    """You've gotta check these dubs!"""
    dubs = int(x) * 2
    return dubs

# Section 6.5 - Functions

def invest(amount, rate, years):
    """This function computes the value of an investment, given ARR (rate) and years."""
    for n in range (1,int(years)+1):
        amount = amount*(1+float(rate))
        print(f"Year {n}: ${amount:.2f}")

# Section 6.4 

# Exercise 1
for n in range(2,11):
    print(f"{n}")

# Exercise 2
tempint = 1
while tempint < 10:
    tempint = tempint + 1
    print(tempint)

# Exercise 3
checkem = 2
for n in range (1,4):
    checkem = doubles(checkem)
    print(checkem)

# SECTION 6.5 CHALLENGE
invest(100, .05, 4)

# Section 6.6