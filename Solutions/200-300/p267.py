from scipy.special import binom
from numpy import linspace
import math

threshold = 1000000000

def probab(f, threshold):
    threshold_value = 0

    if f == 1:
        return 1/2**1000
    else:

        for n in range(1,1001):
            final_amount = (1 + 2*f)**n * (1-f)**(1000-n)
            if final_amount > threshold:
                threshold_value = n
                break
        #print(threshold_value)
        possibilities = 0
        for n in range(threshold_value,1001):
            possibilities += binom(1000,n)

        #print(possibilities)
        probability = possibilities/2**1000
        return probability

maxi = 0
max_prob = 0
for f in linspace(0.1,0.5,3201):
    new_value = probab(f,threshold)
    if new_value > max_prob:
        max_prob = new_value
        maxi = f

print(max_prob, 'at f=',maxi)
