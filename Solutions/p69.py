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

maximum_n = 0
maximum = 0
for n in range(2,1000000):
    if n % 100000 == 0:
        print(n)
    val = n/phi(n)
    if val > maximum:
        maximum = val
        maximum_n = n

print(maximum_n, maximum)