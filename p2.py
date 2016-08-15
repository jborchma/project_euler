fibon_list = [1,1]

small = True
while small:
    new_element = fibon_list[-1] + fibon_list[-2]
    fibon_list.append(new_element)
    if new_element > 4000000:
        small = False

fibon_even = []
for number in fibon_list:
    if number % 2 == 0:
        fibon_even.append(number)

print(sum(fibon_even))
