"""Solution to problem 686

Checking first digits of large exponential numbers reminded me of proble, so I might be able to use
parts of that solution for this problem.

This works, but it's too slow to just loop through until 678910...

Turning the power function into multiplication does the trick, though. Saved A LOT of
multiplications that way.
"""
from numba import jit

@jit
def scaling_mult(a, b, scaling_factor=10 ** (-10)):
    """scaled down power function

    This function calculates a*b and scales down the result in case it's larger than 10^20.

    Parameters
    ----------
    a: float, int
        Number to be
    b: int
        Exponent
    scaling_factor: float, optional
        Scaling factor that is used to scale down large numbers

    Returns
    -------
    float
        Result of a*b scaled down by powers of the scaling_factor
    """
    result = a*b
    if result > 1e20:
        result *= scaling_factor

    return result

def main():
    """main function
    """
    i = 2
    counter = 0
    previous_i = 0
    number = 2
    while True:
        number = scaling_mult(number, 2)
        if str(int(number))[:3] == "123":
            counter += 1

            if counter % 10000 == 0:
                interval = i - previous_i
                previous_i = i
                print(i, interval, counter)
            if counter == 678910:
                print("The answer is:", i)
                break
        i += 1


if __name__ == "__main__":
    main()
