largest = 0
for a in range(1,100):
    for b in range(1,100):
        numb = sum([int(i) for i in str(a**b)])
        if numb > largest:
            largest = numb

print(largest)