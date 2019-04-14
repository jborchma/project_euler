"""Solution to problem 1

Just a simple brute force solution
"""
def main():
    """main function
    """
    add_list = [i for i in range(1000) if (i%3 == 0 or i % 5 == 0)]
    print(sum(add_list))

if __name__ == "__main__":
    main()
