numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

for i in range(9000, 9999 + 1):
    num_str = str(i) + str(2 * i)
    if len(num_str) != 9:
        continue
    else:
        if all(str(digit) in num_str for digit in numbers):
            print(str(i) + str(2 * i))
