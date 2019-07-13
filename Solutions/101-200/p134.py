"""Solution to problem 134

We are looking for a number n with n = i * 10**(digits) + prime_1 and n % prime_2 == 0

This means (i * 10**(digits) + prime_1 ) % prime_2 = 0 -> i = -prime_1 * 1/(10**(digits)) % prime_2

So we need the modular inverse of 10**digits and then just loop through all primes up to 1000000
"""
from itertools import compress
from numba import jit


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


# found at https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    """Helper function for the modular inverse calculation
    """
    if a == 0:  # pylint: disable=R1705
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    """Calculates the modular inverse of a with respect to m, if it exists
    """
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


@jit
def main():
    """main function
    """
    n_max = 1000000
    prime_list = prime_sieve(2 * n_max)
    prime_list = prime_list[2:]

    summe = 0
    for j, prime_1 in enumerate(prime_list[:-1]):
        prime_2 = prime_list[j + 1]
        if prime_1 > n_max:
            break
        digits = len(str(prime_1))
        i = -prime_1 * modinv(10 ** digits, prime_2) % prime_2
        summe += i * 10 ** (digits) + prime_1

    print("Answer:", summe)


if __name__ == "__main__":
    main()
