"""Solution to problem 3

again, brute force
"""

def main():
    """main function
    """
    limit = 600851475143
    i = 2
    while i*i < limit:
        while limit % i == 0:
            limit = limit / i
        i = i + 1

    print(limit)

if __name__ == "__main__":
    main()
