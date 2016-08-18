from scipy.special import binom


# calculate the probabilities for n dice with s sides
def dice_possibilities(n,s):
    possibilities = {}
    possibilities[n] = 1
    for k in range(s*n+1):
        if k < n:
            possibilities[k]=0
        else:
            possibilities[k] = sum([(-1)**j * binom(n,j)*binom(k-s*j-1,n-1) for j in range(0,int((k-n)/s) + 1)])

    return possibilities

#initiate problem
pete_possib = dice_possibilities(9,4)
pete_total = sum([pete_possib[i] for i in range(37)])
colin_possib = dice_possibilities(6,6)
colin_total = sum([colin_possib[i] for i in range(37)])

# calculate how many possibilities for Pete to beat colin
summe = 0
for i in range(6,36):
    pete_probab = sum([pete_possib[j] for j in range(i+1,37)])/pete_total
    summe += colin_possib[i]/colin_total * pete_probab

print(summe)


