import numpy as np
from collections import Counter

data = np.loadtxt('p59.txt',dtype=int,  delimiter=',') #import as integers

#since the key is only three letters, we need to split the data into three lists
one = []
two = []
three = []

for i, digit in enumerate(data):
    if i % 3 ==0:
        one.append(digit)
    elif i % 3 ==1:
        two.append(digit)
    else:
        three.append(digit)

#now there are 26 possible keys for each of the three lists
decrypt_one = []
decrypt_two = []
decrypt_three = []

numb_list = [one, two, three]
decrypt_list = [decrypt_one, decrypt_two, decrypt_three]

key = []
# we are going to use frequency analysis to find the right key. here I am only testing for the space and e to be in 
# the most common symbols and that's already enough
for i in range(3):
    for num in range(97,123):
        for digit in numb_list[i]:
            decrypt_list[i].append(digit^num)

        counts = Counter(decrypt_list[i])
        ranks = counts.most_common(3)
        ranks = [ranks[0][0], ranks[1][0], ranks[2][0]]
        if 32 in ranks and 101 in ranks:
            key.append(num)
            print(i,num)
            break
        del decrypt_list[i][:]

# sum all the decoded sympols
summe = 0
for i in range(3):
    summe += sum(decrypt_list[i])
print(summe)



