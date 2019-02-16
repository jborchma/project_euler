import time

start = time.time()

num_list = []
for n in range(1000000):
    num = str(n)
    if num == num[::-1]  and str(bin(n)[2:]) == str(bin(n)[2:])[::-1]:
        num_list.append(n)

print(sum(num_list))

print(time.time()-start)