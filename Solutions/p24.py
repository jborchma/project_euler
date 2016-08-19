import itertools

def memoize(f):
    cache = {}
    def wrapper(*args):
        if not args in cache:
            cache[args] = f(*args)

        return cache[args]
    return wrapper

def all_perms(num_list):
    if len(num_list) <= 1:
        yield num_list
    else:
        for perm in all_perms(num_list[1:]):
            for i in range(len(num_list)):
                yield perm[:i] + num_list[0:1] + perm[i:]


for i,perm in enumerate(itertools.permutations([0,1,2,3,4,5,6,7,8,9])):
    if i == 999999:
        print(perm)
        print(i)
        break
    