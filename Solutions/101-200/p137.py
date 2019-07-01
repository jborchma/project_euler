"""Solution to problem 137

Plugging in the formula for the Fibonacci sequence, doing the limit of the geometric series one gets
and solving for x yields a formula

x = - (+/- sqrt(5*n**2 + 2*n + 1) + n + 1) / (2*n)

So x can only rational if 5*n**2 + 2*n + 1 is a perfect square. Looking util 100M didn't take too
long, but this only yields the first 10 (as known from the problem statement). However, using the
first 10, one can see that a(n) = F(2*n) * F(2*n+1)

So, now all that remains to be done is to calculat the 30th and 31st Fibonacci number and
multiply them. I also found this one: http://oeis.org/A081018
"""
import math
from numba import jit

def is_square(number):
    """Check if a number is the square of an integer.

    Parameters
    ----------
    number: int
        Number to be checked
    """
    square_root = int(math.sqrt(number) + 0.5)
    return square_root * square_root == number

def memoize(f):
    """Memoization decorator
    """
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)

        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    """recursive Fibonacci function

    Parameters
    ----------
    n: int
        calculate the nth Fibonacci element
    """
    if n <= 2: #pylint: disable=R1705
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)


@jit
def search_solutions(limit):
    """Searches solutions up to a limit

    Parameters
    ----------
    limit: int
        Upper limit of the search
    """
    counter = 0
    for n in range(2, limit):
        if is_square(5*n**2 + 2*n + 1):
            counter += 1
            x = - (- math.sqrt(5*n**2 + 2*n + 1) + n + 1) / (2*n)
            print("Counter:", counter, n, x)



def main():
    """main function
    """
    print(f"Answer: {fibonacci(30)*fibonacci(31)}")

if __name__ == "__main__":
    main()
