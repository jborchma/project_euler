"""Solution to problem 106

Only the pairs that have equal number of elements in each set need to be checked.

Sets with one element in it are trivial.  So for n=4 we only need to check 2. For n=7, 2 and 3.

For n = 12 we need to check 2, 3, 4, 5 and 6.

Now, for n=4 we have 3 possible pairs we need to check. We also know a_1 < a_2 < a_3 < a_4
and we only need to check a_1 + a_4 != a_2 + a_3. This is the only one where the min and max
are in one set.

For general n we need to know the number of equal member pairs, which is
1/2 * binom(n, j) * binom(n-j, j)

Next, we need to figure out how many combinations can be eliminated. These are the ones that are
"ordered". It is effectively binom(n, 2*j) * C_j, where C_j are the Catalan numbers
1/(j+1)*binom(2*j, j) https://en.wikipedia.org/wiki/Catalan_number
"""
from scipy.special import binom

def number_of_pairs(n):
    """Calculates the number of subset pairs for n

    Parameters
    ----------
    n: int
        Size of set A

    Returns
    -------
    int
        Number of possible subset pairs
    """
    summe = 0
    for k in range(1, n // 2 + 1):
        for g in range(k, n - k + 1):
            if k == g and k + g != n:
                summe += binom(n, k) * binom(n-k, g) / 2
            elif k + g == n and k != g:
                summe += binom(n, k)
            elif k + g == n and k == g:
                summe += binom(n, k) / 2
            else:
                summe += binom(n, k) * binom(n-k, g)

    return int(summe)

def main():
    """main function
    """
    n = 12
    summe = 0
    for j in [k for k in range(2, n//2+1)]:
        number_of_equal_pairs = 1/2 * binom(n, j) * binom(n-j, j)
        number_of_eliminated_pairs = 1/(j+1) * binom(2*j, j) * binom(n, 2*j)
        summe += number_of_equal_pairs - number_of_eliminated_pairs

    print(f"Answer: {int(summe)}.")

if __name__ == "__main__":
    main()
