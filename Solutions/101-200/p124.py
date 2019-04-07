"""Solution to problem 124
"""
import operator
from functools import reduce
from numba import jit

def prod(iterable):
    """Product function (Python 3.7) (3.8 will have math.prod)
    """
    return reduce(operator.mul, iterable, 1)

# find prime factors
@jit
def prime_factors(n):#pylint: disable=C0103
    """This function finds the prime factors of n

    Parameters
    ----------
    n: int
        Number to be factorized

    Returns
    -------
    list
        List of prime factors
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def calculate_radical(n):#pylint: disable=C0103
    """This function calculates the radical of n
    """
    return prod(set(prime_factors(n)))

def main():
    """main function
    """
    radical_dict = {}
    for number in range(1, 100001):
        radical_dict[number] = calculate_radical(number)

    sorted_dict = sorted(radical_dict.items(), key=operator.itemgetter(1))

    print(sorted_dict[9999])


if __name__ == "__main__":
    main()
