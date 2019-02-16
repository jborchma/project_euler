"""Solution to Project Euler problem 69
"""

def prime_factors(n):
    """Calculates the prime factors of n and returns them in a list
    """
    i = 2
    factors = []
    while i * i <= n:
        # if i does not divide n, increase i by 1
        if n % i:
            i += 1
        # if i divides n, divide n by i and append i to the factors
        else:
            n //= i
            factors.append(i)
    # if we are done and the remainder of n is still larger 1, it is a prime and a divisor
    if n > 1:
        factors.append(n)
    return factors

def phi(n):
    """Computes Euler's totient function via

    phi(n) = n * prod_i (1 - 1/p_i),

    where p_i are the prime factors of n.
    """
    prime_facts = prime_factors(n)
    result = n
    for prime in set(prime_facts):
        result *= (1-1/prime)
    return result

def main():
    """Main function
    """
    maximum_n = 0
    maximum = 0
    for n in range(2, 1000000):
        if n % 100000 == 0:
            print(n)
        val = n/phi(n)
        if val > maximum:
            maximum = val
            maximum_n = n

    print(maximum_n, maximum)

if __name__ == "__main__":
    main()
