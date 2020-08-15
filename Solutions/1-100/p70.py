"""Solution to problem 70
"""


def prime_factors(n):  # pylint: disable=C0103
    """This function finds the prime factors of n

    Parameters
    ----------
    n: int
        Number to be factorized

    Returns
    -------
    list
        List of prime factors
    """
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def phi(n):  # pylint: disable=C0103
    """Calculate Euler's totient function
    """
    prime_facts = prime_factors(n)
    result = n
    for prime in set(prime_facts):
        result *= 1 - 1 / prime
    return result


def main():
    """main function
    """
    min_n = 0
    minimum = 10e38
    for n in range(2, 10000000):  # pylint: disable=C0103
        if n % 1000000 == 0:
            print(n)
        val = int(phi(n))
        if sorted(str(n)) == sorted(str(val)) and n / val < minimum:
            minimum = n / val
            min_n = n

    print(min_n, minimum)


if __name__ == "__main__":
    main()
