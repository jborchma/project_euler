"""Solution to problem 174

This problem should be easily solved using my solution to problem 173. I just used the formula
I derived there and then counted the possible solutions.
"""
from collections import Counter

N_MAX = 250001
N = 1000000


def main():
    """main function
    """
    tiles = [
        4 * M ** 2 - (8 - 4 * i) * M
        for M in range(1, 250001)
        for i in range(3, N // (4 * M) - M + 3)
        if 4 * M ** 2 - (8 - 4 * i) * M < N
    ]
    counted = Counter(tiles)
    counter = 0
    for i in range(1, 11):
        counter += sum(value == i for value in counted.values())

    print(f"Answer: {counter}.")


if __name__ == "__main__":
    main()
