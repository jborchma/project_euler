# from itertools import product
# from functools import reduce
# import operator

# def mark(sieve, x):
#     for i in range(2*x, len(sieve), x):
#         sieve[i] = False

# def triangle(n):
#     return int(1/2*n*(n+1))

# def is_prime(n):
#     is_prime = True
#     for div in range(2,n):
#         if n % div == 0:
#             is_prime=False

#     return is_prime

# def prime_factors(n):

#     prime_factors = []

#     sieve = [True] * (n)

#     for x in range(2,n):
#         if sieve[x]:
#             mark(sieve,x)

#     prime_list = [i for i in range(2,len(sieve)) if sieve[i]]

#     if is_prime(n):
#         prime_list.append(n)

#     searching = True
#     while searching:
#         for prime in prime_list:
#             if n == 1:
#                 searching = False
#                 break
#             if n % prime == 0:
#                 prime_factors.append(prime)
#                 n = n // prime
#                 continue

#     factors = []
#     exponents = []
#     for prime in list(set(prime_factors)):
#         factors.append(prime)
#         exponents.append(prime_factors.count(prime))


#     return factors, exponents

# def prod(l):
#    return reduce(operator.mul, l, 1)

# def powered(factors, powers):
#    return prod(f**p for (f,p) in zip(factors, powers))


# def divisors(n):

#     divisors = [1,n]

#     factors, exponents = prime_factors(n)

#     exponents2 = [range(i+1) for i in exponents]
#     return sorted([powered(factors,es) for es in product(*exponents2)])

#     # divisors.extend(prime_factor)

#     # for i,prime1 in enumerate(prime_factor):
#     #     for j in range(i+1,len(prime_factor)):
#     #         divisors.append(prime1*prime_factor[j])



#     #return list(set(divisors))


# flag = True
# n = 73920
# while flag:
#     triangle_num = triangle(n)
#     div_num = len(divisors(triangle_num))
#     if div_num > 200:
#         print(triangle_num)
#         break

#     n +=1

prime_list = [2, 3, 5, 7, 11, 13, 17, 19, 23]   # Ensure that this is initialised with at least 1 prime
prime_dict = dict.fromkeys(prime_list, 1)
lastn      = prime_list[-1]

def _isprime(n):
    ''' Raw check to see if n is prime. Assumes that prime_list is already populated '''
    isprime = n >= 2 and 1 or 0
    for prime in prime_list:                    # Check for factors with all primes
        if prime * prime > n: break             # ... up to sqrt(n)
        if not n % prime:
            isprime = 0
            break
    if isprime: prime_dict[n] = 1               # Maintain a dictionary for fast lookup
    return isprime

def prime(x):
    ''' Returns the xth prime '''
    global lastn
    while len(prime_list) <= x:                 # Keep working until we've got the xth prime
        lastn = lastn + 1                       # Check the next number
        if _isprime(lastn):
            prime_list.append(lastn)            # Maintain a list for sequential access
    return prime_list[x]

def num_factors(n):
    ''' Returns the number of factors of n, including 1 and n '''
    div = 1
    x = 0
    while n > 1:
        c = 1
        while not n % prime(x):
            c = c + 1
            n = n / prime(x)
        x = x + 1
        div = div * c
    return div

for i in range(1, 1000000000):
    n = i * (i+1) / 2
    if num_factors(n) > 500:
        print(n)
        break


# print(num_factors(10))



