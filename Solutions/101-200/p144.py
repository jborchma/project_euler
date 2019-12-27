"""Solution to problem 144

1. Take the last two points and calculate d = p2 - p1
2. calculate the normal vector at p2 given by (4x/y, 1) * 1/sqrt(1+16x**2/y**2)
3. new vetor will be r = d - 2*(d*n)*n
4. calculate new point
"""
import math

def normalize_vector(vector):
    """Normalizes a vector

    Parameters
    ----------
    vector: tuple
        Tuple containing the vector components

    Returns
    -------
    tuple
        Normalized vector
    """
    norm = math.sqrt(sum([element**2 for element in vector]))
    return tuple(1/norm * element for element in vector)

def dot(v1, v2):
    return sum(element * v2[i] for i, element in enumerate(v1))


# b = (2 sqrt(-(p0^2 - 25) r1^2 + 2 p0 p1 r0 r1 - (p1^2 - 100) r0^2)
#     - 4 p0 r0 - p1 r1)/(4 r0^2 + r1^2) and 4 r0^2 + r1^2!=0

def calculate_next_point(p1, p2):
    """Based on the last two points, calculate the next one

    Parameters
    ----------
    p1: tuple
        Tuple containing the second to last point the light beam hit
    p2: tuple
        Tuple containing the last point the light beam hit

    Returns
    -------
    tuple:
        Second to last point the light beam hit (this is the last point from the input)
    tuple:
        New last point the light beam hit
    """
    d = (p2[0]-p1[0], p2[1] - p1[1])
    d = normalize_vector(d)
    n = normalize_vector((4*p2[0]/p2[1], 1))
    r = (d[0] - 2*dot(d, n) * n[0], d[1] - 2*dot(d, n) * n[1])

    # now that we have the reflected beam, we need to calculate the intersection
    root = math.sqrt(-(p2[0]**2 - 25)*r[1]**2 + 2*p2[0]*p2[1]*r[0]*r[1]- (p2[1]**2-100)*r[0]**2)
    num = 2 * root - 4*p2[0]*r[0] - p2[1]*r[1]
    denom = (4 * r[0]**2 + r[1]**2)
    factor = num / denom
    new_point = (p2[0] + factor * r[0], p2[1] + factor* r[1])

    return p2, new_point

def main():
    """main function
    """
    old_point = (0.0, 10.1)
    new_point = (1.4, -9.6)
    found = False
    n = 0
    while not found:
        n += 1
        if n % 1000 == 0:
            print(n)
        old_point, new_point = calculate_next_point(old_point, new_point)
        if abs(new_point[0]) <= 0.01 and new_point[1] > 0:
            found = True

    print("The answer is:", n)

if __name__ == "__main__":
    main()
