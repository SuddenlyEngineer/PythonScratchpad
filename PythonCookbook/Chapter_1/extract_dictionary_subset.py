prices = {
   'ACME': 45.23,
   'AAPL': 612.78,
   'IBM': 205.55,
   'HPQ': 37.20,
   'FB': 10.75
}

# Make a dictionary of all prices over 200
p1 = { key:value for key, value in prices.items() if value > 200 }

# Make a dictionary of tech stocks
tech_names = { 'AAPL', 'IBM', 'HPQ', 'MSFT' }
p2 = { key:value for key, value in prices.items() if key in tech_names }

# Above are dictionary comprehensions
# Can also create a sequence of tuples, pass to dict()
# Dictionary comprehension is twice as fast as the below, however

p1 = dict((key, value) for key, value in prices.items() if value > 200)

# This solution is almost 1.6 times slower than the dictionary comprehension
p2 = { key:prices[key] for key in prices.keys() & tech_names}