"""Solution to problem 77

I think this can be a combination of the prime sieve and the coin combination problem 31.
"""


def prime_sieve(limit):
    """Sieve of Eratosthenes for prime numbers
    """
    result = [True] * (limit + 1)
    result[0] = False
    result[1] = False
    for i in range(2, len(result)):
        if result[i]:
            for j in range(i * i, len(result), i):
                result[j] = False
    return result


def main():
    """main function
    """
    target = 100
    sieve_list = prime_sieve(100)
    prime_list = [i for i, indicator in enumerate(sieve_list) if indicator]

    ways = {i: 0 for i in range(target + 1)}
    ways[0] = 1

    for prime in prime_list:
        for j in range(prime, target + 1):
            ways[j] += ways[j - prime]

    for number in ways:
        if ways[number] > 5000:
            print(number, ways[number])
            break


if __name__ == "__main__":
    main()
