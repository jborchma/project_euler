from decimal import *


def decimal_length(d):
    return len(str(Decimal(1) / Decimal(d)))


def primes(n):
    primes = []
    for number in range(2, n):
        prime = True
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                prime = False
                break

        if prime:
            primes.append(number)

    return primes


def period_length(d):
    i = 1
    if d % 2 == 0:
        return period_length(d / 2)
    if d % 5 == 0:
        return period_length(d / 5)
    while True:
        if (pow(10, i) - 1) % d == 0:
            return i
        else:
            i = i + 1


maximum = 0
d_max = 0
for prime in primes(1000):
    length = period_length(prime)
    if length > maximum:
        d_max = prime
        maximum = length

print(d_max)
