primeList = [2]

i = 3
while True:

    if all(i % number != 0 for number in primeList if number < int(i**0.5)+1):
        primeList.append(i)

    if len(primeList) ==10001:
        break
    i = i+1

print(primeList[-1])

