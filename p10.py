n = 2000000
sieve = [True] * n

def mark(sieve, x):
    for i in range(x+x, len(sieve), x):
        sieve[i] = False

for x in range(2,int(len(sieve)**0.5)+1):
    if sieve[x]:
        mark(sieve,x)


def test_prime(n):
    if sieve[n]:
        return True
    else:
        return False

def prime_euqation(n,a,b):
    return n**2 + a*n +b

summe = 0
for i in range(2,2000000):
    if sieve[i]:
        summe += i

print(summe)


