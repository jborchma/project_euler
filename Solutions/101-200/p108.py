"""Solution to problem 108

My first solution that solved it eventually (but much longer than 1min is just brute force
testing solutions for x if they are integer for each n and then counting. I am sure there is a
more elegant solution, though.

Thinking more about this:
Writing x = ny / (y-n) and defining k = y-n, we can see that
x = n + n**2 / k
Hence k needs to be a divisor of n**2

Also, if we say y <= x -> k + n <= n + n**2 / k -> k <= n

Hence, we need to find all divisors of n^2 that are smaller or equal to n. This yields

(tau(n^2) + 1) / 2, where tau is the divisor function. The +1 is necessary since the number of
divisors of a square number are always odd.

Now, the huge speed up comes from the fact that tau(n^2) = prod_i (1 * 2*k_i), where the k_i are
the exponents of the prime factorization of n, not n^2! This can be seen by writing
n = prod_i p_i ^ (k_i) and squaring
"""
from operator import mul
from functools import reduce


def tau_square(n):
    """
    Return the number of divisors of n^2

    Parameters
    ----------
    n: int
        Number, for which we want the number of divisors of n^2

    Returns
    -------
    int
        Number of divisors
    """
    return reduce(mul, ((1 + 2 * k) for _, k in factorization(n)), 1)


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


def divisor_search():
    """Divisor search
    """
    for n in range(200000):
        if n % 10000 == 0:
            print(n)
        if (tau_square(n) + 1) / 2 > 1000:
            print("Answer:", n)
            break


def brute_force_approach():
    """Brute force search
    """
    maximum = 851
    n = 174000
    while maximum < 1001:
        if n % 1000 == 0:
            print(n, maximum)
        counter = len(
            [
                y * n / (y - n)
                for y in range(n + 1, 2 * n + 1)
                if y * n / (y - n) % 1 < 10e-10
            ]
        )
        if counter > maximum:
            maximum = counter
        n += 1

    print("Answer:", n - 1)


def main():
    """main function
    """
    divisor_search()
    # brute_force_approach()


if __name__ == "__main__":
    main()
