def fn(n):  # creates the quadratic functions used in the problem in the form of tuples
    return (
        (3, int(n * (n + 1) / 2)),
        (4, n * n),
        (5, int(n * (3 * n - 1) / 2)),
        (6, n * (2 * n - 1)),
        (7, int(n * (5 * n - 3) / 2)),
        (8, n * (3 * n - 2)),
    )


def next(
    types, data
):  # this function takes a first number and adds numbers to see if we can find a chain of length 6
    if (
        len(types) == 6 and data[0] // 100 == data[-1] % 100
    ):  # tests if the length of the chain is 6 and if it is periodic
        print(data, sum(data))
    else:  # if not yet length 6
        for t, n in ds.get(
            (types[-1], data[-1]), []
        ):  # take the last number from the list given to next() and get its partners from ds (loop through them)
            if t not in types:  # check if we don't already have that type
                next(types + [t], data + [n])  # append to input list and run again


p = []  # build a list of polygonal numbers with their type (type, pnum)
n = 19  # first n for octogonal number > 999

while n < 141:  # last n for triangle numbers < 10000
    for type, data in fn(
        n
    ):  # loop through functions and save tupels with value and function type
        if 1000 <= data <= 9999 and data % 100 > 9:  # find all the four digits numbers
            p.append((type, data))
    n += 1

ds = (
    {}
)  # build a dictionary of tuples that adds all the pairs into a list for each tupel
for t1, d1 in p:  # loop through all numbers with four digits
    for t2, d2 in p:  # loop through all numbers with four digits
        if (
            t1 != t2 and d1 % 100 == d2 // 100
        ):  # see if the connection condition is fulfilled and the numbers are not equal
            ds[t1, d1] = ds.get((t1, d1), []) + [
                (t2, d2)
            ]  # this gets the entry in ds of (t1,d1) and adds (t2,d2) to it. the get method returns an empty
            # list if (t1,d1) is not in ds

print("Project Euler 61 Solution Set")
for type, data in ds:  # start looping through all the keys in the dictionary
    next([type], [data])
