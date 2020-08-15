from numpy import loadtxt, zeros

data = loadtxt("p82.txt", delimiter=",")
dimension = data.shape[0]
solution = zeros([dimension], int)

solution = data[:, dimension - 1]

for i in range(
    dimension - 2, -1, -1
):  # this will loop through the columns, starting on the right
    solution[0] += data[0, i]  # for the top row, I just add going to the right
    for j in range(
        1, dimension
    ):  # from the top, I go down, testing if it is better to go up or right
        solution[j] = min(solution[j - 1] + data[j, i], solution[j] + data[j, i])

    # now I know for each row, if it is better to go up or directly to the right
    for j in range(
        dimension - 2, -1, -1
    ):  # now I loop from the bottom and test if it is better to go down in place of the previous better solution
        solution[j] = min(solution[j], solution[j + 1] + data[j, i])


print(min(solution))
