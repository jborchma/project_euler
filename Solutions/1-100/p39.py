# number_dict = {}
# for p in range(1,1001):
#     number_dict[p]=0
#     for a in range(1,int(p/2)):
#         for b in range(1,int(p/2)):
#             c = p - a - b
#             if abs(a**2 + b**2 - c**2) < 0.00001:
#                 number_dict[p]+=1


# way faster
number_dict = {}
for p in range(1, 1001):
    number_dict[p] = 0
    for a in range(1, int(p / 2)):
        b = p * (2 * a - p) / (2 * a - 2 * p)
        if b % 1 == 0 and a < b:
            number_dict[p] += 1


print(max(number_dict, key=number_dict.get))
