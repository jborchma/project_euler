"""Solution to problem 92
"""
import numpy as np
from numba import jit

def memoize(f):
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)

        return cache[args]
    return wrapper

@jit
def calculate_digit_square(n):
    """Calculate the sum of the squares of all digits
    """
    return np.sum([int(digit)**2 for digit in str(n)])

@jit
@memoize
def sequence_ending(n):
    """Calculate ending of digit sequence
    """
    input_int = n
    result = calculate_digit_square(input_int)
    if result == 1:
        return 1
    if result == 89:
        return 89
    else:
        return sequence_ending(result)


@jit
def main():
    """main function
    """
    N = 10000000
    ones = 0
    for i in range(1, N):
        if i % 10000 == 0:
            print("{0}:".format(i), ones)
        ending = sequence_ending(i)
        if ending == 89:
            ones += 1

    print(ones)

if __name__ == '__main__':
    main()
