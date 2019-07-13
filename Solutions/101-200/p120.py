"""Solution to problem 120

This problem can be easily solved by just using a brute force solution and checking all
exponents up to sume `n_max`. As it turns out, 1000 wasn't enough, but 2000 was.
"""


def main():
    """main function
    """
    summe = 0
    for a in range(3, 1001):
        r_max = max([((a - 1) ** n + (a + 1) ** n) % a ** 2 for n in range(1, 2000)])
        summe += r_max

    print(summe)


if __name__ == "__main__":
    main()
