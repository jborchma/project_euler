import itertools as it
from numpy import *

# tactics, run through integers starting from 100 and cube them.
n = 100
searching = True
cubic_numbers = {}
min_cube = 1e38

while searching:
    cube = n * n * n  # cube current number
    digits = "".join(sorted(str(cube)))  # sort digits of the cube
    if digits in cubic_numbers:
        cubic_numbers[digits] += [cube]
        if len(cubic_numbers[digits]) == 5:
            min_cube = min(min_cube, cubic_numbers[digits][0])
            if len(digits) > len(str(min_cube)):
                searching = False
    else:
        cubic_numbers[digits] = [cube]
    n += 1

print(min_cube)
