"""Solution to problem 97

Non-Mersenne prime: We can just calculate the exponentiation modulo 10**10
and then do the remaining calculations. Luckily the builtin pow function can do this
very easily.
"""

first_10_digits = pow(2, 7830457, 10**10)
first_10_digits = 28433 * first_10_digits + 1

print(first_10_digits)
