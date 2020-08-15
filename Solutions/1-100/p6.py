"""Solution to problem 6
"""


def main():
    """main function
    """
    n = 100  # pylint: disable=C0103

    sum_squared = ((n + 1) * n / 2) ** 2

    sum_of_squares = 1 / 6 * n * (n + 1) * (2 * n + 1)

    print(sum_squared - sum_of_squares)


if __name__ == "__main__":
    main()
