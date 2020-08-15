"""Solution to problem 7
"""


def main():
    """main function
    """
    prime_list = [2]

    i = 3
    while True:

        if all(i % number != 0 for number in prime_list if number < int(i ** 0.5) + 1):
            prime_list.append(i)

        if len(prime_list) == 10001:
            break
        i = i + 1

    print(prime_list[-1])


if __name__ == "__main__":
    main()
