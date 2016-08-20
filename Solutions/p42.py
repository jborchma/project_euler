from numpy import *

with open('p42.txt') as f:
    for line in f:
        words = line.split('","')

# handle the first and last element
words[0] = words[0].replace('"','')
words[-1] = words[-1].replace('"','')

tranlation_dict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F': 6, 'G': 7, 'H': 8, 'I':9, 'J':10, 'K': 11, 'L': 12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 'R': 18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

# calculate value of a word
def number_value(word):
    value = 0
    for letter in word:
        value += tranlation_dict[letter]

    return value

max_value = number_value(max((word for word in words), key=number_value))

triangle_numbers = [int(1/2*n*(n+1)) for n in range(1,int(max_value/6) ) ]
print(triangle_numbers)

count = 0
for word in words:
    if number_value(word) in triangle_numbers:
        count +=1

print(count)

