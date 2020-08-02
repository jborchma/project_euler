"""Solution to problem 700

n: 612019000 Sum: 1517926250410182 lowest: 14988102
"""
import numpy as np
from numba import jit

def sequence(n):
    """Calculates Euler coin sequence
    """
    return (1504170715041707 * n) % 4503599627370517


# found at https://stackoverflow.com/questions/4798654/modular-multiplicative-inverse-function-in-python
def egcd(a, b):
    """Helper function for the modular inverse calculation
    """
    if a == 0:  # pylint: disable=R1705
        return (b, 0, 1)
    else:
        g, y, x = egcd(b % a, a)
        return (g, x - (b // a) * y, y)


def modinv(a, m):
    """Calculates the modular inverse of a with respect to m, if it exists
    """
    g, x, _ = egcd(a, m)
    if g != 1:
        raise Exception("modular inverse does not exist")
    else:
        return x % m


@jit
def main():
    """main function
    """
    e = 1504170715041707
    mod = 4503599627370517
    answer = e
    current_min = current_max = e

    while True:
        print("min+max:", current_min + current_max)
        if current_min == 1:
            break
        current = current_min + current_max
        current %= mod
        if current > current_max:
            current_max = current
        if current < current_min:
            current_min = current
            print("min:", current_min)
            answer += current_min
    print("The answer is: ", answer)

    modinv(1504170715041707, 4503599627370517)

    print((3451657199285664*1504170715041707) % 4503599627370517)

if __name__ == "__main__":
    main()
