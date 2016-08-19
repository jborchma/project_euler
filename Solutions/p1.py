# simple brute force solution

add_list = [i for i in range(1000) if (i%3==0 or i % 5 == 0)]

print(sum(add_list))