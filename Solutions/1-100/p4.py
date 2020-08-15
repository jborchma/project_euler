"""Solution to problem 4
"""
# again, just brute force
# smallest 10000 and largest 999*999=998001

# function checks if a number is a palindrome
def check_palindrome(number):
    """Checks if number is a palindrome (check in problem 125 is 50% faster)

    Parameters
    ----------
    number: int
        Number to test

    Returns
    -------
    bool
        Boolean indicator that is True when the number is a palindrome
    """
    return number == int(
        str(number)[::-1]
    )  # old way: str(number) == ''.join(reversed(str(number)))


def main():
    """main function
    """
    # loop through all the possible numbers
    largest = 0
    for first in range(100, 999):
        for second in range(100, 999):
            product = first * second
            if check_palindrome(product) and product > largest:
                largest = product

    print(largest)


if __name__ == "__main__":
    main()
