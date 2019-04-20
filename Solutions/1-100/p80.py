"""Solution to problem 80

This is actually a very cool problem. I ended up using the mapping a/b -> (a + n*b)/(a+b), which
converges to sqrt(n). I had to write my own matrix squaring because numpy uses its own int64
integer type which overflows with the numbers that come up in this problem. Hence, the
multiplication is just done by hand using lists (could probably be improved)

Then, I set the precision for the Decimal package to 102 (in order to prevent rounding issues) and
then looped through the first 100 integers. 16 squarings was enough, which I found by manual search.
"""
from decimal import getcontext, Decimal
import math

getcontext().prec = 102

def is_square(number):
    """Check if a number is the square of an integer.
    """
    square_root = int(math.sqrt(number) + 0.5)
    return square_root * square_root == number

def square_matrix(A): #pylint: disable=C0103
    """Square matrix
    """
    a_11_new = A[0][0]**2 + A[1][0] * A[0][1]
    a_21_new = A[0][0] * A[0][1] + A[0][1] * A[1][1]
    a_12_new = A[1][0] * A[0][0] + A[1][1] * A[1][0]
    a_22_new = A[1][1]**2 + A[0][1] * A[1][0]

    return [[a_11_new, a_12_new], [a_21_new, a_22_new]]

def square_root_digits(n, power): #pylint: disable=C0103
    """Calculates square root digits
    """
    A = [[1, n], [1, 1]] #pylint: disable=C0103
    for _ in range(power):
        A = square_matrix(A) #pylint: disable=C0103

    result = [A[0][0] + A[0][1], A[1][0] + A[1][1]]
    return result

def main():
    """main function
    """
    summe = 0
    for i in range(2, 101):
        if not is_square(i):
            res = square_root_digits(i, 16)
            integer, decimal_digits = str(Decimal(int(res[0]))/Decimal(int(res[1]))).split(".")
            summe += int(integer) + sum([int(digit) for digit in decimal_digits[:99]])

    print(f"Answer: {summe}")

if __name__ == "__main__":
    main()
