"""Solution to problem 172
"""
from operator import mul
from functools import reduce
import itertools


def factorial(n):
    """Calculates the factorial of n
    """
    if n == 0: #pylint: disable=R1705
        return 1
    else:
        return reduce(mul, (i for i in range(1, n+1)))

def possibilities(vector, n=10, k=18):
    """Calculates all possibilities
    """
    temp = 1
    # every vector does not take into account permutations for the frequencies, i.e., I only
    # generate (0, 0, 0, 0, 3, 3, 3, 3, 3, 3) and not (0, 0, 0, 3, 0, 3, 3, 3, 3, 3)
    # Hence, I need to calculate all permumations that I am skipping. These are given by
    # 10! / ((# of 0's)! * ... * (# of 3's)! )
    frequencies = [0] * 4
    for mult in vector:
        frequencies[mult] += 1

    temp *= factorial(n)
    for frequecy in frequencies:
        temp //= factorial(frequecy)


    # now that I have calculated the degeneracy of each vector that I am generating, I need to
    # calculate the number of different numbers that I can generate with the specific set of
    # digits that I calculated. This is given by 18! / (prod_k k_i!)
    temp *= factorial(k)
    for factor in vector:
        temp //= factorial(factor)

    return temp

def vector_generator(n=10, k=18):
    """generates vectors that sum up to 18

    This function yields all the vectors that count the different combinations of 0, 1, 2 and 3.
    However, this does not take into accounts degeneracies, so we need to take care of them later.

    Parameters
    ----------
    n: int, optional
        Number of different digits. Default is 10
    k: int, optional
        Number of digits. Default is 18.

    Yields
    ------
    tuple
        Tuple holding the vector
    """
    numbers = [0, 1, 2, 3]
    for vector in itertools.combinations_with_replacement(numbers, n):
        if sum(vector) == k:
            yield vector

def main():
    """main function
    """
    summe = 0
    for vector in vector_generator():
        print(vector)
        summe += possibilities(vector)

    # multiply by 9/10 because we need to exclude leading 0's
    print(f"Answer: {summe * 9 // 10}.")

if __name__ == "__main__":
    main()
