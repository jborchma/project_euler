"""Solution to problem 123
"""

def mark(sieve, x):
    """This function marks prime numbers
    """
    for number in range(x+x, len(sieve), x):
        sieve[number] = False

def make_prime_list(max_n, sieve):
    """make prime number list
    """
    prime_list = [0]
    for i in range(2, max_n):
        if sieve[i]:
            prime_list.append(i)

    return prime_list

def main():
    """main function
    """
    # create prime sieve
    n_max = 400000
    sieve = [True] * n_max

    for x in range(2, int(n_max**0.5) + 1):
        if sieve[x]:
            mark(sieve, x)

    # create prime list from sieve
    p_list = make_prime_list(n_max, sieve)

    # loop through primes and calculate remainder
    for n in range(17985-1, len(p_list)):
        number = ((p_list[n] - 1)**n + (p_list[n]+1)**n) % p_list[n]**2
        if number > 10**10:
            print("Found n:", n)
            break

if __name__ == "__main__":
    main()
