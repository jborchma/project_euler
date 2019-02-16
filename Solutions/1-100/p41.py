import time

start = time.time()

# create a quick prime sieve
N = 100000000
sieve = [True] * N
sieve[0] = False
sieve[1] = False

def mark(sieve,x):
    for i in range(2*x,N,x):
        sieve[i] = False

for i in range(2,int(N**(1/2))+1):
    if sieve[i]:
        mark(sieve,i)

digits = ['1','2','3','4','5','6','7','8','9']

max_pan = 0
max_length = 0
for i in range(N):
    if sieve[i]:
        length = len(str(i))
        if all(digit in str(i) for digit in digits[:length]):
            max_pan = i
            max_length = length


print('Max. pandigital number is %s with length %s.' % (max_pan,max_length))