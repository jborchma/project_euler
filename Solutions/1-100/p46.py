from numpy import *

N = 10000


sieve = [True] * N


def mark(sieve, x):
    for i in range(2 * x, len(sieve), x):
        sieve[i] = False


for i in range(2, int(N ** (1 / 2)) + 1):
    if sieve[i]:
        mark(sieve, i)

found = False
for i in range(3, N, 2):
    if not sieve[i]:
        for j in range(2, len(sieve)):
            if j > i - 2:
                found = True
                print(i)
                break
            if sieve[j]:
                diff = i - j
                if diff % 2 == 0 and sqrt(int(diff / 2)) % 1 == 0:
                    break

    if found:
        break
