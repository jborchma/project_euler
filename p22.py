import string

with open('p22.txt') as f:
    for line in f:
        names = line.split('","')

names[0] = names[0].replace('"','')
names[-1] = names[-1].replace('"','')

names.sort()

tranlation_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F': 6, 'G': 7, 'H': 8, 'I':9, 'J':10, 'K': 11, 'L': 12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R': 18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

full_sum = 0
for i,name in enumerate(names):
    full_sum += (i+1) * sum([tranlation_dict[letter] for letter in name])


print(full_sum)