"""Solution to problem 125
"""
import math
from numba import jit

N_MAX = 10**8

def create_palindromic_list(n_max):
    """Creates list with all palindromic numbers <= n_max

    Parameters
    ----------
    n_max: int
        Maximum number considered.

    Returns
    -------
    list
        List holding all palindromic numbers <= n_max
    """
    # intialize
    palindromic_list = [str(number) for number in range(0, 10)]
    two_digits = [str(number) + str(number) for number in palindromic_list]
    palindromic_list += two_digits

    number_of_digits = len(str(n_max))
    for _ in range(3, number_of_digits + 1):
        for i in range(0, 10):
            palindromic_list += [str(i) + str(number) + str(i) for number in palindromic_list
                                 if int(str(i) + str(number) + str(i)) <= n_max]

    # filter out all numbers with leading 0's and dedupe
    palindromic_list = list(set(int(number) for number in palindromic_list if not number[0] == '0'))

    return palindromic_list

@jit
def test_square_sum(number):
    """Function to test if a number is the sum of squares

    The algorithm works in the following way:
    1. We initialize the upper and lower bound to 1
    2. We calculate the maximum number possible (the square root of our N_MAX
    3. initialize sum as 1
    ----- WHILE LOOP ------ (as long as the sum is not equal the input number)
    if the sum is smaller than the number:
        add the square of the upper bound to the sum and increase the upper bound by 1
    elif the sum is larger than the number:
        subtract the square of the lower bound and increase lower bound by 1

    if now the upper bound is larger than the maximum number:
        the number is not a sum of consecutive square numbers
    ----- END OF WHILE LOOP -----

    if the upper bound is larger than the lower bound:
        the number is the sum of at least two consecutive square numbers
    (if upper_bound = lower_bound it would be only one square number)


    Parameters
    ----------
    number: int
        Number to be tested

    Returns
    -------
    bool
        Indicator that returns True if the number is the sum of two or more
        consecutive square numbers
    """
    summe = 1
    lower_bound = 1
    upper_bound = 1

    maximum_number = int(math.sqrt(number))
    while summe != number:
        if summe < number:
            upper_bound += 1
            summe += upper_bound ** 2
        elif summe > number:
            summe -= lower_bound ** 2
            lower_bound += 1

        if upper_bound > maximum_number:
            return False

    return upper_bound > lower_bound


def main():
    """main function
    """
    palindromic_numbers = create_palindromic_list(N_MAX)# generate palindromes and sort

    summe = 0
    pal_list = []
    for palindrome in palindromic_numbers:
        if test_square_sum(palindrome):
            summe += palindrome
            pal_list.append(palindrome)

    print("Result:", summe)


if __name__ == "__main__":
    main()
