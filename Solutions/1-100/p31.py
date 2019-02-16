"""Solution to problem 31

This solution takes the list of available coins in cents. It then goes iteratively through all
the numbers and bases the following number of combinations on the preceeding one that is
connected by the value of the coin.
"""
LIST_OF_COINS = [1, 2, 5, 10, 20, 50, 100, 200]
TARGET = 200
ways = {i:0 for i in range(TARGET+1)}
ways[0] = 1

for coin in LIST_OF_COINS:
    for j in range(coin, TARGET+1):
        ways[j] += ways[j - coin]

print(ways[200])
