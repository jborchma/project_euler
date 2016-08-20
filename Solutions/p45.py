from numpy import *

def is_triagonal(n):
    if abs(1/2 * (-1 + sqrt(1 + 8*n)) % 1) < 10**(-7):
        return True
    else:
        return False

def is_pentagonal(n):
    if abs(1/6 * (1 + sqrt(1 + 24 *n)) % 1) < 10**(-7):
        return True
    else:
        return False

def is_hexagonal(n):
    if abs(1/4 * (1 + sqrt(1 + 8 * n)) % 1) < 10**(-7):
        return True
    else:
        return False

for n in range(286,100000):
    T = n/2*(n+1)
    if is_pentagonal(T) and is_hexagonal(T):
        print(n,T)
        break