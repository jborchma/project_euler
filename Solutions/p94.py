"""Solution to problem 94

The triangles we are looking for are called Heronian triangles:
https://en.wikipedia.org/wiki/Heronian_triangle

However, what I found worked best was to just use Heron's formula for the area of the triangle
and loop through the possible integer area solutions. The possible triangles are

a = b = c + 1
a = b = c - 1

I had trouble with precision for very large numbers. As it turned out, I only had to check
the parts (3*n+1)*(n - 1) and (3*n-1)*(n + 1) if they are a square of an integer, since the other
factors were perfect squares by default.
"""
import numpy as np
from numba import jit
import math

@jit
def is_square(x):
    s = int(math.sqrt(x) + 0.5)
    return s * s == x

@jit
def main():
    """main function
    """

    circs = 0
    counter = 0
    for n in range(2, 10**9//3):
        if n % 10**7 == 0:
            print(n, counter)
        A_plus = (3*n+1)*(n - 1)
        A_minus = (3*n-1)*(n + 1)

        if is_square(A_plus):
            counter += 1
            circs += 3 * n + 1
            print(n, n, n + 1, ':', A_plus)
        if is_square(A_minus):
            counter += 1
            circs += 3 * n - 1
            print(n, n, n - 1, ':', A_minus)

    print(circs)
    print(counter)




if __name__ == "__main__":
    main()
