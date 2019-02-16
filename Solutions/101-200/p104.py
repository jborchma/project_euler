"""Solution for problem 104

This solutions needs to things: We need to get the first 9 digits as well as the last 9 of
elements of the Fibonacci sequence. The last 9 are quite easy since we can just work modulo
1,000,000,000. However, the first 9 are a little bit trickier, since this will require us
to calculate very large numbers with some different kind of approximation.

In order to solve this, we will use the large n approximation for the Fibonacci sequence by using
the golden ratio phi = (1+sqrt(5))/2. For large n the ratio F_{n+1}/F_{n} -> phi for
n -> infty. This should be good enough for the first 9 digits, since we will be working with
n >= 2749.
"""
import math
from numba import jit

# golden ratio phi
PHI = (1 + math.sqrt(5)) / 2

def check_pandigital(number_string):
    """checks if a string of numbers is pandigital

    Parameters
    ----------
    number_string: str
        String of number to test

    Returns
    -------
    bool
        Boolean indicator is number is pandigital
    """
    return set(number_string) == set('123456789')

@jit
def scaling_pow(x, n, scaling_factor=10**(-10)):
    """scaled down power function

    This function calculates x^n, but scales down the result by the scaling_factor
    in order to avoid overflows.

    Parameters
    ----------
    x: float, int
        Number to be
    n: int
        Exponent
    scaling_factor: float, optional
        Scaling factor that is used to scale down large numbers

    Returns
    -------
    float
        Result of x^n scaled down by powers of the scaling_factor
    """
    result = 1
    for _ in range(n):
        result *= x
        if result > 1E20:
            result *= scaling_factor

    return result

@jit
def check_first_fibonacci_digits(number):
    """checks if first digits of Fibonacci number are pandigital
    """
    result = scaling_pow(PHI, number) / math.sqrt(5)
    result = str(result)
    if check_pandigital(result[:9]):
        print(number)
        return True
    else:
        return False

@jit
def main():
    """main function
    """
    first_number, second_number, index = 1, 1, 1
    while True:
        if index % 10**6 == 0:
            print(index)
        if check_pandigital(str(first_number)[-9:]):
            # if the last digits are pandigital, check first ones
            if check_first_fibonacci_digits(index):
                print(index)
                break
        first_number, second_number = second_number, first_number + second_number
        # scale by 10**10
        second_number = second_number % 1000000000
        index += 1


if __name__ == "__main__":
    main()
