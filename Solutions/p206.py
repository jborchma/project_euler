"""Problem

check squares of 1010101010 and 1389026623 and only even numbers
"""
import math
from numba import jit

NUMBER_STRING = "1234567890"

@jit
def is_square(number):
    """Function that checks if a number is prime.
    """
    square = int(math.sqrt(number) + 0.5)
    return square * square == number

def is_correct(number):
    """Function that checks if it is the right number.
    """
    return all(str(number)[2*i] == digit for i, digit in enumerate(NUMBER_STRING))


@jit
def main():
    """main function
    """
    for number in range(1010101010, 1389026623, 10):
        if is_correct(number**2):
            print(number)

if __name__ == "__main__":
    main()
