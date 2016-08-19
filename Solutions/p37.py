import time

start = time.time()

n = 1000000

sieve = [True] * n

sieve[1] = False

def mark(sieve,x):
    for x in range(2*x,len(sieve),x):
        sieve[x] = False

for x in range(2,int(n**0.5)+1):
    if sieve[x]:
        mark(sieve,x)

truncatables = []
for i in range(10,1000000):
    if sieve[i]:
        num_str = str(i)
        if all(sieve[int(num_str[j:])] for j in range(1,len(num_str))) and all(sieve[int(num_str[:j])] for j in range(1,len(num_str))):
            truncatables.append(i)

print(sum(truncatables))
print(time.time()-start)