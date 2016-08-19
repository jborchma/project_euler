# I will solve this with dynamic programming. 
# Starting from the bottom right I will iteratively move to the left and top
from numpy import *

N = 20
grid = zeros([N+1,N+1])

# initialize boundaries
for i in range(N):
    grid[i,N] = 1
    grid[N,i] = 1

for i in range(N-1,-1,-1):
    for j in range(N-1,-1,-1):
        grid[i,j] = grid[i+1,j] + grid[i,j+1]

print(grid[0,0])

