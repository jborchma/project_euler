"""Solution to problem 135

Plugging in y=x-d and z=x-2*d and reducing the equation, we get a simple formula with only
two variables. Simply looping through them and throwing away useless solutions solves this.
I actually learned about `.count` in this one.
"""
import math


def create_solutions(n_limit=1000000):
    """creates solutions
    """
    number_of_solutions = [0] * n_limit
    for x in range(1, 2 * n_limit):  # pylint: disable=C0103
        for d in range(
            int(math.ceil(x / 5)), int((x + 1) / 2)
        ):  # pylint: disable=C0103
            solution = (d - x) * (x - 5 * d)
            if solution >= n_limit:
                break
            number_of_solutions[solution] += 1

    return number_of_solutions


def main():
    """main function
    """
    counted = create_solutions()
    print("Answer:", counted.count(10))


if __name__ == "__main__":
    main()
