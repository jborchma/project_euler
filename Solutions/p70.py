def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n //= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors

def phi(n):
    prime_facts = prime_factors(n)
    result = n
    for p in set(prime_facts):
        result *= (1-1/p)
    return result

min_n = 0
minimum = 10e38
for n in range(2,10000000):
    if n % 1000000 == 0:
        print(n)
    val = int(phi(n))
    if sorted(str(n)) == sorted(str(val)) and n/val < minimum:
        minimum = n/val
        min_n = n

print(min_n, minimum)