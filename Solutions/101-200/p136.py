"""Solution to problem 136

Same as 135, just a higher limit and we didn't search for 10 but 1
"""
import math

def create_solutions(n_limit=50000000):
    """creates solutions
    """
    number_of_solutions = [0] * n_limit
    for x in range(1, 2*n_limit):
        for d in range(int(math.ceil(x/5)), int((x+1)/2)):
            solution = (d-x) * (x - 5 * d)
            if solution >= n_limit:
                break
            number_of_solutions[solution] += 1

    return number_of_solutions

def main():
    """main function
    """
    counted = create_solutions()
    print("Answer:", counted.count(1))

if __name__ == "__main__":
    main()
