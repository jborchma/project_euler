written_numbers = {}

written_numbers[1] = "one"
written_numbers[2] = "two"
written_numbers[3] = "three"
written_numbers[4] = "four"
written_numbers[5] = "five"
written_numbers[6] = "six"
written_numbers[7] = "seven"
written_numbers[8] = "eight"
written_numbers[9] = "nine"
written_numbers[10] = "ten"
written_numbers[11] = "eleven"
written_numbers[12] = "twelve"
written_numbers[13] = "thirteen"
written_numbers[14] = "fourteen"
written_numbers[15] = "fifteen"
written_numbers[16] = "sixteen"
written_numbers[17] = "seventeen"
written_numbers[18] = "eighteen"
written_numbers[19] = "nineteen"
written_numbers[20] = "twenty"
written_numbers[30] = "thirty"
written_numbers[40] = "forty"
written_numbers[50] = "fifty"
written_numbers[60] = "sixty"
written_numbers[70] = "seventy"
written_numbers[80] = "eighty"
written_numbers[90] = "ninety"
written_numbers[100] = "hundred"
written_numbers[1000] = "onethousand"

summe = 0
for i in range(1, 1000):
    if i <= 20:
        summe += len(written_numbers[i])
    elif i > 20 and i < 100 and i % 10 != 0:
        summe += len(written_numbers[int(i / 10) * 10]) + len(
            written_numbers[i - int(i / 10) * 10]
        )
    elif i > 20 and i < 100 and i % 10 == 0:
        summe += len(written_numbers[i])
    elif i >= 100:
        summe += len(written_numbers[int(i / 100)] + written_numbers[100])
        j = i - int(i / 100) * 100
        if j > 0:
            summe += 3
            if j <= 20:
                summe += len(written_numbers[j])
            elif j > 20 and j < 100 and j % 10 != 0:
                summe += len(written_numbers[int(j / 10) * 10]) + len(
                    written_numbers[j - int(j / 10) * 10]
                )
            elif j > 20 and j < 100 and j % 10 == 0:
                summe += len(written_numbers[j])

summe += len(written_numbers[1000])


print(summe)
