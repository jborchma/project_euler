"""Solution to Project euler problem 85

It's easy to derive the formula for the number of squares for a rectangle of size n * m:

sum_{i=0}^{m-1}sum_{j=0}^{n-1}(m-i)(n-j)

With this formula we can just loop through n and m from 2 to 100 and take the best solution.
"""
import itertools
import numpy as np
from numba import jit


@jit
def sumproduct(*lists):
    """Product function
    """
    return itertools.product(*lists)


@jit
def square_sum(m, n):
    """Calculate square sum
    """
    return np.sum(
        [
            x * y
            for x, y in sumproduct(
                [m - i for i in range(0, m)], [n - i for i in range(0, n)]
            )
        ]
    )


@jit
def main():
    """Main function
    """
    target = 2000000
    best_value = 0
    best_size = 0
    best_tuple = None
    for i in range(2, 100):
        for j in range(2, 100):
            value = square_sum(i, j)
            if abs(target - value) < abs(best_value - target):
                best_value = value
                best_size = i * j
                best_tuple = (i, j)

    print(best_value)
    print(best_size)
    print(best_tuple)


if __name__ == "__main__":
    main()
