numbers = []
for i in range (2,101):
    for j in range(2,101):
        numbers.append(i**j)

print(len(set(numbers)))