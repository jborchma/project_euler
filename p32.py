def memoize(f):
    cache = {}
    def wrapper(*args):
        cache[args] = f(*args)

        return cache[args]
    return wrapper

numbers = [1,2,3,4,5,6,7,8,9]


