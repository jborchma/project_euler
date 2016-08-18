from numpy import *

#solve exactly like problem 286 with Markov chains
# define the transition matrix
def transition_matrix(i):
    transition = zeros([16,16])
    transition[range(0,16),range(0,16)] = i/(1+i)
    transition[range(0,15),range(1,16)] = 1/(1+i)

    return transition

probabilities = zeros([1,16])
probabilities[0,0] = 1

for j in range(1,16):
    transition = transition_matrix(j)
    probabilities = dot(probabilities,transition)


win_probabiltiy = 1 - sum(probabilities[0,:8])

expectation = -10000000
n = 1000
while True:

    expecation_temp = win_probabiltiy * n - (1 - win_probabiltiy)
    if expecation_temp > 0:
        print(expecation_temp)
        print(n)
        break
    else:
        n +=1
