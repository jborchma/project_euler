from numpy import zeros

# for p18 set number_of_lines to 15

number_of_lines = 100

triangle = zeros([number_of_lines, number_of_lines], int)


with open("p67.txt") as f:
    for i, line in enumerate(f):
        for j, number in enumerate(line.split()):
            triangle[i, j] = int(number)

for line in range(2, number_of_lines + 1):
    for i, element in enumerate(triangle[-line, :]):
        if element > 0:
            triangle[-line, i] = element + max(
                triangle[-line + 1, i], triangle[-line + 1, i + 1]
            )

print(triangle[0, 0])
