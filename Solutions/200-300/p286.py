from numpy import *
import time

start = time.time()

# define transition matrix
def transition_matrix(x,q):
    transition = zeros([51,51])
    transition[range(0,51),range(0,51)] = x/q
    transition[range(0,50),range(1,51)] = (1-x/q)

    return transition


# this function calculates the probability for score a certain number of times for some q
def hit_probability(q):
    #I can hit 0 - 50 times
    hit_probability = zeros([1,51])

    # initialize the array (0 throws, probability of 1 to score 0 times)
    hit_probability[0,0] = 1
    # now I loop through the throws
    for i in range(1,51):
        transition = transition_matrix(i,q)
        hit_probability = dot(hit_probability,transition)


    return hit_probability[0,20]

# now I do a simple binary search
high = 100
low = 50
while True:
    mid = (high + low)/2
    probab_temp = hit_probability(mid)

    if probab_temp < 0.02:
        high = mid
    else:
        low = mid
    if abs(probab_temp - 0.02) < 10**(-16):
        print('%.10f' % mid)
        break

print('The calculation took %ss.' % (time.time()-start))