"""Solution to problem 215

My first solution was to create a function to find all square divisors of (k+1)**2 * (8*k+5). This
works and gives the right solution for 1000, but it's way too slow to yield the result for the
bound 110000000. Hence, I will need to come up with a different solution.

Currently, for every k I need to factorize a number, then calculate all the sqaure divisors and then
calculate all b's and c's and check the condition.

Maybe one tactic could be to factorize all number up to the bound at the same time and also get
all the divisors at the same time. That way I could maybe save some time...




"""
from functools import reduce
from itertools import compress, product
from itertools import chain, combinations
import operator
import math

def prod(iterable):
    return reduce(operator.mul, iterable, 1)

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


def prime_factorization(n, prime_list):
    """Return the prime factorization of n

    This function returns a list of the prime factors of n including the exponent of each prime
    factor. It expects the list of prime factors to be given as an argument, to enable rapid
    calls to this function without having to recalculate the prime list.

    Parameters
    ----------
    n: int
        Number to be factored
    primes_list: [int]
        List of prime numbers

    Returns
    -------
    list
        List holding tuples (p, e), where p is the prime factor and e is the exponent in the
        factorization
    """
    prime_factors = []
    for prime in prime_list:
        if prime * prime > n:
            # in case the prime numbers are larger than sqrt(n), break
            break
        count = 0  # initialize the count
        while not n % prime:  # in case prime divides n
            n //= prime
            count += 1
        if count > 0:
            prime_factors.append((prime, count))
    if n > 1:
        prime_factors.append((n, 1))
    return prime_factors

def square_divisors(prime_factorization, bound):
    """Find square divisors from a prime factorization
    """
    factors = [prime_exp for prime_exp in prime_factorization for _ in range(prime_factorization[prime_exp]//2)]

    combs = list(set(powerset(factors)))
    list_of_b = [produkt for factors in combs if (produkt := prod(factors)) < bound]
    return list_of_b

def main():
    """Main function.
    """
    N = 110000000

    sf = ((N+3)//8 + 1) * [True]  # sf[k] is True iff 8k - 3 is square free

    for q in range(5, N, 8):
        k = (q + 3)//8
        if sf[k] != 1:
            continue
        d = 3
        while True:
            qq = q * d*d
            if qq > N:
                break
            kk = (qq + 3)//8
            sf[kk] = False
            d += 2

    cnt = 0

    for q in range(5, N + 1, 8):
        if not sf[(q + 3)//8]:
            continue

        # c = q*d^2 < N ==> d < sqrt(N/q)
        dMax = int(math.sqrt(N / q))

        for p in range(1, N+1, 2):
            k = (q * p*p + 3)//8
            a = 3*k - 1
            kp = k * p
            # b = kp / d > kp / dMax; c > q
            if a + kp // dMax + q > N:
                break
            d_hi = min(kp, dMax)
            for d in range(1, d_hi + 1):
                if kp % d != 0:
                    continue
                b = kp // d
                c = q * d**2
                if a + b + c <= N:
                    cnt += 1

    print(cnt)


if __name__ == "__main__":
    main()
