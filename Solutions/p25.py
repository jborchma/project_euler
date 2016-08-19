def memoize(f):
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)

        return cache[args]
    return wrapper

@memoize
def fibonacci(n):
    if n <= 2:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
n = 1
while True:
    length = len(str(fibonacci(n)))
    if length == 1000:
        print(n)
        break
    n += 1
