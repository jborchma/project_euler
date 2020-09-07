"""Solution to problem 68

Given the example with three rows of numbers, we should start by constructing all possible
solutions and then generalize to 5 rows. For n=3, the possible sums for each row are 9, 10, 11
and 12. Going through all combinations for 3 numbers our of 6 without replacemnt, only 9-12 have
3 different combinations.

Doing this for digits 1-10 and 5 rows, we get a possible range of 11-22. This is ignoring the fact
that we are only looking for combinations with 10 only appearing once. This will probably
further limit the range.

The logic is: pick 3 numbers out of the bucket from 1 to 6 (order matters). The second row needs to
end in the second number from row 1. The third row is then the last remaining number, the third
number from row 1 and the second number from row 2.

a b c
d c e
f e b

where a + b + c = d + c + e = f + e + b and a < d and a < f. Looking at multiplicities, a, d, and f
show up once, b, c and e two times. For n=5, we will have 5 numbers with multiplicity 1 and 2 with
multiplicity 2.

So the question is to construct all possible matrices that have this property.

As it turns out, listing all possible combinations with the right multiplicities, there was only one
that worked. And from the numbers one can easily construct the string by hand.
"""
from itertools import combinations


def multiplicity(rows, max_number):
    """Function that returns a dictionary with the multiplicity or each number as well as a list
    where the number of numbers with each multiplicy is counted.

    Parameters:
    rows: list of tuples of numbers
        List holding the combinations (3 numbers picked out of m)
    m: int
        Maximum number that's possible

    Returns
    -------
    list:
        List counting how many times each multiplicty is found. Starts with 0 for index 0.
    dict:
        Dictionary listing the multiplicty (value) of each number (key)
    """
    mults = {i: 0 for i in range(max_number + 1)}
    multiplicities = [0] * len(rows)
    for comb in rows:
        for number in comb:
            mults[number] += 1

    for number, mult in mults.items():
        if number > 0:
            multiplicities[mult] += 1
    return multiplicities, mults


def main():
    """main function"""
    max_sum = 27
    n = 5
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    counts = [0] * (max_sum + 1)
    combs = {i: [] for i in range(max_sum + 1)}

    for comb in combinations(numbers, 3):
        counts[sum(comb)] += 1
        combs[sum(comb)].append(comb)

    for _, kombs in combs.items():
        if len(kombs) >= n:
            for comb in combinations(kombs, n):
                mults, individual_counts = multiplicity(comb, len(numbers))
                # identify if a given combination would work
                if mults == [0, 5, 5, 0, 0] and individual_counts[10] == 1:
                    # now we need to create the number, starting with the lowest mult 1 number and
                    # then iteratively creating the biggest number from it. Keeping track of the
                    # maximum found number while looping through all possible combinations should
                    # yield the end result
                    starting_numbers = [
                        i
                        for i in range(len(individual_counts))
                        if individual_counts[i] == 1
                    ]
                    print(starting_numbers)
                    print(comb)


if __name__ == "__main__":
    main()
