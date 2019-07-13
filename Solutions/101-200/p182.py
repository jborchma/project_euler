"""Solution to problem 182

I'll start by using a sieve to calculate all coprimes for phi. Then we can test all m
and calculate how many unconcealed messages are there for each value of e.

As it turns out, the search space for this is way too large, so we need to wiggle down the number
of m's and e's we need to check.

I think, we can restrict ourselves to only look at the m that are coprime to n.

Or, by doing some more math, we can find out that we need to test the e to fulfill
gcd((e-1), phi) == 2, which will be the optimal e.
"""
import math
from numba import jit

# find prime factors
@jit
def prime_factors(n):  # pylint: disable=C0103
    """This function finds the prime factors of n

    Parameters
    ----------
    n: int
        Number to be factorized

    Returns
    -------
    list
        List of prime factors
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def coprime_sieve(n):  # pylint: disable=C0103
    """A sieve to calculate all coprime integers for n

    Parameters
    ----------
    n: int
        Integer for which all coprimes in [1, n-1] will be calculated

    Returns
    -------
    list
        List holding all coprimes
    """
    n_prime_factors = prime_factors(n)
    sieve = [False] + (n - 1) * [True]
    for prime_factor in n_prime_factors:
        for i in range(prime_factor, n, prime_factor):
            sieve[i] = False

    coprimes = [i for i, ind in enumerate(sieve) if ind]

    return coprimes


def main():
    """main function
    """
    p = 1009
    q = 3643
    # n = p * q
    phi = (p - 1) * (q - 1)

    phi_coprimes = coprime_sieve(phi)

    res = sum([coprime for coprime in phi_coprimes if math.gcd(coprime - 1, phi) == 2])
    print("Answer:", res)
