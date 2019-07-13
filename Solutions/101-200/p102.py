"""Solution to problem 102

We can immediately rule out triangles where all points lie in the first or third quadrant. Same
for all the permutations of this. Then we can calculate the formula for the diagonal lines
and check if the offset is > or < 0.
"""


def load_file():
    """Loading the file
    """
    with open("p102_triangles.txt", "r") as file:
        text = file.read()
        triangles = [line.split(",") for line in text.split("\n")]
        for i, triangle in enumerate(triangles):
            triangles[i] = [
                (int(triangle[0]), int(triangle[1])),
                (int(triangle[2]), int(triangle[3])),
                (int(triangle[4]), int(triangle[5])),
            ]

    return triangles


def quadrant(point):
    """Determine the quadrant of a point
    """
    if point[0] > 0 and point[1] > 0:
        return 1
    elif point[0] > 0 and point[1] < 0:
        return 2
    elif point[0] < 0 and point[1] < 0:
        return 3
    elif point[0] < 0 and point[1] > 0:
        return 4
    elif point[0] == 0:
        return 5
    elif point[1] == 0:
        return 6


def calculate_y_offset(right_point, left_point):
    """Calculate the y offset
    """
    x_diff = right_point[0] - left_point[0]
    y_diff = right_point[1] - left_point[1]
    slope = y_diff / x_diff
    y_offset = right_point[1] - slope * right_point[0]

    return y_offset


def contains_origin(triangle):
    """Tests if the triangle contains the origin
    """
    quadrant_set = set(quadrant(point) for point in triangle)
    # all points in bottom half
    if all(quadrant(point) in [2, 3] for point in triangle):
        return False
    # all points in top half
    elif all(quadrant(point) in [1, 4] for point in triangle):
        return False
    # all points on right side
    elif all(quadrant(point) in [1, 2] for point in triangle):
        return False
    # all points on left side
    elif all(quadrant(point) in [3, 4] for point in triangle):
        return False
    # test diagonal
    elif quadrant_set == set([1, 2, 4]):
        for point in triangle:
            if quadrant(point) == 4:
                left_point = point
            if quadrant(point) == 2:
                right_point = point
        y_offset = calculate_y_offset(right_point, left_point)
        if y_offset > 0:
            return False
        else:
            return True
    elif quadrant_set == set([1, 2, 3]):
        for point in triangle:
            if quadrant(point) == 3:
                left_point = point
            if quadrant(point) == 1:
                right_point = point
        y_offset = calculate_y_offset(right_point, left_point)
        if y_offset >= 0:
            return True
        else:
            return False
    elif quadrant_set == set([2, 3, 4]):
        for point in triangle:
            if quadrant(point) == 4:
                left_point = point
            if quadrant(point) == 2:
                right_point = point
        y_offset = calculate_y_offset(right_point, left_point)
        if y_offset >= 0:
            return True
        else:
            return False
    elif quadrant_set == set([1, 3, 4]):
        for point in triangle:
            if quadrant(point) == 3:
                left_point = point
            if quadrant(point) == 1:
                right_point = point
        y_offset = calculate_y_offset(right_point, left_point)
        if y_offset > 0:
            return False
        else:
            return True
    # points in opposite quadrants
    elif quadrant_set == set([1, 3]):
        quadrant_three_count = 0
        quadrant_three_index = []
        quadrant_one_index = []
        for i, point in enumerate(triangle):
            if quadrant(point) == 3:
                quadrant_three_index.append(i)
                quadrant_three_count += 1
            else:
                quadrant_one_index.append(i)
        if quadrant_three_count == 1:
            left_point = triangle[quadrant_three_index[0]]
            right_point_1 = triangle[quadrant_one_index[0]]
            right_point_2 = triangle[quadrant_one_index[1]]
            y_offset_1 = calculate_y_offset(right_point_1, left_point)
            y_offset_2 = calculate_y_offset(right_point_2, left_point)
            if y_offset_1 * y_offset_2 < 0:
                return True
            else:
                return False
        else:
            right_point = triangle[quadrant_one_index[0]]
            left_point_1 = triangle[quadrant_three_index[0]]
            left_point_2 = triangle[quadrant_three_index[1]]
            y_offset_1 = calculate_y_offset(right_point, left_point_1)
            y_offset_2 = calculate_y_offset(right_point, left_point_2)
            if y_offset_1 * y_offset_2 < 0:
                return True
            else:
                return False
    # points in opposite quadrants
    elif quadrant_set == set([2, 4]):
        quadrant_two_count = 0
        quadrant_two_index = []
        quadrant_four_index = []
        for i, point in enumerate(triangle):
            if quadrant(point) == 2:
                quadrant_two_index.append(i)
                quadrant_two_count += 1
            else:
                quadrant_four_index.append(i)
        if quadrant_two_count == 2:
            left_point = triangle[quadrant_four_index[0]]
            right_point_1 = triangle[quadrant_two_index[0]]
            right_point_2 = triangle[quadrant_two_index[1]]
            y_offset_1 = calculate_y_offset(right_point_1, left_point)
            y_offset_2 = calculate_y_offset(right_point_2, left_point)
            if y_offset_1 * y_offset_2 < 0:
                return True
            else:
                return False
        else:
            right_point = triangle[quadrant_two_index[0]]
            left_point_1 = triangle[quadrant_four_index[0]]
            left_point_2 = triangle[quadrant_four_index[1]]
            y_offset_1 = calculate_y_offset(right_point, left_point_1)
            y_offset_2 = calculate_y_offset(right_point, left_point_2)
            if y_offset_1 * y_offset_2 < 0:
                return True
            else:
                return False
    # one point including 0
    else:
        return True


def main():
    """main function
    """
    list_of_triangles = load_file()
    print(sum([contains_origin(triangle) for triangle in list_of_triangles]))


if __name__ == "__main__":
    main()
