n = 1000000
sieve = [True] * n

sieve[1] = False

def mark(sieve, x):
    for i in range(2*x, len(sieve),x):
        sieve[i] = False

for x in range(2,int(len(sieve)**0.5)+1):
    if sieve:
        mark(sieve,x)

def test_prime(n):
    if sieve[n]:
        return True
    else:
        return False

def all_circ_perms(num_list):
    if len(num_list) <= 1:
        yield num_list
    else:
        for position in range(len(num_list)):
            yield num_list[position:] + num_list[0:position]

circular = [2,5]
for i in range(2,1000000):
    if sieve[i]:
        num_str = str(i)
        if '2' in num_str or '5' in num_str:
            continue

        else:
            if all(sieve[int(perm)] for perm in all_circ_perms(num_str)):
                circular.append(i)


print(len(circular))
