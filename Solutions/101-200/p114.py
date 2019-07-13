"""Solution to problem 114

I used mainly combinatorics to solve this problem: First I calculated the number of
allowed sequences of red and black blocks given a number of red blocks, r and a number of black
blocks b.

Once I had that, I had to figure out, for a given length m, how many different combinations of
r (the number of red block) with different possible lengths there are. The fact that the red
blocks could have different lengths, made this a little harder.

I figured this out by finding the number of compositions given a specific number of red tiles r
as well as the overall length of red tiles combined (which then leaves the number of single squared
black tiles). This can be found here:
https://en.wikipedia.org/wiki/Composition_(combinatorics)#Number_of_compositions


Now, all I had to do was loop through all possible numbers of red tiles, r, calculate different
sequences there are per given r and total number of red squares and sum them all.
"""
from numpy.polynomial import polynomial as P
from scipy.special import binom

M = 50


def calculate_polynomial_coefficient(n, k, n_min, n_max):
    """calculates the polynomial coefficient

    need coefficient of n given (sum_i x^i)^k where i in [n_min, n_max]

    This is the number A-restricted compositions, the number of compositions of n into exactly k
    parts, where A is the set of integers from n_min to n_max, i.e., A = [n_min, n_max]

    Parameters
    ----------
    n: int
        Number for which we look for the number of compositions into k parts
    k: int
        Number of parts into which we want to compose n
    n_min: int
        Lower limit of range of integers of set A
    n_max: int
        Upper limit of range of integers of set A

    Returns
    -------
    int
        number of compositions into k parts given the set A as a restriction
    """
    initial_polynomial = [
        1 if (n_min <= i <= n_max) else 0 for i in range(0, n_max + 1)
    ]
    res = P.polypow(initial_polynomial, k)

    return res[n]


def main():
    """main function
    """
    summe = 2  # start with no reds and all red
    for r in range(1, M - 2):
        for k_times_r in range(3 * r, M):
            summe += binom(M - k_times_r + 1, r) * calculate_polynomial_coefficient(
                k_times_r, r, 3, M - 1
            )

    print(summe)


if __name__ == "__main__":
    main()
