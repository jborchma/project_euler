"""Solution to problem 145

Any multiple of 10 will not have to be checked.

The sum of a reversible pair with 2 digits is the sum of the digits of one of the numbers times 11,
the general case is found here:
https://plus.maths.org/content/arithmetic-made-easy-reversible-numbers

Just brute forced this. Took a little too long, though...

"""


def all_odd(number):
    """Checks if all digits of a number are odd

    Parameters
    ----------
    number: int
        Number to be checked

    Returns
    -------
    bool
        Boolean indicator that is true if all digits are odd
    """
    return all(int(n) % 2 == 1 for n in str(number))


def main():
    """main function
    """
    counter = sum(
        all_odd(number + int(str(number)[::-1]))
        for number in range(11, 1000000000)
        if number % 10 > 0
    )

    print("Answer:", counter)


if __name__ == "__main__":
    main()
