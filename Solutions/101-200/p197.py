from numpy import *
import matplotlib.pyplot as plt

def memoize(func):
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

def f(x):
    return int(2 ** (30.403243784 - x**2)) * 10**(-9)

@memoize
def seq(n):
    if n == 0:
        return -1
    else:
        return f(seq(n-1))

values = [seq(i) for i in range(0,1001)]

epsilon = 10**(-10)

flag = True
n=100
diff = abs(seq(98)-seq(96))
while flag:
    diff_temp = abs(seq(n) - seq(n-2))
    if diff_temp > epsilon:
        diff = diff_temp
        n+=2
    else:
        summe = seq(n) + seq(n+1)
        print(n)
        print('%.9f' % summe)
        print(seq(1000)+seq(1001))
        flag = False
