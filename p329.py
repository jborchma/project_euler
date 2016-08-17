from numpy import *
import time
import scipy
from decimal import Decimal, getcontext
from fractions import Fraction,gcd
getcontext().prec = 64

start = time.time()

N_max = 500

# added a 6 to the probabilities, such that I only have integers

P = zeros([N_max,N_max]) #transition matrix for P
N = zeros([N_max,N_max]) #transition matrix for N

#create a sieve for the prime numbers up to 500
def primes(n):
    sieve = [True] * (n+1)
    sieve[0] = False
    sieve[1] = False
    for p in range(2, n+1):
        if (sieve[p]):
            for i in range(2*p, n+1, p):
                sieve[i] = False

    return sieve

prime_list = primes(500)


# fill the two transition matrices
# start with the ends of the chain, 499 is prime
P[0,1] = Fraction(2,3)*6
N[0,1] = Fraction(1,3)*6

P[N_max-1,N_max-2] = Fraction(2,3)*6
N[N_max-1,N_max-2] = Fraction(1,3)*6

for i in range(1,N_max-1):
    if prime_list[i+2]:
        P[i,i+1] = Fraction(1,2) * Fraction(2,3)*6
        N[i,i+1] = Fraction(1,2) * Fraction(1,3)*6
    elif not prime_list[i+2]:  
        P[i,i+1] = Fraction(1,2) * Fraction(1,3)*6
        N[i,i+1] = Fraction(1,2) * Fraction(2,3)*6
    if prime_list[i]:
        P[i,i-1] = Fraction(1,2) * Fraction(2,3)*6
        N[i,i-1] = Fraction(1,2) * Fraction(1,3)*6
    elif not prime_list[i]:  
        P[i,i-1] = Fraction(1,2) * Fraction(1,3)*6
        N[i,i-1] = Fraction(1,2) * Fraction(2,3)*6

# P[0,1] = 1
# N[0,1] = 1

# P[N_max-1,N_max-2] = 1
# N[N_max-1,N_max-2] = 1

# for i in range(1,N_max-1):
#     if prime_list[i+2]:
#         P[i,i+1] = 1
#         N[i,i+1] = 1
#     elif not prime_list[i+2]:  
#         P[i,i+1] = 1
#         N[i,i+1] = 1
#     if prime_list[i]:
#         P[i,i-1] = 1
#         N[i,i-1] = 1
#     elif not prime_list[i]:  
#         P[i,i-1] = 1
#         N[i,i-1] = 1


summe = 0

# p_first_P = 0
# for i in range(1,501):
#     if prime_list[i]:
#         p_first_P += 1

# p_first_P = Fraction(2,3)*Fraction(p_first_P,500) + Fraction(1,3)*Fraction(500-p_first_P,500)
# print(p_first_P)

alpha = ones([1,N_max])
for i in range(0,500):
    if prime_list[i+1]:
        alpha[0,i] = Fraction(2,3)*6
    else:
        alpha[0,i] = Fraction(1,3)*6

for case in ['P','P','P','N','N','P','P','P','N','P','P','N','P','N']:

    if case == 'P':
        alpha = dot(alpha,P)
    else:
        alpha = dot(alpha,N)

summe = sum(alpha)

# i need to get rid of the factors of 6 again and normalize by 500
print(Fraction(int(summe),int(500*6**15)))
print('It took %ss to calculate the result.' % (time.time()-start))


    



