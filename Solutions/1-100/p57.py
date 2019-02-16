"""Solution to problem 57

At first my solution failed because I reached maximum recursion depth. However, after adding
the memoization, it ran super quickly.
"""
from fractions import Fraction

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
def fraction(order):
    """Function to expand the fraction
    """
    if order == 0:
        return Fraction(1, 2)
    else:
        return Fraction(1, (2 + fraction(order - 1)))

def main():
    """main function
    """
    counter = 0
    for i in range(1000):
        frac = str(1 + fraction(i))
        numerator, denominator = frac.split('/')
        if len(numerator) > len(denominator):
            counter += 1

    print(counter)

if __name__ == "__main__":
    main()
