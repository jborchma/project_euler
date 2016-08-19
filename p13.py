from numpy import *

# each number is data[i]
data = loadtxt('p13.txt')

summe = 0
for i in range(len(data)):
    summe += data[i]

print(summe)
    
