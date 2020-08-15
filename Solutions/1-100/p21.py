# find divisors and sum them
def find_div_sum(n):
    div_list = []

    for i in range(1, n // 2 + 1):
        if n % i == 0:
            div_list.append(i)

    return sum(div_list)


# make a dictionary of a number and its divisor sum
tupel_list = dict(((n, find_div_sum(n))) for n in range(2, 10000))

# sum elements that have divisor sums that equal the element
summe = sum(
    n
    for n in range(2, 10000)
    if tupel_list.get(tupel_list[n]) == n and tupel_list[n] != n
)

print(summe)
