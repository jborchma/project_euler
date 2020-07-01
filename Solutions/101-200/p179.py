"""Solution to problem 179

One can write the divisor function (i.e. the function that returns the number of divisors) as
tau(n) = prod (1+a_i), where a_i are the prime factor exponents of the prime factorization of n

So we could calculate the number of divisors for all numbers and then check if n and n+1 have the
same number.
"""
from operator import mul
from functools import reduce
from numba import jit

@jit
def factorization(n):
    """
    Generate the prime factorization of n in the form of pairs (p, k)
    where the prime p appears k times in the factorization.

    Parameters
    ----------
    n: int
        Integer to be factorized

    Yields
    ------
    tuple
        Tuple holding the prime factor and its exponent

    >>> list(factorization(1))
    []
    >>> list(factorization(24))
    [(2, 3), (3, 1)]
    >>> list(factorization(1001))
    [(7, 1), (11, 1), (13, 1)]
    """
    p = 1
    while p * p < n:
        p += 1
        k = 0
        while n % p == 0:
            k += 1
            n //= p
        if k:
            yield p, k
    if n != 1:
        yield n, 1

def tau(n):
    """
    Return the number of divisors of n

    Parameters
    ----------
    n: int
        Number, for which we want the number of divisors of n

    Returns
    -------
    int
        Number of divisors
    """
    return reduce(mul, ((1 + k) for _, k in factorization(n)), 1)

@jit
def main():
    """main function
    """
    counter = 0
    previous = tau(2)
    for i in range(3, 10**7):
        current = tau(i)
        if current == previous:
            counter += 1
        previous = current

    print("result:", counter)

if __name__ == "__main__":
    main()
