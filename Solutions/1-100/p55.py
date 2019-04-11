"""Solution to problem 55
"""

def is_palindrome(number):
    """Checks if number is a palindrome

    Parameters
    ----------
    number: int
        Number to test

    Returns
    -------
    bool
        Boolean indicator that is True when the number is a palindrome
    """
    return str(number) == str(number)[::-1]

def main():
    """main function
    """
    counter_all = 0
    for i in range(1, 10001):
        flag = True
        counter = 0
        summe = i + int(str(i)[::-1])
        while flag:
            if is_palindrome(summe):
                flag = False
            counter += 1
            if counter == 50:
                flag = False
                counter_all += 1
            else:
                summe = summe + int(str(summe)[::-1])

    print(counter_all)

if __name__ == "__main__":
    main()
