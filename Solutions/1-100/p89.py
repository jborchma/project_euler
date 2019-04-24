"""Solution to problem 89

This problem is decently straight forward. We need to check the ones, tens and hundreds and reduce.
Then we need to check all the "nines" and reduce.
"""

def clean_numeral(numeral):
    """This function cleans a roman numeral and makes it optimal
    """
    saved = 0
    corresponding_five = ["V", "L", "D"]
    for i, symbol in enumerate(["I", "X", "C"]):
        if symbol * 9 in numeral:
            saved += 7
        elif symbol * 8 in numeral:
            saved += 4
        elif symbol * 7 in numeral:
            saved += 4
        elif symbol * 6 in numeral:
            saved += 4
        elif symbol * 5 in numeral:
            saved += 4
        elif symbol * 4 in numeral and corresponding_five[i] not in numeral:
            saved += 2

    for combination in ["VIIII", "LXXXX", "DCCCC"]:
        if combination in numeral:
            saved += 3

    return saved

def main():
    """main function
    """
    total_saved = 0
    with open('p089_roman.txt', 'r') as file:
        for line in file:
            total_saved += clean_numeral(line.strip())

    print("Answer:", total_saved)

if __name__ == "__main__":
    main()
