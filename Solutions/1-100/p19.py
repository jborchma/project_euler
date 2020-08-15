# define leap year function
def leap_year(n):
    if n % 4 == 0 and n % 400 == 0:
        return True
    elif n % 4 == 0 and n % 100 == 0:
        return False
    elif n % 4 == 0:
        return True
    else:
        return False


normal_year_months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
leap_year_months = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

number_of_sundays = 0

day = 1
for n in range(1901, 2001):
    if leap_year(n):
        for month in leap_year_months:
            day = (day + month) % 7
            if day == 6:
                number_of_sundays += 1

    else:
        for month in normal_year_months:
            day = (day + month) % 7
            if day == 6:
                number_of_sundays += 1


# 01.01.1900 was a Monday
# 01.01.1901 was a Tuesday

print(number_of_sundays)
