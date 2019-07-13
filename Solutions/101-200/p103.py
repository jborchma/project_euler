"""Solution

I am using the check function from my solution to problem 105. The rule that was mentioned in the
problem statement yield a special set with sum 255. Hence, the optimal set should have a sum < 255.
Now, we only need to search for a special set with lenght 7 that has a smaller sum. It is
actually the initial guess, so all the code is kind of useless...
"""
import itertools
from collections import defaultdict


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
            for i in range(summe // 2, summe + 1):
                if summen[i]:
                    for item in summen[i]:
                        if len(item) > length and not any(i in item for i in comb):
                            return False
            summen[summe].append(comb)

    return True


# for i, comb in enumerate(itertools.combinations(range(17, 50), 7)):
#     if i % 10000 == 0:
#         print(i, comb)
#     if sum(comb) < 255:
#         if check_partial_sums(comb):
#             print(comb, sum(comb))

initial_guess = [20, 31, 38, 39, 40, 42, 45]  # sums up to 255
