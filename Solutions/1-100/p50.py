"""Solution to problem 50
"""

N = 1000000

def mark(sieve, x): #pylint: disable=C0103
    """Marks consecutive multiples as not prime
    """
    for i in range(2*x, len(sieve), x):
        sieve[i] = False

def main():
    """main function
    """
    sieve = [True] * N

    for i in range(2, int(N**(1/2))+1):
        if sieve[i]:
            mark(sieve, x=i)

    prime_list = []
    for i in range(2, N):
        if sieve[i]:
            prime_list.append(i)

    max_summe = 0
    max_length = 0
    for length in range(800, 0, -1):
        for x in range(0, len(prime_list)): #pylint: disable=C0103
            summe = sum(prime_list[x:x+length])
            if summe > 1000000:
                break
            if summe in prime_list:
                if length > max_length:
                    max_length = length
                    max_summe = summe
                    print(max_summe)

    print(max_summe)
