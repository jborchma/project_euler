"""Solution to problem 527.

Most of the work was actually done by hand and is in my notebook.
"""
import math
import numpy as np
from scipy.special import digamma


def B(n):
    """Expected number of steps for binary search.

    Taken from https://en.wikipedia.org/wiki/Binary_search_algorithm#Performance
    """
    logarithm = int(math.log(n, 2))
    return logarithm + 1 - (2 ** (logarithm + 1) - logarithm - 2) / n


def R_recursive(n):
    """Recursive expected number of steps for random binary search.

    The first, commented out version is the one I derived. It essentially comes from the thought
    that when one picks the random guess, the problem turns into the problem for n-1 based on the
    number that one guessed.

    The second formula is then derived by squishing in R(n-1) into the equation to turn it into
    a much easier recursive formulation by getting rid of the sum. That way, the formula can be
    turned into an explicit formula.
    """
    if n == 1:
        return 1

    # return 1 + 2/n**2 * (sum([i * R_recursive(i) for i in range(1, n)]))
    return (
        1
        + (2 * (n - 1) + (n - 1) ** 2) / n ** 2 * R_recursive(n - 1)
        - ((n - 1) / n) ** 2
    )


def R(n):
    """Based on the formula above and computed through Wolfram Alpha:
    RSolve[{a[n] == 1 + (2*(n-1) + (n-1)^2)/n^2 * a[n-1] - (n-1)^2/n^2 , a[1] == 1}, a[n], n]

    a(n) = (2 gamma n - 3 n + 2 n polygamma(0, n + 1) + 2 polygamma(0, n + 1) + 2 gamma )/n
    """
    return (
        2 * np.euler_gamma * n
        - 3 * n
        + 2 * n * digamma(n + 1)
        + 2 * digamma(n + 1)
        + 2 * np.euler_gamma
    ) / n


def main():
    """Main function."""
    print(f"The answer is {R(10**10) - B(10**10)}.")


if __name__ == "__main__":
    main()
