from decimal import *

def decimal_length(d):
    return len(str( Decimal(1)/Decimal(d)))

def primes(n):
    primes = []
    for number in range(2,n):
        prime = True
        for i in range(2,int(number**0.5)+1):
            if number % i == 0:
                prime = False
                break

        if prime:
            primes.append(number)

    return primes



def period_length(d):
    number = str( Decimal(1)/Decimal(d))
    for length in range(1,1000):
        period_found = False
        for digit in range(len(number)-2*length):
            if number[digit:digit+length] == number[digit+length:digit+2*length] and number[digit:digit+length] == number[digit+2*length:digit+3*length]:
                period_found=True
                return length
        if period_found:
            break

for prime in primes(1000):
    print(prime,period_length(prime))