"""
This script covers the generation of random numbers and the picking of random items from a sequence.

The random module can be used for this.

The random module computes random numbers using the Mersenne Twister algorithm. This is a deterministic algorithm
but you can alter the initial seed using random.seed() - see example below.

Random also includes functions for uniform, Gaussian + more.

WARNING: Do not use for cryptography. Instead use ssl module.
"""
import os
import random

values = [1, 2, 3, 4, 5, 6]
random.choice(values)  # Picks out a random item from the sequence

# To take a sampling of N items - where selected items are removed from sample use random.sample()
random.sample(values, 2)

# To shuffle items use random.shuffle
random.shuffle(values)
print(values)

# To produce random integers use random.randint()
random.randint(0, 10)
random.randint(0, 100)

# To produce uniform floating-point values in the range 0 to 1 use random.random()
random.random()  # 0.2586297964404668
random.random()  # 0.5748583004167666

# To get N random-bits expressed as an integer use random.getrandbits()
random.getrandbits(200)  # 1207787373697312185244627490110841223765059933614606463327352

# Changing the random seed
random.seed()
os.urandom(10)  # Argument is size of seed
random.seed(123456)
random.seed(b'bytedata')
