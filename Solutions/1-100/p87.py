"""Solution for Project Euler problem 87

This is really only a brute force approach that computes all needed powers and loops through
them until we exceed the limit. We use set in the end to dedupe.
"""

N_LIMIT = 50000000
MAX_ROOT = 7071  # since 7071**2 > N_LIMIT

# we need all the primes up to MAX_ROOT
def sieve(n):
    "Return all primes <= n."
    np1 = n + 1
    s = list(range(np1))
    s[1] = 0
    sqrtn = int(round(n ** 0.5))
    for i in range(2, sqrtn + 1):
        if s[i]:
            s[i * i : np1 : i] = [0] * len(range(i * i, np1, i))
    return [number for number in s if number]


# get all prime numbers
list_of_primes = list(sieve(MAX_ROOT))
power_dict = {}
# take the powers of all needed prime numbers
for power in range(2, 5):
    power_dict[power] = [prime ** power for prime in list_of_primes]

# loop through ordered lists of powers
# once we are too large, stop that loop
number_of_special_numbers = set()
for first_number in range(len(list_of_primes)):
    for second_number in range(len(list_of_primes)):
        for third_number in range(len(list_of_primes)):
            current_sum = (
                power_dict[2][first_number]
                + power_dict[3][second_number]
                + power_dict[4][third_number]
            )
            if current_sum <= N_LIMIT:
                number_of_special_numbers.add(current_sum)
            else:
                break

print(len(number_of_special_numbers))
