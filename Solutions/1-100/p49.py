N = 10000


sieve = [True] * N


def mark(sieve, x):
    for i in range(2 * x, len(sieve), x):
        sieve[i] = False


for i in range(2, int(N ** (1 / 2)) + 1):
    if sieve[i]:
        mark(sieve, i)

prime_list = []
for i in range(2, N):
    if sieve[i] and i > 1000:
        prime_list.append(i)


candidates = []
for i in range(len(prime_list)):
    for j in range(i + 1, len(prime_list)):
        if (prime_list[i] + int((prime_list[j] - prime_list[i]) / 2)) in prime_list:
            if set(str(prime_list[i])) == set(str(prime_list[j])) and set(
                str(prime_list[i])
            ) == set(str((prime_list[i] + int((prime_list[j] - prime_list[i]) / 2)))):
                print(prime_list[i])
                print(prime_list[j])
                print((prime_list[i] + int((prime_list[j] - prime_list[i]) / 2)))
