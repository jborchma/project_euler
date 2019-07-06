"""Solution to problem 165
"""
from fractions import Fraction


def generate_blum_blum_shub(s_previous):
    """Generates pseudo random integers

    Generally, this series starts with s_0 = 290797

    Parameters
    ----------
    s_previous: int
        Previous generated s_{n-1}

    Returns
    -------
    int
        Pseudo random integer. Generally t_n = s_n % 500 is used
    """
    s_n = (s_previous ** 2) % 50515093

    return s_n


def generate_segments(n_segments):
    """Generate n_segments segments based on pseudo random numbers

    Parameters
    ----------
    n_segments: int
        Number of segments that will be generated

    Returns
    -------
    list
        List of lists containing the generated segments. They are output not like in the problem
        statement but in the form [(base point), (direction vector)]
    """
    s_0 = 290797
    s_current = s_0
    list_of_segments = []
    # for _ in range(3):
    #     s_current = generate_blum_blum_shub(s_current)
    #     list_of_segments[0].append(s_current % 500)
    for _ in range(n_segments):
        new_segment_temp = []
        for _ in range(4):
            s_current = generate_blum_blum_shub(s_current)
            new_segment_temp.append(s_current % 500)

        new_segment = new_segment_temp[:2] + [
            new_segment_temp[2] - new_segment_temp[0],
            new_segment_temp[3] - new_segment_temp[1],
        ]
        list_of_segments.append(new_segment)

    return list_of_segments


def test_intersection(segment_1, segment_2):
    """Function to test if segment 1 and 2 intersect
    """
    a_1 = segment_1[0]
    a_2 = segment_1[1]
    b_1 = segment_1[2]
    b_2 = segment_1[3]
    c_1 = segment_2[0]
    c_2 = segment_2[1]
    d_1 = segment_2[2]
    d_2 = segment_2[3]
    try:
        epsilon = 10e-7
        if d_1 * b_2 - d_2 * b_1 == 0:
            return None

        if d_1 == 0 and b_1 != 0 and d_2 != 0:
            x_1 = Fraction((c_1 - a_1), b_1)
            x_2 = Fraction(
                (-a_1 * b_2 + a_2 * b_1 - b_1 * c_2 + b_2 * c_1), (b_1 * d_2)
            )

        elif d_1 == 0 and b_1 == 0 and a_1 == c_1 and d_2 != 0 and b_2 != 0:
            return None

        elif d_2 == 0 and b_2 == 0 and a_2 == c_2 and d_1 != 0:
            return None

        elif d_1 != 0:
            x_1 = Fraction(
                (d_2 * (a_1 - c_1) - a_2 * d_1 + c_2 * d_1), (b_2 * d_1 - b_1 * d_2)
            )
            x_2 = Fraction(
                (-a_1 * b_2 + a_2 * b_1 - b_1 * c_2 + b_2 * c_1),
                (b_1 * d_2 - b_2 * d_1),
            )
        else:
            return None

        if epsilon < x_1 < 1 - epsilon and epsilon < x_2 < 1 - epsilon:
            return (a_1 + x_1 * b_1, a_2 + x_1 * b_2)

        return None

    except ZeroDivisionError:
        return None


def main():
    """main function
    """
    segments = generate_segments(5000)
    intersections = []
    for i, segment_1 in enumerate(segments):
        for segment_2 in segments[i + 1 :]:
            point = test_intersection(segment_1, segment_2)
            if point is not None:
                intersections.append(point)

    n_intersections = len(set(intersections))

    print(f"Answer: {n_intersections}.")


if __name__ == "__main__":
    main()
