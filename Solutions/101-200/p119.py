"""Solution to problem 119

The trick is to not loop through all numbers and check if their sums to some power
match the number. Rather, we can loop through the sums of digits, square them, cube them, etc.
and if the sum of digits of such a power matches the original sum of digits, we have found a number
of the sequence.

Also, the searched sequence is A023106 on https://oeis.org/A023106.
"""


def main():
    """main function
    """
    max_digits = 20  # Finds all terms with <= 20 digits
    maximum_value = 10 ** max_digits
    found_sequence_members = []
    for sum_of_digits in range(2, 9 * max_digits):
        candidate_number = sum_of_digits
        while candidate_number < maximum_value:
            # if sum of digits of the number is equal to the original sum of digits
            if sum(int(i) for i in str(candidate_number)) == sum_of_digits:
                if candidate_number > 10:
                    found_sequence_members.append(candidate_number)
            # increase power by 1
            candidate_number *= sum_of_digits

    found_sequence_members.sort()
    print(found_sequence_members[29])


if __name__ == "__main__":
    main()
