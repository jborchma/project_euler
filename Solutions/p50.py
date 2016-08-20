N = 1000000


sieve = [True] * N

def mark(sieve,x):
    for i in range(2*x,len(sieve),x):
        sieve[i] = False

for i in range(2,int(N**(1/2))+1):
    if sieve[i]:
        mark(sieve,i)

prime_list=[]
for i in range(2,N):
    if sieve[i]:
        prime_list.append(i)
max_summe  = 0
max_length = 0
for length in range(800,0,-1):
    for x in range(0,len(prime_list)):
        summe = sum(prime_list[x:x+length])
        if summe > 1000000:
            break
        if summe in prime_list:
            if length > max_length:
                max_length = length
                max_summe = summe
                print(max_summe)

print(max_summe)


