"""Solution for problem 75

I first tried a brute force approach, which was super slow. However, using the fact that the
numbers a, b and c need to be a Pythagorean triple https://en.wikipedia.org/wiki/Pythagorean_triple
we can just create all triples and severely decrease the search space we need to cover.
The formulas are:

a = k * (m**2 - n**2)
b = k * (2*m*n)
c = k * (m**2 + n**2)

where m > n and m and n are coprime and not both odd (m+n must be odd).

number = a + b + c
"""
from fractions import gcd
import math

LIMIT = 1500000
M_LIMIT = int(math.sqrt(LIMIT/2))
NUMBER_LIST = [0] * (LIMIT + 1)

number_of_1_sequence = 0
for m in range(2, M_LIMIT):
    for n in range(1, m):
        if (m + n) % 2 == 1 and gcd(m, n) == 1:
            a = m**2 - n**2
            b = 2 * m * n
            c = m**2 + n**2
            number = a + b + c
            while number <= LIMIT:
                NUMBER_LIST[number] += 1
                if NUMBER_LIST[number] == 1:
                    number_of_1_sequence += 1
                if NUMBER_LIST[number] == 2:
                    number_of_1_sequence -= 1
                number += a + b + c

print(number_of_1_sequence)
