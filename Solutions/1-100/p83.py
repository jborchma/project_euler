from numpy import loadtxt, zeros, asarray, ones
from operator import itemgetter


def min_dict(d, reverse=False):
    """ proposed in PEP 265, using  the itemgetter """
    return sorted(d, key=itemgetter(1), reverse=False)[0]


data = loadtxt("p83.txt", delimiter=",")
dimension = data.shape[0]

minimum = data.min()
G_score = zeros([dimension, dimension], int)
g = ones([dimension, dimension], int)
g = 100000000 * g
searched = zeros([dimension, dimension], int)
for i in range(dimension):
    for j in range(dimension):
        G_score[i, j] = minimum * (2 * (dimension - 1) - i - j)

open_list = {}
closed_list = {}

moves = [(1, 0), (0, 1), (-1, 0), (0, -1)]

# initialize open_list
open_list[(0, 0)] = data[0, 0] + G_score[0, 0]
g[0, 0] = data[0, 0]
searched[0, 0] = 1


status = True
while status:
    current = min_dict(open_list)  # this is our current square
    closed_list[
        current
    ] = (
        1
    )  # Look for the lowest F cost square on the open list and put it in closed_list
    searched[current[0], current[1]] = 2
    del open_list[current]

    for move in moves:
        neighbour = tuple(map(lambda x, y: x + y, current, move))
        if (
            neighbour[0] in range(0, dimension)
            and neighbour[1] in range(0, dimension)
            and not neighbour in closed_list
        ):  # tests that I'm still in the array
            if searched[neighbour[0], neighbour[1]] < 2:
                if (
                    g[neighbour[0], neighbour[1]]
                    > g[current[0], current[1]] + grid[neighbour[0], neighbour[1]]
                ):
                    g[neighbour[0], neighbour[1]] = (
                        g[current[0], current[1]] + grid[neighbour[0], neighbour[1]]
                    )

                open_list[neighbour] = (
                    data[neighbour[0], neighbour[1]]
                    + G_score[neighbour[0], neighbour[1]]
                )
