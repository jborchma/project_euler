# tactic: create list of prime pairs that fulfill the condition, then find pairs that overlap

# first, create prime sieve and list
n = 100000000
sieve = [True] * n


def mark(sieve, x):
    for i in range(x + x, len(sieve), x):
        sieve[i] = False


for x in range(2, int(len(sieve) ** 0.5) + 1):
    if sieve[x]:
        mark(sieve, x)

prime_dict = {}
for i in range(3, 30000):
    if sieve[i]:
        prime_dict[i] = []

prime_list = []
for i in range(3, 30000):
    if sieve[i]:
        prime_list.append(i)

# now, create lists of pairs
prime_pairs = []
for i, prime1 in enumerate(prime_list):
    for prime2 in prime_list[i + 1 :]:
        new_prime1 = int(str(prime1) + str(prime2))
        new_prime2 = int(str(prime2) + str(prime1))
        if (
            new_prime1 <= n
            and new_prime2 <= n
            and sieve[new_prime1]
            and sieve[new_prime2]
        ):
            prime_dict[prime1].append(prime2)
            prime_dict[prime2].append(prime1)

print("###########Created pair lists############")

minimum = 10000000000
# now create intersections
for prime1 in prime_list:
    for prime2 in prime_dict[prime1]:
        inters = set(prime_dict[prime1]).intersection(prime_dict[prime2])
        if not inters:  # if intersection is empty, continue
            continue
        else:
            for prime3 in inters:
                inters2 = inters.intersection(prime_dict[prime3])
                if not inters2:
                    continue
                else:
                    for prime4 in inters2:
                        # print(prime1,prime2,prime3,prime4)
                        inters3 = inters2.intersection(prime_dict[prime4])
                        if not inters3:
                            continue
                        else:
                            prime5 = min(inters3)

                            summe = prime1 + prime2 + prime3 + prime4 + prime5
                            if summe < minimum:
                                minimum = summe
                                print(prime1, prime2, prime3, prime4, prime5, summe)
                            continue

print("Minimum is", minimum)
