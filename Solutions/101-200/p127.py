"""Solution to problem 127

I first tried a brute force approach based on the answer from problem 125, but the
search space is too large. Hence, I need to make some smart improvements that will
narrow down my search.

First, use the sieve of Eratosthenes to calculate all radicals up to the limit.
Next, we also have rad(a * b * c) = rad(a) * rad(b) * rad(c) since a, b and c are coprime. Using
this, we can just try values of a with rad(a) * rad(c) < c. We will order the radicals in ascending
order, such that we can stop the search early when rad(a) * rad(c) > c. In order to take advantage
of this, we will search through the space of c in the outer loop and then a in the second loop.
"""
import math
from numba import jit

@jit
def radical_sieve(limit):
    """Function that creates a list of radicals based on the sieve of Eratosthenes

    Parameters
    ----------
    limit: int
        Limit for the sieve. Up to this number, all radicals will be calculated

    Returns
    -------
    list:
        List holding the radicals for number n at index n
    """
    radical_list = [1] * (limit + 1)
    radical_list[0] = 0
    for i in range(2, len(radical_list)):
        if radical_list[i] == 1:
            for j in range(i, len(radical_list), i):
                radical_list[j] *= i
    return radical_list

def main():
    """main function
    """
    n_max = 120000
    summe = -1 #takes care of the 0 entry in our sieve
    counter = -1 #takes care of the 0 entry in our sieve

    # create radical list
    radical_list = radical_sieve(n_max)
    # sort radicals in ascending order
    sorted_radicals = sorted((radical, n) for (n, radical) in enumerate(radical_list))

    for c in range(1, n_max): #pylint: disable=C0103
        for radical_a, a in sorted_radicals: #pylint: disable=C0103
            total_radical = radical_list[c] * radical_a
            if total_radical < c:
                b = c - a #pylint: disable=C0103
                total_radical *= radical_list[b]
                if a < b and total_radical < c and math.gcd(a, b) == 1:
                    summe += c
                    counter += 1
            else:
                break

    print("Sum:", summe)
    print("Count:", counter)

if __name__ == "__main__":
    main()
