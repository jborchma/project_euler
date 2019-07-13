"""Solution to problem 112 - Bouncy numbers

simple way: use modulo to get last digit, loop through number to check if bouncy
"""
from numba import jit


@jit
def check_bouncy(number):
    """checks if number is bouncy
    """
    increasing = False
    decreasing = False

    # take last digit
    last_digit = number % 10
    # take rest of number
    number = number // 10
    while number > 0:
        # take next digit
        next_digit = number % 10
        if next_digit < last_digit:
            increasing = True
        elif next_digit > last_digit:
            decreasing = True

        last_digit = next_digit

        if decreasing and increasing:
            return True

        # update number
        number = number // 10

    return decreasing and increasing


@jit
def main():
    """main function
    """
    number_of_bounces = 0
    for number in range(100, 10000000):
        if check_bouncy(number):
            number_of_bounces += 1
        # compare integers
        if 100 * number_of_bounces == 99 * number:
            print("Found number: ", number)
            break


if __name__ == "__main__":
    main()
