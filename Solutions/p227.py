from numpy import *
from numpy.linalg import solve

# I classify the probabilities by the distance between players with dice. d=1 are adjacent players, d=0 ends the game

def create_probability_table(max_dist):
    probab_table = zeros([max_dist+1,max_dist+1])
    probab_table[0,0]=0 # as the game is over, there are no probabilities, found this via trial and error....

    # special case with distance 1
    probab_table[1,0] = 2/9
    probab_table[1,1] = 19/36
    probab_table[1,2] = 2/9
    probab_table[1,3] = 1/36

    for d in range(2,max_dist-1):
        probab_table[d,d-2] = 1/36
        probab_table[d,d+2] = 1/36
        probab_table[d,d-1] = 2/9
        probab_table[d,d+1] = 2/9
        probab_table[d,d] = 1/2

    # special cases with periodic boundary
    probab_table[max_dist-1,max_dist-1] = 1/2+1/36
    probab_table[max_dist-1,max_dist] = 2/9
    probab_table[max_dist-1,max_dist-2] = 2/9
    probab_table[max_dist-1,max_dist-3] = 1/36

    probab_table[max_dist,max_dist] = 1/2
    probab_table[max_dist,max_dist-1] = 4/9
    probab_table[max_dist,max_dist-2]= 1/18

    return probab_table

max_dist = 50

# Now I need to solve the linear equation (A-1)*x + b = 0, where A is the probability matrix, b is [0,-1,-,1,...,-1], where the constant vector
# comes from the fact that I will take one roll of the two dice, and then I will have the new situation with probabilities

x = solve(create_probability_table(max_dist)-eye(max_dist+1),[0]+[-1 for i in range(max_dist)])
print(x)
print(allclose(dot(create_probability_table(max_dist)-eye(max_dist+1), x), [0]+[-1 for i in range(max_dist)]))
