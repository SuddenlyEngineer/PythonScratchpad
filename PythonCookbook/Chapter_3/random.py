import random
values = [1, 2, 3, 4, 5, 6]
random.choice(values) # Picks a random value out of a sequence
random.sample(values, 2) # Takes a sampling of N items where selected items are removed from further consideration.divmod
random.shuffle(values) # Shuffles items in a sequence
random.randint(0,10) # Produces random integers from 0 to 10
random.random() # Produces uniform floating-point values in the range 0 to 1.
random.getrandbits(200) # Randomly generates N random-bits as an integer

# Uses deterministic algorith,, can be alterated by using random.seed()
# Random.uniform() is for uniform distribution, .gauss() for gaussian
# For crypto, use the ssl module. Like ssl.RAND_bytes()