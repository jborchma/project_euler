from numpy import *
number = 0
for i in range(1,10):
    number_of_possible_n = int(log(10)/(log(10)-log(i)))
    number += number_of_possible_n

print(number)