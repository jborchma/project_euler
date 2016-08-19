# again, find the sum of the divisors of a number

N = 28123
def find_divisor_sum(n):
    div_list = []
    for i in range(1,n//2+1):
        if n % i == 0:
            div_list.append(i)

    return sum(div_list)


#sum_dict = dict( ((n,find_divisor_sum(n))) for n in range(28123) )

abundant = [n for n in range(1,N+1) if find_divisor_sum(n) > n]
abundant_dict = dict.fromkeys(abundant, 1)

summe = 0
for i in range(1,N+1):
    abun_sum = False
    for abun in abundant:
        #print(abun)
        if abun > i:
            break
        if abundant_dict.get(i-abun):
            abun_sum = True
            break
    if not abun_sum:
        summe += i

print(summe)


