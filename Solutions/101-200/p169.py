"""Solution to problem 169
"""
import math

def combinations_of_powers(binary_number, steps):
    """Recursive solution
    """
    #print(binary_number, steps)
    if math.log(int(binary_number, 2), 2) % 1 == 0:
        #print("woo")
        return steps + [int(math.log(int(binary_number, 2), 2)) + 1]

    if len(binary_number) == 1:
        return steps + [1]

    if binary_number[-1] == "1":
        p = combinations_of_powers(binary_number[:-1], steps)
        if p:
            return p
    else:
        p = combinations_of_powers(binary_number[:-1], steps + [len(binary_number)-1])
        if p:
            return p


TARGET = bin(12)[2:]
print(sum(combinations_of_powers(TARGET, [])))
#combinations_of_powers(4)
