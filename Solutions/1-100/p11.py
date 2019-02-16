from numpy import *

data = loadtxt('p11.txt')

largest_prod = 0
for i in range(0,20):
    for j in range(16):
        prod = data[i,j]*data[i,j+1]*data[i,j+2]*data[i,j+3]
        if prod > largest_prod:
            largest_prod = prod
        prod = data[j,i] * data[j+1,i] * data[j+2,i] * data[j+3,i]
        if prod > largest_prod:
            largest_prod = prod

for i in range(16):
    for j in range(16):
        prod = data[i,j]*data[i+1,j+1]*data[i+2,j+2]*data[i+3,j+3]
        if prod > largest_prod:
            largest_prod = prod

for i in range(3,20):
    for j in range(16):
        prod = data[i,j]*data[i-1,j+1]*data[i-2,j+2]*data[i-3,j+3]
        if prod > largest_prod:
            largest_prod = prod

print(largest_prod)