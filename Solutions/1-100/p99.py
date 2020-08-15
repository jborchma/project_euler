from numpy import *

# with open('p99.txt') as f:
#     for line in f:

data = loadtxt("p99.txt", delimiter=",")

maximum = 0
max_i = 0
for i in range(shape(data)[0]):
    temp = data[i, 1] * log(data[i, 0])
    if temp > maximum:
        maximum = temp
        max_i = i

print(maximum, max_i + 1)
