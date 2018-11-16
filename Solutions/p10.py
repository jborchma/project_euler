"""Solution for problem 10
"""

N = 2000000
SIEVE = [True] * N

def mark(sieve, x):
    """This function marks prime numbers
    """
    for number in range(x+x, len(sieve), x):
        sieve[number] = False

for x in range(2, int(N**0.5) + 1):
    if SIEVE[x]:
        mark(SIEVE, x)


def test_prime(n):
    """Tests if a number is prime
    """
    if SIEVE[n]:
        return True
    else:
        return False

def prime_euqation(n, a, b):
    return n**2 + a * n + b

summe = 0
for i in range(2, 2000000):
    if SIEVE[i]:
        summe += i

print(summe)
