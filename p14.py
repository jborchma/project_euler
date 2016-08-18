import time

start = time.time()

def memoize(f):
    # this decorator function creates a cache for all n that I input into collatz_chain
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)
        #print(cache)
        return cache[args]
    return wrapper

# define the function
@memoize
def collatz_chain(n):
    if n == 1:
        return 1
    elif n % 2 == 0:
        return 1 + collatz_chain(n/2)
    else:
        return 1 + collatz_chain(3*n+1)

target = 1000000


# print the maximum
print(max(range(1, target+1), key=collatz_chain))

print('The calculation took %s s.' % (time.time()-start))