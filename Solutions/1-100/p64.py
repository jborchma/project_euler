# wikipedia helps with this one: https://en.wikipedia.org/wiki/Methods_of_computing_square_roots#Continued_fraction_expansion
# from this we can find easily calculate the series and check for periodicity

from math import sqrt

odd_period = 0

for N in range(2, 10001):
    r = limit = int(sqrt(N))
    if limit ** 2 == N:
        continue
    k, period = 1, 0
    while k != 1 or period == 0:
        k = (N - r * r) // k
        # print('k',k)
        r = (limit + r) // k * k - r
        # print('r',r)
        period += 1
        # print('#####')
    if period % 2 == 1:
        odd_period += 1

print(odd_period)
