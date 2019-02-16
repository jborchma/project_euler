"""Solution to problem 105

It's a pretty simple solution:

For each set, I go from longest possible subsets to smallest lengths. I get all combinations
and take the sum. If I already have a subset with the sum, I check if they are disjoint. If they're
not, I continue, if they are, the test fails.

For the second condition, I check for all sums smaller than the one I calculated for a specific
subset, if there is a subset with more element but a smaller sum. In that case, the test fails.
"""
import itertools
from collections import defaultdict

def load_sets():
    """Function to load sets
    """
    sets = []
    with open("p105_sets.txt", "r") as file:
        for line in file.read().split("\n"):
            new_set = []
            for number in line.split(","):
                new_set.append(int(number))
            sets.append(new_set)

    for menge in sets:
        menge.sort()

    return sets

def check_partial_sums(menge):
    """Check if two partial sums match
    """
    summen = defaultdict(list)
    for length in range(len(menge), 0, -1):
        for comb in itertools.combinations(menge, length):
            summe = sum(comb)
            # first condition
            if summen[summe]:
                for item in summen[summe]:
                    if any(i in item for i in comb):
                        continue
                    else:
                        return False
            # second condition
            for i in range(summe//2, summe + 1):
                if summen[i]:
                    for item in summen[i]:
                        if len(item) > length and not any(i in item for i in comb):
                            return False
            summen[summe].append(comb)

    return True

def main():
    """main function
    """
    sets = load_sets()
    res = [sum(menge) for menge in sets if check_partial_sums(menge)]
    print(sum(res))

if __name__ == "__main__":
    main()
