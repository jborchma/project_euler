"""Solution to problem 76

This is pretty much just an adaption of my solution to problem 31. In exchange for a list of coins,
it's just the list of integers. The target is now 100.
"""
LIST_OF_INTEGERS = range(1, 100)
TARGET = 100
ways = {i:0 for i in range(TARGET+1)}
# initialize with a 1
ways[0] = 1

for integer in LIST_OF_INTEGERS:
    for j in range(integer, TARGET+1):
        ways[j] += ways[j - integer]

print(ways[100])
