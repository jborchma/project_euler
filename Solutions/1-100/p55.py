def is_palindrome(n):
    if str(n) == str(n)[::-1]:
        return True
    else:
        return False

counter_all = 0
for i in range(1,10001):
    flag = True
    counter = 0
    summe = i + int(str(i)[::-1])
    while flag:
        if is_palindrome(summe):
            flag = False
        counter +=1
        if counter == 50:
            flag = False
            counter_all += 1
        else:
            summe = summe + int(str(summe)[::-1])

print(counter_all)