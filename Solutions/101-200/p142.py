"""Solution to problem 142

A naive solution would take way too long to run (especially in Python). So doing some math
beforehand is the way to go for this one.

alpha = x + y
beta = x - y
gamma = x + z
delta = x - z
epsilon = y + z
zeta = y - z

One can derive:
zeta = alpha - gamma
epsilon = alpha - delta
beta = gamma - epsilon

So we need alpha, gamma and delta and get the rest. This is still three loops, but now the search
space is much, much smaller since we will have much less wrong tries.

One more thing is that gamma and delta need to either be both odd or even, so we get another
reduction of our search space.
"""
import math
from numba import jit

def is_square(number):
    """Check if a number is the square of an integer.
    """
    square_root = int(math.sqrt(number) + 0.5)
    return square_root * square_root == number

@jit
def main():
    """main function
    """
    solved = False
    a = 4 #minimum value for a is 4
    while not solved:
        # loop through numbers and square, saved on a lot of tries
        alpha = a**2
        c = 3 #minimum value for c is 3
        while not solved and c < a:
            gamma = c**2
            zeta = alpha - gamma
            # if not valid solution, increase c and continue
            if zeta <= 0 or not is_square(zeta):
                c += 1
                continue
            # if c is odd, we need d to be odd, otherwise d needs to be even
            if c % 2 == 1:
                d_start = 1
            else:
                d_start = 2
            for d in range(d_start, c, 2):
                delta = d**2
                epsilon = alpha - delta
                beta = gamma - epsilon
                if beta <= 0 or epsilon <= 0 or not is_square(epsilon) or not is_square(beta):
                    continue

                x = (alpha + beta) / 2
                y = (epsilon + zeta) / 2
                z = (gamma - delta) / 2
                result = x + y + z
                solved = True
            c += 1

        a += 1

    print("The answer is:", int(result))

if __name__ == "__main__":
    main()
