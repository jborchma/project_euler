"""Solution to problem 27
"""


def mark(sieve, x):
    for i in range(x + x, len(sieve), x):
        sieve[i] = False


def test_prime(sieve, n):
    return sieve[n]


def prime_euqation(n, a, b):
    return n ** 2 + a * n + b


def main():
    """main function
    """
    n = 1000000
    sieve = [True] * n

    for x in range(2, int(len(sieve) ** 0.5) + 1):
        if sieve[x]:
            mark(sieve, x)

    max_length = 0
    a_max = 0
    b_max = 0
    for a in range(-1, -1000, -1):
        if a % 100 == 0:
            print(a)
        for b in range(1, 1000):
            length = 0
            for n in range(0, 100):
                if test_prime(sieve, prime_euqation(n, a, b)):
                    length += 1
                else:
                    if max_length < length:
                        max_length = length
                        a_max = a
                        b_max = b
                    break

    print(max_length)
    print(a_max, "a_max")
    print(b_max, "b_max")


if __name__ == "__main__":
    main()
