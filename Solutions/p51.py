"""Solution to problem 51

This is a brute force approach to the problem. I loop through the numbers, get all combinations
of indeces for the digits and the test which substitutions are prime. In case, I have more than
two variations that are not prime, I can end the search for that number early.
"""
import itertools

N = 1000000
SIEVE = [True] * N

def mark(sieve, x):
    """This function marks prime numbers. Works well up to O(10**7)
    """
    for number in range(x+x, len(sieve), x):
        sieve[number] = False

for x in range(2, int(N**0.5) + 1):
    if SIEVE[x]:
        mark(SIEVE, x)

print("Generated the sieve...")

def test_prime(n):
    """Tests if a number is prime
    """
    if SIEVE[n]:
        return True
    else:
        return False

def test_number_chain(number):
    """Function to test if number is in a 8 part chain
    """
    # for each possible number of digits
    max_prime_counter = 0
    max_prime_list = []
    string_number = str(number)
    for number_of_digits in range(1, len(string_number)):
        combs = itertools.combinations(range(0, len(string_number)), number_of_digits)
        for comb in combs:
            prime_list = []
            prime_counter = 0
            non_prime_counter = 0
            for digit in range(0, 10):
                new_number = ""
                for position, old_digit in enumerate(string_number):
                    if position in comb:
                        new_number += str(digit)
                    else:
                        new_number += old_digit
                if test_prime(int(new_number)) and len(str(int(new_number))) >= len(string_number):
                    prime_counter += 1
                    prime_list.append(int(new_number))
                    if prime_counter > max_prime_counter:
                        max_prime_counter = prime_counter
                        max_prime_list = prime_list
                else:
                    non_prime_counter += 1
                    if non_prime_counter > 2:
                        break

    return max_prime_counter, max_prime_list

def main():
    """main function
    """
    for number in range(100000, N):
        if number % 100000 == 0:
            print(number)
        max_prime_counter, prime_list = test_number_chain(number)
        if max_prime_counter == 8:
            print("Found:", min(prime_list))
            break

if __name__ == "__main__":
    main()
