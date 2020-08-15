"""Solution to problem 58

This is Ulam's spiral: https://oeis.org/A200975

Very inefficient solution:

- find all primes up to 10^8
- calculate the ratio by looping through the spirals from 3000 to 10000
"""
from math import sqrt


def is_prime(num):
    """Test if number is prime.

    This function works well if I need to work with very large numbers where I can't just
    create a sieve like in problem 10.
    """
    if num == 2:
        return True
    if (num < 2) or (num % 2 == 0):
        return False
    return all(num % i for i in range(3, int(sqrt(num)) + 1, 2))


def create_diagonal_list():
    """Function to create the diagonal list
    """
    n = 1
    step = 2
    since_last = 0
    while True:
        yield n
        n += step
        since_last += 1
        if since_last == 4:
            step += 2
            since_last = 0


def main():
    """main function 26241
    """
    level = 0
    primes = 0
    for i, n in enumerate(create_diagonal_list()):
        if (i - 1) % 4 == 0:
            level += 1

        if is_prime(n):
            primes += 1
        side_length = (2 * level) + 1

        ratio = float(primes) / float(i + 1)
        if 0 < ratio < 0.1:
            print(side_length)
            return


if __name__ == "__main__":
    main()
