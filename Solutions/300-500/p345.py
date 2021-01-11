"""Solution to problem 345

The large matrix is 15x15, so there are 15! possible solutions. Way too many to
search.

I am going row by row (more convenient than column by column due to the way the
matrix is defined) and I am going to check if it is still possible to beat my current best.
If not, abort the search along that path in the search space.

This worked super fast. However, since this is a search problem, a bunch of other methods can
work too. For example, a genetic algorithm or annealing. I implemented annealing. It works pretty
well with the current values for the starting temperature and the cooling rate.
"""
from math import exp
from random import shuffle, randint, random

MATRIX = (
    (7, 53, 183, 439, 863, 497, 383, 563, 79, 973, 287, 63, 343, 169, 583),
    (627, 343, 773, 959, 943, 767, 473, 103, 699, 303, 957, 703, 583, 639, 913),
    (447, 283, 463, 29, 23, 487, 463, 993, 119, 883, 327, 493, 423, 159, 743),
    (217, 623, 3, 399, 853, 407, 103, 983, 89, 463, 290, 516, 212, 462, 350),
    (960, 376, 682, 962, 300, 780, 486, 502, 912, 800, 250, 346, 172, 812, 350),
    (870, 456, 192, 162, 593, 473, 915, 45, 989, 873, 823, 965, 425, 329, 803),
    (973, 965, 905, 919, 133, 673, 665, 235, 509, 613, 673, 815, 165, 992, 326),
    (322, 148, 972, 962, 286, 255, 941, 541, 265, 323, 925, 281, 601, 95, 973),
    (445, 721, 11, 525, 473, 65, 511, 164, 138, 672, 18, 428, 154, 448, 848),
    (414, 456, 310, 312, 798, 104, 566, 520, 302, 248, 694, 976, 430, 392, 198),
    (184, 829, 373, 181, 631, 101, 969, 613, 840, 740, 778, 458, 284, 760, 390),
    (821, 461, 843, 513, 17, 901, 711, 993, 293, 157, 274, 94, 192, 156, 574),
    (34, 124, 4, 878, 450, 476, 712, 914, 838, 669, 875, 299, 823, 329, 699),
    (815, 559, 813, 459, 522, 788, 168, 586, 966, 232, 308, 833, 251, 631, 107),
    (813, 883, 451, 509, 615, 77, 281, 613, 459, 205, 380, 274, 302, 35, 805),
)


# MATRIX = (
#     (7, 53, 183, 439, 863),
#     (497, 383, 563, 79, 973),
#     (287, 63, 343, 169, 583),
#     (627, 343, 773, 959, 943),
#     (767, 473, 103, 699, 303),
# )

SIZE = len(MATRIX)

REMAIMING_MAX = []
for i in range(0, SIZE):
    max_sum = sum([max(row) for row in MATRIX[i:]])
    REMAIMING_MAX.append(max_sum)


def get_sum(permutation):
    """Calculate matrix sum of permutation.

    I use a permutation where the index means the row and the number means the column.
    """
    summe = 0
    for row, column in enumerate(permutation):
        summe += MATRIX[row][column]
    return -summe


def calculate_probability(energy, new_energy, temperature):
    """Calculates the Boltzman factor."""
    if new_energy < energy:
        return 1.0
    else:
        return exp(float(energy - new_energy) / temperature)


def anneal():
    """Search maximum sum by annealing."""
    best_sol = list(range(SIZE))
    best_sum = get_sum(best_sol)
    shuffle(best_sol)

    temp = 10000000
    cool_rate = 0.0003

    counter = 0
    while temp > 1:
        new_sol = best_sol.copy()
        i, j = randint(0, SIZE - 1), randint(0, SIZE - 1)
        new_sol[i], new_sol[j] = new_sol[j], new_sol[i]
        new_energy = get_sum(new_sol)
        cur_energy = best_sum
        if calculate_probability(cur_energy, new_energy, temp) > random():
            best_sol = new_sol.copy()
            best_sum = new_energy
        temp *= 1 - cool_rate
        counter += 1

    print(counter)

    print(best_sol)
    print(best_sum)
    return best_sol, best_sum


def search_matrix(row, current_sum, best, mask):
    """Search through the matrix by row."""
    if row == SIZE:
        return current_sum

    # if we compare the current_sum plus the max sum of the remaining columns, and we can't beat our
    # best sum, abort
    if current_sum + REMAIMING_MAX[row] <= best:
        return 0

    for column in range(0, SIZE):
        # if column is already being used, move to next
        if mask[column]:
            continue

        # go to next column
        new_mask = mask.copy()
        new_mask[column] = True

        current = search_matrix(
            row + 1, current_sum + MATRIX[row][column], best, new_mask
        )

        if current > best:
            best = current

    return best


def main():
    """Main function."""
    # dynamic programming
    # mask = [False] * SIZE
    # best = search_matrix(0, 0, 0, mask)
    # print(best)

    # annealing
    anneal()


if __name__ == "__main__":
    main()
