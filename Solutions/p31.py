list_of_coins = [1,2,5,10,20,50,100,200]
target = 200
ways = {i:0 for i in range(target+1)} #creates dict of tuples
ways[0] = 1

for i in range(len(list_of_coins)):
    for j in range(list_of_coins[i],target+1):
        ways[j] += ways[j - list_of_coins[i]]

print(ways[200])


