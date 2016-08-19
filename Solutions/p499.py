from numpy import *
from numpy import linalg as LA


dt = dtype(float64)

# this matrix relates the probability of ending with an amount smaller than 15 with starting amount s to the prob. to end there with starting amount s-1
def M(x):
    M = zeros([14,14], dtype=dt)
    M[range(1,14),range(0,13)] = 1
    M[:,13] = x[:]

    return M

# initialize x
b = zeros([14], dtype=dt)
b[0]=1/2
b[1]=1/4
b[3]=1/8
b[7]=1/16

# self consistent calculation for solve for x
x = b
for n in range(1000):
    x = b + sum((1/2)**k * dot(LA.matrix_power(M(x), 2**(k-1)-15), x) for k in range(5,200))

# calculate M^(10**9-15) by diagonalizing
D, P = LA.eig(M(x))
DN = diag(D**(10**9-15))
P1 = LA.inv(P)

#calculate the final x
result_vector = dot(dot(P,dot(DN,P1)),x)
#the result is the opposite of ending with anything less than 15
result = 1- sum(result_vector[:])
print(result)