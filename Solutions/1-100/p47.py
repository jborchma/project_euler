from numpy import *

N = 200000


sieve = [True] * N


def mark(sieve, x):
    for i in range(2 * x, len(sieve), x):
        sieve[i] = False


for i in range(2, int(N ** (1 / 2)) + 1):
    if sieve[i]:
        mark(sieve, i)

prime_list = []
for i in range(2, N):
    if sieve[i]:
        prime_list.append(i)


print("primes generated....starting to search")


def prime_divisors(n):
    div_list = []
    while n > 1:
        for i in prime_list:
            if n % i == 0:
                div_list.append(i)
                n = int(n / i)
                break
    return div_list


four_list = [1, 2, 3, 4]

for i in range(37960, 200000):
    if not sieve[i]:
        if len(set(prime_divisors(i))) == 4:
            four_list.append(i)
            if (
                four_list[-4] == i - 3
                and four_list[-3] == i - 2
                and four_list[-2] == i - 1
                and four_list[-1] == i
            ):
                print(i - 3)
                break
