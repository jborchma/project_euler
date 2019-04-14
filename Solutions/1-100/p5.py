"""Solution to problem 5
"""

def main():
    """main function
    """
    check_list = [11, 13, 14, 16, 17, 18, 19, 20]
    i = 2520
    while True:
        if all(i %divisor == 0 for divisor in check_list):
            print(i)
            break
        else:
            i = i+2520

if __name__ == "__main__":
    main()
