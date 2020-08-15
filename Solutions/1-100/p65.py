from fractions import Fraction

e_list = []

for k in range(1, 35):
    e_list.append(1)
    e_list.append(2 * k)
    e_list.append(1)

frac = 0
for i in range(98, -1, -1):
    frac = Fraction(1, (e_list[i] + frac))
result = Fraction(2) + frac

print(sum([int(digit) for digit in str(result.numerator)]))
