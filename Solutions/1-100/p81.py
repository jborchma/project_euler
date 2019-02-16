from numpy import loadtxt

data = loadtxt('p81.txt',delimiter=',')

dimension = data.shape[0]

# this calculates the bottom row and the right column, where we add the previous cells
for i in range(dimension-1,0,-1):
    data[dimension-1,i-1] += data[dimension-1,i]
    data[i-1,dimension-1] += data[i,dimension-1]


# after having initialized the last row and column, I now go though the matrix from data[-2:-2] and always add the minimum of either the cell below or to the right
for i in range(dimension-2,-1,-1):
    for j in range(dimension-2,-1,-1):
        data[i,j] += min(data[i+1,j],data[i,j+1])

print(data[0,0])



