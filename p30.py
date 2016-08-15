def test_power(n):
    number_string = str(n)
    summe = 0
    for digit in number_string:
        summe += int(digit)**5
    if summe == n:
        return True
    else:
        return False
numbers = []
for n in range(10,1000000):
    if test_power(n):
        numbers.append(n)

print(sum(numbers))

