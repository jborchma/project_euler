from numpy import *
from fractions import Fraction

prod = 1

for i in range(10, 100):
    for j in range(i + 1, 100):
        frac = Fraction(i, j)
        equals = [int(num) for num in str(i) if num in str(j)]
        if len(equals) == 1:
            if str(i)[0] != str(i)[1] and str(j)[0] != str(j)[1]:
                if int(str(j).replace(str(equals[0]), "")) != 0:
                    new_frac = Fraction(
                        int(str(i).replace(str(equals[0]), "")),
                        int(str(j).replace(str(equals[0]), "")),
                    )
                    if new_frac == frac:
                        if i % 10 != 0:
                            prod *= new_frac
                            print(i, j, new_frac)
            elif str(i)[0] == str(i)[1] and str(j)[0] != str(j)[1]:
                if int(str(j).replace(str(equals[0]), "")) != 0:
                    new_frac = Fraction(
                        int(str(i)[:1]), int(str(j).replace(str(equals[0]), ""))
                    )
                    if new_frac == frac:
                        if i % 10 != 0:
                            prod *= new_frac
                            print(i, j, new_frac)
            elif str(i)[0] != str(i)[1] and str(j)[0] == str(j)[1]:
                if int(str(j)[:1]) != 0:
                    new_frac = Fraction(
                        int(str(i).replace(str(equals[0]), "")), int(str(j)[:1])
                    )
                    if new_frac == frac:
                        if i % 10 != 0:
                            prod *= new_frac
                            print(i, j, new_frac)
            else:
                if int(str(j)[:1]) != 0:
                    new_frac = Fraction(int(str(i)[:1]), int(str(j)[:1]))
                    if new_frac == frac:
                        if i % 10 != 0:
                            prod *= new_frac
                            print(i, j, new_frac)

print(prod)
