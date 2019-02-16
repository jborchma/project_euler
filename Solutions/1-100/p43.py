import itertools

list_of_divisors = [2,3,5,7,11,13,17]

list_of_digits = ['0','1','2','3','4','5','6','7','8','9']

# generate all permutations
perms = list(itertools.permutations(list_of_digits))

summe = 0
for perm in perms:
    # exclude the permutations starting with 0
    if perm[0] != '0':
        number = ''.join(perm)
        # check the conditions
        if all(int(number[i+1:i+4]) % list_of_divisors[i] == 0 for i in range(len(list_of_divisors)) ):
            summe += int(number)

print(summe)

