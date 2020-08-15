# straight forward checking for pandigitals

numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]

number_dict = {}

for i in range(1, 2000):
    for j in range(i, 2000):
        number_string = str(i) + str(j) + str(i * j)
        if len(number_string) == 9:
            if "0" in number_string:
                continue
            if all(number in number_string for number in numbers):
                print(i, j, i * j)
                if not i * j in number_dict:
                    number_dict[i * j] = 1

print(sum([key for key in number_dict.keys()]))
