"""Solution to problem 116

This time, different lengths of blocks cannot be mixed but now the special blocks can touch
each other. The number of allowed permutations is
(r+b)!/(r! * b!) = binom(m + (1 - k) * r, r),
where k is the allowed length of the special tiles (2, 3 and 4) and m is the overall length.

Now, all that's left to do is loop through all possible numbers of special tiles r, for each
r loop through k from 2 to 4 and then sum everything up.
"""
from scipy.special import binom

M = 50


def main():
    """main function
    """
    summe = 0
    for r in range(1, M - 2):
        for k in [2, 3, 4]:
            if M + (1 - k) * r >= 0:  # in order to prevent NaN results
                summe += binom(M + (1 - k) * r, r)

    print(summe)


if __name__ == "__main__":
    main()
