from numpy import ones, zeros, diag, dot, add
import scipy
from time import time
from decimal import Decimal, getcontext
getcontext().prec = 64

NumRow, NumCol = 30, 30
NumRing = 50
size = NumRow * NumCol

def state(i,j):
    return i * NumCol + j

t = time()

# transition matrix
Q = zeros((size,size),dtype='float64')

# set 4 corners
Q[state(0,0), state(0,1)], Q[state(0,0), state(1,0)] = Decimal(1)/Decimal(2), Decimal(1)/Decimal(2)
Q[state(0,NumCol-1), state(0,NumCol-2)], Q[state(0,NumCol-1), state(1,NumCol-1)] = Decimal(1)/Decimal(2), Decimal(1)/Decimal(2)
Q[state(NumRow-1,0), state(NumRow-2,0)], Q[state(NumRow-1,0), state(NumRow-1,1)] = Decimal(1)/Decimal(2), Decimal(1)/Decimal(2)
Q[state(NumRow-1,NumCol-1), state(NumRow-2,NumCol-1)], Q[state(NumRow-1,NumCol-1), state(NumRow-1,NumCol-2)] = Decimal(1)/Decimal(2), Decimal(1)/Decimal(2)

# set 4 borders
for j in range(1, NumCol-1):
    Q[state(0,j), state(0,j-1)], Q[state(0,j), state(0,j+1)], Q[state(0,j), state(1,j)] = Decimal(1)/Decimal(3), Decimal(1)/Decimal(3), Decimal(1)/Decimal(3)
    Q[state(NumRow-1,j), state(NumRow-1,j-1)], Q[state(NumRow-1,j), state(NumRow-1,j+1)], Q[state(NumRow-1,j), state(NumRow-2,j)] = Decimal(1)/Decimal(3), Decimal(1)/Decimal(3), Decimal(1)/Decimal(3)

for i in range(1, NumRow-1):
    Q[state(i,0), state(i-1,0)], Q[state(i,0), state(i,1)], Q[state(i,0), state(i+1,0)] = Decimal(1)/Decimal(3), Decimal(1)/Decimal(3), Decimal(1)/Decimal(3)
    Q[state(i,NumCol-1), state(i-1,NumCol-1)], Q[state(i,NumCol-1), state(i,NumCol-2)], Q[state(i,NumCol-1), state(i+1,NumCol-1)] = Decimal(1)/Decimal(3), Decimal(1)/Decimal(3), Decimal(1)/Decimal(3)

# set middle part
for j in range(1,NumCol-1):
    for i in range(1,NumRow-1):
        Q[state(i,j), state(i-1,j)], Q[state(i,j), state(i,j+1)], Q[state(i,j), state(i+1,j)], Q[state(i,j), state(i,j-1)] = Decimal(1)/Decimal(4), Decimal(1)/Decimal(4), Decimal(1)/Decimal(4), Decimal(1)/Decimal(4)

# time for transition matrix initialization
print('Time to initiate transition matrix: ' + str(time()-t))
t = time()

result = ones((1,size),dtype='float64')

# for each flea on square i, calculate probability of emptiness for each square
for i in range(0,size):
    #initialize on field i at bell 0
    P = zeros((1,size),dtype='float64')
    P[0,i] = 1.0

    #probability for flee i to be anywhere after the first bell
    tmp = zeros((1,size),dtype='float64')
    tmp = dot(P, Q)

    # evolve probability for further bells
    for x in range(1, NumRing):
        tmp = dot(tmp,Q)

    # probability to not be on a field
    tmp = 1 - tmp

    #combine emptiness probability across all fleas for each square (the star operator multiplies each entry by entry
    result = result * tmp

# time for Markov matrix multiplication for NumRing steps
print('Time to calculate Markov status for all fleas: ' + str(time()-t))

# final probability of emptiness for each square
result = result.reshape(NumRow,NumCol)

print('Expected # of empty cells is: ' + str(scipy.sum(result)))




