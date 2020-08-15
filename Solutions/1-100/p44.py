# I will just generate a list of pentagon numbers and search through them


def pentagon_number(n):
    return n * (3 * n - 1) / 2


pentagon_numbs = []
for i in range(1, 2500):
    pentagon_numbs.append(pentagon_number(i))

print("Start searching....")

for index, i in enumerate(pentagon_numbs):
    for j in pentagon_numbs[index + 1 :]:
        if i + j in pentagon_numbs and abs(i - j) in pentagon_numbs:

            D = abs(i - j)
            print(D)
            print(i)
            print(j)

print(D)
