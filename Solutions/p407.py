"""Solution to problem 407

M(n) = max_{a < n}(a^2 % n = a)

M(2) = 1
M(3) = 1
M(4) = 1
M(5) = 1
M(6) = 4
M(7) = 1
M(8) = 1
M(9) = 1
M(10) = 6

Theorem 1: for prime numbers n: M(n) = 1 (easy proof)
Theorem 2: if M(n) = x and x > 1: gcd(n, x) > 1
Theorem 1 follows from 2, since for any prime n gcd(n, m) = 1 for all m
The proof for theorem 2 is in my notebook.
"""
from collections import defaultdict
from functools import reduce
from itertools import combinations
from operator import mul
from numba import jit

@jit
def factorize(n: int):
    """This function factorizes all integers >= n and computes the totient.

    It then returns the factors and a list of each number's value of Euler's totient
    function (see project euler problem 69).
    """
    totient = list(range(n+1))
    factors = defaultdict(list)
    for number in range(2, n+1):
        if number not in factors:
            totient[number] = number -1
            for i in range(2*number, n+1, number):
                j, k = i, 1
                while j % number == 0:
                    j //= number
                    k *= number
                factors[i].append(k)
                totient[i] = totient[i] * (number - 1) // number
    return factors, totient

def uw(f: dict, t:list , i: int):
    """Helper function
    """
    for j in range(1, len(f[i])):
        for c in combinations(f[i], j):
            u = reduce(mul, c)
            v = i // u
            w = pow(u, t[v] - 1, v)
            yield u * w

@jit
def main():
    """main function
    """
    n = 10**7
    f, t = factorize(n + 1)
    summe = 0
    for i in range(2, n + 1):
        # in case i is prime
        if i not in f or len(f[i]) < 2:
            summe += 1
            continue

        summe += max(uw(f, t, i))

    print(summe)

if __name__ == "__main__":
    main()
