"""Solution to problem 110

This problem is a more difficult version of 108. I will first try my fast solution to 108 and
see how far I make it. As it turns out, it's definitely not the right approach. I think my
program would run forever by simply searching through the increasing integers.

I think the approach will be to construct integers by looking at the number of distinct
prime factors. In the end it doesn't matter which numbers are the actual prime factors, what
matters is what the exponents are.
"""
import math
from operator import itemgetter, mul
from functools import reduce

PRIMES = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67]
LOG_PRIMES = [math.log(prime) for prime in PRIMES]

MIN_LOG_DN2 = math.log(8000000)
K_INIT = [1] * 15
MIN_N = reduce(mul, (prime ** K_INIT[i] for i, prime in enumerate(PRIMES[:15])))
MIN_LOG_N = sum(K_INIT[i] * log_prime for i, log_prime in enumerate(LOG_PRIMES[:15]))


class Optimizer:  # pylint: disable=R0903
    """Optimizer class

    Using this class to have a persistent search list that can be used by the optimization method

    Attributes
    ----------
    search: list
        List that will hold the search results
    exponents: [int]
        List of exponents for the prime factorization
    """

    def __init__(self):
        self.search = []
        self.exponents = [0] * 15

    def optimize(
        self, i, maximum_terms, log_dn2, log_n, min_log_n  # pylint: disable=C0330
    ):  # pylint: disable=R0913
        """Searches recursively through number space

        Parameters
        ----------
        i: int
            Starting index of the exponent chain where the recursive search starts
        maximum_terms: int
            Maximum number of exponents that will be used to determine the cutoff
        log_dn2: float
            Logarithm of d(n^2) used for checking if the solution satisfies the constraint
        log_n: float
            Logarithm of n used for checking if n is the lowest solution found so far
        min_log_n: float
            Minimum of of the logarithm of n that is currently found
        """
        # end recursion
        if i == maximum_terms - 1:
            if log_dn2 >= MIN_LOG_DN2 and log_n < min_log_n:
                min_log_n = log_n
                # needed to use copy here to actually append the current state of the
                # exponent list to my search list
                self.search.append((self.exponents.copy(), log_n))
                return None
            return None

        self.exponents[i] = 0
        new_log_dn2 = 0
        while self.exponents[i] <= self.exponents[i - 1] and new_log_dn2 < MIN_LOG_DN2:
            new_log_dn2 = log_dn2 + math.log(1 + 2 * self.exponents[i])
            self.optimize(
                i + 1,
                maximum_terms,
                new_log_dn2,
                log_n + self.exponents[i] * LOG_PRIMES[i],
                min_log_n,
            )
            self.exponents[i] += 1


def main():
    """main function
    """
    optimizer = Optimizer()
    for initial_exponent in range(15, 0, -1):
        optimizer.exponents[0] = initial_exponent
        optimizer.optimize(
            1,
            15,
            math.log(1 + 2 * initial_exponent),
            initial_exponent * LOG_PRIMES[0],
            MIN_LOG_N,
        )

    result = min(optimizer.search, key=itemgetter(1))[0]
    n_answer = reduce(mul, (prime ** result[i] for i, prime in enumerate(PRIMES[:15])))
    print(f"The answer is: {n_answer}.")


if __name__ == "__main__":
    main()
