"""Solution to problem 243

After thinking about it a little, what this question essentially asks is the
value of Euler's totient function for each n divided by n itself. In order to solve this I
need to:

1. pick n
2. calculate phi(n)
3. check if phi(n)/n is smaller than 15499 / 94744
4. pick next n

First try: use phi(n) from solution 69 and just loop through the numbers. This way, I found the
solution this way, but it took a very long time.

One way to speed it up could be to use memoization for prime factorization. Another one might be
to see if something along those lines would also be possible for the totient function itself.
"""
from numba import jit

@jit
def prime_factors(n):
    """Calculates the prime factors of n and returns them in a list
    """
    i = 2
    factors = []
    while i * i <= n:
        # if i does not divide n, increase i by 1
        if n % i:
            i += 1
        # if i divides n, divide n by i and append i to the factors
        else:
            n //= i
            factors.append(i)
    # if we are done and the remainder of n is still larger 1, it is a prime and a divisor
    if n > 1:
        factors.append(n)
    return factors

def phi(n):
    """Computes Euler's totient function via

    phi(n) = n * prod_i (1 - 1/p_i),

    where p_i are the prime factors of n.
    """
    prime_facts = prime_factors(n)
    result = n
    for prime in set(prime_facts):
        result *= (1-1/prime)
    return result

@jit
def main():
    """main function
    """
    for number in range(890000000, 900000000):
        if number % 100000 == 0:
            print(number)
        if phi(number) / (number-1) < 15499 / 94744:
            print("Found the number: ", number)
            break

if __name__ == "__main__":
    main()
