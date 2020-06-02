"""Solution to problem 231

I think the key to this problem is the fact that n! is a multiple of ALL primes up to n. Hence,
the prime factorization is just to count the number of times each prime shows up for n, k, and n-k.

For this we will need to use a sieve to create the primes up to n. Then we need to count the number
of times each prime shows up. This can be done via checking the multiples of each power of a prime p
and adding them all up:

[n!/p] + [n!/p^2] + ...
"""
from itertools import compress


def prime_sieve(n):
    """List of primes < n for n > 2

    This sieve is essentially the usual sieve of Eratosthenes, but with a couple of smart
    improvements and tweaks:
    - It uses a byterray, which speeds things up compared to a list
    - It only creates the sieve for odd numbers, which speeds things up by a factor of two.
      This is the reason for all the `//2` in the code
    - It uses itertools compress function to turn the sieve (a list of booleans, essentially)
      into a list of integers

    All these things combined make this sieve essentially ten times faster than the old one I have
    used so far (for example in problems 10, 77, ...)

    Parameters
    ----------
    n: int
        Upper limit up to which we will look for primes

    Returns
    -------
    list
        List holding all primes < n
    """
    sieve = bytearray([True]) * (n // 2)
    for i in range(3, int(n ** 0.5) + 1, 2):
        if sieve[i // 2]:
            sieve[i * i // 2 :: i] = bytearray((n - i * i - 1) // (2 * i) + 1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def check_power_of_prime_in_factorial(n, p):
    """Function to compute the power of the prime p in the prime factorization of n!

    Parameters
    ----------
    n: int
        Factorial n! to calculate the exponent of p in the prime factorization of
    p: int
        Prime to calculate the multiple of

    Returns
    -------
    int
        Exponent of p in the prime factorization of n!
    """
    result = 0
    while True:
        n //= p
        if n == 0:
            break
        result += n

    return result


def main():
    """main function
    """
    n = 20000000
    k = 15000000
    primes = prime_sieve(n)
    result = sum(
        prime * check_power_of_prime_in_factorial(n, prime)
        - prime * check_power_of_prime_in_factorial(k, prime)
        - prime * check_power_of_prime_in_factorial(n - k, prime)
        for prime in primes
    )

    print(f"The result is: {result}.")


if __name__ == "__main__":
    main()
