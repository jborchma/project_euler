"""Solution to problem 117

This solution is similar to 116, but now the calculation of the permutations is

(r + g + b + s)!/(r!g!b!s!) = (m - r - 2*g - 3*b)!/(r!g!b!*(m - 2*r - 3*g - 4*b)!)

Now we just need to loop through all possible combinations of r, g and b.
"""
import math
M = 50

def main():
    """main function
    """
    summe = 0
    for r in range(0, M-2):
        for g in range(0, M-3):
            for b in range(0, M-3):
                if M - 2 * r - 3 * g - 4 * b >= 0: # prevent negtive numbers
                    summe += math.factorial(M - r - 2 * g - 3 * b)/(
                        math.factorial(r) * math.factorial(g) * math.factorial(b)
                        * math.factorial(M - 2 * r - 3 * g - 4 * b))

    print(summe)

if __name__ == "__main__":
    main()
