"""Solution to problem 157

Even though the problem is very similar to problem 108, I was not able to directly use the same
solution due to the p. The overall derivation is still valid, though. After calculating all divisors
of 10^2n with <= 10^n, we now need to find all possible p by using the fact that p needs to be a
divisor of both 10^n+d as well as 10^2n/d +10^n, where d is a divisor of 10^2n. Once we have all
unique p for each d, we only need to count and sum them.

Not the fasted solution...
"""
import math

def divisor_generator(n): #pylint: disable=C0103
    """Generate divisors of n

    Parameters
    ----------
    n: int
        Integer for which the divisors will be generated

    Yields
    ------
    int
        Divisor of n
    """
    large_divisors = []
    for i in range(1, int(math.sqrt(n) + 1)):
        if n % i == 0:
            yield i
            if i*i != n:
                large_divisors.append(int(n / i))
    for divisor in reversed(large_divisors):
        yield divisor

def main():
    """main function
    """
    summe = 0
    for n in range(1, 10): #pylint: disable=C0103
        n_divisors = list(divisor_generator(10**(2*n)))
        n_divisors = [divisor for divisor in n_divisors if divisor <= 10**n]
        counter = 0
        for divisor in n_divisors:
            solution_1 = list(divisor_generator(10**n+divisor))
            solution_2 = list(divisor_generator(10**(2*n) / divisor + 10**n))
            cross_section = [divisor for divisor in solution_1 if divisor in solution_2]
            counter += len(cross_section)

        summe += counter

    print(f"Answer: {summe}")

if __name__ == "__main__":
    main()
