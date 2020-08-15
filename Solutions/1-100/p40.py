# brute force, construct the number, pick the right elements

number_string = ""
for i in range(1, 200000):
    number_string += str(i)

print(
    int(number_string[9])
    * int(number_string[99])
    * int(number_string[999])
    * int(number_string[9999])
    * int(number_string[99999])
    * int(number_string[999999])
)
