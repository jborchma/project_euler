"""Solution to problem 213

In this problem, we will construct the transition matrix Q for each round and then calculate the
full transition matrix for the problem.
"""

from numpy import ones, zeros, dot
import scipy
from time import time
from decimal import Decimal, getcontext

getcontext().prec = 64


def state(i, j):
    """Translate grid position to row/column in matrix Q
    """
    num_col = 30
    return i * num_col + j


def initializa_transition_matrix(num_row, num_col):
    """Initializes the transition matrix for a given number of rows and columns

    Parameters
    ----------
    num_row: int
        Number of rows in the grid
    num_col: int
        Number of columns in the grid

    Returns
    -------
    np.array
        Transition matrix Q
    """
    # transition matrix
    size = num_row * num_col
    Q = zeros((size, size), dtype="float64")

    # set 4 corners
    Q[state(0, 0), state(0, 1)], Q[state(0, 0), state(1, 0)] = (
        Decimal(1) / Decimal(2),
        Decimal(1) / Decimal(2),
    )
    Q[state(0, num_col - 1), state(0, num_col - 2)], Q[
        state(0, num_col - 1), state(1, num_col - 1)
    ] = (Decimal(1) / Decimal(2), Decimal(1) / Decimal(2))
    Q[state(num_row - 1, 0), state(num_row - 2, 0)], Q[
        state(num_row - 1, 0), state(num_row - 1, 1)
    ] = (Decimal(1) / Decimal(2), Decimal(1) / Decimal(2))
    Q[state(num_row - 1, num_col - 1), state(num_row - 2, num_col - 1)], Q[
        state(num_row - 1, num_col - 1), state(num_row - 1, num_col - 2)
    ] = (Decimal(1) / Decimal(2), Decimal(1) / Decimal(2))

    # set 4 borders
    for j in range(1, num_col - 1):
        Q[state(0, j), state(0, j - 1)], Q[state(0, j), state(0, j + 1)], Q[
            state(0, j), state(1, j)
        ] = (Decimal(1) / Decimal(3), Decimal(1) / Decimal(3), Decimal(1) / Decimal(3))
        Q[state(num_row - 1, j), state(num_row - 1, j - 1)], Q[
            state(num_row - 1, j), state(num_row - 1, j + 1)
        ], Q[state(num_row - 1, j), state(num_row - 2, j)] = (
            Decimal(1) / Decimal(3),
            Decimal(1) / Decimal(3),
            Decimal(1) / Decimal(3),
        )

    for i in range(1, num_row - 1):
        Q[state(i, 0), state(i - 1, 0)], Q[state(i, 0), state(i, 1)], Q[
            state(i, 0), state(i + 1, 0)
        ] = (Decimal(1) / Decimal(3), Decimal(1) / Decimal(3), Decimal(1) / Decimal(3))
        Q[state(i, num_col - 1), state(i - 1, num_col - 1)], Q[
            state(i, num_col - 1), state(i, num_col - 2)
        ], Q[state(i, num_col - 1), state(i + 1, num_col - 1)] = (
            Decimal(1) / Decimal(3),
            Decimal(1) / Decimal(3),
            Decimal(1) / Decimal(3),
        )

    # set middle part
    for j in range(1, num_col - 1):
        for i in range(1, num_row - 1):
            Q[state(i, j), state(i - 1, j)], Q[state(i, j), state(i, j + 1)], Q[
                state(i, j), state(i + 1, j)
            ], Q[state(i, j), state(i, j - 1)] = (
                Decimal(1) / Decimal(4),
                Decimal(1) / Decimal(4),
                Decimal(1) / Decimal(4),
                Decimal(1) / Decimal(4),
            )

    return Q


def main():
    """main function
    """
    num_row, num_col = 30, 30
    num_ring = 50
    size = num_row * num_col
    start = time()

    Q = initializa_transition_matrix(num_row, num_col)

    result = ones((1, size), dtype="float64")

    # for each flea on square i, calculate probability of emptiness for each square
    # we are essentially evolving each flea individually, calculate the probabilities for each flea
    # to not be on a field and then mutliply all those probabilities together
    for i in range(0, size):
        # initialize on field i at bell 0
        P = zeros((1, size), dtype="float64")
        P[0, i] = 1.0

        # probability for flee i to be anywhere after the first bell
        tmp = zeros((1, size), dtype="float64")
        tmp = dot(P, Q)

        # evolve probability for further bells
        for _ in range(1, num_ring):
            tmp = dot(tmp, Q)

        # probability to not be on a field
        tmp = 1 - tmp

        # combine emptiness probability across all fleas for each square (the star operator
        # multiplies each entry by entry
        result = result * tmp

    # time for Markov matrix multiplication for num_ring steps
    print("Time to calculate Markov status for all fleas: " + str(time() - start))

    # final probability of emptiness for each square
    # only a superficial step, doesn't change answer
    result = result.reshape(num_row, num_col)

    print("Expected # of empty cells is: " + str(scipy.sum(result)))


if __name__ == "__main__":
    main()
