# defined my own factorial function


def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n - 1)


number = factorial(100)

summation = sum(map(int, str(number)))
print(summation)
