"""Solution to problem 2

Again, a simple brute force calculation
"""


def main():
    """main function
    """
    # initiate fibonacci sequence
    fibon_list = [1, 1]

    # generate sequence elements
    small = True
    while small:
        new_element = fibon_list[-1] + fibon_list[-2]
        fibon_list.append(new_element)
        if new_element > 4000000:
            small = False

    # filter out all even elements
    fibon_even = [number for number in fibon_list if number % 2 == 0]

    print(f"Answer: {sum(fibon_even)}")


if __name__ == "__main__":
    main()
