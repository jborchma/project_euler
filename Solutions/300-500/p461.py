# use a genetic algorithm
from random import randint, random
import math
import time
from numpy import *
import bisect

start = time.time()

n = 10000
n_max = int(ceil(n *log(pi + 1)))
f_values = [exp(i/n) - 1 for i in range(0,n_max+1)]


def f(n,k):
    return exp(k/n) - 1

def binary_search(a,b,c):
    n = 10000
    low = 1
    high = 14400
    rest = f(n,a) + f(n,b) + f(n,c) - pi
    if rest > 0:
        return 0
    else:
        while high - low > 1:
            mid = int((high + low)/2)
            diff = f(n,mid) + rest 
            if diff > 0:
                high = mid
            else:
                low = mid

        if abs(f(n,low)+rest) < abs(f(n,high)+rest):
            return low
        else:
            return high

def sorted_values(n_max):


    added_values = zeros(int((n_max+2)*(n_max+1)/2))

    index = 0
    for i in range(n_max+1):
        for j in range(i,n_max+1):
            added_values[index] = f_values[i] + f_values[j]
            index += 1

    sorted_values = sort(added_values)

    return sorted_values

def binary_array_search(sorted_values):

    low = 0
    high = shape(sorted_values)[0]-1
    global_best = 1000
    partial_best_values = [] 

    while low <= high:
        temp_best = 1000
        diff = abs(sorted_values[low] + sorted_values[high] - pi)
        while diff < temp_best:
            temp_best = diff
            low += 1
            diff = abs(sorted_values[low] + sorted_values[high] - pi)
        if temp_best < global_best:
            global_best = temp_best
            partial_best_values = [sorted_values[low-1], sorted_values[high]]
        high -= 1
        low -= 1

    k = []
    # find the four values for the best approximation of pi
    for i in range(0, n_max+1):
        for j in range(i, n_max+1):
            T = f_values[i] + f_values[j]
            if T == partial_best_values[0] or T == partial_best_values[1]:
                k.extend([i, j])

    print(k, global_best)
    print('g = ', sum([i**2 for i in k]))



sorted_values = sorted_values(n_max)
max_ind = bisect.bisect_left(sorted_values, pi) #gives me the first index that has a larger value than pi
sorted_values = sorted_values[:max_ind]
binary_array_search(sorted_values)


print(time.time() - start)



