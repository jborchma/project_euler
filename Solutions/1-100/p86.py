"""Solution to problem 86

We can pick a x_0 on the side of the cube and denote
f(x_0) = sqrt(x_0^2 + y^2) + sqrt(z^2 + (x-x_0)^2)
f'(x_0)=0 -> x_0 = xy/(y+/-z)

For the example, the solution is with the + sign.

f(x_0) = (y+z) * sqrt(1+ x^2 / (y + z)^2)

x >= y >= z: sqrt(x^2 + (y+z)^2)

"""
import math
from numba import jit


#@jit
def main():
    for M in range(1000, 4000):
        counter = 0
        for z in range(1, M+1):
            for y in range(z, M+1):
                for x in range(y, M+1):
                    res = math.sqrt(x**2 + (y + z)**2)
                    if res % 1 == 0:
                        counter += 1

        print(counter)
        if counter > 1000000:
            print("Answer:", counter, M)

main()
