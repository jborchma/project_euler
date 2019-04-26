"""Solution to problem 95

I used an optimized prime sieve to calculate all primes below 1000000 and then calculated the
divisor sum using the prime factorization of each number. Then, it just searched through each number
below 1000000 and ended the search if the aliquot sum was prime or exceeded 1000000.
"""
from itertools import compress
from operator import itemgetter

def prime_sieve(n):
    """List of primes < n for n > 2

    This sieve is essentially the usual sieve of Eratosthenes, but with a couple of smart
    improvements and tweaks:
    - It uses a byterray, which speeds things up compared to a list
    - It only creates the sieve for odd numbers, which speeds things up by a factor of two.
      This is the reason for all the `//2` in the code
    - It uses itertools compress function to turn the sieve (a list of booleans, essentially)
      into a list of integers

    All these things combined make this sieve essentially ten times faster than the old one I have
    used so far (for example in problems 10, 77, ...)

    Parameters
    ----------
    n: int
        Upper limit up to which we will look for primes

    Returns
    -------
    list
        List holding all primes < n
    """
    sieve = bytearray([True]) * (n//2)
    for i in range(3, int(n**0.5)+1, 2):
        if sieve[i//2]:
            sieve[i*i//2::i] = bytearray((n-i*i-1)//(2*i)+1)
    return [2, *compress(range(3, n, 2), sieve[1:])]


def prime_factorization(n, prime_list):
    """Return the prime factorization of n

    This function returns a list of the prime factors of n including the exponent of each prime
    factor. It expects the list of prime factors to be given as an argument, to enable rapid
    calls to this function without having to recalculate the prime list.

    Parameters
    ----------
    n: int
        Number to be factored
    primes_list: [int]
        List of prime numbers

    Returns
    -------
    list
        List holding tuples (p, e), where p is the prime factor and e is the exponent in the
        factorization
    """
    prime_factors = []
    for prime in prime_list:
        if prime * prime > n:
            # in case the prime numbers are larger than sqrt(n), break
            break
        count = 0 # initialize the count
        while not n % prime: # in case prime divides n
            n //= prime
            count += 1
        if count > 0:
            prime_factors.append((prime, count))
    if n > 1:
        prime_factors.append((n, 1))
    return prime_factors


def divisors(n, prime_list):
    """Unsorted list of the divisors of n
    """
    divs = [1]
    for prime, exponent in prime_factorization(n, prime_list):
        divs += [x * prime**k for k in range(1, exponent + 1) for x in divs]
    return divs


def divisor_sum(n, prime_list):
    """Calculates the sum of all proper divisors
    """
    summe = 1
    for prime, exponent in prime_factorization(n, prime_list):
        summe *= int((prime ** (exponent + 1) - 1) / (prime - 1))

    return summe - n

def main():
    """main function
    """
    n = 1000000
    primes_list = prime_sieve(int(n**0.5)+1)
    prime_lookup_dict = {prime: None for prime in primes_list}
    # print(divisors(n, primes_list))
    # print(divisor_sum(n, primes_list))
    sequence_results = []
    for number in range(2, n):
        if number in prime_lookup_dict:
            continue
        sequence_list = [number]
        searching = True
        while searching:
            aliquot_sum = divisor_sum(number, primes_list)
            if aliquot_sum > 1000000 or aliquot_sum in prime_lookup_dict:
                break
            if aliquot_sum not in sequence_list:
                sequence_list.append(aliquot_sum)
            else:
                searching = False
                if aliquot_sum == sequence_list[0]:
                    sequence_results.append((sequence_list[0], len(sequence_list),
                                             min(sequence_list)))

            number = aliquot_sum


    print("Answer:", max(sequence_results, key=itemgetter(1)))

if __name__ == "__main__":
    main()
