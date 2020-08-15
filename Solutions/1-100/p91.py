"""Solution to problem 91

We have two points (x_1, y_1) and (x_2, y_2). If the triangle has a right angle, the sides
need to fulfil Pythagoras' theorem. Plugging that in, we get three equations:

1. x_1 * x_2 + y_1 * y_2 == 0
2. x_1 * (x_1 - x_2) + y_1 * (y_1 - y_2) == 0
3. x_2 * (x_2 - x_1) + y_2 * (y_2 - y_1) == 0

For N=50, we can just loop through all possible combinations.
"""

N = 2


def test_equality(set_of_points):
    """This function tests if two points are the same
    """
    return set_of_points[0] == set_of_points[1]


def main():
    """main function
    """
    solutions = []
    for x_1 in range(0, N + 1):
        for x_2 in range(0, N + 1):
            for y_1 in range(0, N + 1):
                for y_2 in range(0, N + 1):
                    if (x_1 > 0 or y_1 > 0) and (x_2 > 0 or y_2 > 0):
                        if x_1 * x_2 + y_1 * y_2 == 0 and not test_equality(
                            ((x_1, y_1), (x_2, y_2))
                        ):
                            solutions.append(((x_1, y_1), (x_2, y_2)))
                        elif x_1 * (x_1 - x_2) + y_1 * (
                            y_1 - y_2
                        ) == 0 and not test_equality(((x_1, y_1), (x_2, y_2))):
                            solutions.append(((x_1, y_1), (x_2, y_2)))
                        elif x_2 * (x_2 - x_1) + y_2 * (
                            y_2 - y_1
                        ) == 0 and not test_equality(((x_1, y_1), (x_2, y_2))):
                            solutions.append(((x_1, y_1), (x_2, y_2)))

    # I am overcounting by a factor of 2 since a solution with (x_1, y_1) and (x_2, y_2)
    # and one where the points are exchanged are the same solution
    print(len(solutions) // 2)


if __name__ == "__main__":
    main()
