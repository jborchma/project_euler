# again, just brute force
# smallest 10000 and largest 999*999=998001

# function checks if a number is a palindrome
def check_palindrome(number):
    return str(number) == ''.join(reversed(str(number)))

# loop through all the possible numbers
largest = 0
for first in range(100,999):
    for second in range(100,999):
        product = first* second
        if check_palindrome(product) and product > largest:
            largest = product

print(largest)