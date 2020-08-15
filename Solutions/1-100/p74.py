"""Solution for problem 74

This is just a brute force approach that uses the precalculated factorials for the 10 digitsself.
Any iteration is stopped if there are over 60 terms.
"""
import numpy as np

FACT_LIST = [1, 1, 2, 6, 24, 120, 720, 5040, 40320, 362880]


def calculate_factorial_sum(integer):
    """Calculate factorial sum
    """
    string_n = str(integer)
    fact_sum = np.sum([FACT_LIST[int(digit)] for digit in string_n])

    return fact_sum


# calculate fact sum chain

number_of_60_chains = 0
for i in range(3, 1000000):
    if i % 10000 == 0:
        print(i, number_of_60_chains)
    chain_numbers = {}
    current_number = i
    chain_numbers[current_number] = None
    current_number = calculate_factorial_sum(current_number)
    while current_number not in chain_numbers:
        chain_numbers[current_number] = None
        current_number = calculate_factorial_sum(current_number)
        if len(chain_numbers) > 60:
            break

    # print(len(chain_numbers))
    if len(chain_numbers) == 60:
        number_of_60_chains += 1

print(number_of_60_chains)
