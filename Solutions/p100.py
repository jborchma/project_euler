import math

def probab(n,b):

    return (b/n)*(b-1)/(n-1)

def relation(n):


    return 1/2 * (1 + math.sqrt(1 - 2*n + 2*n**2))
print(707106781187)
for n in range(10**12,10**12+10**6):
    if relation(n) % 1 == 0:
        print(n)
        print(relation(n))
        print((relation(n)/n)*(relation(n)-1)/(n-1))
        break

# print(int(1/2 * (1 + math.sqrt(1 - 2*(10**2) + 2*(10**12)**2))))