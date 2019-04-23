"""Solution to problem 86

We can pick a x_0 on the side of the cube and denote
f(x_0) = sqrt(x_0^2 + y^2) + sqrt(z^2 + (x-x_0)^2)
f'(x_0)=0 -> x_0 = xy/(y+/-z)

For the example, the solution is with the + sign.

f(x_0) = (y+z) * sqrt(1+ x^2 / (y + z)^2) = sqrt((y+z)^2 + x^2)

This shows that we need to find a Pythagorean triple. We did this already in problem 75 and I think
we should be able to use that solution with slight modifications.


"""
import numpy as np

# gotten from stack overflow: my solution from problem 75 was too slow
def gen_prim_pyth_trips(limit=None):
    """Generates all primitive Pythagorean triples up to limit
    """
    u = np.mat(" 1  2  2; -2 -1 -2; 2 2 3")
    a = np.mat(" 1  2  2;  2  1  2; 2 2 3")
    d = np.mat("-1 -2 -2;  2  1  2; 2 2 3")
    uad = np.array([u, a, d])
    m = np.array([3, 4, 5])
    while m.size:
        m = m.reshape(-1, 3)
        if limit:
            m = m[m[:, 2] <= limit]
        yield from m
        m = np.dot(m, uad)


def gen_all_pyth_trips(limit):
    """Generates all Pythagorean triples up to limit
    """
    for prim in gen_prim_pyth_trips(limit):
        i = prim
        for _ in range(limit // prim[2]):
            yield i
            i = i + prim


def find_possible_side_lengths(a, b, c, limit):
    """Based on a Pythagorean triple, find all side lengths
    """
    counter = 0
    z = b
    for x in range(1, a):
        y = a - x
        if y < x:
            break  # no double counting
        if c ** 2 == min(
            ((x + y) ** 2 + z ** 2, (z + y) ** 2 + x ** 2, (x + z) ** 2 + y ** 2)
        ):
            if max(x, y, z) <= limit:
                counter += 1

    return counter


def binarySearch(low, high, value, triplet_list):
    """Use binary search, since the function takes quite some time to evaluate
    """
    if high >= low:

        # mid = (low + high)/2
        mid = low + (high - low) // 2
        print(mid)

        # If f(mid) is greater than 0
        # and one of the following two
        # conditions is true:
        # a) mid is equal to low
        # b) f(mid-1) is negative
        if path_count(mid, triplet_list) > value and (
            mid == low or path_count(mid - 1, triplet_list) <= value
        ):
            return mid

        # If f(mid) is smaller than or equal to 0
        if path_count(mid, triplet_list) <= value:
            return binarySearch((mid + 1), high, value, triplet_list)
        else:  # f(mid) > 0
            return binarySearch(low, (mid - 1), value, triplet_list)

    # Return -1 if there is no positive
    # value in given range
    return -1


def path_count(M, list_of_triplets):
    """Count the number of integer paths
    """
    possible_triplets = [
        triplet
        for triplet in list_of_triplets
        if (triplet[1] <= 2 * M and triplet[0] <= M)
        or (triplet[0] <= 2 * M and triplet[1] <= M)
    ]

    # now find all possible combinations
    counter = 0
    for a, b, c in possible_triplets:
        counter += find_possible_side_lengths(a, b, c, M)
        counter += find_possible_side_lengths(b, a, c, M)

    return counter


def main():
    """main function
    """
    list_of_triplets = list(gen_all_pyth_trips(10000))

    print("created all triplets")
    result = binarySearch(1500, 2000, 1000000, list_of_triplets)

    print("Answer:", result)


main()
