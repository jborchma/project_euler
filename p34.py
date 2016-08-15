def fac(n):
    if n == 0:
        return 1
    prod = 1
    for i in range(1,n+1):
        prod *= i
    return prod

factorials = {i:fac(i) for i in range(0,10)}


all_nums = []
for i in range(10,2540161):
    number = str(i)
    summe = 0
    for digit in number:
        summe += factorials[int(digit)]
    if summe == i:
        all_nums.append(i)

print(sum(all_nums))


