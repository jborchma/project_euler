"""Solution to problem 115

This problem should be quickly solved by my solution from problem 114.
"""
from numpy.polynomial import polynomial as P
from scipy.special import binom
m = 50

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
    initial_polynomial = [1  if (n_min <= i <= n_max) else 0 for i in range(0, n_max + 1)]
    res = P.polypow(initial_polynomial, k)

    return res[n]

def main():
    """main function
    """
    for n in range(m, 1000):
        summe = 2 # start with no reds and all red
        for r in range(1, n-2):
            for k_times_r in range(m * r, n):
                summe += (binom(n - k_times_r + 1, r)
                          * calculate_polynomial_coefficient(k_times_r, r, m, n-1)
                         )
        if summe > 1000000:
            print("n:", n, "Summe:", summe)
            break

if __name__ == "__main__":
    main()
