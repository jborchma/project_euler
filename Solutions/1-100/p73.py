"""Solution to problem 73

Just a simple brute force solution
"""
import math

def main():
    """main function
    """
    d_max = 12000

    summe = 0
    for d in range(5, d_max+1):
        for n in range(d // 3 + 1, (d - 1) // 2 + 1):
            if math.gcd(n, d) == 1:
                summe += 1
    print(f"Answer: {summe}")

if __name__ == "__main__":
    main()
